# Q646: height of the small robot (m). Prior: big robot (tank) speed = 5.924 m/s

fps = question_fps = 24, so the tank moves 0.24683 m per frame.

## Geometry
- The video is labelled 2D, but the perspective is clear. The robot's feet touch the floor at y≈956-974, while the tank's
  near track touches at y≈893, so the robot is nearer the camera. A single m/px scale would overestimate its height
  by about 18% (that gives 302.5 px × 0.00477 = 1.44 m), so I did not use one.
- Camera pitch is zero: the pillar edges are exactly vertical (x = 641 / 712 / 1575 / 1653 at every row from y 220 to 810,
  `edges.py`). The horizon is therefore at the principal point, y = 540 (Blender default). For a level camera at height hc,
  the scale at a ground-contact row y_g is hc / (y_g − 540) m/px, whatever the focal length.
- Tank (`track_plate.py`): the near-side track frame plate and two hubs move at 50.75 / 50.79 / 50.81 px/frame
  (residuals < 0.4 px). The bottom edge of the near track is at y = 893. So 0.24683 / 50.78 = 0.004861 m/px at that
  depth, and hc = 0.004861 × 353 = 1.716 m.
- Robot: the near foot touches at about 973 and the far foot at about 956. Its centre (origin) ground row is therefore
  about 960 ± 5, which gives a scale of 1.716 / 420 = 0.00409 m/px.
- Height = hc × (y_g − y_top) / (y_g − 540). The dome top along the body axis was re-measured in code (`headtop.py`).
  It agrees with the record: 648.5 to 670.5 px, depending on gait bob (frame 0: 661.5).
  - Highest pose (frames 12-13 and 49): 1.273 m.
  - Mean: about 1.226 m.
  - Lowest: 1.183 m.
  - Frame 0: 1.220 m.
  - The result is insensitive to y_g: ±5 px changes it by only ±0.006 m.

## Answer
The AABB height changes with the gait (1.18 to 1.27 m). The rest/standing height is at least the highest walking pose,
and the mean is 1.23 m. Answer: **1.25 m**.

## Checks
- The tank speed measured on three independent near-side parts agrees to within 0.1%.
- The robot's walking speed comes out at 8.40 px/frame × 0.00409 × 24 = 0.82 m/s, which is plausible for a 1.2 m robot.
- The naive single-scale 2D route (1.44 m) was rejected because of the clear depth difference.

Confidence: moderate. The geometry is about ±2%; the main uncertainty is which pose the reference height uses (±4%).
