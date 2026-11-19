# q_2952 — speed of the red car (m/s); prior lane width = 3.66 m

Time base: file is 24 fps (44 frames), question_fps = 30 -> per-frame displacements converted with 30 fps
(benchmark convention). File rate noted: 24 fps.

## Method (measure.py)
- Camera static (scene record: dash shift < 0.5 px), nadir view, 2D: one m/px scale from the lane width.
- Lane width: per-pixel temporal median background (cars removed), fit a line to each of the 6 dash rows.
  Red car's lane (rows y≈330 and y≈437, centre to centre): 107.0 px (105.9–108.0 along x); mean of all 5 lanes
  105.95 px. Scale = 3.66 / 107.0 = 0.03421 m/px. (Fits on single frames were biased by cars — discarded.)
- Red car track (scene/tracks/red_pickup_mid_lane.csv, verified on frame 12 overlay/grid): fully in view f0–f36.
  Net centroid displacement f0->f36 = 1021.5 px (2D incl. slight downward drift) over 36 frames = 28.38 px/frame;
  mean of per-frame steps = 28.42 px/frame. Duplicate frames (3,8,14,19,25,30,36) give 0 steps; non-duplicate steps
  ≈ 35.2 px.
- Speed = 28.42 px/frame x 30 fps x 0.03421 m/px = 29.2 m/s (≈105 km/h).

## Checks
- Second route: rear bumper (x_left) and front bumper (x_right) give 28.47 and 28.33 px/frame -> 29.2 / 29.1 m/s.
- Using the 5-lane mean width (105.95 px): 29.5 m/s.
- Alternatives (not chosen): file rate 24 fps -> 23.3 m/s; non-duplicate step only x 30 -> 36.1 m/s.

Answer: 29.2 m/s. Confidence: moderate (scale ±2%; main uncertainty is the frame-rate / duplicate-frame convention).
