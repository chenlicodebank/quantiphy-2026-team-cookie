# Q397 – length of the police car (m)

2D top-down render, static camera, 24 fps (file fps = question_fps, no re-timing).
Prior: bike speed 5.52 m/s -> one m/px scale from the cyclist's pixel speed.

## Measurements
- Cyclist pixel speed: scene record pelvis track linear fit 14.415 px/frame (mean per-frame |d| 14.44);
  independent whole-rider template matching (check.py) linear fit 14.44 px/frame, windows 0-40: 14.39, 10-70: 14.46.
  The per-frame speed oscillates (pedalling surge), but the rig moves at a constant mean speed, so use the mean: 14.43 px/frame
  = 346.3 px/s.
- Scale: 5.52 / 346.3 = 0.01594 m/px.
- Car length (bumper to bumper): record 289 px (template box 802-1091 at f40); check.py background-difference
  extents at thresholds 20-30 on frames 35, 40, 50: 287-291 px (lower thresholds pick up the blue glow). Use 289 px.

## Answer
289 x 0.01594 = 4.61 m (a plausible police car length).

Second route: the two speed routes agree to 0.2 %, and the length measurements spread ±1 %. Remaining
uncertainty: perspective, because the cyclist's pelvis sits higher than the car's bumpers (a few %). Confidence: good (~±4 %).
