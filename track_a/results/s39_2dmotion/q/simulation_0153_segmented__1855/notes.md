# q_1855 — acceleration of the blue car at t = 1 s

Question: "What is the acceleration of the blue car at time 1s in m/s^2?" Prior: the blue car's tyre diameter is 0.369 m.
No depth_info is given. The video is a 2D side-view scene. The file rate and question_fps are both 24, so t = 1 s is frame 24.
By the benchmark convention, a(24) = (speed(24) - speed(23)) x fps = (x24 - 2 x23 + x22) x fps^2.

## Motion (px)
- Tracks: I used the drift-free template tracks in scene/tracks/cart.csv: the sill marker and the front and rear hubs.
  These are rigid near-side points. I also made my own NCC template track (measure.py -> track_own.csv; the sill and
  body patches).
- The image-space motion is a cubic in time. The marker cubic over frames 17-41 has an rms of only 0.04 px, which
  means a linearly falling acceleration and a parabolic speed peaking at about frame 30. That pattern matches a Blender
  Bezier ease.
- Raw one-frame second differences at frame 24 are too noisy to use alone: marker 0.67, front hub 1.04, rear hub 0.36,
  own sill 0.63 px/frame^2.
- From the cubic fits (accel.py), the second difference at frame 24 is:
  - marker 0.749 px/frame^2
  - front hub 0.741
  - rear hub 0.754 (0.78 with a quartic)
  - own sill track 0.729 (cubic over frames 18-30)
- Adopted value: **0.748 px/frame^2 = 430.8 px/s^2**.
- Second route: the two hub tracks are independent of the marker and agree within 1 %.
- Hub y and tyre bottom (y ≈ 946.6) stay constant, so there is no depth change. A linear drift between the marker and
  the hub midpoint (about 0.3 px/frame) does not affect the curvature.

## Scale (tyre diameter in px)
| method | result (px) |
|---|---|
| circle fit to the front tyre's right silhouette against white, frames 38-40 (tire6.py, rms 0.4 px) | 108.0-109.7 |
| SAM 3 "tire" masks, box widths, frames 32-38 | 108.6-110.6 |
| SAM 3 box heights | 107.4-109.0 |
| front tyre vertical profile through the hub (profile.py; top meets the fender trim, bottom meets the ground line) | 110.6 |
| horizontal dark run through the hub row (profile.py / tire4.py) | 112-114.7 |
| scene/notes.md | ≈112 (113 horizontal) |

- The horizontal dark runs come out larger because the run includes the tread and the far-side tyre seen in
  perspective, plus the dark gap at the end of the sill. This is the >3 % disagreement with SAM. On zoomed frames
  (frames/wheels38.png, frames/wheel_front_30.png) the tread and the far tyre do widen the silhouette on one side, so
  the side-wall circle (~109-110) is the right measure. scene/notes.md's 112-113 has the same bias.
- The bottom of the tyre is flattened by the ground line, and the hub template sits about 2-3 px off the side-wall
  centre. Because of that, I did not use radii measured from the hub.
- Adopted D = **110 px** (uncertainty ±1.5 %), giving a scale of 0.369/110 = 3.355e-3 m/px.

## Answer
a = 430.8 px/s^2 x 0.369/110 = **1.445 m/s^2**.
Sensitivity: D = 109 gives 1.458, D = 111 gives 1.432, and D = 113 gives 1.407.

## SAM check of the car
- SAM 3 "blue car" masks at frames 22/23/24/30/36 (sam_car.py) land on the cart.
- The whole-mask centroid and box edges shift with the changing perspective outline: the centroid minus the marker
  drifts from 63 to 28 px. They are therefore unusable for a second difference (it comes out at -1.4 px/frame^2).
  The rigid template points are the right measure for the motion.

Confidence: moderate-high. The motion curvature is good to about 2 % and the tyre pixel size to about 2-3 %.
