# Q1210: height of the first (bottom) step in front of the door of the nearer house

Answer: **0.132 m**. Time base: question_fps = file fps = 33.

## Which house
There are two doors with stairs: the green clapboard house (center stoop, x 835-1125) and the grey stone house
(arched door, steps x 1550-1760). The street recedes to the left, so the stone house on the right is the nearer one
to the camera. I answered for it. For the green stoop the value is about 0.139 m (0.134-0.147 depending on the horizon).

## Scale (focal length) from the prior
- I back-projected the pedestrian's pelvis (torso_x smoothed with a cubic fit, pelvis_y_est; cx, cy = 960, 383) at frame
  33 (d = 15.8652 m) and frame 66 (d = 16.6708 m). Then I solved for f so that the 1-s 3D displacement = 1.236 m:
  **f = 2982 px** (3005 px with ±2-frame averaging instead) (focal3.py).
- Check: extrapolating that constant-velocity 3D line to frames 0 and 98 reproduces the observed pixel x
  (1563.4 vs 1562.7; 1042.4 vs 1040.9).
- The bike/pedestrian directions are parallel only at f ≈ 7000. That is not used: it contradicts the speed prior, and the
  bike may veer (4° difference at f = 3000).

## Riser height
- Row-gradient profiles of the stone steps (riser.py, frames 40/60/80/96, 7 column bands of x 1580-1720): bottom step
  nosing at y = 633.7 and base on the sidewalk at y = 658.7 (657.4-660.1 across x). **Riser = 25.1 ± 0.5 px.**
  The other pitches are 25-28 px, which is consistent. Treads are almost edge-on (the camera is low, horizon ≈ 569).
- Depth of the step: at frame 0 the pedestrian stands right in front of these steps: Z = 14.80 m, sole level y ≈ 664.
  Ground plane: Z_step = Z_ped·(664 − y_h)/(658.7 − y_h). The horizon from the facade/road line vanishing point
  (vp.py) is (−2716, 569), giving y_h ≈ 569. Z_step ≈ 15.67 m, so 5.26 mm/px.
- Height = 25.1 × 15.67 / 2982 = 0.132 m.

## Checks and sensitivity
- Horizon at 551 / 563 / 588 (feet fit, walking-direction VP, line VP): 0.129-0.134 m.
- Nose-to-nose pitch average (26.4 px) gives about 0.139 m for a typical step. The bottom riser is slightly lower.
- If the prior is a mean of per-frame speeds (hip bob), f would be about 1% larger, so the answer would be about 1% smaller.
- Sanity: pedestrian height ≈ 270 px × 14.8/2982 ≈ 1.34 m. The scene is not at real-world scale, so this was not used.
Confidence: moderate (about ±5% from the scale, plus the house-choice ambiguity, which is small: 0.132 vs 0.139).
