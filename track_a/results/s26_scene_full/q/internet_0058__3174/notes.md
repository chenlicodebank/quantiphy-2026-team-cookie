# Q3174: distance between the ball and the floor at t = 1.00 s

The file and the question both run at 30 fps, so t = 1.00 s is frame 30. This is internet footage, so I used one planar scale.

## Scale from the gravity prior
- `fit.py` fits a quadratic to the ball centre's y over the free flight (scene/tracks/ball.csv, frames 23-63, with release at 22 and catch at 64).
  - Stabilised y: 2.2234 px/frame² = 2001 px/s².
  - Raw y: 1999.6 px/s².
  - Scale: 9.8 / 2001 = **0.00490 m/px**.
- Sub-windows give 0.00483-0.00511 m/px. Frames 23-42 give 0.00486; frames 30-55 give 0.00483. The median second difference is 2.16 px/frame².
- Sanity check: the ball diameter of 50 px gives 0.245 m (a real basketball is about 0.24 m). The player's height of 344 px gives 1.69 m. Both are plausible.

## Pixel distance at frame 30 (raw image)
- Ball centre: y = 205.7 px (circle fit, checked on the frame). Radius ≈ 24.3 px.
- Floor below the ball: the player's shoe soles at frame 30 are at y ≈ 889-891 px (3x zoom, frames/f30feet.png). The ball is
  roughly above her, at her depth, so I took the floor line as y ≈ 890.
  - The first bounce (frame 77) is nearer the camera, so its contact point is lower in the image. I did not use it.
- Centre to floor: 684 px → 3.35 m.
- Ball bottom to floor: 660 px → 3.23 m.

## Answer
The two readings differ by 3.6 %. I answered with the midpoint, **3.29 m**, which is within 2 % of both.

Confidence: moderate. The scale is good to about 2 %; the main uncertainty is whether the reference uses the ball's centre or its bottom.
