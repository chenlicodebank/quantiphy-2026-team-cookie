# Q1766 — height of the white car (the white van), metres

Answer: **2.14 m**

The video and the question both run at 24 fps (frame = round(t·24)). The depth times 0.58 s and 1.58 s are frames 14 and 38.
The white car is the white van (the `van` track in scene/). The scene is a 3D Blender render with a static camera.

## Method
1. **Van motion direction.** I tracked 118 LK features on the van (`track_van.py`). The van moves in a straight line with no rotation.
   - The feature tracks meet at the vanishing point VP_u = (613, 72) px (`fit_vp.py`; median line distance 0.7 px).
   - I also fitted each track with a 1D projective model x(t) = (A + B t²)/(1 + C t²), which assumes a uniform acceleration starting at t0 = 0. It gives the same VP (`vp_proj.py`).
   - A scan over t0 gives a best fit at t0 = 0.00 s. So s(t) = ½·4·t² (the prior a = 4 m/s², starting from rest at frame 0).
2. **Focal length from vanishing points** (`sidewalk.py`, `ground_lines.py`, `calib.py`).
   - The sidewalk's long edge, extrapolated about 1000 px, passes within 2.7 px of VP_u. So the van drives parallel to that edge.
   - Three lines meet at a second ground vanishing point, VP_b = (3209, 47), within a few px: the sidewalk's perpendicular top edge, the purple sedan's wheel-tangent line and the green sedan's wheel-tangent line.
   - Orthogonality of the two directions gives f = sqrt(-(VP_u - c)·(VP_b - c)) = **872 px** (hfov ≈ 102°), with the principal point at the image centre.
   - The horizon is almost level (roll ≈ 0.6°). Assuming zero roll instead gives f = 846–860.
   - The ground normal is the cross product of the two vanishing directions (pitch ≈ 28° down).
3. **Metric 3D of the van** (`vanlib.py`, `sfm.py`). I triangulated each feature using the known metric translation s(t)·m, where m is the motion direction from VP_u. Reprojection error is 0.8 px median.
   - Coordinates are (height along the ground normal, along the motion, lateral), relative to the camera.
4. **Roof** (`roof.py`, `roof_perframe.py`).
   - I took the topmost point of the van silhouette (mask = non-white pixels below 250, connected component) at frames 12–69, every 3 frames, and triangulated it as one point.
   - Result: the far-rear roof corner at h = **−4.687 m**, rms 2.5 px.
   - Heights implied frame by frame agree from far to near views (−4.687 / −4.701 / −4.670), so it is a real top point and not a sliding tangent.
   - A fitted-line virtual corner gives −4.77.
5. **Ground** (`ground.py`, `ground_perframe.py`).
   - I triangulated the lowest silhouette pixel of the rear-left tire over 20 frames: h = **−6.85 m** (best per-frame consistency at −6.83 to −6.85, sd 0.024 m).
   - The camera is therefore about 6.84 m above the ground.
6. **Height** = −4.69 − (−6.84) ≈ **2.15 m**.
   - Roof reading: 2.06 (fitted corner) to 2.16 (topmost).
   - Focal length: f = 845 / 872 / 900 gives 2.19 / 2.16 / 2.13 (`sens.py`). H depends only weakly on f.
   - Final answer: 2.14.

## Checks
- **Independent check with the pedestrian's given depths** (`ped_check2.py`).
  - With this camera (f, ground normal, camera height 6.83 m) I placed the walker's pelvis point vertically above the feet, on the centroid ray.
  - On 12 clean frames near t = 0.58 s and 1.58 s, its distance matches the given depths with a mean ratio of 1.0014 (sd 0.007). This confirms the metric scale.
  - The walker's implied standing height is 1.85 m, which is plausible.
- **Van depth_info.** One fixed point on the van, about 1.3 m behind the box centre (near the rear axle), reproduces both given depths, 23.59 m and 19.99 m. The centre-feature depth ratios alone show the van's origin is not at its geometric centre. This does not affect the height.
- **Sanity check.** Other dimensions come out at length ≈ 6.0 m and width ≈ 2.0 m, close to a full-size van (Chevy Express-like, real height about 2.1 m).

## Confidence
Moderate to high. The estimated error is about ±4%. The main sources are where the roof top sits (rounded roof edge) and the exact ground contact.
