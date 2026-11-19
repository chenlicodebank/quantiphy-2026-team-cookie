# q2560 — ping pong ball velocity at t = 1.5 s (cm/s)

The video is a lab clip at 24 fps, and question_fps is also 24. t = 1.5 s is frame 36, when the ball has just rolled off the front-left table
edge (it leaves at about f35) and is falling toward the camera. The image is heavily motion-blurred, and the ball is gone after f37.
Camera: f = 763 px, principal point (640, 360).

## Measurements (measure.py, measure2.py, velocity.py)
- Centroids came from a background-difference mask. The background is the median of f38–48, when the ball is out of frame. The masks were
  checked on overlays (frames/masks.png, frames/zoom.png). Values: f34 (477.4, 486.6), f35 (455.1, 499.5), f36 (407.0, 576.1),
  f37 (373.4, 654.6). These agree with scene/tracks/ball.csv within 1–7 px.
- Apparent diameter at f36/f37 comes from a stadium (blurred-disc) fit using area and streak length: about 56 and 57 px. With D = 40 mm
  that gives Z ≈ 0.55 and 0.54 m.
- At f34 a diameter of about 40 px (horizontal extent minus blur) matches depth_info's 0.738 m (41 px expected).
- depth_info: f22 is 1.457 m and f34 is 0.738 m. Their ratio matches the ratio of the table's far and near edge widths (313 vs 603 px),
  so the ball travels from the far part of the table to the near edge. Rolling toward the camera is about 0.06 m/frame
  (~1.45 m/s), plus about 0.02 m/frame sideways.
- Depths used: f34 0.738 (given), f35 0.67, f36 0.58, f37 0.54. f35–f37 blend the depth_info rate with the apparent-size depth.

## Result
- Forward differences: f34→35 1.64 m/s, f35→36 2.41 m/s, f36→37 1.46 m/s. Averaging the three as vectors (the reference smooths over
  about 5 frames) gives 1.75 m/s.
- Physics check (second route): horizontal speed about 1.48 m/s from the rolling phase. Adding free fall for 0.04–0.06 s after leaving
  the edge gives 1.53–1.59 m/s.
- Answer: **170 cm/s**.

## Confidence
Moderate to low. Depth at f35–37 is not given and is uncertain (blur, rolling shutter, and size versus depth_info inconsistency:
the apparent size at f22 suggests about 1.0 m, not 1.457 m). Plausible range is 140–250 cm/s.
