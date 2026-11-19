# q_2331: height of the left person (cm)

- The left person is the farther one (white tank top). The record notes and the image agree, so her depth is distance_far_person_camera = 3.130 m.
- File fps = question fps = 24.
- Pixel height (measure.py): non-white rows in columns 320-440, frames 0-25. Top of the head is at y = 174 and the shoe soles at y = 577, giving 404 px (405 in one frame). This was stable at both thresholds (200 and 230) and matches scene/tracks/person_left.csv.
- Lab method card: H = D × px / f = 3.130 × 404 / 763 = 1.657 m, so the answer is **165.7 cm**.
- Second-route check: the record's track CSV gives the same 404 px. Treating depth_info as Euclidean range and converting to z-depth (person centre at u ≈ 385, so Z = 3.13 / sqrt(1 + 0.334²) = 2.97 m) would give 157 cm. The floor-row consistency between the two people slightly favours that reading, but the task's method card says to use D directly, so I answer 165.7 cm. The soccer ball check (45 px at 2.8 m gives 16.5 cm) cannot tell the two readings apart because the ball is near the image centre.
- Confidence: moderate. The pixel measurement is solid (±1 px). The main uncertainty is the depth convention, about 5%.
