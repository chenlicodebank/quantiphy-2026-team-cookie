# q_2193 – ball velocity at t=0.3 s (captured_0010)

File fps = question fps = 24; t=0.3 s -> frame 7. Lab camera f = 0.5959*1280 = 762.75 px, pp (640,360).

Ball = orange pendulum bob swinging mostly toward/away from the camera; at f7 it is mid-swing coming toward the camera
(far turn f3, near turn f17).

## Method (fit.py)
- Image centre per frame from scene/tracks/ball.csv (mask centroid, ±0.5 px per the record; not re-tracked here,
  but the track is smooth and its turning points match the depth fit).
- Depth per frame: a sinusoid d(t)=a+b cos(wt+phi) fitted to the 6 given distances (frames 7,14,22,29,36,43).
  Fit: a=1.566, b=0.264, period 29.2 frames (agrees with the 29.5-frame period from image turning points),
  residuals ≤1.1 cm. Fixed-period (29.5 fr) fit gives nearly identical results.
- 3D centre = d * unit ray; velocity = forward difference *24, smoothed over 5 frames around f7.

## Results (|v| at f7, m/s)
- sinusoid depth: 5-frame smoothed 1.39, central diff 1.41, raw forward diff (f7->f8) 1.47
- fixed-period sinusoid: 1.40 / 1.42 / 1.48
- Second route, depth from apparent ball size (d = K / diameter_px, K calibrated on the given depths): smoothed
  1.43-1.47, but noisy frame to frame (size noise ±3%), so used only as a check.
- Physical check: depth amplitude 0.264 m * w 5.16 * sin(phase 1.03 rad) = 1.17 m/s along depth alone, plus the
  vertical/lateral components -> ~1.4 m/s. Matches.

Answer: 1.42 m/s (between the centred-smoothed 1.39-1.40 and the forward-difference 1.47). Confidence: moderate, ±5%.
