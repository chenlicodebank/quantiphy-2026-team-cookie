# q_2495 — speed of the tennis ball when it hits the whiteboard (cm/s)

File fps = question_fps = 24. Hit at t=1.24 s -> frame 30 (image y minimum, depth maximum; reversal after 30).
Camera: f = 0.5959*1280 = 763 px, c = (640,360). Depths given: f24 0.901 m, f30 1.144 m, f38 1.027 m (used as Z).

## Measurements (measure.py, plane.py)
- Ball centre per frame 20-42: least-squares circle fit to the HSV mask contour (agrees with scene/ track to <0.2 px).
- Check of scale: area-equivalent diameter x given depth / f = 6.2-6.4 cm vs prior 6.7 cm (SAM mask slightly tight),
  calibration ratio consistent at all three given times (0.93-0.95) -> depths and focal are consistent.
- Route C (main): the ball rolls on the table, so its centre lies on a plane; plane through the three given 3D
  points (normal ~vertical, 0.15 m below camera — physically sensible). Per-frame depth = ray/plane intersection.
  Back-difference 3D speeds (cm/s): f24 114, f25 125, f26 100, f27 121, f28 126, f29 118, f30 52 (contact), then
  rebound ~40-50.  Mean of approach frames 25-29 = 118 cm/s; chord f24->f30 = 107; chord f25->f29 = 116.
- Route A (depth from apparent size, scaled to given depths): noisy per frame, chord 24->30 103, 24->29 120.
- Route B (depth linearly interpolated between the given depths): per-frame 105-111, chord 24->30 107.
- Using depth as Euclidean range instead of Z: ~6 % higher (124 / 110).

## Answer
Approach speed right before impact ~118 cm/s; windows that end at the contact frame 30 give ~104-107.
Answer 115 cm/s (between, weighted to the immediate pre-impact speed). Confidence moderate (±8 %), the main
ambiguity being how the reference's smoothing window treats the impact frame.
