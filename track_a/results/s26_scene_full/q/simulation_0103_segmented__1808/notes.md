# q_1808 – average speed of the boat (m/s)

2D side-view render, 24 fps (file fps = question_fps = 24), 54 frames. Prior: shark acceleration = 1 m/s^2.

## Scale from the shark (fit.py, tracks from scene/ checked: shark never clipped, y constant)
Quadratic fit x(frame) over frames 1-53 (motion starts f1->f2 with an initial ~7.3 px/frame, then uniform acceleration):
- bbox centre: a = 0.1486 px/frame^2; nose 0.1500; tail 0.1473; mask centroid 0.1490 -> a ~ 0.149 px/frame^2
- = 0.149 x 24^2 = 85.8 px/s^2 = 1 m/s^2  ->  scale = 0.01165 m/px

## Boat speed
Constant velocity after rest at f0-f1: linear fit f1-53 bow tip 17.85 px/frame, ref_x 17.87, stern x_min (f21-53) 17.96;
bow 522 -> 1451 over 52 frames = 17.87 px/frame. -> 17.87 x 24 = 428.9 px/s -> 428.9 / 85.8 = 5.00 m/s.

Second route: ratio form v/a = 17.87 / 0.149 frames = 119.9 frames -> v = 1 m/s^2 x 119.9/24 s = 5.00 m/s.
Alternative reading including the stationary f0->f1 step in the mean: (1451-523)/53 = 17.51 px/frame -> 4.90 m/s.
Answer 5.0 m/s (the boat's steady speed; a round value, consistent with a designed scene). Confidence: high (~2%).
