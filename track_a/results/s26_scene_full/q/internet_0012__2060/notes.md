# Q2060: length of the car in the leftmost lane (prior: lane width = 3.66 m)

- Object: the leftmost lane of the left carriageway runs between the solid edge line (x≈741–753) and the first dashed line
  (x≈839–852). The only car in it is `white_car_lower` (centre x≈829→820, partly over the dash at f0 and drifting left).
  `white_car_upper` (x≈868) is in the middle lane. The camera is a static top-down drone, so the measurement is 2D.
- Lane width in px (`lanes.py`, line-centre to line-centre, along the car's path y≈2560–3090):
  - leftmost lane (edge line to dash): 98.5–99.5 px
  - middle lane (dash to dash): 96.0–96.9 px
  - Near the top of the image (y≈1360–1890): 97.8–98.8 and 95.4–96.4 px.
  - Value used: mean ≈ 97.8 px, so the scale is 3.66/97.8 = 0.0374 m/px.
- Car length in px, bumper to bumper along y:
  - From the scene record body box / per-frame edges: 105.7 px (f0) to 108.5 px (f107), ≈107 mid-track.
  - Independent half-max column profiles (`carlen.py`): 104–105 px. A zoomed visual check at f54 gives ≈106 px.
  - Value used: ≈106.5 px.
- Result: 106.5 × 3.66 / 97.8 = 3.99 m.
  - If the scale comes from the leftmost lane only (99 px): 3.94 m.
  - From the middle lane (96.5 px): 4.04 m.
- Confidence: moderate-high, about ±3%. The main uncertainty is which lines the annotator spanned for the lane width.
