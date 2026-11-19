# q_2370: speed of the yellow toy at t = 0.60 s (cm/s)

- **Time base:** question_fps = file fps = 24, so t = 0.60 s is frame round(14.4) = **f14**. This is the fruit's first
  free-flight frame. The far person released it at f13/14.
- **Object:** the yellow toy is the scene's `yellow_fruit`, a pale-yellow mango/pear-like toy with a dark stem cap. The far
  person throws it to the near person. In depth_info it is the "carrot" (2.63 m at 0.60 s), which fits: it is just in
  front of the far person (3.237 m). The "jar" (1.9735 m at 0.60 s) is the white ball, which is still in the near
  person's hand at f14.
- **Camera:** f = 0.5959 × 1280 = 763 px, principal point (640, 360).

## Measurement
- **Centroids:** I re-measured both objects with an alpha-weighted silhouette (`remeasure2.py`, written to
  `remeasured2.json`, masks checked in `frames/fruit_masks2.png`).
  - Alpha comes from greenness, and the stem cap and blurred rim are included. The scene record's yellow-only mask
    left out the cap, which biased it by 1-3 px.
  - Dropped: fruit f18-19 and ball f18-19, where the two objects overlap.
- **Depth along the throw:** depth_info gives only one depth per object, so the change in depth comes from physics
  (the prior: g = 9.8 m/s²).
  - Each throw is fitted as a 3D ballistic trajectory p(t) = p0 + v t + ½ g t², projected through the pinhole.
  - The fitted unknowns are the gravity direction in camera coordinates (pitch, roll), plus position and velocity.
  - Each throw's position is pinned to its given depth: fruit |p(f14)| = 2.63 m, ball |p(f14)| = 1.9735 m.
- **Fitted gravity direction** (`fit2.py`, `fit_ball.py`):
  - fruit alone: pitch 59.6°, roll 8.7°, rms 0.62 px;
  - ball alone: pitch about 58-60°, roll about 10°, rms 1.44 px;
  - joint fit: pitch 59.3°, roll 9.6°.

  The camera looks steeply down. The two independent throws agree on this.
- **Fruit velocity at f14:** (-1.17, 0.38, -3.91) m/s. Most of it is the approach toward the camera: depth goes from
  2.63 m to 1.72 m at f23.
  - Instantaneous speed: 418 cm/s.
  - Reference convention (forward difference f14→f15, positions smoothed over 5 frames centred on f14): 402-404 cm/s.
  - Back-projecting the measured pixels with the model depths gives forward differences of 475, 438, 407, 372 and
    338 cm/s for f12-16. The centred 5-frame value is 404 cm/s.
  - The parabola extrapolates to the hand-phase frames f12-13 within about 4 px, so the centred smoothing window is
    valid.
- **Answer: 404 cm/s.**

## Checks and caveats
- **Second route:** the ball's trajectory fitted alone gives the same gravity direction as the fruit's. Predicted
  catch depths are plausible:
  - ball reaches about 2.78 m at f26, in front of the far person (3.24 m);
  - fruit is at 1.68 m at f24, near the near person (1.58 m).
- **Sensitivity:** the speed depends strongly on the pitch: 340 cm/s at 40°, 369 cm/s at 50°, 405 cm/s at 60° (forward
  difference at f14).
  - A rough check from the people (taking their given distances as pelvis distances, and their feet on one floor)
    suggested about 40-50°.
  - That check rests on hand-picked pelvis points and on what the person distances refer to. I gave more weight to the
    two projectile fits, which agree with each other and fit to under 1.5 px.
- **Confidence:** moderate. The likely range is 370-420 cm/s.
- **Scene record:** the record's "camera looks steeply down" is consistent with this result. Its fruit centroids are
  biased by 1-3 px because the stem cap was left out of the mask.
