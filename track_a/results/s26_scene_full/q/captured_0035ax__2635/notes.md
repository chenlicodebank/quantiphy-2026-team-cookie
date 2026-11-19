# q2635 – soccer ball velocity at 1.5 s (cm/s)

- t = 1.5 s -> frame 36 (question_fps 24 = file fps). The ball is rolling back toward the far person after the collision at frame 19, with a clean silhouette.
- Camera: f = 0.5959 x 1280 = 763 px, principal point (640, 360).
- depth_info: the soccer ball is at 3.052 m at t = 1.6 s (frame 38). The second "soccer" entry at 1.6 s (2.412 m) must be the basketball, since it
  matches the basketball's 69 px diameter (2.412 x 69 / 763 = 21.8 cm, against 22.0 cm at t = 0.6 s from 2.27 m and 74 px; prior 23.2 cm).
  The t = 0.6 s soccer depth is before the collision, so it was not used for depth interpolation.
- Depth per frame: Z ∝ 1/diameter. I fitted 1/diam linearly over frames 26–48 and anchored it at Z(38) = 3.052 m, which gives Z(36) = 3.013 m, with Z rising about 2 cm per frame.
- 3D centres: back-projection ((u-cx)/f, (v-cy)/f, 1) x Z. Speed = |forward difference| x 24.
- Route 1 (scene track centres): per-frame speeds are about 66–68 cm/s, but the 35→36 step is 94 cm/s because of a probable dropped frame.
  Mean over a 5/7/9-frame window centred on 36: 72.8 / 70.8 / 70.0 cm/s.
- Route 2 (my own mask-centroid track, measure.py): 72.9 / 70.9 / 70.9 cm/s for the same windows. Excluding the anomalous step gives a median of about 67–68 cm/s.
- Answer: 70 cm/s, the smoothed value over at least 5 frames, which follows the reference convention.
- Confidence: moderate. The main uncertainty is the depth rate taken from the apparent size, since the depth component is about half of the speed.
