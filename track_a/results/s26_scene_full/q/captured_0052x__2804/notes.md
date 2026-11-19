# q_2804 — distance basketball to shoe (m)

The file is 24 fps and question_fps is also 24. I used t = 1.0 s, which is frame 24. Both objects are static.

## Method (measure.py)
- Green-screen foreground mask at frame 24, then connected components.
  - **Basketball:** least-squares circle fit to the contour, leaving out the frame-edge rows. Centre (801.6, 671.5),
    r = 46.9 px. The bbox centre is (802, 672), so the two agree.
  - **Shoe:** mask centroid (285.7, 658.3). The bbox centre is (284, 657).
- Camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
- Back-projection follows the lab method card: X = ((u-cx)/f, (v-cy)/f, 1) x depth.
  - Basketball depth 1.9365 m, shoe depth 2.2310 m.
  - Distance = **1.479 m**.

## Checks
- **Size check:** basketball diameter = 2 x 46.9 x 1.9365 / 762.8 = 0.238 m. A real basketball is about 0.24 m, so
  the scale is right.
- **Choice of centre points:** circle centre or bbox centre, and shoe centroid or bbox centre, change the result by
  less than 0.5%.
- **Other reading of depth:** if depth_info is the Euclidean range along the ray instead of Z, the distance is
  1.268 m. Both objects are far off-axis (ray-norm factors 1.10 and 1.17), which is why the two readings differ by
  16%. I answered with the method-card (depth-as-Z) reading.

## Confidence
Pixel measurements are good to about 1%. The main uncertainty is the depth convention: about 1.48 m if depth is Z,
1.27 m if it is the range along the ray.
