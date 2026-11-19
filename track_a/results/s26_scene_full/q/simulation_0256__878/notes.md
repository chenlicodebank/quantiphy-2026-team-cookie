# Q878: speed of the tennis ball at t = 1 s (m/s)

2D sim, 24 fps (file fps = question_fps, so no re-timing). t = 1 s -> frame 24; speed = |p24 - p23| x 24.
The camera is static and there is one ball moving horizontally (cy is constant at about 363.5).

## Measurements (measure.py, diam.py)
- Centroid (Lab b* mask, thresholds 8/12/18): dx 23->24 = 54.15 / 54.21 / 55.09 px. The bbox left/right edges both move 54 px.
  A quadratic fit of cx over frames 6-39 (residual 0.25 px) gives a backward difference at frame 24 of 54.66 px.
  Adopted value: 54.4 px/frame.
- Ball diameter: the bbox height is 36 px (inclusive, threshold 8/12, median over frames). The b* half-max profile gives 32-33.5 px,
  but it underestimates because the darker rim has less chroma. A visual edge read on a 10x crop at frame 24 gives about 35 x 34.5 px.
  Adopted value: 35.5 ± 1 px.
- Scale: 0.17 / 35.5 = 0.004789 m/px.

## Answer
v = 54.4 x 24 x 0.004789 = 6.25 m/s. With D = 36 px it would be 6.16 m/s. Answer: 6.21 m/s.
Second-route check: the direct difference (54.2) and the fitted value (54.66) agree within 1%. The main uncertainty is the pixel
diameter (±3%).
