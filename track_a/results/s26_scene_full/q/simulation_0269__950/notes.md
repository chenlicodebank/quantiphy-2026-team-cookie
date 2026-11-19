# q_950 — phoenix wingspan (m)

Prior: acceleration of the phoenix at 2.0 s = 2 m/s^2. 2D simulation, fps 24 (file = question_fps, no re-timing).

## Scale from the prior (fit.py, fit2.py)
- Beak x track (scene/tracks/bird.csv, checked as clean): the bird flies left and its per-frame steps rise in stairs
  (~5, ~16, ~25 px/frame), because the body surges inside each flap cycle.
- Model: x(f) = quadratic + 1st and 2nd harmonics of the flap period T (linear least squares, grid over T).
  Beak: a = 0.4138 px/frame^2, T = 25.0 frames, rms residual 0.94 px. The result is the same for frame windows 2–71,
  2–52 and 10–71 (0.4135–0.4155). bbox_cx gives 0.413–0.417 and centroid_x 0.417–0.424.
  -> The origin is uniformly accelerated, a = 0.4138 x 24^2 = 238.3 px/s^2.
- Second route: average speed over whole flap cycles. Frames 2→27: 150 px / 25 = 6.00 px/f. Frames 27→52: 408 / 25 = 16.32 px/f.
  This gives Δv/25 = 0.413 px/f^2, which agrees.
- Scale = 2 / 238.3 = 0.008391 m/px.

## Wingspan (span.py)
- The wings spread along image y. Chroma mask (thresholds 12/18/30) vertical extent at the fully-spread frames:
  frame 21: 622–630, frame 46: 626–634, frame 71: 622–628 px. Taking 628 px (±4).
- The other wing-extension peaks are smaller (~542 px, up-stroke), and the folded minimum is ~238 px.
- I checked the overlay on frame 46: the mask covers both red wing tips, and the grey shadow is excluded.

## Answer
- Wingspan (maximum spread) = 628 x 0.008391 = **5.27 m**.
- Other readings: the folded minimum is 238 px = 2.0 m, and the secondary spread is 542 px = 4.55 m.
- Confidence: good on scale (about 1%) and span (about 1%). The main risk is whether the reference uses the rest-pose bounding box rather than the maximum span in flight.
