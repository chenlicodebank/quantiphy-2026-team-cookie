# q_308 – width of the hot air balloon (prior: speed = 4 m/s)

2D scene, the balloon rises straight up at constant speed, camera static. fps 24.004 vs question_fps 24 (<0.02 % apart, so it doesn't matter).

Measurement (`measure.py`, mask = |RGB − sky| > 30, every frame):
- Width: 358 px on every frame (x 361–718), no change at all.
- Vertical pixel speed: basket bottom 4.000 px/frame, mask centroid 4.020 px/frame, envelope top 4.07 px/frame
  (constant; fits match the mean of the frame-to-frame differences).

Scale: 4 m/s / 24 fps = 0.16667 m/frame. 
- Basket bottom (4.000 px/frame) → 0.041667 m/px → width 14.92 m
- Centroid (4.020 px/frame) → 0.04146 m/px → width 14.84 m
Second route: the speed comes out the same from the linear fit and from the per-frame differences, and with three
different reference points (bottom, centroid, top) the width stays between 14.67 and 14.92 m.

Answer: 14.9 m. The width is the horizontal extent of the envelope, which is the widest part. Confidence: high (about ±1 %).
