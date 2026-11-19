# Q2052 — initial distance between the two players

- **Prior.** The prior says "court width = 4.88 m". 4.88 m is 16 ft, which is the width of the lane (key). On frame 0 the lane measures 1077 px (x 1414-2491, from the scene record; the gridded frame shows about 1411-2492). That gives 4.53 mm/px.
  - Check: at this scale the sideline separation of 3334 px comes to 15.1 m, which matches a 15 m court width. So taking the lane as the prior's object is consistent.
- **Positions.** The drone looks straight down and is nearly static, so the scene is treated as 2D with one scale. "Initial" means frame 0. Mask centroids from the scene tracks, checked on the zoomed crop `frames/f0c.png`:
  - white player: (1543.7, 577.1)
  - black player: (2021.9, 492.4)
  - distance: 485.6 px
- **Answer.** 485.6 × 4.88 / 1077 = **2.20 m**.
- **Second route.** I also measured between other reference points:
  - head to head: 457 px, or 2.07 m
  - torso to torso: 500 px, or 2.27 m

  Both are within about 6% of the centroid result, so I kept the centroid value.
- **Time base.** Only frame 0 is used, so whether the rate is 20.43 or 25 fps makes no difference.
- **Confidence.** Moderate to high. The main uncertainty is which point on each body the annotator chose.
