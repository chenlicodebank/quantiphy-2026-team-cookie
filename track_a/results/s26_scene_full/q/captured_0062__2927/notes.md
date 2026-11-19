# q_2927: length of the white box (cm)

**Object.** The "white box" is the small white/red drink carton lying on its side on the floor, centre-left, at about (516,496) px. In scene/ it is called `milk_carton`. It does not move during the clip. Its depth at t=1.4 s is 2.082 m. The file fps and question_fps are both 24.

**Pixel measurements.**
- I averaged frames 26-48 (`boxmask.py` → frames/box_avg.png, x6 zoom). The colour mask failed on the dark side face, so I read the corners by hand on that zoom.
- Three faces are visible: the top face (long × width), the red end face (width × height) and the right side face.
- Corners in px: A (520.4,462.9), B (542.9,470.4), C (514.6,514.1), D (491.8,505.8), D' (490.9,521.6), C' (513.8,527.1).
- The top long edges are DA = 51.5 px and CB = 52.1 px; the end width DC = 24.3 px.
- The long axis points away from the camera along the floor, so in the image it is strongly foreshortened.

**Geometry** (`floor.py`, `seams.py`, `boxlen.py`):
- Focal length f = 0.5959 × 1280 = 762.8 px, principal point (640,360).
- Floor normal, route 1: from the vanishing points of the sliding white board's rectangle edges over frames 22-48. This gives pitch 34.2°, roll 12.6°. The board's edge directions come out near-perpendicular (mean |cos| 0.09).
- Floor normal, route 2: from three vertical wall seams on the right wall. This gives pitch 36.6°, roll 10.3°, 3.1° away from route 1.
- Box centre = back-projection of (516,496) at 2.082 m. The top face lies on a plane parallel to the floor, h/2 above the centre plane. I solved for h (≈5.4-5.8 cm) so that the edges DD' and CC' come out vertical.
- The top-face corners are then intersected with that plane.

**Results (length / width / height, cm):**
| floor normal | length | width | height |
|---|---|---|---|
| board vanishing points | 17.8-17.9 | 6.3-6.6 | 5.4 |
| wall seams | 17.0-17.2 | 6.4-6.6 | 5.8 |
| mean of the two | 17.4-17.5 | 6.4-6.6 | 5.6 |

- Sensitivity: about ±0.35 cm per degree of pitch; roll hardly matters.
- The naive method card (depth × 2D pixel length / f, no foreshortening correction) gives 14.1 cm. That underestimates a long axis that points away from the camera, so I did not use it.

**Consistency check of the given depths.**
- With the box depth fixed, the floor plane predicts the board at 2.58 m (given 2.815), the bag at 3.22 m (given 3.307) and the mario toy at 1.83 m (given 2.016).
- The board speed comes out 1.6-1.7 m/s against the 1.934 m/s prior. The step from frame 35 to 36 looks like a dropped frame, which makes this check noisy.
- No single floor tilt fits all the given depths, so they contain several percent of noise. The "trashbin" depth (2.303 m) does not fit the far blue bin at all.
- I kept the box's own depth for the scale. If the box depth reads low like the others, the true length could be 3-10% larger.

**Answer:** 17.5 cm (the mean of the two floor-normal routes). Confidence is moderate: about ±1 cm from the floor tilt and corner reading, plus the depth-scale uncertainty.
