# q_68: distance between the black-shirt and white-shirt men at 1.0 s

- The scene is a top-down 2D view at 24 fps. question_fps is also 24, so there is no re-timing, and t = 1.0 s is frame 24.
- On frame 24 (frames/f24.png), the black-shirt man is the upper walker (centre ≈ (1066, 420)) and the white-shirt man is the lower one (≈ (985, 604)). This matches scene/.
- **Scale.** The prior is that the black-shirt man walks at 1 m/s. His pixel speed comes from a linear fit of his track over frames 12–36, using the same reference point as the distance, so the head-height versus pelvis parallax cancels.
- **Distance.** I fitted both men's x(t) and y(t) linearly over frames 12–36 and evaluated the fits at frame 24, which removes the gait wobble (measure.py).

| point | black-shirt speed (px/frame) | distance (px) | distance (m) |
|---|---|---|---|
| head | 12.26 | 218.4 | 0.742 |
| mask centroid | 11.23 | 201.7 | 0.749 |
| pelvis_est | 11.53 | 205.3 | 0.742 |

Fitting over other windows gives 0.739 (frames 6–42) and 0.751–0.763 (frames 2–71).

- **Second route.** The raw head distance at frame 24 is 215.6 px, against a mean head step of 12.15 px/frame. That gives 215.6 / (12.15 × 24) = 0.739 m.
- **Answer: 0.745 m.** Confidence is good, about ±3%. The main uncertainty is which speed estimate the prior refers to.
