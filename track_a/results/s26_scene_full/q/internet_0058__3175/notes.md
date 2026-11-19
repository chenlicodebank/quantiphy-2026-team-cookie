# q3175: ball to basket distance at 1.00 s

- Time base: file fps = question_fps = 30, so t = 1.00 s is frame 30 (ball in free flight, rising; release about frame 22).
- Scale from the prior g = 9.8 m/s^2: quadratic fit to the ball centre's cy (scene/tracks/ball.csv, stabilised against the
  camera drift) over the free flight (`fit.py`):
  windows 24-62 / 26-60 / 28-56 / 24-42 give 2.227 / 2.234 / 2.250 / 2.240 px/frame^2 (raw coordinates give the same).
  Taking 2.227 px/frame^2 = 2004 px/s^2 gives 0.00489 m/px.
  - Sanity check: ball diameter 50.4 px x 0.00489 = 0.246 m, which matches a real basketball (0.24 m).
- Positions at frame 30: ball centre raw (1079.9, 205.7), stabilised (1081.8, 213.0). Rim centre (basket) is (883, 297)
  in frame-0 coordinates and about (881, 290) raw at frame 30 (checked on the zoomed frame `frames/f30.png`).
- Distance: 215.8 px (stabilised) / 217.0 px (raw), which is 1.055-1.061 m. **Answer 1.06 m.**
- Second route: raw coordinates against the rim read on the frame-30 crop give about 216 px, the same value.
- Other reading: if "basket" means the centre of rim plus net (about y 330), the distance is about 235 px = 1.15 m.
  The rim centre is used.
- Confidence: good. The scale is uncertain by about ±1.5 %. The main risk is which point counts as the basket.
