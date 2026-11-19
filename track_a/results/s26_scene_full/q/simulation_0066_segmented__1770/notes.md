# q_1770: diameter of the bicycle wheel (m). Answer: 0.66 m

Video: 3D Blender segmentation render, 2160x1080, 24 fps (same as question_fps), static camera.
Prior: the white van's acceleration is 4 m/s². depth_info gives the bike's distance at t=0.58 s (frame 14) as 19.065 m and at t=1.58 s (frame 38) as 14.6515 m.

## Focal length (the main uncertainty)
Depth-only routes are weak here. The van and bike move mostly toward the camera, so their displacement barely depends on f:
- Van acceleration fit with a = 4 gives f ≈ 1000–1300, but this is poorly conditioned.
- The ground-plane (horizontal displacement) test gives inconsistent results between objects.

So f was taken from image geometry, assuming no camera roll and the principal point at the image centre:
1. **Purple sedan rims** (`radial.py`, `purfit.py`, `purfit2.py`). The car is static, so the rims are sharp. Each rim was fitted as an ellipse from sub-pixel radial edges:
   - rear: ratio 0.544, minor-axis angle 86.2°
   - front: ratio 0.647, minor-axis angle 82.3°

   The model treats each rim as a circle in the vertical side plane. That plane contains the car axis, whose vanishing point is where the hub line meets the horizon.
   - All 4 numbers fit with chi² ≈ 0.4, but f trades off against the horizon row yh: **f ≈ 900 − 0.75·yh**.
2. **Sidewalk corner** (`sidewalk.py`, `perp.py`). Two perpendicular ground edges: one runs toward the van's vanishing point, the other is parallel to the purple sedan. This gives f ≈ 880–950 (for yh 0–40).
3. **Bike front-wheel ellipse orientation**, frames 56–71 (`bikeang.py`): f ≈ 950 − yh.
4. **Pedestrian body lean** (`pedlean.py`): f ≈ 920–1110. This is a soft cue (posture).

Horizon: the cues disagree, giving yh between about 10 and 60.
- The van and bike image tracks intersect at about (593, 55).
- The van depth geometry gives about 10–25.
- The bike depth geometry gives about 60–85.

Result: f ≈ 855–915 px (hFOV ≈ 100–103°).

## Wheel
- **Pixel size** (`wheellib.py`, `bikewheels.py`): the front-wheel silhouette ellipse, fitted with RANSAC on frames 53–71 (before frame 53 the wheel merges with the legs and van). The major axis grows from 53 to 81 px.
  - The threshold choice was checked against a sub-pixel gradient edge (`edgecheck.py`): median ratio 1.00, so no bias.
- **Hub 3D track** (`diam.py`, `diam2.py`): the hub moves as H0 + v·t, with constant bike speed (the fitted acceleration is ≈ 0).
  - Variant 1: v from the given bike distances at frames 14 and 38 and the origin proxy pixel (centroid, or lowest wheel point).
  - Variant 2: v direction from the hub-track vanishing point; speed from |19.065·u14 + s·d| = 14.6515.
  - H0 is fitted to the hub (ellipse centre) track; track rms is 0.6–1.9 px depending on variant and proxy.
- **Diameter**: each frame's measured major axis divided by the projected major axis of a 1 m circle at the hub (exact pinhole projection, which includes off-axis stretch). The median is taken over frames.

## Results (`diam_grid.py`, along the rim curve f = 900 − 0.75·yh)

| yh | f | v1-cx | v2-cx | v1-bottom | v2-bottom | mean |
|---|---|---|---|---|---|---|
| 0 | 900 | 0.624 | 0.691 | 0.650 | 0.712 | 0.669 |
| 40 | 870 | 0.639 | 0.668 | 0.666 | 0.687 | 0.665 |
| 60 | 855 | 0.648 | 0.656 | 0.675 | 0.674 | 0.663 |

- The two variants agree with each other at yh ≈ 60–65, giving 0.65 (centroid proxy) and 0.675 (bottom proxy).
- The 4-way mean is stable at 0.66–0.67 across the curve.
- Answer: **0.66 m**, which is plausible for a 26–28 inch wheel with tyre.

Confidence: moderate. The estimated uncertainty is about ±5%; it is dominated by the focal length and horizon, and by the choice of the bike's origin proxy pixel.
The scene/ record's cyclist track was used only for proxies at frames 14 and 38; the wheel ellipses were measured fresh.
