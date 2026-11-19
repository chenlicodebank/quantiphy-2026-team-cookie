# Q2439 – length of the slope (cm)

Lab video, 24 fps (file and question_fps agree), 1280x720, static camera. f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).

## Method
- Slope = white board leaning from the table (near/lower end) onto a book stack (far/upper end).
- `measure.py`: bright mask (grey > 225) of the board in frame 48, polygon fit. Corners: UR (859,361), UL (750,360),
  LL (610,467), LR (706,490). This matches the scene record. Frame 0, with the notebook at the top, gives the same lower corners.
- Far end = midpoint of the upper edge (804.5, 360.5), depth 1.243 m. Near end = midpoint of the lower edge (658, 478.5),
  depth 0.990 m. The depth is the Euclidean distance, so each point = unit ray x depth (`compute.py`).
- Slope length = |A - B| = **36.9 cm**.

## Checks
- Left edge (UL->LL) 35.8 cm and right edge (UR->LR) 37.9 cm. Their mean is 36.9 cm, the same as the midpoint route.
- Treating the depth as z instead of the Euclidean distance gives 38.4 cm (not the convention; it shows the sensitivity).
- `check.py`: the notebook's 3D displacement from frame 24 to frame 29 (from the book depths) is 0.158 m, 7 deg from the
  slope direction. Constant acceleration of 2.8 m/s^2 from release at frame 19 predicts 0.18 m, which roughly agrees.
  The notebook centres sit 3.5–5 cm off the slope line, which is within depth noise and the notebook thickness.
- The upper and lower edge widths come out as 16.9 and 12.6 cm. They are not comparable, because the lower edge recedes
  in depth while the single endpoint depth is applied to both of its corners.

## Confidence
Moderate to good: about ±2 cm, limited mainly by which points the given far and near depths refer to.
