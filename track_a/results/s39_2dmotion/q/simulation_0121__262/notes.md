# q_262 – speed of the left first ball (ball1) at 0.5 s

- 2D Newton's cradle. Prior: ball diameter = 2 m. Ball diameter = 163 px (fixed-radius rim fits; the static balls' SAM masks give 160–165 px horizontally and 165 vertically, about 1 % larger, from the soft mask edges). Scale = 2/163 = 0.01227 m/px.
- Time base: question_fps = 30 (file fps = 30.0075, a negligible difference). t = 0.5 s -> frame 15. Speed = |p15 − p14| × 30.
- Own measurement (`measure.py`): subtract the frame-1 background (the glitch frame with no balls), then fit a fixed-R = 81.5 circle rim, ignoring samples on the dark loop. Centres: f14 (372.96, 712.97), f15 (387.16, 720.76). Step = 16.20 px -> 486 px/s -> **5.96 m/s**.
- The scene track gives f14 (374.35, 713.80) and f15 (388.56, 721.43). Its centres sit about 1.4 px away from mine, but the step is the same: 16.13 px -> 5.94 m/s.
- Smoothed route (`speed.py`): fit the pendulum angle about the pivot (640.6, 240.4) with a quartic over frames 8–22 (residual 0.16 px), then take the backward chord at frame 15. That gives 16.12 px -> 5.93 m/s (mine) and 15.96 px -> 5.88 m/s (scene).
- SAM 3 check: ball1's centroid is (376.0, 713.0) at f14 and (390.7, 720.3) at f15, so the step is 16.41 px (5.96 → 6.04 m/s, +1.3 %). SAM's centroids sit about 3 px right of the rim fit because the dark loop crosses the ball and cuts a notch out of the mask (checked on the overlay, frames/seg_01_f14.jpg). Its horizontal extent (168–173 px) is inflated by motion blur. The rim fit is the better measurement; the step agrees within 1.3 %.
- Answer: 5.94 m/s (the measurements range from 5.88 to 6.04). Confidence: high, within about 2 %.
