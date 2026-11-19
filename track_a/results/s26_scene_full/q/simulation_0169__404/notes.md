# q404 — astronaut acceleration at t = 1 s (frame 24)

- 2D scene, static camera, fps = question_fps = 24 (no retiming question).
- Scale: astronaut upright at frame 0, pixel height 90-91 px (height.py, thresholds 15-80 give 89-91; visible
  boot-to-helmet ≈ 90.5 px). 2.2 m / 90.5 px = 0.02431 m/px.
- Track: scene/tracks/astronaut.csv mask centroid (checked: single blob, no occlusion).
- Route 1 (fit.py): whole path fits a Blender Bezier ease-in/ease-out (smoothstep 3s²-2s³) with keyframes at
  frame ≈ -0.25 and ≈ 78.15, D = 274.6 px, rms residual 0.35 px. Discrete convention speed(24)-speed(23) =
  0.109 px/frame² (analytic at frame 24: 0.102).
- Route 2: local cubic fits of the path distance over ±6…±12 frames around frame 24: 0.088-0.105 px/frame²
  (≈0.100), speed ≈ 4.52 px/frame.
- Adopted 0.107 px/frame² × 576 = 61.6 px/s² × 0.02431 m/px ≈ 1.50 m/s².
- Confidence: moderate-good (±7 %); the motion is eased, so acceleration varies with time; main uncertainty is
  the local slope of the speed profile and the 1 % pixel-height uncertainty.
