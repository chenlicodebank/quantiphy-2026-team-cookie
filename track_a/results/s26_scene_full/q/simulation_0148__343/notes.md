# Q343 — speed of the train at t = 1 s (m/s)

Prior: side window width = 1.8 m. No depth_info. fps = question_fps = 24, so t = 1 s is frame 24.
The train is visible only in frames 2-20 and is gone by frame 21, so the speed at frame 24 has to be extrapolated.

## Method (scripts in this folder)
- `edges.py` finds window edges in the band y 540-680. `gasket.py` measures 11 fully visible side windows
  (frames 7-17). On each side it finds the dark rubber-gasket centre (sub-pixel minimum) and the glass edge.
  Gasket-centre widths are 352.6-364.8 px (mean 358.0) and glass widths are 346-357 px (mean 351.5).
  The pixel width grows slightly with x (0.008 px/px) and with time (0.77 px/frame). The camera scale is not
  perfectly constant: the train side is a little oblique and gets a little closer over time.
- `speed.py` tracks the same gasket edges between consecutive frames. This gives 14 shifts: 358.4 px (f8) up to
  389.5 px (f17). These agree with the record's near-layer line d(i) = 334.1 + 3.2 i. Each shift is divided by the
  window width fitted at the same x and time, so the scale is local and comes from the same near-side layer.
  The ratio shift/width rises linearly: 1.017 at f8 to 1.078 at f17 (rms 0.003). That means constant acceleration
  of about 6.9 m/s².
- v(i) = 1.8 m × ratio(i) × 24. The linear extrapolation of the ratio to frame 24 is 1.123, so v ≈ 48.5 m/s
  using the gasket-centre width.

## Second route / checks
- Using the record's raw shift line (d24 = 410.9 px) with a constant width gives 50.5 m/s with the glass width
  (351.5) and 49.6 m/s with the gasket width (358). This route ignores the slow growth in scale, so it is a little high.
- If the glass width is taken as "window width" instead of the gasket centre, the answer is about 1.8 % higher (49.4).
- Final answer: 48.8 m/s, a compromise between the two width definitions.

## Confidence
Moderate. The main risks are the extrapolation over 7 frames past the last measurement, assuming the acceleration
stays constant (the measured speeds are very linear, rms 0.3 %), and which edges define the window width (±2 %).
