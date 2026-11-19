# Q1566: length of the table (desk), in metres. Answer: 2.47 m

The file's fps (24) is the same as question_fps (24). The camera is static and the principal point is assumed to be at the image centre (1062, 540).

## Corners (frame 29, desk.py / crops.py)
- The desk-top silhouette corners are: left-back L (458,699), back-right B (1597,524), front-right R (2000,657), near front-left N (698,893).
- I also tried an "inner top-surface" set: L (470,688), B (1597,530), R (1985,645), N (700,880).
- Which corner is "far right"? If it were B, the back-right corner, the desk would come out 3–6 m long, which is absurd (desk_geom.py). Taking R, the front-right corner, gives a consistent rectangle. So the near corner (3.593 m) and the far-right corner (5.009 m) are the two ends of the front long edge, and the length is |P_N − P_R|.

## Focal length, two independent routes
1. **Fall of the magnifying glass** (fall_fit.py, fall_fit2.py):
   - The 3D model is p0 = 4.2401 m along the ray at frame 0, an unknown starting velocity, and 9.8 m/s² gravity with fitted camera pitch and roll.
   - Fitted to the tracked centre over frames 0–11 (rms 0.3 px), plus the t = 0.5 s depth of 4.4097 m.
   - Result: f = 2637 px with pitch 13.3° and an almost zero starting velocity. The lens-centre and mask-centroid tracks give 2644 and 2649.
   - With the pitch fixed anywhere from 10° to 30°, f stays between 2550 and 2790.
2. **Desk-top rectangle** (rect_test.py):
   - P_N and P_R come from their given depths. The depths of L and B are solved so that the four corners form a parallelogram (closure error 0.3 cm for the inner set).
   - The corner angle is exactly 90° at f ≈ 2640 (outer set) or 2590 (inner set).
   - The implied camera pitch is about 13°, the same as the fall fit found independently.

## Length
- |NR| = 2.48 m (outer set, f = 2640) and 2.46 m (inner set). Across f = 2570–2700 it runs from 2.52 to 2.43 m.
- Answer: **2.47 m**.
- The width comes out at about 1.06–1.07 m.
- Scale check:
  - Magnifying glass about 0.28 m long.
  - Revolver about 0.27 m.
  - Typewriter about 0.44 m wide.
  - All are plausible at real-world scale.

Confidence: moderate to high, about ±4%. The answer is sensitive to f: a 5% change in f gives about a 3% change in length.
