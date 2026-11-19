# q3082 – velocity of the white (ping-pong) ball at t = 1.50 s

Time base: file fps = question_fps = 30, so t = 1.50 s is frame 45. The ball is in free flight there (thrown arc, released about frame 40, first bounce at frame 49.15).

## Scale from the prior (g = 9.8 m/s²)
- `fit.py`: quadratic fits of the image y of the ball centre (record `cx_f0/cy_f0`, background-stabilised) on each clean arc
  give a vertical acceleration of 20.05 (frames 41-48), 19.83, 18.84 (arc with fill rows), 19.50, 19.67 and 19.60 px/frame².
  I used 19.8 px/frame², which is 17820 px/s².
- Scale = 9.8 / 17820 = 5.50e-4 m/px. Sanity check: the ball's diameter of about 76 px comes out at 41.8 mm (a real table-tennis ball is 40 mm). OK.

## Velocity
- Internet convention: forward difference, so v(45) = |p46 - p45| × 30.
- Record: p45 = (1490.1, 472.8), p46 = (1443.3, 521.4). The step is (-46.8, +48.6), which is 67.5 px/frame or 2025 px/s.
- Independent re-segmentation (`seg.py`, raw frames, background frame 170): p45 = (1488.2, 471.5), which agrees within 2 px.
  At frame 46 my blob merged with the kettle handle (frames/seg_46.png). Reading that frame by eye gives a centre of about (1443, 520),
  which matches the record.
- v = 2025 × 5.50e-4 = **1.11 m/s**.

## Second-route check and alternatives
- The fitted arc (vx = -45.1 px/frame, vy from the parabola) gives an instantaneous speed of about 59 px/frame (0.98 m/s) exactly at frame 45.
  The backward difference gives 53 px/frame (0.88 m/s). The forward difference represents the velocity at frame 45.5,
  and the fitted-parabola speed there is about 67 px/frame, so the forward difference is consistent with the fit.
- I answer with the annotators' forward-difference convention: 1.11 m/s. Taking g anywhere between 19.5 and 20.05 px/frame² moves the result by ±1.5%.

Confidence: moderate-high. The main risk is the choice of difference convention.
