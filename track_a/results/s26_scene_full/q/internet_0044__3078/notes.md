# q3078 – height of the plastic bottle (cm)

Object: the plastic juice bottle with the yellow cap (x ≈ 565-685 px), the only plastic bottle (the other one is green glass).
Prior: g = 9.8 m/s². Internet video, single planar scale (annotator convention). fps = question_fps = 30.

## Scale from gravity (measure.py)
Fitted quadratics y(frame) to the ball's vertical image position on each flight arc between bounces (scene/tracks/ball.csv,
stabilised cy_f0, arc-fill rows excluded). Vertical accelerations (px/frame²): 20.05, 19.83, 18.84, 19.50, 19.67, 19.60,
20.15, 19.94, 19.70; one short arc against the white bowl (126-130) gives 25.0 and was dropped as bad segmentation.
Median second differences agree (19.3-20.2). Mean 19.70 px/frame² = 17728 px/s² → scale 9.8 / 17728 = 0.553 mm/px.

## Bottle pixel height (frame 0, column gradient profiles x = 610-640)
Top of the yellow cap at y = 423-424; bottom of the bottle base (dark rim, then desk) at y = 811-812.5 → ~389 px
(the scene record gave 386 px from reading by eye).

Height = 389 × 0.553 mm = 21.5 cm (using 386 px gives 21.3 cm).

## Check
With the same scale the ball's apparent diameter (~76 px) comes out at 4.2 cm. A real table-tennis ball is 4.0 cm, and this
one is a little closer to the camera than the bottles, so the scale holds up. A ~21 cm drink bottle is also realistic.
Perspective is ignored because the convention uses one planar scale.
Confidence: good (±3%).
