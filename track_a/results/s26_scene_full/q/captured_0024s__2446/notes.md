# q_2446 – length of the book (cm)

The file rate and question_fps are both 24. Frame = round(t*24): t=1.0 -> 24 and t=1.2 -> 29. Camera: f = 0.5959*1280 = 762.8 px, principal point (640,360).

## Geometry
- The given depths are 1.0685 m at frame 24 (centre 751.0,397.7) and 0.977 m at frame 29 (671.0,453.7). Back-projecting them
  gives the 3D up-slope direction m = (0.72,-0.42,0.55), so the ramp runs strongly towards the camera. Moving 15.9 cm in
  5 frames from a start at about frame 18.5 implies about 2.3 m/s^2, which roughly agrees with the 2.8 prior.
- The book's long axis on the ramp runs along the image-horizontal edges of the cover. It is NOT parallel to the image
  plane. The ramp's lower and upper edges converge at a vanishing point near (139,360), which is close to the table's
  left-front edge vanishing point (183,333). This means the long axis is about 55 deg out of the image plane. So
  "depth x pixel length / f" (13.1 cm with the 89.5 px cover edge, or 18.2 cm with the 130 px bbox) is not reliable here.
- Cover top-face long edge (mask polygon, frame 0, sharp; `book_mask.py`): left side midpoint (737.5,367.5) and right
  side midpoint (827,368.5), giving 89.5 px. The frame-0 centre lies on the 3D line through the frame-24 and frame-29 centres,
  at a depth of 1.116 m (`length.py`).

## Results (`length.py`, `width.py`)
| long-axis direction | frame 0 | frame 24 (blurred, inflated) |
|---|---|---|
| perpendicular to m, image-horizontal | 17.3 | 18.4 |
| ramp-edge vanishing point (139,360) | 18.4 (18.2 local) | 19.7 |
| table-edge vanishing point (183,333) | 19.3 | 20.7 |
| least-squares ramp rectangle fit (uses the slope depths) | 15.4 | 16.2 |
The width along the slope comes out at about 8.6 cm, which suggests a small notebook.

## Second route
The book at rest on the table (frames 36-48) is nearly parallel to the image plane and spans 150 px. The table plane is
seen almost edge-on, so its depth cannot be found well (0.72-0.95 m gives 14-21 cm). With L = 17.5 cm the rest depth would
be about 0.89 m. That is plausible: the book was at 0.977 m at frame 29 and kept moving towards the camera and to the left.

## Answer
17.6 cm: the middle of the best routes, 17.1-18.4 cm. Confidence is moderate (about ±10%). The main uncertainty is how far
the long axis is turned away from the image plane.
