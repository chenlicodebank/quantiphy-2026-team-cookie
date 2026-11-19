Box centroid tracked every frame (colour mask, IoU 0.94 with scene masks; silhouette is centrally symmetric so centroid = box centre). Straight-line path along the groove; duplicate frames f11/f28 handled. Savitzky-Golay/local quadratic fits give a(1.75 s, frame 42) = 657 px/s^2 (acceleration falls from ~900 to a 657 plateau; global quadratic 750). Scale from the prior: the box's slope-parallel side projects to ~86.5 px (zonotope/support-function fit, 84-90 px over the clip; the box is a cuboid, not a cube), so 0.611/86.5 = 0.00706 m/px. Answer 657 x 0.00706 = 4.64 m/s^2. Second route: a(v)=a0-kv^2 extrapolates to a0=994 px/s^2 = 7.0 m/s^2, matching g*sin(44.2 deg)=6.8 m/s^2 from the slope angle in the image, confirming the scale.

Final message:
Answered question 862: **4.6 m/s²**.

Method summary:
- **Track**: colour-masked box centroid on all 45 frames (IoU 0.94–0.95 vs the scene masks; the silhouette is a centrally symmetric zonotope, so its centroid is the box centre). Path is straight; duplicate frames f11/f28 identified and f27 excluded.
- **Acceleration**: the acceleration is not constant — it falls from ~900 px/s² to a plateau of ~657 px/s². Local quadratic fits around frame 42 (t = 1.75 s) give 590–657 px/s² (rms 0.3 px); Savitzky–Golay gives 657 px/s².
- **Scale**: the box is a cuboid (a cube is geometrically impossible here). The slope-parallel side projects to ~86.5 px (support-function/zonotope fit, 84–90 px), and the motion shares that same 3D direction, so scale = 0.611/86.5 = 0.00706 m/px.
- **Check**: fitting a(v) = a₀ − k v² extrapolates to a₀ ≈ 994 px/s² ≈ 7.0 m/s², matching g·sin(44.2°) = 6.8 m/s² from the slope angle read off the groove line — a 3 % agreement that validates the scale.

657 px/s² × 0.00706 m/px ≈ **4.6 m/s²**.
