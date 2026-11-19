# q_1651 — height of the person (m)

File fps 33 = question_fps 33.

## Method
- Prior: person speed 1.3 m/s. depth_info: d(t=0, frame 0) = 5.424 m, d(t=1, frame 33) = 4.886 m.
- Pixel speed (scene/tracks/person.csv; checked with speed.py): head_cx between gait-matched mid-stance frames 6 and 90
  gives 7.648 px/frame = 252.4 px/s. Linear fits over different windows give 7.59-7.79 px/frame, and the fit over 0-100 gives 7.63.
- Scale at the person's depth: 1.3 / 252.4 = 0.005151 m/px.
- Check that the motion is parallel to the image plane (constant Z):
  - From d1 and pelvis u = 252 at frame 33: Z = 4.656 m and f = 904 px.
  - Using the same Z, the predicted d0 at u0 = -1.5 is 5.426 m, against 5.424 m given. The depths and the speed agree, so
    the motion is lateral at constant depth.
- solve.py is a second route: a general 3D fit with P = d·ray at frames 0 and 33 and |P1 - P0| = 1.3. It gives f = 910 and Z ≈ 4.66, with nearly equal Z at
  both ends, and a height of 1.865 m. That route is sensitive to the extrapolated pelvis x at frame 0 (±8 px gives 1.80-1.94).
- Height in pixels: frames 4-7 (mid-stance, foot visible left of the bench) run from head top y = 368 to sole y = 731,
  which is 363-364 px. I checked this on a zoomed frame 6 (frames/f6.png).
- Height = 364 × 0.005151 = 1.875 m. Rest standing height may be about 0.5-1% more than the walking mid-stance height.

## Answer
1.88 m. Confidence: good (±3%).
