# q1472 — width (wingspan) of the plane

- The file is 24 fps; question_fps is 25. t=1 s is frame 25 and t=2 s is frame 50 (frame indices from the scene track).
- What the video shows: the craft is seen from **behind and below**, flying away. Its horizontal image extent runs
  wingtip fin to wingtip fin, so it is the **wingspan**, which is the asked width. scene/notes.md calls it a side view
  with the nose to the right; that is wrong. The canopy is in the middle and there are fins at both wingtips.
- Focal length, from the prior: the speed is 22.16 m/s, so the plane covers 22.16 m between frames 25 and 50.
  I back-projected the bbox centre and the mask centroid with the given ranges (102.67 m and 121.83 m) and solved
  |P50 − P25| = 22.16 m. Result: f = 3425 px (bbox centre) or 3472 px (centroid). Scripts: solve.py and fit_line.py.
  A pure straight-line image fit gives no usable f (ill-conditioned).
- Naive width = bbox_w × z / f: 17.0–17.2 m at frame 25 and 17.6–18.0 m at frame 50. It keeps rising, from 16.2 m
  at frame 0 to 18.2 m at frame 71. The cause is foreshortening: the span is seen obliquely, and the angle eases as
  the line of sight swings with the left/up motion. The fuselage-like structure runs diagonally toward the tail,
  which is consistent with this.
- Fix (fit_heading.py): 3D positions on the constant-speed line through the two given depths. I fitted a horizontal
  span vector of fixed direction and length W so that its projected pixel length matches bbox_w in frames 2–71.
  Result: W = 18.4–18.6 m, span yawed 23° from the image plane, rms 0.6 px over 70 frames.
- Second route (foreshort.py): assume the heading equals the velocity, so the span is perpendicular to it. Then W
  is 19.1–20.2 m, falling over the clip, which means this overcorrects. The naive range, 16.2–18.2 m, is a lower
  bound. The fitted 18.5 m lies between the two.
- Answer: **18.5 m**. Confidence is moderate, about ±7%. The main uncertainties are the yaw of the plane and the
  focal length from the speed route: a 1% error in the speed changes f by about 2%.
