# captured_0035bx — measurement record (pixels, seconds)

Lab recording (24 fps, 49 frames, t = frame/24, 0–2.0 s, 1280x720). The background was replaced by pure white (SAM2;
watermark "Modified with Segment Anything 2 Demo" at bottom-right x≥1030, y≥690, not an object). It's a 3D scene seen by
an elevated static camera looking obliquely down. Benchmark intrinsics: fx = fy ≈ 763 px, principal point ≈ (640, 360).

## What happens
Two people stand roughly facing each other, each with a ball at their feet. At frame 11 (t = 0.458 s) both kick at the same
moment. The **near person** (bottom-left, long dark hair, dark grey T-shirt, black trousers) kicks the **white/black soccer
ball** with their right foot. It rolls up-right, away from the camera. The **far person** (top-right, light top, dark blue
baggy jeans, only waist-down visible) kicks the **orange basketball**, which rolls left-down toward the near person/camera.
The balls meet at frames 24–26 (contact around frame 25, t ≈ 1.04 s). After that the soccer ball slows and turns right/slightly
down, and the orange ball's path flattens slightly. The near person bends down, touches the orange ball at frame 45
(t = 1.875 s) and holds it to the end. The soccer ball is still rolling at frame 48.

## Files
- `scene.json`: inventory, camera, events (frame + time), apparent ball sizes at sample frames, direction notes.
- `tracks/<object>.csv`: one row per frame (0–48) for `soccer_ball`, `basketball_orange`, `person_near_left`,
  `person_far_right`. Columns:
  - `cx, cy`: mask centroid. This is the reference point ("visible centre").
  - `bbox_x0..y1, bbox_w, bbox_h`: inclusive pixel bounding box.
  - `area_px`
  - `len_main_axis, width_across, main_axis_deg`: PCA extents of the mask.
  - `occluded`: 1 = merged, touching, held or truncated.
  - Balls only: `circle_cx, circle_cy, circle_diam`, the minimum enclosing circle of the mask. For a ball this is the best
    centre and apparent diameter. Prefer `circle_*` over centroid when the mask is partly cut.
- `scripts/`:
  - `track.py`: all tracking.
  - `events.py`: per-frame steps, ball-ball distance, person boxes.
  - `check_crops.py`, `strip.py`: visual checks.
  - `write_json.py`
  - `_debug/`: overlays of frames 0, 12, 26 and 48, plus 3x ball crop montages with bbox/circle drawn.

## How it was measured
- Foreground = pixels with min(BGR) < 241 (background is exactly 255).
- **Orange ball**: HSV mask (H<20, S>140, V>80), then the convex hull of near-white-inclusive foreground (<245) inside a disk
  around it, excluding the soccer ball and the people. This adds the dark rim and seams. From frame 45 on it uses the colour
  mask only, because the hands cover part of the ball (flagged occluded).
- **Soccer ball**: its white panels are 230–254, almost background. It is found as a low-saturation/dark blob, then rebuilt
  as the convex hull of pixels <252 inside a disk around that blob.
  - Frames 12–13: the ball is merged with the kicking shoe and motion-blurred. Its centre was read by eye from 2x crops,
    (485,628) and (504,604), ±4 px, and the mask is a 72 px circle (occluded=1).
  - Frames 0–10: the ball touches the bottom image edge (y=719). Centre ≈ (437, 683), width 80–82 px, possibly slightly
    truncated at the bottom.
  - Frame 11: the ball is in contact with the shoe and the mask includes a little of the toe (occluded=1).
- **People**: the large foreground components left after removing the balls. Their centroid is the centre of the
  *visible* part only.
  - Far person: always cut at y=0, so the centroid is not the body centre. Use the feet (bbox_y1 ≈ 321) as ground contact.
  - Near person: legs cut at the bottom edge, left edge cuts the body in frames 17–31, and the person bends over in frames
    36–48. Its centroid/bbox describe the visible silhouette only.
- All masks were drawn on frames and inspected. Ball boxes fit to within about 1–3 px; they include a faint 1–2 px
  anti-alias/blur halo.

## Apparent size over time (depth cue)
For apparent diameter, use the bbox (`bbox_w`/`bbox_h`). `circle_diam` is the enclosing circle and runs 2–5 px larger
because of rim irregularities and blur.
- Soccer ball bbox width:
  - ~80–82 px in frames 0–10 (at rest, nearest the camera, bottom touching the image edge, height 76–77 cut)
  - 76 → 66 px in frames 14–16 (blurred)
  - ~63–64 px in frames 18–23
  - ~61–64 px in frames 24–34, the farthest. In frames 24–26 the height is cut to 50–58 by the overlapping orange ball.
  - 64–69 px in frames 35–48, slowly growing
- Orange ball bbox:
  - 56x56 px in frames 0–11 (at rest)
  - 60–65 px in frames 12–21
  - 66–70 px in frames 22–28
  - 70–73 px in frames 29–39
  - 74–79 px in frames 40–44, nearest the camera
  - Frames 45–48: covered by the hands, so the measured size is an underestimate.
- Bigger and lower in the image means nearer the camera. With a given depth Z of a ball centre, size ≈ diam_px·Z/763, and
  lateral position ≈ ((u−640)·Z/763, (v−360)·Z/763).

## Reliability and ambiguities
- Ball centres: ±1–2 px when free.
  - ±4 px in frames 11–13 (merged with the shoe and blurred).
  - ±4 px in frames 24–26: the balls overlap in the image. The orange ball is drawn over the top of the soccer ball, so the
    soccer ball's mask/centre is biased low by about 2–5 px there.
- **Likely dropped capture frames.** The step 11→12 (soccer ~70 px, orange ~28 px, versus ~30 / ~20 px in the following
  frames) and the step 35→36 (both balls about 2× their neighbours) look like a capture frame is missing at each place.
  Smooth over these points when you fit velocities.
- Motion blur is strong for the soccer ball in frames 12–16 (elongated mask: len_main_axis > width).
- Lighting/colour: the soccer ball's white parts nearly match the background, so its area_px varies (1700–3600) more than
  its bbox/circle do. Use bbox/circle.
- No static scene objects (floor and furniture removed by segmentation). No shadows remain.
- Camera static: there's no background to verify this against, but both resting balls in frames 0–10 move <1 px.
