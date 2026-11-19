# q_918 – speed of the mug at t = 0.2 s

- 2D scene, file fps = question_fps = 24, so t = 0.2 s is frame 5. Speed = backward difference over frames 4 to 5.
- Scale comes from the prior (g = 9.8 m/s² before 1 s). `fit.py` re-measures the mug mask directly from the video and fits a
  quadratic to the vertical centroid over frames 0-17. The fall is free from frame 0, and impact is between frames 18 and 19.
  - Measured acceleration a = 8.847 px/frame², so the scale is 9.8 / (8.847 × 24²) = 0.001923 m/px.
  - Fit residuals have rms 0.22 px.
  - The fit's vertex is at frame -0.09, so the mug falls from rest at t ≈ 0.
- Centroid step from frame 4 to 5 = 40.6–40.7 px (my mask and the scene record agree).
  - Measured step: v = 40.7 × 24 × 0.001923 = 1.88 m/s.
  - Fitted parabola: v = 1.874 m/s.
- Second route: the bbox-centre series gives a = 8.853 and v_fit = 1.873. A pure free fall from rest at frame 0 would give
  g × 4.5/24 = 1.84, slightly lower because the release is about 0.09 frame before frame 0.
- Scale check: the 82 px body diameter is about 0.16 m, so this is a big mug, but plausible enough. The scene is 2D, so the
  prior sets the scale.
- Answer: 1.874 m/s. Confidence: high (about ±1%).
