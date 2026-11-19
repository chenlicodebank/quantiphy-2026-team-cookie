# captured_0030 — measurement record (lab video, 3D, 24 fps, 49 frames, 1280x720)

## Scene
A person (left; black top, light-blue denim overalls, face blurred) holds a thin light-coloured
stick/string in their right hand and swings a **small red/orange ball** around in a roughly horizontal
loop just above a wooden table (centre). The ball keeps moving for the whole clip (frame 0 to 48). Its image path is a loop:
- near side: low in the image (y ≈ 495–516), large (~65–75 px), moving left;
- far side: higher (y ≈ 421–435), small (~31–45 px), moving right.
It covers about 1.8 laps in 2 s. Background: tripod with a light, a wall screen (top right), grey wall panels. The whole frame is
softly blurred (the video carries a "Modified with Segment Anything 2 Demo" watermark, bottom right).
The only object tracked frame by frame is the ball. The person's body is nearly static, and their hand moves in a small circle.

## Files
- `scene.json`: inventory (description, moving or not, visible frames), static pixel extents, camera, perspective cues, events.
- `tracks/ball.csv`: one row per frame (0–48). Columns: frame, t (= frame/24), visible, cx, cy (mask centroid = visible
  centre, px), bbox x0/y0/x1/y1/w/h, mask_area, equiv_diam (2·sqrt(area/π)), len_major / wid_minor (mask extent along and
  across its principal axis), major_axis_deg, occluded (always 0).
- `scripts/`: `track_ball.py` (HSV colour mask, hysteresis core s>175 grown into s>120 rim, holes filled; also writes overlay
  crops into ../frames/ov), `static_measure.py` (camera-shift check and table mask), `write_scene.py` (builds scene.json),
  `montage.py`, `probe_hsv.py`.

## How it was measured and how far to trust it
- Ball mask: checked visually on every frame (overlay montages). It covers the ball body and leaves out the orange reflection
  on the table below it and the person's skin. The centroid is good to about ±2 px.
- **Ball diameter**: motion blur stretches the mask along the motion direction on the fast near side (frames 0–5 and
  25–31, where a red smear extends a few px beyond the mask horizontally). Use `wid_minor` / `bbox_h` as the diameter.
  The apparent diameter runs from ~31–37 px (far, frames 16–18) to ~70–75 px (near, frames 25–30). The apparent size
  roughly scales as 1/depth, so near/far depth ratio ≈ 2. Frame 0 (moving slowly): bbox_h 60 px, wid_minor 66 px.
- Frame-to-frame steps are mostly smooth. The exception is the jump 11→12 (51 px, against ~15 and ~31 px around it), which may
  be an irregular capture interval or blur affecting frame 11. Smooth over ≥5 frames, as the reference convention does.
- Camera: static. Phase correlation of the background against frame 0 gives a shift below 0.1 px in every frame.
- For back-projection use the lab intrinsics f = 763 px, (cx, cy) ≈ (640, 360) together with depth_info. Pixel positions
  here are the visible centre, which matches the annotators' clicked centres.
- Table (frame 16, ±5 px): top far edge y≈440 (x 380–805), top front edge y≈532 (x 210–955, 745 px long), apron bottom
  y≈558, pedestal x 575–615. The side edges converge at about (600, 328), which gives a horizon at y ≈ 328 (the camera looks
  slightly down). The table top is a horizontal plane; the ball moves a few cm above it.
- Hand/pivot positions are only approximate (blurred): ~(575,380) at f6 and ~(640,360) at f22. The stick/string runs from the
  fingers to the ball, ~150–250 px apparent length. Neither is tracked.

## Ambiguities
- The holder may be a string (pendulum) or a thin stick; it looks fairly straight.
- The orange reflection/shadow of the ball on the table could be mistaken for the ball; the mask excludes it.
- Skin has a similar hue to the ball; the saturation threshold separates them (checked visually).
