# captured_0054bs – measurement record

**The clip:** a lab recording, 3D, 24 fps, 49 frames (t = 0 … 2.0 s), 1280×720. The original background (room, floor and people) was replaced with Segment Anything 2. A static snowy blue-to-white gradient is left behind, with a SAM2 watermark at the bottom right. The camera is static. No floor, wall or horizon is visible, so the only perspective cue is apparent size. Lab intrinsics: f = 763 px, principal point about (640, 360).

The scene has four thrown balls:
- **basketball**: orange.
- **soccer_ball**: black and white.
- **yellow_object**: a small yellow ball, probably a tennis ball.
- **grey_object**: a light-grey or off-white oval ball, a little larger than the yellow one.

The people throwing them are masked out, so they are invisible. No static scene objects are visible.

## Files
- `scene.json`: inventory, event list, camera, timing anomalies and sample apparent sizes.
- `tracks/<object>.csv`: one row per frame in which the object is visible. Columns:
  - `frame`, `time_s` (= frame/24).
  - `ref_x`, `ref_y`: the reference point (the object's centre).
    - For the basketball and soccer ball this is a least-squares circle fit to the convex hull of the mask. This stays reliable when part of the ball is hidden.
    - For the yellow and grey objects it is the mask centroid.
  - `centroid_x/y`: the mask centroid.
  - `bbox_*`: inclusive pixel box.
  - `mask_length` / `mask_width`: minimum-area rectangle, along the main axis and across it. `main_axis_deg` gives that axis, with 0 = +x and angles turning toward +y (down).
  - `mask_height` = bbox_h.
  - `circle_diam`: diameter of the fitted circle.
  - `mask_area`.
  - `occluded` (0/1) and `note`.
- `scripts/`:
  - `bg.py`: full-resolution median background.
  - `track.py`: segmentation and tracking. It writes `*_raw.csv`.
  - `assemble.py`: builds the final CSVs and the flags.
  - Checking tools: `check_obj.py`, `check_soccer.py`, `draw_tracks.py`, `montage.py`, `ovmont.py`, `dump.py`, `diffview.py`.
  - `steps.py`: per-frame steps and frame differences.
  - `show.py`, `probe_faint.py`: helpers.

## How it was measured
- **Foreground:** each frame is compared with the median background. Outside the objects the background is pixel-identical from frame to frame.
- **Colour classes:**
  - orange → basketball;
  - yellow (G−B>40) → yellow object;
  - neutral → soccer ball or grey object, assigned by how close each piece is to that object's previous position.
- **Faint soccer ball:** from frame 27 the SAM2 output fills the soccer ball as a faint grey disc with no texture. It was found by its missing background texture: a disc is fitted to the smooth region, then refined.
- **Checks:** every track was drawn on crops and checked by eye (montages in `frames/`, which are scratch files).

## Reliability
- **basketball**
  - Frames 12–48 are clean: centre ±1 px, diameter ±1.5 px.
  - Frames 0–10 are partial because the hand is masked out, and in frames 0–4 the ball is also cut by the bottom edge. The centre comes from the visible arc: about ±3–5 px.
  - Its apparent diameter shrinks from 75.8 px (frame 12) to a minimum of about 50 px (frames 38–41), then grows to 52.3 px (frame 48). So it flies away from the camera, rebounds at frame 39 and comes back.
- **soccer_ball**
  - Frames 0–24: the ball is held and partly hidden. Frames 10–16 are heavily hidden, and their centre and size are unreliable.
  - Frames 25–28: textured and complete, but blurred. Diameter about 70 px.
  - Frames 29–48: faint disc. Centre ±3 px, diameter ±5 px. Frames 39, 40, 44 and 45 give about 62–63 px, which is probably too large. A smooth trend from about 65 px (frame 29) to about 52 px (frame 48) is more trustworthy.
  - It moves up and slightly left while shrinking, so it is moving away from the camera.
- **yellow_object and grey_object**
  - Frames 17–29: strong motion blur stretches them along the motion. Use `mask_width` as the size across the motion, not `mask_length`.
  - Frame 17: the yellow object is cut by the left edge.
  - Frame 20: the grey object appears suddenly. It is probably present earlier but was not segmented.
  - The grey object is gone after frame 47.
  - Frames 38–41: the two touch and were separated by colour. Centroids ±2 px.

## Events (frame / time)
- Basketball:
  - starts moving at 5 (0.208 s);
  - released at about 11 (0.458 s);
  - impact and rebound at 39 (1.625 s): the x and y motion reverse and its size starts growing.
- Yellow ball:
  - enters at 17 (0.708 s);
  - apex at 27 (y 237.6);
  - bounces at 37 (1.542 s, lowest y 489).
- Grey ball:
  - first visible at 20 (0.833 s);
  - apex at 27–28 (y about 199);
  - bounces at 38 (1.583 s, lowest y 471);
  - last seen at 47.
- Soccer ball:
  - leaves the hand at about 23–24 (0.96–1.0 s);
  - free from about 25;
  - still rising at the end.

## Timing anomalies (important for speeds and accelerations)
- **Frames 35 → 36:** every object's step doubles, so one source frame is missing there. The displacement across this pair covers about 2/24 s.
- **Frames 11 → 12:** probably one more dropped frame (the basketball step goes 27 → 53 → 24 px).

The benchmark keeps t = frame/24 regardless. For speeds, avoid using the 35→36 step as a single frame, or smooth across it.

## Ambiguities
- The yellow and grey balls cannot be identified for certain; they are named here by colour.
- The hands, wall and floor that cause the throws and bounces are not visible.
- No metric scale was assumed anywhere.
