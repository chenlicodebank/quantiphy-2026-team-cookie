# Q1722: average speed of the person (m/s)

The prior is the person's height, 1.75 m. depth_info puts the human at 139.10 m at t=1 s and t=2 s. The file rate and question_fps are both 24 fps.

## Method (measure_h.py -> human_sub.csv)
- I segmented the human (darkness > 0.1) in every frame and took its binary bbox height and a darkness-weighted centroid.
- **Height:** the median is 40.5 px over frames 0-64. In frames 65-71 the head is clipped by the mask, so I excluded them. The height trend is -0.003 px/frame (flat): 40.8 / 40.4 / 40.5 px over the three thirds of the clip. A flat height means there is no motion in depth. A depth change of 1 m/s would change the height by about 2 % (about 1 px), and no such change appears. The gait changes the width (legs spread), which fits a side view, so the motion is lateral.
- **Pixel motion:** I fitted a linear trend over frames 0-64. Centroid x moves 1.043 px/frame and the feet move down 0.093 px/frame, giving 1.047 px/frame = 25.1 px/s.
- **Scale:** 1.75 m / 40.5 px = 0.0432 m/px, which gives a speed of **1.086 m/s**.
- **Second route (pinhole):** f = 40.5 x 137.9 / 1.75 ≈ 3190 px, where 137.9 m is the depth along the optical axis (139.1 m times the cosine of the 7.4° off-axis angle). That is a horizontal FOV of about 19°. The lateral speed = 25.1 px/s x 137.9 / f, which is identical to the route above.
- The given distance barely changes (139.1030 to 139.1044 m). Lateral walking at that off-axis position should change it by about 0.12 m/s. So the character's origin stays put and the distance cannot be used for the body's motion; I used the body's pixel track instead.
- The mean of raw per-frame displacements (1.34 m/s) is inflated by the centroid's gait wobble. The pelvis moves smoothly, so I used the trend slope.
- **Plausibility:** 1.09 m/s is a normal walking speed.

## Confidence
Moderate-high, about ±5 %. Two effects on the 40.5 px height pull in opposite directions and roughly cancel: faint antialiased edges make it larger, and walking height is a little below rest height.
