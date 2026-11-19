# q_2407: velocity of the book at 1.2 s (cm/s)

The file and the question are both 24 fps, so t = 1.2 s is frame 29. At that frame the book is on the lower part of the ramp, sliding toward the camera. It reaches the ramp foot at f30, drops onto the table between f31 and f35, and is at rest from f37.
I used the book track in scene/tracks/book.csv (mask centroid) and checked it against crops (frames/view.png, f20-f38). It is correct.

## Scale (lab card: f = 0.5959*1280 = 762.8 px, principal point (640, 360))
- Ramp centre line in 3D: I back-projected the ramp's top edge (585, 356) using slope_far = 1.201 m and its bottom edge (585, 482) using slope_near = 0.9555 m.
  This gives a board 0.30 m long at about 31° incline. The ramp's top and bottom image widths are 145 px and 183 px. Their ratio, 1.26, matches the depth ratio 1.257.
- Each frame's centroid ray was intersected with this line. At f29 this gives a depth of 1.030 m, against the given 1.02 m (1 % off; the book centre sits slightly above the board).
  I also tried a version with the line scaled to give exactly 1.02 m; it changes the speed by 1 %.

## Speeds (m/s, one-frame differences on the ramp line)
- Per-frame speeds: f25 0.54, f26 0.52, f27 0.60, f28 0.68, f29 0.75, f30 0.77.
- Quadratic fits over f21-30: v(f29) = 0.76-0.79.
- After f30 the book leaves the ramp and keeps moving fast. Going from the f30 ramp point to the f34 point (given depth 0.857 m) averages 0.92 m/s; from f29 to f34 it averages 0.88 m/s.
- The reference convention smooths the forward differences over at least 5 frames (f27-f31): (0.67 + 0.75 + 0.77 + ~0.9 + ~0.9) / 5 ≈ 0.80.
- Second route: I took depth from the book's apparent length, calibrated at rest with 0.851 m at f38, and back-projected the centroid.
  Smoothing those positions over 5 frames gives a forward difference of 0.82 and a central difference of 0.85. This route is less exact: the length-based depth at f29 is 0.994 m, versus 1.02 m given.
- Uniform acceleration from release at f20.5 over the measured ramp travel would give a = 2.6-2.7 m/s² (close to the prior's 2.8) and v(f29) = 0.91-0.96.
  However, the per-frame speeds do not follow uniform acceleration from rest: the early motion at f21-24 is too fast. So I give this route little weight.
- The prior (2.8 m/s² at f34, during landing) could not be reproduced directly. The book is almost at rest by f36.

## Answer
82 cm/s. This is the 5-frame-smoothed value, between the on-ramp instantaneous speed of 0.76-0.78 m/s and the post-ramp speeds of about 0.9 m/s.
Confidence: moderate, about ±12 %.
