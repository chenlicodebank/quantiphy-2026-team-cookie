# q472 — speed of the box at t = 0.4 s (simulation_0191, 2D, 120 fps = question_fps)

Prior: box acceleration before 0.6 s = 9.8 m/s^2 (free fall). t = 0.4 s -> frame 48.

Method (fit.py): quadratic fit to the box's centre track cy (scene/tracks/box.csv, template matched, checked
continuous/no rotation) over the free-fall frames 0–60 (impact at frame 61).
- Pixel acceleration 1976 px/s^2 -> scale 9.8/1976 = 0.00496 m/px; fit residual rms 0.06 px.
- Zero-velocity time t0 = -0.0014 s (release at frame 0).
- Backward-difference speed at frame 48 = g*(47.5/120 - t0) = 3.893 m/s.
Robustness: fit windows 0–40 … 30–60 give 3.886–3.915. Raw one-frame difference (y48-y47) gives 3.946
(noisy, ±0.3 px tracking), 9-frame local slope 3.929.
Scale sanity: truck 1690 px -> 8.4 m long, box 2.0 m x 0.95 m (large, but the answer is independent of scale since
it comes from g and timing).

Answer: 3.89 m/s. Confidence high (~2%).
