# captured_0047x – measurement record

Lab (captured) clip, 3D scene, 24 fps, 49 frames (t = 0 … 2.000 s), 1280×720. The background was replaced with flat chroma green
(Segment Anything 2 demo watermark at bottom-right, x 1030–1280, y 690–720; not a scene object). Benchmark camera:
focal ≈ 763 px, principal point ≈ (640, 360). No metric scale is assumed anywhere here.

## Scene
- **ball** – a large dark-grey (slightly bluish) exercise ball with shiny highlights. It is the only ball. The person holds it at rest
  (frames 0–13), pushes it, and it rolls **toward the camera and to the left** (down-left in the image). It touches the bottom
  image edge at frame 33, the last centre fit is at frame 45, it is only a sliver at frame 46, and it is out of view in frames 47–48.
- **person** – one person squatting behind the ball (face masked green, long dark hair, black T-shirt and trousers, white shoes).
  The feet stay fixed (shoe bottoms at y≈543, shoes at x≈600–632), so the person does not travel. Only the arms move: hands on the
  ball sides in frames 0–16, hands over the top of the ball at 17, arms thrown up at 19–30, then lowered or crossed at 38–48.
  Squat bounding box (frame 40): x 506–639, y 348–543 → height 196 px, width ≈128 px with arms down.
- There are no other objects, floor markings or furniture: the background is removed. No floor or horizon is visible.

## Files
- `scene.json` – inventory, events, camera, rest-state numbers and selected ball diameters.
- `tracks/ball.csv` – one row per frame, 0–46:
  - `cx, cy`: centre of the circle fitted to the silhouette outline. This is the reference point (the visible ball centre).
  - `circle_R`, `circle_diam`: apparent radius and diameter in px.
  - `ell_*`: ellipse fit to the same outline points.
  - `full_bbox_*`: bbox of the fitted ellipse, which can extend outside the image.
  - `vis_bbox_*`, `vis_area_px`: the part of the ball inside the image.
  - `top_y`, `bottom_y`: top and bottom of the circle. `bottom_y` is the floor-contact point in the image.
  - `outline_cover_deg`: how much of the outline the fit used, in degrees.
  - `fit_rms_px`: RMS residual of the circle fit.
  - `cut_by_frame_edge`: 1 if the fitted ellipse runs past the image edge.
  - `frac_outline_in_image`: fraction of the circle that lies inside the image.
  - `occluded_by_person`: always 0, because the ball is in front of the person.
  - Frame 46 has only the visible bbox (x 24–133, y 704–719) and no centre.
- `tracks/person.csv` – one row per frame, 0–48:
  - `cx, cy`: centroid of the person mask.
  - `bbox_*`, `width_px`, `height_px`, `area_px`: mask extents.
  - `occluded_by_ball`: 1 if the person's bbox overlaps the ball's bbox.
  - `gap_to_ball_px`: smallest distance from any person pixel to the ball circle.
- `scripts/`:
  - `segment.py`: green-key foreground mask, plus a "ball-coloured" mask (low saturation, bluish or neutral, V ≥ 34).
  - `track.py`: makes all tracks and the overlays. It fits the ball as an iterative circle on the outline points near the previous estimate, with the radius change limited to −10 %/+15 % per frame. The person is the foreground minus the dilated ball ellipse.
  - `montage.py`: crop montages used for visual checks.
  - `probe.py`: colour probing.
  - Overlay checks are in `../frames/trk_*.png`, `m1.png` and `m2.png`.

## Events (frame / t)
- 0–13 (0–0.542 s): ball at rest, centre (570.1, 496.6), diameter 117.6 ± 0.4 px, bottom y ≈ 555.
- Ball starts moving at frame 14 (t = 0.583 s). The centre moves 1.1, 2.5 and 6.2 px at frames 14, 15 and 16, so the onset is between frames 13 and 14.
- Release / last hand contact is at frame 17 (t = 0.708 s): the hands slide over the top of the ball. By frame 18 (0.75 s) the hands are off.
- Frame 28 (1.167 s): the ball's silhouette separates from the person's silhouette in the image (`gap_to_ball_px` goes above 5).
- Frame 33 (1.375 s): the ball first reaches the bottom image edge.
- Frame 45 (1.875 s): last centre fit. Frame 46 (1.917 s): last visible sliver. Frames 47–48: no ball.
- No bounce. The image path curves smoothly down-left from (570, 497) to (118, 896, extrapolated).

## Camera and perspective
- The camera is static. The background is removed, so this was checked on the person: the feet and head top stay fixed to about 1–2 px.
- The ball approaches the camera: its apparent diameter grows 117 → 131 (fr 18) → 150 (24) → 179 (28) → 206 (32) → 234 (36) → 305 (40) → 407 (44) → 420 (45) px.
  - For a rigid sphere, distance ∝ 1 / apparent diameter. From frame 0 to frame 45 the ball comes about 3.6× closer.
  - With a known ball size D (m): depth ≈ 763·D / diam_px. Back-project the centre with (u − 640, v − 360)·Z / 763.
- At rest the ball's floor contact (y ≈ 555) is lower in the image than the person's shoes (y ≈ 543). So the ball is nearer to the camera than the person's feet.

## Reliability and ambiguities
- **Ball centre and diameter, frames 0–32** (outline fully inside the image): ±1–2 px for the centre and about ±2–3 % for the diameter.
  - The SAM2 mask edge is wavy, so the circle fit RMS is 2–4 px.
  - The silhouette is not a perfect circle: the bottom is slightly flattened and in frames 28–31 it looks a little egg-shaped. Ellipse major/minor differ by up to 10 %.
  - Prefer `circle_diam`. Vertical extents are affected by the flattened bottom.
  - Frames 0–17: the person's legs and hands touch the ball outline, so the fit leans on the bright top arc and the green-facing left and bottom edges.
  - Frame 17: hands cover the top of the ball, so the diameter (120.9) is probably a little low. The jump to 131 px at frame 18 is partly this effect.
- **Frames 33–45** (ball cut by the bottom edge): the centre and diameter come from a partial arc (only 80–290° of outline).
  - The error grows to about ±5 % for the diameter and ±10–20 px for the centre.
  - From frame 39 on, `cy` is below the image (> 720), so it is extrapolated.
  - The `ell_*` values in these frames are unreliable: ignore them and use `circle_*`.
  - A human annotator clicking the "visible centre" would have clicked inside the visible part. That point differs from the fitted true centre in these frames.
- **Person**:
  - In frames 0–16 and 18–19 the lower legs are hidden behind the ball, so `bbox_y1` ≈ 485–513 instead of 543.
  - The centroid moves only because of arm and leg visibility, not because the body moves. Use the fixed feet and head for any person-based scale (squat height 196 px).
  - The `occluded_by_ball` flag uses bbox overlap, so it stays 1 until frame 35. The silhouettes really touch only until about frame 27.
  - The face is masked green, so it is excluded from the mask (small hole).
- There are no shadows, no other balls and no other people. Motion blur is mild on the arms in frames 18–20.
