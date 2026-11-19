# q3183: height of the right billboard (cm)

The prior is g = 9.8 m/s². This is internet footage, so I used one planar scale taken from the ball's vertical acceleration. The time base is 30 fps: the file and the question give the same rate.

- **Ball track:** `scene/tracks/ball.csv`, `cy_bg`, which is corrected for camera drift. I fitted a parabola (fit.py) to the free flight in frames 66-97 and to frames 66-76 + 81-97, leaving out 77-80 where the top of the ball is cut off.
  - Both fits give 4956-4963 px/s². The bbox bottom edge gives 4948 px/s². The post-bounce frames 105-108 give 4950 px/s².
  - The rising part alone gives 5327 px/s² and the falling part alone 4747 px/s². The ball's apparent diameter shrinks from 134 to 121 px, so it moves away from the camera and the per-segment numbers differ. Following the annotators' single-scale convention, I used the full-arc value of about 4955 px/s².
- **Scale:** 9.8 / 4955 = 0.001978 m/px. Sanity check: the ball's 121-128 px diameter gives 24-25 cm, which matches a basketball.
- **Right poster height (outer dark frame):** the record gives 173 px (478-650). On frame 81 I read about 500-675. The thresholded column profiles (poster.py) give 170-171 px at frames 0, 30 and 81. I used 172 px.
- **Height:** 172 × 0.1978 = 34.0 cm. The plausible range is 33.6 to 34.4 cm.

Confidence: moderate. The main uncertainty is in the scale, since the gravity fit depends on which segment is used (±7%).
