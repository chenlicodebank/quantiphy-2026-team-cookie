# Q1381 – diameter of the red blood cell (m)

Prior: speed = 4.7833 m/s. depth_info (left cell, origin distance): 17.9557 m at t=1 s (frame 24), 22.7150 m at t=2 s (frame 48).
question_fps = file fps = 24.

## Method (solve.py, measure.py)
- Tracks from scene/ (left cell centroid) checked; frame 24 viewed. Both cells identical in size/shape and at equal depth.
- Focal length: back-project the left-cell centroid at frames 24 and 48 with the given distances; the 3D
  displacement over 1 s equals the prior speed (motion is constant-velocity: per-frame speeds over frames 2–71
  constant at 4.78 ± 0.005 m/s with depth linear in frame) -> f = 2643 px (hfov 39.9°).
  This is ill-conditioned (motion mostly radial), but it agrees within 1 % with the Blender default 50 mm lens /
  36 mm sensor, f = 2666.7 px, which reproduces the prior speed as 4.7829 m/s. Used both.
- Pixel diameter = horizontal extent of the disc: sub-pixel (50 % edge crossing) width 242.4 px at f24, 192.0 px at f48
  (bbox_w 246 / 194 includes anti-aliased edge pixels). Z = depth along the optical axis (distance × cos of off-axis angle).
- D = width × Z / f:
  - f=2643: 1.640 (f24), 1.640 (f48); bbox width: 1.664 / 1.657
  - f=2667: 1.626 (f24), 1.626 (f48); bbox width: 1.650 / 1.642
- Second route: frame 48 vs frame 24 (independent depth) agree; right cell (same depth by apparent size) gives 1.634–1.639.
  Apparent-size depth ratio 1.268 vs given 1.265 (consistent).

## Answer
D ≈ 1.63 m (range 1.62–1.66 across f choice and edge definition). Confidence: good (±2 %).
