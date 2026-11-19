# q_1829 — speed of the left first ball at 0.5 s

2D video (Newton's-cradle style), 30 fps file = question_fps 30. t = 0.5 s -> frame 15; speed = |p(15) - p(14)| x 30.
"Left first ball" = ball_left (the striker swinging down from the upper left).

## Measurement (measure.py, speed.py)
- Mask = any RGB channel < 235, x < 650, morphological close (15 px) to bridge the white segmentation sliver, convex
  hull, then a least-squares circle fit to the densely sampled hull outline. Overlay frames/fit15.png: the circle matches
  the full outline, crescent included.
- Centres: f14 (372.98, 714.59), f15 (387.13, 721.86) -> raw step 15.91 px/frame (scene record: 15.77).
- Frame-to-frame steps have about ±1 px of noise (15.20, 15.91, 17.96, 17.58 ...). Fitting a polynomial to the centres
  over frames 6-24, 8-22, 9-21 and 10-20 gives a 14->15 step of 15.84-16.29 px/frame. I adopt 16.0 px/frame.
- Scale: ball diameter = 2 m. Left-ball fitted radius 81.8-82.9 px (record median 164.0 px diameter). Other balls
  163.8 / 165.6 px (record), SAM horiz/vert 160-168 px. Adopted D = 164.5 px -> 0.01216 m/px.

## SAM 3 check
- f14, left ball: SAM box 290.6-456.1 x 633-796; my circle gives 290.4-455.5 x 632-797. They agree (<1 px).
- f15: SAM box 308.3-469.9 x 641-802; my circle gives 305.3-469.0 x 640-804. SAM leaves out about 3 px of the pale left
  crescent beyond the white sliver (seen on frames/seg_00_f15.jpg). Its extent, 161 px against 164, is 1.8 % short,
  under the 3 % limit. The crescent is part of the ball, so my circle fit is the correct one. SAM's box-centre step
  (17.3 px) is too large because of this cut.

## Result
speed = 16.0 px/frame x 30 x 2 / 164.5 = 5.84 m/s (raw step: 5.80; smoothed range: 5.78-5.94).
Second route: the scene record's centres give 15.77 px/frame -> 5.75 m/s with D = 164.5 (5.77 with D = 164.0). Consistent.
Confidence: good (about ±3 %).
