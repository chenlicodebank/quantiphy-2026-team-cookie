# Q2665 — basketball velocity at t = 1.3 s (cm/s)

- question_fps = file fps = 24, so t = 1.3 s is frame 31.
- depth_info has a typo: the second t=1.4 s line is labelled soccer ball, but it must be the basketball, because
  that ball rolls toward the camera (it grows from about 67 px to 72 px). Basketball depths used: frame 22 (0.9 s) is
  2.7777 m and frame 34 (1.4 s) is 2.373 m. Depth for each frame is interpolated linearly in time.
- Camera: f = 0.5959 x 1280 = 763 px, principal point (640, 360).
- Centres: scene/tracks/basketball_orange.csv, circle_cx/cy. Checked on frame 31 (crop f31.png): the centre is about
  (563, 448), which matches. No occlusion in frames 26–35. The record suspects a dropped frame at 35→36, so the
  windows used stay clear of it.
- 3D centre = ((u-cx)/f, (v-cy)/f, 1) x Z. Speed = |dP| x 24.
  - Forward difference at frame 31: 115.2 cm/s. Backward difference: 123.1 cm/s.
  - Mean of 5 steps (29–33): 119.2 cm/s.
  - Linear fits of position over frames 29–33, 28–34 and 27–35: 119.3, 119.0 and 119.2 cm/s.
  - Second check using the mask centroid instead of the circle centre: 119.5–120.3 cm/s.
- Answer: 119.3 cm/s.
- Caveat: depth taken from the apparent size (Z = f x 0.232 / d_px) changes only about half as fast as the given
  depths do. With that depth the speed is about 102 cm/s. The given (measured) depths are the reference convention,
  so I used them. Confidence: moderate. The depth rate between the two given points dominates the answer.
