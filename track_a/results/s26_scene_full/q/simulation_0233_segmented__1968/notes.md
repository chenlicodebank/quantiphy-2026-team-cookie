# Q1968 — vertical length of the chair (2D top-down clip)

- 2D segmentation clip at 24 fps (file fps = question_fps). The camera looks straight down; the black cat walks right and the chair (seat plus backrest) is static on the right.
- "length (vertical)" is the chair's vertical extent in the image. I measured the chair mask bbox in `measure.py`: y 496/497 to 715, which is **219-220 px** in frames 0, 25 and 49 (the width is 297 px).
- Scale comes from the cat's speed prior of 0.714 m/s:
  - The cat's silhouette centroid over frames 22-49 (fully visible) moves 13.354 px/frame by mean step and 13.361 by linear fit. That is 320.7 px/s, so the scale is 0.714/320.7 = 0.002227 m/px.
  - Second route: the tail end x0 moves 13.98 px/frame and the nose x1 moves 13.08 px/frame, giving 0.0021-0.0023 m/px.
- Chair vertical size = 219.5 x 0.002227 = **0.489 m**. The other reference points give 0.47-0.50 m.
- Confidence: moderate-high. The main uncertainty is the gait ripple in the cat's speed (about ±3%).
