# Q114: distance between the car and the bike at t = 2.0 s (frame 48, fps 24, which matches question_fps)

The video is a 2D top-down view with a static camera and no perspective (object pixel sizes stay constant).

## Scale from the prior (car acceleration 4.03 m/s^2)
- I fitted quadratics to the car's front-edge x (scene track, checked against the frames) with fit.py and fit2.py.
  - Frames 3-50: a = 0.88-0.90 px/frame^2, with residual about 0.4-0.5 px. In 10-frame windows from 3 to 49 the
    value stays between 0.80 and 0.96.
  - Frames 45-63: the acceleration rises to about 1.2 px/f^2, and the speed then levels off at about 62 px/f.
    This shows on the front edge, the rear edge and the centroid, so the motion is not exactly uniform.
  - The mean over the whole ramp is about 0.98 px/f^2.
- I used a = 0.89 px/f^2, which is 512 px/s^2, giving a scale of 4.03/512 = 0.00786 m/px.
- Sanity check: the car (a Cybertruck-like pickup) is 727 px long, which gives 5.7 m (the real truck is 5.68 m). The
  bike is 208 px long, which gives 1.64 m. Both are plausible, which supports the early-phase value. The alternative
  scales are 0.0072 (from the mean acceleration) and 0.0058 (from the late phase). The late-phase scale would make
  the truck 4.2 m long, which is implausible.

## Positions at frame 48 (mask bounding boxes, checked on frames/f48.png)
- Car: the bounding box spans x 825-1552 and y 570-885, so its centre is (1188.5, 727.5).
- Cyclist: the bounding box centre is (630, 381). The pelvis sits slightly behind it (toward +x) by about 0-15 px,
  so I used x ≈ 637.
- Separation: dx = 551.5 px and dy = 346.5 px, so the distance is 651 px (657 px using the bounding-box centre).

## Answer
651 px x 0.00786 m/px = 5.12 m, rounded to **5.1 m**. The range 5.0-5.2 m covers the choice of origin and the
spread in the scale from the early-phase fits.

The main uncertainty is that the car's acceleration is not uniform. If the reference used the mean acceleration,
the answer would be about 4.7 m. Confidence is moderate.
