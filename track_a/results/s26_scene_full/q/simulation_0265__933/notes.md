# q_933 — length of the spacecraft (m)

Prior: acceleration at 1.0 s = 4 m/s^2. 2D top-down render, 24 fps (file fps = question_fps, no re-timing).
The "spacecraft" is the single dark vehicle driving left from rest (frames 0-1 at rest).

## Scale from the prior (fit.py)
Quadratic fits of x(frame) over several windows (7-50, 7-30, 15-35, 30-50) give a constant acceleration:
- bbox centre: 1.194-1.205 px/frame^2; mask centroid: 1.212-1.217; nose 1.22-1.23, tail 1.17-1.19
  (nose/tail differ because the rendered silhouette stretches slowly along x; the centre averages them).
- Vertex at frame ~0 (starts from rest), fit rms 0.1-0.3 px -> uniformly accelerated, so a(1.0 s) = this constant.
- Used 1.208 px/frame^2 = 695.8 px/s^2 -> scale = 4 / 695.8 = 0.005749 m/px.

## Length
Rest length nose-to-rear-pods = 1012-1013 px (frames 7-9, fully in frame, slow; length fit 1011.7 at f=0).
The silhouette grows to 1071 px by frame 50 (stretch with speed); the object's own length is the at-rest value.
Length = 1012 x 0.005749 = 5.82 m.

## Checks
- Using centre-only accel (1.2048) -> 5.83 m; centroid (1.2136) -> 5.79 m. Spread under 1 %.
- Using the stretched length at t = 1.0 s (1026 px) would give 5.90 m (+1.4 %).
- Width 515 px -> 2.96 m, length/width ratio 1.97, plausible for a car-like vehicle.
Confidence: high (~2 %).
