# Q1527 – height of the striped collision-warning (corner-guard) marking on the pillar

Video: 3D Blender render, 24 fps (file fps = question_fps = 24, no re-timing issue), static level camera.
Prior: tyre diameter 0.764 m. depth_info at t=0.5 s (frame 12): left-front tyre 11.38 m, B1 sign 23.44 m.

## Object
The only collision-warning markings are the striped corner guards at the floor on the pillar corners
(rendered black/yellow; the question calls them black-and-white). The two clearly visible ones are on the
front corners of the left and right mid pillars (x 388-397 and 1526-1536); both are at the same depth and
give identical pixel extents (stripes.py, stripes2.py, guard.py, on frames 0 and 41):
top edge y = 650.0, bottom (floor contact) y = 773.0 → 123 px tall; 4 yellow + 5 black bands.

## Geometry (all measured in code)
- Horizon / vanishing point of the aisle (ceiling light tubes, vp.py): (959.7, 539.2).
- Tyre (rimfit.py, rays.py, overlay.py with circles drawn on frames 24 and 30): rim centre y ≈ 790
  (789.5 / 789.6 / 792.0 / 791.4 in f24 rear, f30, f24 front, f12); tyre outer radius R = 92.5 px
  (overlay circle R=93 follows the tyre outline; contact with floor y ≈ 883). Diameter ≈ 185 px.
  (The scene record's "~175 px" was too small – it stopped at the yellow-tinted rim of the tyre.)
- Camera height from the tyre (wheel centre at 0.382 m, contact on floor):
  h = 0.382 × (y_contact − y_h)/R = 0.382 × 343.8/92.5 = 1.420 m.
- Focal length: f = R·Z/0.382 with Z = 11.38/sqrt(1+((u−cx)²+(v−cy)²)/f²) at frame 12 (u,v = 1656.7, 791.4)
  → f ≈ 2654 px (hFOV ≈ 40°), Z_tyre ≈ 10.96 m.
- Pillar corner depth Z_p = f·h/(773 − 539.2) = 16.1 m.
- Marking height = 123 px × Z_p / f = h × 123/233.8 = **0.747 m**.

## Second route (B1 sign depth)
Back-wall floor line y ≈ 700-705 (glossy floor reflection makes it ±3 px). With the given 23.44 m:
f·h = 23.44 × 164.8 = 3863 (vs 3768 from the tyre depth, 2.5 % apart). Using it with f = 2654 gives
h = 1.456 m → marking 0.766 m. Predicted wall distance from route 1 = 22.9 m vs given 23.44 (−2.4 %).

## Answer
0.75 m (tyre route 0.747 weighted over the wall route 0.766). Main uncertainty: tyre pixel radius
(±1 px ≈ ±1 %) and the 2.5 % tyre/wall disagreement. Confidence: good, about ±3 %.
