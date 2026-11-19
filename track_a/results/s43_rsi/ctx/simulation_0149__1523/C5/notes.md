# q1523: acceleration of the yellow car at t = 0.5 s (frame 12; question_fps = file fps = 24)

Answer: **10.4 m/s^2**

## What the answer depends on
- The car's position along its path in frames 10-12 (a = (s12 - 2 s11 + s10) x 576).
- Metric scale: depth_info (frame 0, camera to the right-front tyre = 14.244 m), the effective horizontal focal
  length F, and the 3D direction of the path.
- The hub of the near front wheel stays on the horizon row (v ≈ 829) in every frame, so it moves in the camera's
  horizontal plane. The 2D (X, Z) geometry is enough.

## Own measurements
- `rimtrack2.py`: segments the white rim of the near front wheel in frames 0-23 (threshold tuned for the dark early
  frames) and fits an ellipse to get the centre u and the height h. `rimtrack.py` covers the brighter later frames.
- `traj.py`: Z = K/h and X = (u - cx)Z/F, with a total-least-squares line fit. The path is straight (residual a few
  cm). The path direction is 35.6° from the optical axis, so the car is heading toward the camera and to the right.
  Each frame's position comes from intersecting its rim-centre ray with the line, scaled so the frame-0 range is
  14.244 m. Cubic, quartic and smoothstep fits over frames 0-23 give:
  - F = 2300: 10.57
  - F = 2410: 10.46
  - F = 2450: 10.42 m/s^2
  - The raw one-frame second difference is 9.1 (noisy), and a quadratic over frames 6-18 gives 9.7. The quadratic
    reads lower because the acceleration is decreasing (ease-in), so I did not use it.
- `dirsens.py`: sensitivity to the path direction. The rim-height growth fits best at 35.6-37° (h rms about 1 px). Over
  that range a = 10.3-10.7. Directions of 40° or more fit the rim growth badly.
- Speed at frame 12 is about 6.5 m/s. It rises to about 9.6 m/s by frame 23.
- F: the vanishing-point value is about 2410 (C2). The tyre/rim-ratio routes give 2300-2430. Across that range the
  answer changes by only about ±1 %.
- Plausibility check: at F ≈ 2350, the frame-0 rim diameter is about 0.49-0.50 m. That gives a tyre/rim ratio of
  1.53-1.57, which matches the image.

## Where the candidates part ways
- C1 (10.35), C2 (10.1), C3 (10.2) and C6 (10.25) all use the same correct route: wheel track, straight 3D line,
  ray intersection and the convention's second difference on a smooth fit. Their differences come from F and the
  fit window. My own result, 10.4-10.6, agrees with them to within about 3 %.
- C4 (7.2) used noisy ECC scale changes of the body, smoothed by low-order polynomials. This underestimates the
  depth motion.
- C5 (2.5) fitted a quadratic to silhouette-centroid positions over frames 13-30, with f ≈ 1950 from silhouette height.
  This is wrong in both the scale and the frame window.

The final 10.4 sits between my 10.45-10.6 and the cluster of earlier careful answers. Confidence is about ±4 %.
