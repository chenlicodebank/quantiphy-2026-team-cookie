# q2161: basketball's initial distance from the desk (cm)

Video file fps = question_fps = 24, so time t is frame round(24t).
Camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360). Script: `measure.py`.

## Method
3D distance between the back-projected ball centre and the back-projected desk centre, using the depth_info distances
as Euclidean ray lengths.
- Ball: centre from scene/tracks/ball.csv. Frame 24 (t=1.0) is (531.4, 158.1), with depth 1.401 m, giving
  (-0.191, -0.355, 1.342) m. The ball is held still in frames 0-20 at (524, 100), giving (-0.200, -0.447, 1.313) m at the same depth.
- Desk: the tabletop is the segmented object. Its corners are NL (440,605), LB (477,417), FR (681,384) and NR (755,542),
  checked on the frame-0 grid image. The centre is either the diagonal intersection (589.7, 467.7) or the corner mean
  (588, 487). With depth 1.725 m these give (-0.112, 0.241, 1.704) or (-0.115, 0.283, 1.698).

## Results (cm)
| ball frame | desk centre: diagonal intersection | desk centre: corner mean |
|---|---|---|
| 24 (t=1.0, the time of the depth) | 70.2 | 73.4 |
| 0 (rest position) | 79.6 | 82.9 |

## Check
The ball diameter calibrated at t=1.5 (107.7 px at 1.5225 m) is 0.213 m. From that size, the frame-0 depth works out
to 1.383 m, close to the given 1.401 m, and gives 79.9 / 83.2 cm, so the frame-0 route agrees with itself. At frame 24
the motion blur makes the size-based depth unreliable (1.44-1.48 m).

## Answer
75 cm. This falls between the t=1.0 reading (about 72 cm, consistent with when the depth was given) and the
rest-position reading (about 81 cm). Most weight goes to t=1.0. Confidence is moderate. The main uncertainties are
which "initial" frame was meant and where the desk centre was clicked.
