# Q314: horizontal distance of the apple's parabolic flight (m)

The video is a 2D sim at 120 fps (file fps = question_fps). The prior is g = 9.8 m/s². There is no depth_info.

## Method (fit.py, using scene/tracks/apple.csv circle-fit centres)
- Free-fall window frames 143–191 (the apple has left the counter; frame 192 is the floor impact).
  A quadratic fit of y(frame) gives a = 0.4434 px/frame² (rms 0.8 px). Other windows (146–191, 150–191, 160–191, 145–180)
  give 0.438–0.447.
- Scale = 9.8 / (0.4434 · 120²) = 0.001535 m/px (range 0.00152–0.00155).
  Check: apple diameter 61 px → 9.4 cm, a realistic apple.
- Horizontal velocity is constant at −3.61 px/frame through the flight.
- Start of flight: the extrapolated parabola vertex is at frame 137.6 (x ≈ 382). Counter top-left edge on frame 0: it runs
  from (380,1130) to (353,1165); at the apple's contact height it is at x ≈ 376, so the centre passes it at about frame 139.
  The apple then pivots briefly and leaves the edge at about frame 140 (x ≈ 373).
- End: the parabola reaches the floor rest height (y ≈ 1743–1744) at frame 191.3 (x ≈ 187.1).
- Horizontal distance ≈ 373 − 187 = 186 px → 0.286 m.

## Uncertainty / second route
- Start = vertex at 137.6 → 195 px → 0.300 m. Start = frame 141 → 182 px → 0.280 m. Chosen answer: 0.286 m.
- Scale spread across fit windows is ±1%.
- Confidence: moderate-good (±5%).
