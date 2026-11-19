# q_551 — speed of the typewriter at t = 0.125 s

question_fps = file fps = 24, so t = 0.125 s is frame 3. Speed = |p3 - p2| x 24 (backward difference).
Prior: free fall at 9.8 m/s^2 before 0.45 s (frames 0-10, impact between 10 and 11), so the scale is
9.8 m/s^2 / (pixel acceleration).

## Method (fit.py)
Used scene/tracks/typewriter.csv (I checked the tracker: background differencing, box fits the typewriter
during the fall). Fitted quadratics y(frame) to the bbox centre, top, bottom and mask centroid over
frames 0-9 / 1-9 / 0-8 / 2-8.
- bbox centre: a = 12.6-13.0 px/frame^2; fitted p3-p2 = 31.1-32.3 px (raw 32.5) -> v = 0.98-1.05 m/s
- top / bottom edges: 1.06-1.10 / 0.91-1.02 m/s (the box height grows as the view changes, so the edges
  move at slightly different rates; the centre averages that out)
- centroid: 0.97-1.06 m/s
Note v = (p3-p2)/a_px x 9.8/24, so the m/px scale cancels out.

## Second-route check
The fitted parabola has its vertex (zero velocity) at frame ~0.0 (-0.07 to +0.10), so the typewriter is
released from rest at t = 0. Ideal kinematics then give a backward-difference speed at frame 3 of
g x 2.5/24 = 1.021 m/s, which agrees with the centre fits (1.02-1.05).

Answer: 1.03 m/s. Confidence: high (about ±4%).
