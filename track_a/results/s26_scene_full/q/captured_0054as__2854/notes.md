# Q2854: distance between the green ball and the white ball at 1.0 s

- File fps = question_fps = 24, so t = 1.0 s is frame 24.
- Identification: the green ball is the tennis ball (scene/ calls it `tennis_ball_yellow`). It is in the standing person's right hand at about (599, 290).
  The white ball is the small pale ball that scene/ calls `grey_ball`. It was released at frame 23 and is at about (569, 271).
  Their given depths (3.04 m and 3.07 m) match the standing person's distance. The soccer ball is about 68 px wide; at about 22 cm across, that puts it near 2.5 m, so it is not the "white ball". The pixel sizes also check out: about 18 px at 3.04 m is about 7 cm, which is right for these small balls.
- Centres were measured in code (`measure.py`) from colour/foreground masks on frame 24 (mask overlays are in frames/):
  - green: centroid (599.0, 290.2), bbox centre (599.5, 290.5)
  - white: centroid (569.7, 271.7), bbox centre (569.5, 271) without a stray pixel blob
  - These agree with the scene/ tracks: (599.3, 290.4) and (569.1, 271.2).
- Back-projection used f = 0.5959 × 1280 = 762.8 px and cx, cy = (640, 360). Each depth was taken as the Euclidean distance along the ray.
  - green: (-0.161, -0.275, 3.022) m
  - white: (-0.281, -0.354, 3.040) m
  - distance: 0.1449–0.1454 m across the centre variants. The scene/ track centres give 0.1454 m.
- Answer: **0.145 m**.
- Confidence: moderate-high. The result depends mostly on the lateral pixel separation (about 36 px). The 3.5 cm difference between the two given depths adds little.
