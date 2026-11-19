# Q712 — width of the paving stones (m)

Prior: speed of the black cat = 1.041 m/s. The "cat" is the only black animal; scene/ calls it the "dog". fps = question_fps = 24.
2D top-down view with a static camera, so I used one metres-per-pixel scale for the deck plane.

## Cat pixel speed (measure.py, from scene/tracks/dog.csv)
- Linear-fit slope: cx 5.456 px/frame, body_cx 5.449, bbox_x1 5.457. Mean per-frame path step (with jitter) 5.478.
- Steady walk, so I took 5.455 px/frame × 24 = 130.9 px/s.
- Scale = 1.041 / 130.9 = 0.007951 m/px.

## Paving stones (measure.py, frame 0, joint darkness profiles)
- Vertical joints are at x = 429, 575, 719, 864, 1007, 1154, 1298, 1443, 1588, 1733, 1876. That gives a pitch of (1876 − 429)/10 = 144.7 px.
- Horizontal joints are at y ≈ 77, 341, 603 (staggered between columns). That gives a pitch of ~263 px.
- So the stones are ~144.7 × ~263 px rectangles. Width is the shorter side: 144.7 px.
- The joint lines are only a few px wide. If the gap were subtracted, the width would be ~140 px (−3%).

## Result
Width = 144.7 × 0.007951 = 1.150 m. The length would be ~263 px ≈ 2.09 m.

Second route: the mean per-frame path step (5.478 px/frame) gives 1.146 m. This agrees within 0.5%.
Caveat: the cat's origin sits slightly above the deck. The perspective effect of that height is unmeasurable here and probably small.
Confidence: moderate-high. Answer 1.15 m.
