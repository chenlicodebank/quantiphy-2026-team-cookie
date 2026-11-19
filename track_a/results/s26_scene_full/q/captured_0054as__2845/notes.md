# q 2845: soccer ball diameter (cm). Answer: 18.4 cm

The file and the question are both 24 fps, so frame = round(t × 24).

## Which object the depths belong to
The depth_info covers the orange ball (basketball) at frames 12 and 24, plus the "white" and "green" balls at frame 24.
The white ball is the small whitish ball that the standing person throws. Zoomed frame 27 shows it as
off-white, next to the yellow-green tennis ball. At frame 24 both small balls are in the standing
person's hands, about 3.05 m away, so these two depths agree with each other. The soccer ball
(white with black patches) is beside the crouching person, much nearer the camera, and **no depth
is given for it**. Its distance therefore has to come from the floor geometry.

## Method (scripts in this folder)
- `seg.py`: background. In the lower image it equals the row median of an empty strip
  (x 820–900), checked to within about 3 RGB units. Foreground = |frame − row background| > 45.
- `bmeasure.py`: per-frame basketball and soccer-ball masks. Records bbox, extent
  perpendicular to the motion (free of blur) and extent along it. → `meas_*.csv`.
- `sphere.py`: exact pinhole projection of a sphere (f = 0.5959·1280 = 762.8 px, pp (640,360)),
  which includes the off-axis elongation.
- `model.py`: joint least-squares fit over basketball frames 11–24.
  - Fitted: ball radius, camera pitch, camera height and a motion-blur exposure fraction. Roll is
    assumed 0. Each ball centre lies on the plane at height r_b above the floor.
  - Observed: bbox left and right and the top edge of each frame. The bottom is not used because it
    carries a dark contact shade.
  - The given depths at frames 12 and 24 are imposed. The rms residual is about 0.6 px.
- `soccer.py`: soccer ball at rest (frames 1–20), placed on the floor plane at height r_s.
  - The widest row spans x 125–191 (67 px, the same for thresholds 30, 45 and 60). The lowest
    pixel is y 635.
  - This solves X, Z and r_s.
  - Check: the same model predicts the resting basketball (x 206–277, bottom 607.5) to within 1 px.
- `soccer_roll.py` (second route): rolling soccer ball, frames 29–33, free of the person. It uses the
  blur-free extent perpendicular to the motion, placed on the same plane.

## Results by depth interpretation (soccer D in m: rest route / rolling route)
| depth_info read as | basketball D | soccer rest | soccer rolling | standing-person height check |
|---|---|---|---|---|
| Euclidean distance to the centre | 0.195 | 0.159 | 0.160 | 1.35 m (implausible) |
| Euclidean distance + surface offset (+0.11) | 0.207 | 0.167 | 0.169 | 1.39 m |
| z-depth (camera-frame Z) to the centre | 0.211 | 0.177 | 0.175 | 1.56 m |
| z-depth to the front surface (+0.11) | 0.224 | 0.186 | 0.185 | 1.61 m |

The two routes agree within 1–2 % in every interpretation. The soccer/basketball diameter ratio
is a stable 0.82.

The z-depth reading is preferred, for three reasons:
- The lab convention back-projects positions as ray × depth, which treats the depth as Z.
- With it, the standing person (feet on the fitted floor) comes out 1.56–1.61 m tall. The Euclidean
  reading gives 1.35 m.
- The basketball comes out 21–22 cm, a standard size-5 ball. Size 3 soccer ball = 18.5–19 cm.

The velocity prior (2.21 m/s at frame 12) cannot separate the readings. A dropped capture frame
between frames 11 and 12 makes the smoothed reference speed sensitive to the window: the z-model gives
1.9–2.5 m/s depending on the window, and the Euclidean model 1.7–2.1 m/s.

Answer: between the z-to-centre (17.6 cm) and z-to-surface (18.6 cm) values, leaning to the
surface reading, since a ToF depth at the clicked centre pixel measures the ball's surface: **18.4 cm**.

Confidence: moderate. The measurement is precise to about 2 % within a given interpretation. The
main risk is the meaning of depth_info: if it is a true Euclidean centre distance, the answer would
be about 16 cm.
