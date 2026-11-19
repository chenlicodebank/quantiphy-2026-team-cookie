# q_1276: height of the streetlight (simulation_0061)

Answer: **3.01 m**. This is the big double-lantern lamp post C in the right foreground, the most prominent streetlight. File fps and question_fps are both 24, and t = 0.58 / 1.58 s map to frames 14 / 38.

## Method (scripts: fit_f.py, solve.py, check.py, lamp.py)
1. **Focal length from the prior** (white van, a = 4 m/s²):
   - A quadratic fit of the van's image x over f0–40 has its vertex at frame −0.1, so the van starts from rest at t0 ≈ 0.
   - Its displacement between f14 and f38 must therefore be a/2·((t2−t0)² − (t1−t0)²) = 4.35 m.
   - The 3D positions are the depth_info distance × the unit pinhole ray through the bbox centre, with the principal point at (1080, 540).
   - Solving for the focal length gives **f = 2282 px**. A ±4 px change in van cx gives ±2 %. Putting the origin at ground level instead of the bbox centre gives 2281.
2. **Ground plane**:
   - Contact points are the pedestrian's feet (bottom of the bbox, below the hip estimate) and the cyclist's wheel bottoms, at f14 and f38. Each is placed at the same camera Z as the object's origin, which comes from depth_info.
   - Fitting a plane through these 4 points gives camera height 2.33 m and pitch 1.1° down. The horizon is at row 497. Residuals are about 1 cm.
3. **Lamp post C**, measured by code on frame 12:
   - The top is the lantern finial at rows 348–351.
   - The base pedestal's front edge is at row 999.5. Allowing for its elliptical footprint, the ground contact at the axis is about row 992.
   - The base ray meets the ground plane at Z = 10.7 m. Solving for the vertical height whose top projects to row 348–349.5 gives **L = 3.01 m**. Using the base front edge instead gives 3.00.

## Checks
- **Same plane, lamp post D** (the same style, further along the right pavement): 3.00 m, which agrees with C.
- **Left-side lamp posts**: A gives 3.28 m and the far-left post gives 3.24 m. Their pixel extents are smaller and come from the record's eye readings (±3 px), they sit far from the contact points used for the plane, and they may be a slightly different variant. C is the most precise measurement.
- **Plausibility of f = 2282**:
  - Pedestrian height comes out at 1.76 m and the cyclist (head to wheel bottom) at 1.69 m.
  - Taxi length comes out at 4.97 m and van length at 5.81 m. All are realistic.
- **Sensitivity**: the result scales roughly as 1/f, so ±5 % in f gives 2.89–3.14 m.

Confidence: moderate-good (±5 %). If "the streetlight" meant one of the left-side posts instead, the answer would be about 3.25 m.
