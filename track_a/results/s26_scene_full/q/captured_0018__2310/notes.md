# Q2310: distance between the pineapple toy and the soccer ball at 3.0 s (cm)

**Main problem:** the clip has 49 frames at 24 fps, so it ends at 2.0 s (frame 48). The question's 3.0 s would be frame 72,
which does not exist. The answer therefore extrapolates the end state, with both objects lying on the floor.
The file fps and question_fps are both 24.

- The pineapple toy is the yellow plush with green leaves, called `lemon_plush` in scene/. The near (right) person drops it at frame 27.
  It hits the floor at about frame 36, bounces and tumbles, and settles near pixel (843, centre about 612, bottom about 628) by frames 44–48.
- The soccer ball (depth 2.8 m) first hits the floor at frame 39, centre (534.5, 541). It rebounds, and at frame 48 it is still rising at
  (554, 402.5) while drifting right by about 2.4 px/frame. At 3.0 s it is probably back on the floor, somewhere around x 554–620 with centre row about 541.
- Camera: f = 0.5959 x 1280 = 763 px, cx/cy = 640/360. Back-projection uses ray x distance.
- Pineapple depth, route 1: no depth is given for the pineapple, so the near person's distance (2.002 m) is used, since that person dropped it.
- Pineapple depth, route 2: a floor plane. Pitch comes from the horizon at y 342. Camera height (0.78 m) comes from the ball's centre at the bounce
  (distance 2.8 m, radius 7.8 cm from its 44 px diameter). This plane reproduces the near person's distance from the feet (1.99 vs 2.002 m).
  It does not reproduce the far person's (2.80 vs 3.13 m). Under this plane the pineapple is at about 2.27 m.
- Distances (cm), ball on the floor at x = 554 / 590 / 620:
  - route 1: 118 / 110 / 105
  - route 2: 106 / 97 / 89
- Answer: about 108 cm, the middle of these scenarios.

**Confidence: low.** The asked time is outside the video, so the ball's final resting place is a guess (±15%).
