# q_2939 – length of the whiteboard (cm)

File fps = question_fps = 24; t = 1.4 s -> frame 34. Lab camera f = 0.5959 x 1280 = 762.8 px, principal point (640,360).
Depth at t=1.4 s: whiteboard centre 2.815 m.

## Method (lines.py, check.py)
- White mask of the board (HSV threshold, largest component) at frame 34; robust line fits to the middle 60 % of
  each of the four mask edges (skipping rounded corners and the two grey knobs on the far corners); corners =
  line intersections. Overlay: frames/lines34.png (fits tight).
- Vanishing points of the two edge pairs back-projected with K: angle between the 3D directions 89.8 deg at
  frame 34 (87.5-90 deg over frames 26-48), confirming f and that the board is a rectangle lying on a plane.
  Plane normal = cross product; plane distance fixed so the board centre (diagonal intersection) is 2.815 m away.
- Corners back-projected onto that plane: frame 34 long edges 0.818 / 0.818 m, short edges 0.634 m.

## Second-route checks
- Method-card route: the midline pixel length (midpoints of the short edges) is 225.8 px, and 2.815 x 225.8 / 762.8 = 0.833 m.
- The same fixed plane applied to frames 26-38 gives L = 0.814-0.822 m, which is stable. It drifts to 0.84 by frame 48, probably
  because of a small error in the plane tilt or lens distortion.
- Earlier coarse fits with the record's quad corners (rectfit.py) gave 0.77-0.80 m. Those corners are less accurate (knobs, rounded corners).
- Velocity prior: the plane-based centre speed near frame 34 is about 1.5-1.6 m/s, against the prior of 1.934 m/s. The reference
  velocity comes from smoothed differences of depth-measured centres, and the recording has a dropped frame at 35->36
  (a double step), which would inflate it. So I did not take the scale from the velocity. If I had, L would be about 0.98 m.
- The static-object depths fit a floor plane only loosely (the trash bin's depth is inconsistent), so they were not used.

## Answer
Length (long horizontal side) = 0.818-0.833 m -> **82 cm**. Width (short side) is about 63.5 cm.
Confidence: moderate-high (about ±3 %), apart from the unexplained gap with the velocity prior.
