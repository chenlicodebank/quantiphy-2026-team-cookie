# q_3228 – diameter of the ball (cm)

The prior is gravity, 9.8 m/s^2. The clip is a top-down phone view of a basketball rolling horizontally across a gym floor.
The ball never falls, bounces or follows a parabola. Its stabilised y drifts only ~20 px over 20 frames and there is no
vertical-acceleration signal, so gravity gives no usable pixel scale. Following the rule, I took the scale from the ball's
known real size: a regulation (size 7) basketball is 29.5 in in circumference, which is a diameter of **~24 cm**.

Independent check from floor markings (lines.py, frame 0):
- The maroon court lines are 48–54 px wide (the horizontal line ~49 px, the vertical line ~52 px). The pale-blue stripe is 54 px wide.
- Court lines are 2 in (5.08 cm) wide, which gives ~0.10 cm/px at the floor plane.
- The ball's unblurred diameter is 258 px (scene record, median bbox_h over frames 5–21). That is ~26 cm at floor scale.
- The ball's centre is ~12 cm above the floor, so it is nearer the camera than the floor. With a handheld camera ~1.3–1.5 m
  up (the filmer's shoes are in view), that shrinks the size by ~0.91. The result is ~23.5–24 cm, consistent with a regulation ball.

Answer: 24 cm. Confidence: moderate-high. A size-6 ball (~23 cm) would be ~4% off.
