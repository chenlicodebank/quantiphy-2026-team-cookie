# Q69: distance between black-shirt and white-shirt man at t=2.0 s (frame 48)

- Prior: black-shirt man's speed is 1 m/s. fps = question_fps = 24, so there is no retiming.
- Scene: top-down perspective camera over a flat floor. Both men walk toward -x at the same depth. I treated it as 2D with one m/px scale taken from the black man's pixel speed.
- I checked identities on frame 48 (frames/f48.png). The black shirt is the upper walker (head ≈ (795,410)) and the white shirt is the lower walker (head ≈ (615,610)).
- measure.py uses scene/tracks. For each tracked point, the scale (px/frame) comes from the black man's steady walking (frames 2–71). The distance is taken at frame 48.
  - head: speed 12.15–12.25 px/frame; d48 = 266.7 px (neighbours 262.5–269.3, smooth); 266.7/(12.15·24) → 0.915 m (0.907 with the mean step)
  - pelvis_est (head pulled 6% toward the image centre): 11.42 px/frame, d48 = 250.7 px → 0.915 m
  - mask centroid: 11.16 px/frame, d48 = 248.3 px → 0.927 m
- Second route: the three point types share the same ratio, so the parallax at different heights mostly cancels. The net-displacement speed and the mean-step speed agree within 1%.
- Answer: 0.915 m. Confidence: good (about ±3%).
