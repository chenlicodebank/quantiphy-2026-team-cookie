# q1375 – acceleration of the white car (white van) at t = 2.0 s (frame 48)

File fps = question_fps = 24, so t = 2.0 s is frame 48. The camera is static (checked in scene/).
The white car is the record's `van`. It starts at rest at the upper right and comes toward the camera, down-left in the image.

## Camera
- Horizon / pitch: from the vanishing points of the kerb lines (kerb.py, vp.py). Kerb lines were fitted to the sidewalk-mask
  boundary; L1/L7 and L2/L5 are collinear edges of one road, and L3/L8 and L4/L6 of the other. The two road
  vanishing points are (-1340,-275) and (2715,-276), so the horizon is at row -275.5 and roll is about 0.
- Focal length: f = 1815 px from the orthogonality of the two road directions (principal point at the image centre).
  Independent check (boxfit.py): a 6 m-long 3D box (the prior) fitted to the van silhouettes puts the van's body centre at 31.85 m
  at f14 for f = 1815 (given 31.28), which implies f ≈ 1775–1795. Used f = 1790. A pedestrian 100 px tall at 37 m comes out 2.0 m, plausible.

## Van track (two routes)
1. Box route (track3.py): globals fitted on frames 6, 14, 20, 58, 60 (camera height 9.64 m, W 1.85, H 1.91, L = 6 fixed), then
   (X, Z, heading) fitted per frame. The near-signal sign region is excluded from the IoU. Heading is constant at about -142°.
   The chord distance from frame 0 fits uniform acceleration from rest at t0 = -0.03 s very well (rms 2 cm):
   a = 4.08 m/s². Cubic and quartic fits give 4.04–4.08 at t = 2.0. The linear fit of per-frame speeds over frames 14–70 gives 4.08.
2. Plane route (track.py, profile.py): the mask centroid intersected with a ground-parallel plane whose height is set from the two van depths
   (f = 1815, horizon -275.5). Uniform-from-rest fit gives a = 4.18; f = 1700–1930 gives 4.06–4.29.
Both routes: the motion has constant acceleration from rest at t = 0, so the acceleration at 2.0 s equals the constant a.

## Unresolved inconsistency
The given van depths (31.283 → 27.720, a 3.56 m approach) imply less approach than my geometry, which gives 3.9 m
(depth ratio 1.1285 against 1.141). The given depths with the centroid rays alone give a displacement of 4.23 m between f14 and f38,
against 4.55 m in the box model. With uniform acceleration from rest, that would mean a ≈ 3.9. The cyclist shows the same
~9% difference (model 4.48 m against the given 4.09 m), and the pedestrian is consistent. A 2° steeper pitch would explain it, but
both road directions put the horizon at -275 ± 10 px (clean kerb lines), so I kept the kerb geometry. A rigid origin
offset of about (2.5 m forward, 3.5 m sideways) also reproduces both depths, and it leaves the acceleration unchanged.
Range: 3.9 (depth-scaled) to 4.18 (plane). Answer: 4.05 m/s², the box route with a slight pull toward the depth-based value.

Confidence: moderate, probably within about 5%.
