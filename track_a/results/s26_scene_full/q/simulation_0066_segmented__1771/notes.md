# q1771 — average speed of the walking pedestrian (m/s)

Answer: **1.34 m/s**

The frame rate is 24 fps in both the file and the question, so frames 14 and 38 are t = 0.58 s and 1.58 s.
The camera is static. The scene is 3D, and the pedestrian walks right to left, almost parallel to the image plane.

## Focal length (the key unknown)
- **Horizon.** Two vanishing points fix it:
  - The van's motion vanishing point is (614, 74) ± 10 px (`van_foe.py`, LK feature tracks, three frame windows). The cyclist's track points to the same place (x ≈ 605–635, `cyc_foe.py`), so this is the road direction.
  - The purple sedan's sill line and the sidewalk's straight edge both meet y = 72 at x ≈ 3130–3160 (`horiz_lines.py`).
  - So the horizon is at y ≈ 72 and roll ≈ 0. Principal point is the image centre.
- **f from a right angle.** If the road (van/cyclist direction) is perpendicular to the curb/parked-car direction, then f² = −(e1−c)·(e2−c), which gives **f ≈ 862 px**.
  - The seam across the sidewalk points to x ≈ 665 (`slot_edges.py`). That is consistent with the road direction within its extrapolation error; taken as perpendicular to the curb it would give f ≈ 800.
- **Checks on f = 862:**
  - Predicted perspective lean of a vertical at the pedestrian is 22.7°. The measured head-to-feet lean has a median of 22.7° (`ped_lean.py`).
  - The pedestrian's head-top-to-lowest-foot height is about 1.83 m and the camera height about 7 m, both plausible.
  - The two given pedestrian depths are consistent with a level pelvis path to within 2–3 cm (`ped_fit_line.py`). This check is weak: gait bob alone allows f ≈ 860–950.
- **Rejected route: the van's acceleration prior (4 m/s²).**
  - Feature tracks give a start time of about −0.8 frame, so the travel between frames 14 and 38 is S ≈ 4.42 m.
  - Combined with the van depths, this points to f ≈ 700–750. But the solution is internally inconsistent: the point at both given distances falls about 2 m below the van body for every f (`origin_box.py`, `van_tri2.py`, `van_ratio_pairs.py`).
  - So I did not use it. If it were right, the speed would be about 1.45 m/s.

## Pedestrian track
- **Reference point.** The head-top point (mean x of the top mask rows, top row y) is smooth and clean in every frame. The lower body renders partly missing in some frames (e.g. 14–16, 39–48), which is why I did not track the body centroid.
- **Pelvis pixel.** Head point plus the mean centroid−head offset from good frames, (+19.8, +48.0) px. Light Savitzky–Golay smoothing, window 7.
- **Route 1 (plane).** The pelvis moves in a horizontal plane (ground normal from the horizon, f = 862). The plane's height is fitted to both given depths: camera drop 6.11 / 6.08 m at frames 14 / 38.
  - Mean of the per-frame speeds over frames 1–71: **1.353 m/s**.
  - Smoothing window 5 / 9 gives 1.373 / 1.342.
- **Route 2 (depths only).** |P38 − P14| from the two given depths and pixel rays alone is 1.267 m over 1 s. Scaled by the track's whole-clip / 14→38 speed ratio, this gives **1.324 m/s**.
- Motion starts at frame 1→2. The pedestrian walks slightly faster in the second half (1.31 vs 1.41 m/s).

## Sensitivity and confidence
The speed scales roughly as 1/f:

| f (px) | speed (m/s) |
|---|---|
| 800 | 1.40 |
| 862 | 1.35 |
| 950 | 1.30 |
| 720 (van route) | about 1.45 |

The answer of 1.34 is the mean of routes 1 and 2 at f = 862. Confidence is moderate, about ±5–8%. The main risk is the focal length: it rests on the roads being perpendicular, and the van's prior does not agree with that.
