# q_2647: basketball velocity at 1.3 s (cm/s)

- t = 1.3 s → frame 31 (question_fps 24 = file fps).
- depth_info labels both 1.4 s entries as soccer ball; one must be the basketball. The soccer ball's apparent size
  barely changes from f22 to f34 (52.5 → 54.5 px), so 2.477 m becomes about 2.38 m → soccer = 2.373 m. The basketball grows from 61 to 67 px
  (2.7777 m becomes about 2.53 m) → basketball = 2.602 m at 1.4 s (frame 34). Basketball 2.7777 m at 0.9 s (frame 22).
- f = 0.5959·1280 = 763 px, principal point (640, 360). Centres from scene/tracks/basketball.csv. I checked them independently with an
  orange HSV mask centroid for frames 26-36 (agreement ≤ 3 px; the pixel speed over 29→33 is 13.0 vs 12.8 px/frame).
- Depth per frame: linear interpolation between the two given depths (alternative: interpolate in inverse apparent size).
  3D centre = ((u-cx)/f, (v-cy)/f, 1)·Z. The 3D forward-difference speeds over frames 26-35 are 91-124 cm/s and scatter frame to frame.
- Smoothed velocity around frame 31: 5-frame window 29→33 = 109.4 (mean of per-frame speeds 109.7); 7-frame window 28→34 = 111.7;
  inverse-size depth model 106-110. All routes give 106-113 cm/s.
- Answer: 110 cm/s. Confidence: good (about ±5 %). Frame 36 follows a dropped frame and lies outside the window.
