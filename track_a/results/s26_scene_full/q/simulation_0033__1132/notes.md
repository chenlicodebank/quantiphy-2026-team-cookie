# q_1132: height of the fire hydrant (m), simulation_0033 (3D Blender render)

Answer: **0.923 m**

The file runs at 30.005 fps and the question at 30 fps. Frame indices from the scene/ track were used, and every time conversion uses 30 fps.

## Focal length (from the orange car: the prior plus depth_info)
- The camera is static and level, with the principal point assumed at (540, 540). The orange car stays at a constant camera-Z (its apparent size does not change), so its pixel x is linear in world X.
- Car origin track: axle midpoint, ref_x from scene/tracks/orange_car.csv, frames 10-53, interpolated rows excluded. A free quadratic fit gives a = 0.522 px/frame² (470 px/s²). The front- and rear-wheel tracks give 0.53-0.54, and the rear bumper gives 0.51.
- Joint solution: I fixed the pixel acceleration at 2.86 / k (k = metres per pixel at the car's depth), fitted x(f), and solved for k so that k²[(u0-cx)² - (u30-cx)²] = 12.048² - 10.432². This gives k = 0.00618-0.00628 m/px. Accel alone gives ≈ 0.00602-0.0061, so the two routes agree within about 3%.
- Z_car = sqrt(10.432² - k²·r30²), which gives Z ≈ 10.06-10.24 m depending on the origin height (y = 862, 929 or 982) and the origin x (axle midpoint or box centre). That makes f = 1600-1657 px; I used **f ≈ 1630 px**.
- Sanity checks at f = 1630: the pedestrian is about 1.76 m tall (217 px at Z ≈ 13.2 m). The car is 4.9 m long and 1.5 m high, with a 3.2 m wheelbase. The ground-line geometry is consistent: camera height about 2.75 m above the road, sidewalk about 0.24 m high, and a curb depth that matches the curb's top and bottom edges within 1%.
- The pedestrian's two depths would give f ≈ 1350, but that is inconsistent: at f = 1630 the implied Z exceeds the given distance. The person probably also moves in depth, so this route was rejected.

## Hydrant pixel height (frames 5, 15 and 20, measured in code in hyd_edges.py)
- Cap: it has a flat, very low-domed top disc. The far-rim silhouette is at y = 753.5 and the front rim edge at 760.5. The minor axis is 7 px, matching the expected 6.6 px for a 25 px cap radius, so the top centre is at **757.0**.
- Base flange: it spans x 61.5-123.5 (radius 31 px, axis u = 92.5), and its front-bottom edge is at y = 890 (contact shadow at 891). Correcting the near-edge perspective by (y-cy)·R/(Z-R) puts the bottom centre at **883.3**.
- Height on the axis = 126.3 px. The raw silhouette is 137 px, but that includes the far top rim and the near bottom edge, so it overstates the world AABB height by about 8%.
- Z_h = 12.565 / sqrt(1 + r²/f²), with r measured from the principal point to the origin (base or centre). This gives Z_h = 11.88-11.96 m.
- H = 126.3 · Z_h / f = 0.920 (origin at the base) to 0.927 (origin at the centre). Answer: **0.923 m**.

## Sensitivity and confidence
- f between 1600 and 1657 gives H = 0.91-0.94.
- If the 137 px silhouette were used without the perspective correction, H would be about 1.00 m. I believe the corrected value is right because the reference is the world AABB.
- Confidence: moderate-good, about ±4%.

Scripts: fit_car.py, solve.py, hyd_px.py, hyd_edges.py, final.py.
