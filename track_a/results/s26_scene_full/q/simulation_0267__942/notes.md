# Q942 – height of the spacecraft (flying car), in metres

Prior: the acceleration at 1.0 s is 4 m/s². This is a 2D-style side view with a static camera and pure horizontal translation, so I used one metres-per-pixel scale from the pixel acceleration. fps = question_fps = 24.

## Pixel acceleration (fit.py, fit2.py; quadratic fits to the scene track, which is consistent with constant acceleration from rest)
- Nose tip x0, frames 2-52: 655.8 px/s². Frames 10-40: 654.4 px/s².
- Tail tip x1, frames 10-40: 680.4 px/s².
- Nose/tail midpoint (origin proxy), frames 10-40: 667.4 px/s². Frames 15-35: 668.8. Frames 10-52: 658.9 (rms 0.3 px in the 10-40 window).
- Adopted value: 663 px/s², with about ±1.5 % spread between routes. Scale = 4 / 663 = 0.006033 m/px.

## Pixel height
On the frame-24 crop I checked that the bbox runs from the antenna tips (y about 731) to the underside (y about 1044).
Over frames 10-52 the median bbox_h is 314 px. Frames where the thin antennas are fully segmented give 316-318 px; the dips to about 300 px are antenna dropouts. Adopted height: 316 px, including the antennas, because the world AABB includes them.

## Result
Height = 316 × 0.006033 = **1.91 m**. Without the antennas, the body is about 266 px, which would give 1.60 m.
Cross-check: the length would be 1009 px × 0.006033 = 6.1 m, which is plausible for a car-sized craft.
Confidence: moderate. The main uncertainty is about 2 % from the choice of reference point for the acceleration.
