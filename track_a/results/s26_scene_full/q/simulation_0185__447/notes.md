# Q447: speed of the gift box at t = 1 s (m/s)

Prior: the box's acceleration after 1 s = 3.18 m/s² (while it slides down the ramp). This is a 2D video at 24 fps, and question_fps is also 24, so no re-timing is needed.
t = 1 s is frame 24.

## Method
- Track: scene/tracks/gift_box.csv (body centroid; `_dupfix` values used at frame 38). I checked frame 24 on a gridded crop
  (frames/f24.png). The box centre is at about (790, 680), which matches the track value (793, 681.5).
- Path length s(t) along the slide, frames 10–37 (after the landing at frames 8→9; frame 38 is a duplicate frame).
- Scale: one m/px factor from the prior, scale = 3.18 / (pixel acceleration along the slide).
  answer = v_px(frame 24) / a_px × 3.18.

## Measurements (fit.py, fit2.py)
- Backward-difference speed at frame 24: raw step 23→24 = 747.6 px/s. Mean of steps 22–26 = 747.3. Quadratic fit value at frame 24 = 744.5.
- Pixel acceleration: quadratic fit over frames 10–37 gives 745 px/s². A linear fit of per-frame speed gives 743. A cubic fit gives a(1 s) = 743.
  Shorter windows give 741–780.
- Answer = 744.5/745 × 3.18 = 3.18. The linear speed fit also gives 3.18, and the cubic fit gives 3.20. Across fit windows the range is 3.05–3.20.

## Second route (independent scale from gravity)
The free fall over frames 0–8 has a pixel acceleration of 2277 px/s². Taking g = 9.81 gives 0.00431 m/px.
Then the slide acceleration is 745 × 0.00431 = 3.21 m/s², which agrees with the prior to within 1%. The speed at 1 s is 745 × 0.00431 = 3.21 m/s.
The two routes agree.

Answer: 3.18 m/s. Confidence: high, about ±3%.
