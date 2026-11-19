# q1986 — length of the deer (m)

Prior: deer speed = 1.277 m/s. No depth_info. Both the file and the question run at 30 fps.
The "deer" is the large horned quadruped in scene/ (track creature.csv). It walks side-on, left to right, at a constant depth:
its foot row and its height (428–439 px) stay constant, so one metres-per-pixel scale applies.

## Measurements (m.py, from scene/tracks/creature.csv, checked against the contact sheet frames/sheet.png)
- Pixel speed: linear fit of the mask centroid x = 7.90 px/frame. Over full gait cycles (40-frame windows) it is 7.86–7.89, and
  the muzzle edge (bbox x1) gives 7.95–8.07. Taken as 7.92 px/frame, i.e. 237.6 px/s.
- Scale: 1.277 / 237.6 = 0.005375 m/px.
- Length = horizontal bbox extent from tail tip to muzzle: mean 580 px, median 580, range 542–617 because the tail and legs swing.
- Length = 580 × 0.005375 = 3.12 m (range 2.91–3.32 m over the gait).

## Check
- Using only the muzzle-edge speed (8.0 px/frame) gives 3.09 m. Using only the centroid speed (7.90) gives 3.125 m.
- The answer depends on a ratio of pixel length to pixel speed, so it does not depend on the focal length or depth.

Confidence: moderate. The main uncertainty is which pose the reference AABB used, about ±5%.
