# q_2249 — width of the book (cm)

Object: the light-blue notebook to the right of the board (scene.json "notebook"). It is static, so I averaged
frames 0, 2, 4, 6, 40, 44 and 48. The file fps is 24 and question_fps is 24, so the rates are the same.
Scale: lab camera f = 0.5959 x 1280 = 763 px, principal point (640, 360); depth_info book distance = 1.665 m at t = 0.
The ball-acceleration prior is not needed for a static size.

## Measurements (scripts: edges.py, topface.py, probe2.py, sens.py, geom.py)
- Outline from the r-b (wood vs book) transition, with lines fitted to each edge (residuals < 0.9 px). The top-face
  front edge is the sharp dark line above the white page-edge strip (fit residual 0.26 px).
  Top-face corners: TL (623.6, 389.0), TR (663.1, 383.9), FR (682.0, 425.3), FL (636.9, 433.3). Overlay: frames/nb_top.png.
- Pixel sizes: back edge 39.8 px, front edge 45.8 px, left/right (long) edges about 46 px. The bottom edge of the
  page-block front face is 46.6 px.
- Brightness transitions per row give an outer width of 41.0 px (y 395), 42.0 px (405), 43.5 px (415) and 44.8 px
  (422). The book looks about 15 % narrower at the back. Perspective at 1.67 m with f = 763 cannot cause more than
  about 4 %, so this comes from the object or its edges, not from the camera. I therefore use the middle value.
- The short edge runs across the image (it is nearly horizontal), and the long edge runs into depth. With any
  plausible table tilt the long edge is 11–20 cm, so width = the short edge.

## Results
- Method card (depth x pixel extent / f): back edge 8.69 cm, front edge 10.00 cm, mid-row width (42.8 px) 9.34 cm.
- Second route: back-project the corners onto a table-parallel plane through the book centre (1.665 m). I tried a
  plane normal from the cookie/pen/book depths, and tilts from 25 to 60 deg:
  back edge 8.85–9.50 cm, front edge 9.89–10.02 cm, mean 9.37–9.76 cm. The width measured perpendicular to the long
  axis at the mid rows is 8.8–9.3 cm. At a 45–51 deg tilt (the depth-derived normal) the edge mean is 9.41–9.45 cm.
- Answer: **9.3 cm** (range of readings 8.7–10.0). The long side (length) is about 12–13 cm under the depth-derived
  normal. That is a sanity check only: it is sensitive to the tilt.

## Confidence
Moderate, about ±7 %. The main uncertainty is the trapezoidal outline (back 40 px vs front 46 px) and whether the
grey rim and spine band count. Under the stated convention there is no other reading of "width" (the short
horizontal extent).
