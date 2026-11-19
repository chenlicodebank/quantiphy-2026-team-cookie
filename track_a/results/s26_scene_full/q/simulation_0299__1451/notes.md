# q_1451 – forklift width (left wheel to right wheel)

Answer: **1.48 m**. The file and question_fps are both 24 fps, and the track covers the forklift in frames 0–71.

## Method
1. **Motion → metric depth** (`track_lk.py`, `fit_foe.py`, `fit_foe2.py`, `recon.py`). About 190 LK features were tracked on the forklift from frame 0 to frame 71, with a forward-backward check. A pure-translation model was fitted to them: each track runs straight to a common focus of expansion (FOE), and s(t) = ½·a·(t−t0)² with a = 2 m/s² (the prior). The free fit gives exponent 2.00 and t0 ≈ 0.00 s, so s = t² m. The residual is about 1 px, and its shape looks like LK drift, so there is no rotation and no turn. The FOE is at (−1140, −481) px. Each feature gets L = Z0/h_z in metres. For a trial focal length f, this gives the 3D position of every feature. The vehicle frame is: heading h = the FOE ray, up ⟂ h (zero camera roll), lateral = h × up.
2. **Focal length**:
   - depth_info: |O + s·h| = 16.7953 m at s = 1 and 19.0980 m at s = 4. This gives d0 = 16.079 m and an angle of 45.47° to the heading, so the origin is 11.275 m along h and 11.463 m from the h-axis.
   - With the origin at the vehicle's ground-level centre, f ≈ 3476 px reproduces both d1 (16.795) and d2 (19.098); separately they give 3477 and 3475. With the lateral centre taken from the symmetric mast/roof features, f ≈ 3510. A body-centre origin does not fit at any f.
   - Check: the vanishing point of the lateral roof and mast crossbars, set orthogonal to the FOE, gives f = 3400–3540.
   - The mast's lateral verticality would suggest a higher f (~3800), but that clashes with the depth data. The width depends only weakly on f (about 1.2% per 100 px), because the metric scale comes from the motion.
3. **Width** (at f ≈ 3476–3510), as lateral coordinates in metres:
   - Near-side wheels: the features at the most outward lateral position are on the front-wheel hub (lat 7.871) and the near rear tyre (7.895).
   - Far side: the rightmost silhouette point is the far rear wheel. It is back-projected onto the plane of the rear tread (a = 9.93–9.99), giving lat 9.31–9.37, a stable value over frames 15–30.
   - Route A, far minus near: 1.44–1.50 m (1.49 at a0 = 9.99).
   - Route B, symmetry: the vehicle centreline is lat 8.60 from the mast rails and 8.64 from the roof edges. Twice the distance from the centreline to the near wheels gives 1.45–1.52 m.
   - Tracked features alone span only 1.33 m laterally, because no feature lies on the far wheel's outer face. That figure is a lower bound.
4. Answer: 1.48 m (spread 1.44–1.52).

## Confidence
Moderate, about ±4%. The main uncertainties are where exactly the far-wheel silhouette point lies along the heading, and f within 3450–3600.
