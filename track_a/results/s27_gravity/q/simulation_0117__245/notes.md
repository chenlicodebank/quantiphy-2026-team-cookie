# Q245: width of the electronic lock (m)

The file runs at 24.020228 fps and the question at 24 fps. I used 24 fps and frame indices throughout.
This is a 2D frontal scene with a static camera, so one metres-per-pixel scale applies.

## Scale from the prior (gravity 9.8 m/s^2)
- I fitted a quadratic to the ball's centre y in frames 2-18 (scene/tracks/ball.csv; frames 0-1 are clipped at the top
  edge, so I left them out). Script: measure.py.
  a = 10.918 px/frame^2, which is 6289 px/s^2 at 24 fps. Residual rms 0.19 px. The median of the second differences is 10.80.
- Scale = 9.8 / 6289 = 1.558e-3 m/px.
- Check: the ball's 45 px diameter comes to 0.070 m (a tennis ball is 6.7 cm). The door, 715 x 1474 px, comes to 1.11 x 2.30 m
  including its frame. Both are plausible.

## Lock width
- On frame 18 (crop.py, frames/lock3.png, column profile averaged over rows 1060-1200), the black lock body runs
  from x ≈ 826-828 (left edge) to x ≈ 866.6 (right edge, where it rises sharply to the background level at 867).
- Just left of the body there is a soft shadow at x 822-825, and the door groove is at x ≈ 821-822. I excluded both.
  The record's 37 px (826-862) cut off the grey right rim at 860-866.
- Width ≈ 40 px (range 38-41).
- 40 px x 1.558e-3 m/px = **0.062 m** (range 0.059-0.064).
- Second check: the lock's height of 189 px comes to 0.29 m, and its 40 px width over 189 px height is about 0.21. Both are typical of a
  real push-pull smart lock (about 6-7 cm wide, 30-40 cm tall).

Confidence: moderate-high. The main uncertainty is ±2 px on the lock edge (shadow and rim), about ±5%.
