# q_2179 — basketball velocity at t = 1.8 s (captured_0009)

Question fps 24 = file fps. t = 1.8 s -> frame 43 (t = 1.7917 s). The ball is rising after the bounce (bounce frame 37, apex frame 46 ≈ 1.92 s,
matching the depth_info note "t=1.92s (max rebounce)").

## Measurements (measure.py -> meas.json)
I re-measured frames 33–48 with an HSV mask limited to the ball region (R−B≥50, R−G≥45), then fitted a circle to the contour.
The centres agree with scene/tracks/ball.csv to within about 1 px. Frame 43: centre (529.4, 503.9), D = 104 px. Frame 46: (528.0, 480.4), D = 107 px.
In image y the apex falls at frame 46.0 (zero crossing of the steps). The apparent diameter grows from 95 px (frame 38) to 107 px (frame 46),
so the ball moves toward the camera as it rises (the oblique, downward-looking camera sees part of the vertical motion along the view ray).

## Routes (analyze.py: quadratic 3D fit of frames 38–48)
- A: lab card, back-projected with the given depth (1.5835 m at 1.8 s and 1.5795 m at 1.92 s, nearly constant).
  The fitted |a| is only 5.6 m/s², which contradicts the exact prior of 9.8. The speed at frame 43 is 0.64 (forward difference),
  0.74 (fit) or 0.78 (centred over 5 frames). The given depths miss the ball's motion along the view ray, and the scale/size cues are
  inconsistent (Z ∝ 1/D gives a ball of 0.216 m at 1.5835 m but 0.252 m at frame 0 with 1.321 m).
- B: size-based depth (Z ∝ 1/D) anchored at 1.5835 m at frame 43: |a| = 7.0, v43 = 0.99 (fit), 0.82 (forward difference).
- C: size-based depth with the scale set so that |a| = 9.8 (the prior): v at frame 43 = 1.39 (instantaneous fit), about 1.15 (forward
  difference 43->44). The fitted apex is at about 1.93 s.
- D: physics with the prior and the given apex time: v = g (t_apex − t) = 9.8 × (1.92 − 1.8) = 1.18 m/s. At frame 43 exactly (1.7917 s)
  this is 1.26. Forward-difference convention (centred at 43.5): 1.05.

## Answer
Routes C and D agree once the scale is set by the prior (g = 9.8): roughly 1.05–1.39 depending on the differencing convention, with a centre
near 1.2. The given-depth route A cannot reproduce the prior acceleration, so I did not use it.
Answer: **1.2 m/s**. Confidence: moderate. The main risk is that the reference used the near-constant sensor depth, which would give about 0.75.
