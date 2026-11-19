# q_2632 – soccer ball displacement between 0.5 s and 0.6 s (cm)

Time base: question_fps = file fps = 24. t=0.5 -> frame 12, t=0.6 -> frame round(14.4) = 14.
Camera: f = 0.5959*1280 = 763 px, principal point (640, 360). Back-projection: unit ray x distance (depth_info is Euclidean).

## Centres (soccer ball, medium reliability – motion blurred, clear of the foot)
- scene track (RANSAC circle): f12 (494.07, 391.21), f14 (525.10, 407.97)
- my own mask centroid (measure.py): f12 (493.45, 391.01), f14 (524.02, 409.90). Image step ~35 px over 2 frames.
- Frames 12 and 14 are both after the dropped capture frame (11->12), so this is a clean 2-frame step.

## Depth
Given: soccer 2.758 m at f14. Depth at f12 is not given -> estimated (answer is sensitive: each +1 cm in dist12 ~ +0.5 cm).
Depth_info line "t=1.6 soccer 2.412" is actually the basketball (size-ratio from f14 gives 2.437); soccer at f38 = 3.052.
- Size fit (sizefit.py): across-motion mask width minus 1.8 px edge inflation, calibrated at f38 (3.052 m); reproduces
  f14 at 2.66-2.70 (given 2.758, ok). Linear fit over f10-19: -0.035 m/frame -> dist12 2.83 -> **14.5 cm**.
- Soccer-centre plane (plane.py, sharp frames, size-based depths), scaled to given f14: dist12 2.818 -> **13.9 cm**.
- Kinematic: ball at rest at ~3.17 m (42 px) to 2.758 at f14 over ~10 effective frames -> ~0.042 m/frame ->
  dist12 2.842 -> **15.4 cm**.
- Collision with basketball at f19 (collide.py, centre distance = sum of radii): d19 ~2.48 -> 0.055 m/frame ->
  dist12 ~2.88 -> **17.5 cm** (most sensitive to basketball depth / contact frame).
- Basketball-only floor plane (plane_bb.py) was ill-conditioned (path nearly a line) – rejected.

## Answer
15.0 cm (dist12 ~2.835 m, dist14 2.758 m). Lateral part alone (same depth) = 12.7 cm; the remainder is the radial
approach toward the camera. Confidence: moderate (±10-15 %), dominated by the unknown depth at t=0.5.
