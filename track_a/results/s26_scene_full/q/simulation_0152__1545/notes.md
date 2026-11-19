# Q1545 – acceleration of the blue car at t = 1 s

- Blue car = the light-blue utility cart ("cart" in scene/). It moves left to right parallel to the image plane at a
  constant depth (scene record: constant scale and hub row). File fps = question_fps = 24, so t = 1 s is frame 24.
- Convention: a(24) = (speed(24) - speed(23)) * fps, i.e. the second difference of position over frames 22-24.

## Scale
- Its near side is its right side, so the right front tire is the visible near-side front tire; depth_info gives 9.312 m to it.
- Front tire outer-edge circle fit (tire3.py, radial edge search, 55-87 edge points per frame, frames 28-41):
  D = 111-114 px, mean about 112.4 px. The rear tire measured horizontally near the image centre (tire2.py) gives about
  108 px, but its top is bounded by the fender, so it is less reliable.
- m/px at the tire's depth = 0.369 / 112.4 = 0.003283 m/px (f = 112.4 * 9.312 / 0.369, about 2837 px, hFOV about 37 deg).
  The motion is a rigid translation parallel to the image plane, so world speed = near-side pixel speed * m/px.
  The origin's depth does not matter.

## Motion (track.py)
- Template matching of the opaque body panel between the wheels (rows 855-925), translation only, sub-pixel.
  Correlation is 0.98-0.99 for frames 19-27. Matching was done frame to frame both ways and also against a frame-24
  anchor.
- Per-frame displacement (px): f20 44.31, 21 45.45, 22 46.31, 23 47.32, 24 48.00, 25 48.70, 26 49.15, 27 49.58,
  28 49.87, with a peak of about 49.9 at frames 29-31, then the cart slows (smooth ease-in/out). These agree with
  scene/tracks/cart.csv to within about 0.5 px.
- Raw d24 - d23 = 0.68 px/frame^2. Smooth polynomial fits give 0.742-0.761 px/frame^2 (mean about 0.75) over windows
  19-34. Route 1 fits the frame-to-frame displacements; route 2 fits the absolute positions against the frame-24
  anchor. Both routes agree.

## Result
a = 0.75 px/frame^2 * 24^2 * 0.003283 m/px = 1.42 m/s^2.
If the 108 px rear-tire diameter is used instead, a = 1.48. Answer: 1.43 m/s^2 (weighted to the front-tire fit).
Confidence: about ±5 %. The main uncertainty is the tire's pixel diameter, from the tread-side bulge and the edge
definition.
Sanity check: the cart is about 550 px long, which is about 1.8 m. Its speed is about 48 px/frame, which is about 3.8 m/s.
