# q1339 — average speed of the walking pedestrian, f0–f71 (m/s)

File fps = question_fps = 24, so the frame numbers are unchanged. Static 3D Blender camera, 2160x1080, principal point taken at the image centre.

## Focal length (three independent routes, all ≈ 850 px)
- Vertical vanishing point: pole axes read from zoomed crops (`crops.py`): near traffic-light pole, right traffic-light pole,
  far-left signal pole, left lamp post. They meet at about (1080, 2190), so roll ≈ 0. Taking the horizon at y ≈ 88 from the road VPs:
  f² = (540−88)(2190−540) → f ≈ 864.
- Orthogonal vanishing points (A = road A (621,80), B = road B (3033,96), V = vertical): A·B gives 832, A·V gives 871 and B·V gives 851.
- Pedestrian walk direction from the depth_info (f14 to f38) is closest to parallel to road B at f ≈ 850, where the angle between them is 1.1°
  (`speed.py`). Further from 850 the angle grows: 2.9° at 800, 8.4° at 1000.
- Van check with the prior (a = 4 m/s², from rest): fitting the van's image track (`calib4.py`) gives f ≈ 850–940 with start t0 = 0,
  so the two are consistent. On its own this route is degenerate: f trades off against t0.
- Result: f = 850 ± 20. The pedestrian is about 2.5 scene-metres tall at this f, which is fine because the scene is not at real-world scale.

## Speed
Pelvis track from scene/tracks/pedestrian.csv (head top + 0.47·box height). I fitted a straight, constant-velocity 3D path
P0 + V·t to all 72 frames of reprojected pixels, constrained by the depths 21.0610 m (f14) and 21.3488 m (f38). The fit leaves
residuals of about 1.9 px (x) and 1.3 px (y).
- |V| = 1.208 / 1.214 / 1.219 m/s at f = 870 / 850 / 830. Using only frames ≥ 25 (lower legs no longer behind the trash can) gives 1.219.
- Second route: the plain chord between the depth-anchored points at f14 and f38 is 1.194 m over 1 s, i.e. 1.194 m/s.
- The answer depends only weakly on f: about 3 % over f = 800–1000.
- The per-frame path of the pelvis also includes the walking bob (about +0.5–1 %).

Answer: **1.22 m/s**. Confidence: about ±4 %.
