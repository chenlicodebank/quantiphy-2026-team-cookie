# Q1159 – eagle speed at t = 1.0 s

Time base: the file is 25 fps (75 frames), question_fps = 24. The file frames 1, 26 and 51 duplicate frames 0, 25 and 50,
so the file is 72 original 24 fps frames with 3 duplicates inserted. Mapping: orig = file − [n≥1] − [n≥26] − [n≥51].
t = 1 s → original frame 24 = file frame 25; t = 2 s → original 48 = file 50. (script: measure.py)

Scale (3D pinhole, principal point at the image centre): the boat translates at a constant 4 m/s (prior), so between
t = 1 and t = 2 its 3D displacement is 4 m. I put the boat at its given depths (177.21 m and 178.00 m) along the pixel
rays at o24 and o48 (positions from a linear fit over ±6 frames) and solved for f:
hull centroid 9105, mask centroid 9078, stern corner (x1, y1) 9068 / 9069 → f ≈ 9080 px (HFOV 9.7°).

Eagle: the tracked mask centroid, checked on a zoomed frame at t = 1 s (body at about (522, 655), matching the track).
The pixel step is about 24 px/frame. The eagle's depth is interpolated linearly between 179.27 m (t = 1) and 177.10 m (t = 2).
Speed = |P(o24) − P(o23)| × 24 with P = depth × unit ray:
- raw one-frame difference: 11.71 m/s
- local linear fit (±4 frames): 11.60
- quadratic fits (±6, ±8 frames): 11.54, 11.56
- bbox-centre route: 11.62 to 11.79 for the fitted versions
→ answer 11.6 m/s. About 11.5 m/s of this is across the image and about 2.2 m/s is toward the camera.

Plausibility checks with f = 9080: eagle wingspan ~90 px → 1.76 m (realistic for an eagle). The person walks at
~2 px/frame → 0.97 m/s (a realistic walking speed).
Confidence: good (±3 %). The remaining uncertainty is wing-pose jitter of the centroid and the unknown boat origin
(it cancels for pure translation).
