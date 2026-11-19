# q_1072 – length of the cart's rectangular cargo box

The file and the question both run at 24 fps. The camera is static. The image is 1920x1954, and I assume the principal point is at the image centre (960, 977).
The "nest" in depth_info is the dark hairy ball (a bird's nest) that falls from the branch. Depths: nest 5.661 m (t=0) and 5.630 m (t=1), cart 27.562 m.

## Focal length (two independent routes)
1. **Gravity** (`acc.py`, `fit2.py`). I took the nest centroid from scene/tracks and used frames 33–48, where the nest is free of the branch and in clean free fall.
   - A quadratic fit of the vertical position gives 6.0–7.0 px/frame², about 3700 px/s². The fall starts from rest at about frame 30.
   - Nest depth along the camera axis is about 5.1 m at release (from the given 5.63 m distance and its ray) and about 5.3 m at rest. The rest depth comes from the ground plane: cart wheel ground contact at row 1248 at the cart's depth, horizon at row 1090.
   - A 3D free-fall fit with that depth path gives f = 1970–2230 px, centre about 2100.
2. **Barn vanishing points** (`beams.py`, `siderail.py`). This route does not use gravity.
   - Two horizontal beams on the front wall (rows 861 and 945) converge to a vanishing point about 12,200 px left of centre, on a horizon at row about 1090. That horizon matches the ground-plane estimate.
   - The side-wall rail and the side roof eave descend with slope about 0.6, which puts their vanishing point about 240–370 px right of centre.
   - For two perpendicular directions, f² = 12170 × (240–370), so f ≈ 1700–2100.

I used f ≈ 2050 px, which corresponds to a horizontal field of view of about 50°.
Consistency check: camera height is about 2.1 m, the nest's branch is about 3.8 m above the ground, and a 3.3 m drop takes 0.82 s, which matches release at about frame 30 and impact at frame 49.5.
**Caveat on realism:** at this scale the barn assets are oversized. The cart wheel diameter would be about 2.6 m, the barrels about 2.4 m tall and the barn door about 5.5 m tall. At real-world sizes they would imply f ≈ 4000–5000.
I nevertheless kept f ≈ 2050, because two independent routes agree on it and neither is compatible with 4000–5000: gravity would need roughly 0.4 g, and the side-wall slope would need to be about 0.09.
So I conclude the farm assets are built at about twice real size, and the answer is in scene (Blender) units.

## Box pixel length (`boxedge.py`, frame 72)
- The near-side top edge of the box is a straight line from (1257, 1096) to (1566, 1017), giving 319 px along the box axis. The box is tilted about 14° because the shafts rest on the ground.
- The outer extent along the axis, including the bottom-left and rear-bottom corners, is about 348 px. The horizontal image extent from x 1257 to 1597 is 340 px.
- I used 330 ± 15 px.
- The cart's camera-axis depth is Z = 27.562 / 1.028 = 26.8 m. Yaw is near zero: the wheel appears almost circular, 192 × 186 px.

L = 330 × 26.8 / 2050 ≈ **4.3 m**. The range is 4.1 m (319 px) to 4.5 m (348 px), and f uncertainty adds about ±8 %.
If the realistic-asset scale (f ≈ 4500) were true instead, the answer would be about 2.0 m. I rejected that scale for the reasons above.

Confidence: moderate. The main uncertainty is f (±10 %) and which box outline the reference answer uses.
