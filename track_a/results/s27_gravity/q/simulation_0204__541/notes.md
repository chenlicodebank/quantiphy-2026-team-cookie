# Q541 – typewriter height (m)

Prior: the magnifying glass falls at 9.8 m/s² before 0.5 s. depth_info is null. The file and the question both use 24 fps.

## Scale from the fall (fit.py)
- I fitted a quadratic to the magnifier's y position over frames 0-11 (scene/tracks/magnifier.csv): centroid gives
  7408-7430 px/s² and bbox centre gives 7445-7453 px/s², so a ≈ 7430 px/s².
  Scale at the magnifier's depth: s = 7430/9.8 = 758 px/m.
- The fall is purely vertical, and the lens is about 103-104 px wide both in flight and at rest. So the glass lands
  at the same depth it fell at.
- Real-scale check: the glass is 0.21 m long with a 0.137 m lens. The typewriter is about 0.41 m wide and about
  0.29 m deep. All of these are plausible.

## The scene is 3D: camera above the desk, looking slightly down
- edges.py and vp.py: the desk's left and right edges, fitted over rows 950-1077 (residual about 1 px), meet at
  (1057, 544.6). That is the image centre, so the camera is level and the horizon is at y = 544.6.
- Check on the focal length: the rim of the resting lens appears as an ellipse with minor/major ≈ 0.18, which
  gives f ≈ 2450 px (about 47° horizontal field of view). With that f, the lens at the horizon (frame 7, y≈524)
  should be seen edge-on, showing only the rim. The track shows a 20-21 px height there, which matches the rim's
  measured height of about 22 px. Consistent.
- Camera height above the desk: Hc = (row of the ground under the glass, 1023.5 − 544.6) / 758 = 0.632 m.
- Because the camera is level, a point at height h above a ground point at row yg satisfies
  h = Hc·(yg − y_top)/(yg − yh). This route does not depend on f.

## Typewriter
- Top of the bounding box: the top edge of the paper rest at row 861 (vp.py).
- Bottom: the base sits on the desk. The front edge of the base touches the ground at row ≈1029. The base's right
  side edge runs toward the vanishing point and ends at its back corner, (800, 989).
- The paper rest stands roughly upright behind the platen, possibly leaning back slightly (rest.py: its width
  narrows by about 1-2 % toward the top). I placed its top 60-100 % of the way back in the typewriter's depth,
  i.e. at a ground row between 1004 and 989, with best estimate 80 % → row 996.5:
  - h = 0.632 × (996.5 − 861)/451.9 = **0.189 m**
  - range 0.182 (top above the back edge) to 0.197 (60 % back)
- For comparison, the naive flat 2D conversion (172 px / 758) gives 0.227 m. That figure is too large because it
  counts the depth of the top deck seen from above.

## Confidence
Moderate, roughly ±5-8 %. The horizon, the focal length and the edge-on rim all agree with each other. The main
remaining uncertainty is how far back the top edge of the paper rest sits.
