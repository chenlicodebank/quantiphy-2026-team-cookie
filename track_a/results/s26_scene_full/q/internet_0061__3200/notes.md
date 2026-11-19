# q 3200 – displacement of the acorn between 1.30 s and 1.40 s (cm)

Prior: gravity = 9.8 m/s^2. Internet video, planar convention: one scale = 9.8 m/s^2 / (pixel acceleration of the toy in free flight).

Time base: file fps 30.013 vs question_fps 30 – identical for frame lookup: t=1.30 -> frame 39, t=1.40 -> frame 42.

## Measurements (frames 39-43 = free flight; released ~38, hits the backrest/rail at 44-45)
- Camera: ECC translation vs a background frame (54) is < 2 px over 38-45, negligible.
- `edges.py`: dome leading (right) edge from row profiles vs background: 447, 496, 590, 718, 886, 1092 (frames 38-43).
  Second differences 39-43: 34, 40, 38 px/frame^2; quadratic fit a = 37.7 px/frame^2 (2D incl. small y component).
- `diffmask.py`: background-difference dome centroid 391, 481, 614, 786, 989 (39-43): fit a = 37.9 px/frame^2.
- The scene record's cx (dome mask + fixed cap offset, ±20 px) gives 42.9 px/frame^2 / 386 px – cruder, not used.
- The flight is consistent with near-constant acceleration along image +x (the toy is dropped/falls across the image).

## Answer
Displacement 39->42: 390 px (leading edge) / 395 px (centroid).
Scale = 9.8 / (37.7 x 30^2) = 0.0289 cm/px -> 11.27 cm (edge), 11.34 cm (centroid). Answer **11.3 cm**.
Sanity: held toy length 279 px x 0.029 = 8.1 cm – plausible acorn toy size.

Second route agrees (edge vs centroid within 1%). Main uncertainty: the pixel acceleration (34-45 per-step spread), ~±8%.
