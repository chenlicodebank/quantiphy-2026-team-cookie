# q1605: length of the black cat, tail included (m)

File fps = question_fps = 24, so t=1.0 s is frame 24. I used the scene/tracks/cat.csv rows (bbox, core centroid) for
frames 0–23 and 45–49, where the cat is not occluded. The cat is clear at frame 24 too (checked on frames/f24.png).

## Focal length (scripts: measure.py, fscan.py)
- Prior: cat speed 0.94 m/s. Depths: 4.199 m at t=0 and 4.481 m at t=1. Assuming constant speed on a straight path, the
  3D chord between the origins at t=0 and t=1 is 0.94 m. I back-projected the origin pixels (principal point at the
  image centre) with the given depths and solved for f:
  - raw core centroid f0 / f24: f = 2156
  - mask centroid: 2147; bbox centre: 2099
  - quadratic fit of the core track over frames 0–23, evaluated at 0 and 24 (reduces gait jitter): 2087
  - I chose f ≈ 2120 ± 35 (HFOV ≈ 48°). Check: at f=2120 the mean of the per-frame speeds along the fitted 3D line is
    0.955 m/s, against the prior 0.94. Frame-to-frame noise inflates this a little, so it agrees.
- 3D motion direction (camera frame) ≈ (0.90, 0.00, 0.44): the cat walks right and away from the camera.

## Length
For each clear frame I put the origin on the 3D walking line. I took the mask's horizontal pixel extremes (tail tip or
back paw, and nose/ear) and found the points along the walking direction through the origin that project to them. The
u coordinate does not depend on height, so a raised tail or a low paw does not bias this. Length = the separation of
those two points.
- f=2087: 0.692 m, f=2120: 0.683 m, f=2156: 0.673 m (median over 28 frames)
- Frame to frame it varies 0.665–0.72 with the gait. Frame 0 gives 0.690.
- Second route: frames 46–49 (after the cat comes out from behind the dog, depth ≈ 4.9 m, extrapolated along the line)
  give 0.68–0.72. That agrees with frames 0–23 (≈0.69), which supports the geometry.

Answer: **0.683 m**. This assumes the cat's walking direction is aligned with a world axis, so that the AABB length
equals the extent along the motion. The raised tail adds little horizontal length; the extent from the tail tip or
back paw to the nose is what was measured.
Confidence: moderate, about ±5%. The main uncertainties are f (±2%), gait/pose (±4%) and the AABB axis alignment.
