# q_762: height of the white backboard (prior: ball diameter = 0.282 m)

fps = question_fps = 24, so no re-timing issue. The answer is a static size, so time does not matter.

## Measurements (scripts in this folder)
- `geom.py`: backboard edges at the half-level crossing, frame 0. Height 208.9 px (top 71.5, bottom 280.4, the same in 4 columns),
  width 357.9 px. The left and right edges are vertical to within 0.1 px over 200 rows, so the camera is not pitched.
  The horizon is therefore at the image centre row, v = 540 (Blender principal point).
- `balldiam.py`: horizontal ball chord through the centre with the same half-level edge criterion, every 4th frame:
  74.16 ± 0.14 px. The vertical extent is about 1 px larger because of off-axis radial stretching, so I used the width.
- `bracket.py`: the teal wall meets the floor at row 980.7. The legs of the black support bracket converge from x 809/1137
  at the board (y 280) to 814/1131 at the wall crossbar (y 317), a width ratio of 1.035.

## Scale and perspective
- Single scale (the 2D convention): 208.9 / 74.16 × 0.282 = 0.7945 m.
- There is clear perspective, though. The ball meets the floor at frame 24 (centre 1004.24 + radius 37.08, so contact at v = 1041.3),
  which is 60 px below the wall base. The ball therefore falls well in front of the wall.
  With no pitch, a floor point's offset below the horizon is proportional to 1/depth, so Z_wall / Z_ball = 501.3 / 440.7 = 1.138.
- The converging bracket legs put the board slightly in front of the wall: Z_board = Z_wall / 1.035.
  So Z_board / Z_ball = 1.099.
- Height = 0.7945 × 1.099 = **0.873 m**.

## Checks
- Implied camera height: f·R/Z_ball = 37.08 px gives f/Z_ball = 263 px/m, so h = 501.3 / 263 = 1.91 m.
  The board bottom comes out at about 2.99 m, the rim at about 3.1 m and the board at 1.50 × 0.873 m (aspect 1.71).
  These are plausible gym proportions.
- The other cases: board flush with the wall gives 0.904 m (+3.5 %); the pure single-scale answer gives 0.795 m (−9 %).
  I chose the bracket-corrected depth.

Confidence: moderate. The pixel measurements are good to about 0.5 %. The main uncertainty is the depth model:
whether the reference uses a single 2D scale or the true 3D size, and how far the board stands off the wall.
