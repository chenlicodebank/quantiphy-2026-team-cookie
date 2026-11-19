# q_250 — length of the table (m)

2D top-down Blender scene, static camera. Prior: toy car speed = 0.05 m/s (uniform straight motion along +x).

## Scale
- Car pixel speed (scene/tracks/toy_car.csv, linear fit vs frame): mask centroid 2.609 px/frame (resid 0.5 px),
  rear bbox edge 2.615, front edge 2.603; halves 0–60 / 60–120: 2.616 / 2.608. Adopted 2.61 px/frame.
  My own quick saturation tracker (measure.py) gave 2.67 but with 5.8 px residual (noisy mask), so it carries less weight.
- fps 24.003 (file) vs 24.0 (question): differ by 0.01 %, so the choice makes no difference. Speed = 62.65 px/s.
- Scale = 0.05 / 62.65 = 7.98e-4 m/px.

## Table
- The table-top contour on frame 0 (measure.py, approxPolyDP) has corners (158,144), (1019,246), (953,907), (94,807).
  Long sides are 867.0 and 864.8 px, and the short side is 664.3 px. This matches scene.json (≈867 × 665).
  Long side ≈ 866 px.
- Length = 866 × 7.98e-4 = **0.691 m** (width ≈ 665 px → 0.53 m).

## Check
- Car length 130 px → 0.104 m, which is plausible for a toy car. The two opposite long sides agree within 0.3 %.
- Confidence: good. The main uncertainty is the ~1 % uncertainty in the car's pixel speed.
