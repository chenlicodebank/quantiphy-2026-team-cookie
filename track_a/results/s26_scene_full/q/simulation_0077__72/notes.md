# Q72: distance between the black-shirt and white-shirt persons at t = 2.0 s (frame 48)

The view is top-down and both people walk on the same floor, so I treated it as 2D with one scale (fps 24 = question_fps).
- Scale from the prior: black-shirt torso speed is 11.47 px/frame on average over frames 3–71 (median 11.41, and 11.2–11.9 around frame 48).
  That is 275.4 px/s = 1 m/s, so 1 m = 275.4 px.
- Frame 48 positions, torso centroids from scene/tracks, checked on frames/f48.png: black (1544.7, 414.5), white (298.5, 606.4).
  Distance = 1260.9 px, which gives **4.58 m**.
- Second route: the head points give 1357 px / (12.12 px/frame × 24) = 4.66 m (+2%). The perspective magnification cancels in the
  ratio of distance to speed, because both points sit at a similar height. The pelvis is probably a little lower, which changes the result negligibly.
- Confidence: high, about ±3%. The script is measure.py.
