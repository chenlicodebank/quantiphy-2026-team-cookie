# q_1929: lampshade height (m)

Prior: black cat speed = 0.94 m/s. No depth_info. fps 24 = question_fps, so no retiming.

## Scale from the cat
- From scene/tracks/cat.csv (the walk is steady, the camera static and the cat never occluded): the net x-step is
  17.64 px/frame (cx), 17.83 (dark_cx) and 17.97 (torso_cx). The 2D path step is 17.86. I used 17.8 px/frame,
  which is 427 px/s.
- That gives 0.94 / 427 = 0.00220 m/px at the cat's depth.

## Lampshade pixel height (measure.py, ellipse.py, frame 0, static object)
- The shade silhouette runs from row 502.3 (top) to 610.5 (bottom), about 108 px.
- The camera looks slightly down: the bench top and the base shelf are seen from above, and the shade's bottom rim
  sags about 6 px at its centre (width 208 px, so b/a ≈ 0.058). The silhouette therefore includes the near half of
  the rim ellipse. The rim-to-rim vertical extent, which is what the bounding box measures, is about 102 px.

## Perspective (the furniture is behind the cat)
- I took the vanishing point of the console's top-face end edges (both rounded corners). It is at about
  (988, 476), so the horizon is at y ≈ 470.
- Ellipse check: the shade rim b/a is 0.058 at y 606, which gives f ≈ 2350 px (HFOV ≈ 44°). That f predicts lamp
  base and vase base sags of 3–4 px, and I measured 3–5 px. Consistent.
- Ground contact rows: the cat's centreline is at y ≈ 1018. The console centre floor is at y ≈ 969 (the base runs
  from about 950 to 989).
- Depth ratio Z_lamp / Z_cat = (1018 − 470) / (969 − 470) ≈ 1.095. Moving the horizon from 430 to 510 changes it
  only from 1.09 to 1.11.
- That gives 0.00220 × 1.095 = 0.00241 m/px at the lamp.

## Answer
- 102 px × 0.00241 ≈ **0.246 m**.
- Other routes, for comparison:
  - Plain 2D, single scale, 108 px silhouette: 0.238 m.
  - Perspective-corrected but with the silhouette uncorrected: 0.260 m.
- The answer sits between these. Confidence is moderate, about ±6%. The main uncertainties are the depth ratio
  (where the lamp origin sits along the console's depth) and the ellipse correction.
