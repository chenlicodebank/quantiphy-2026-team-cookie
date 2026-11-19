# q_2514 — velocity of red ball at 0.6 s (cm/s)

- Video and question fps are both 24, so t = 0.6 s → frame 14. depth_info is given at frames 5, 10, 14 and 19
  (0.8715, 1.166, 1.372 and 1.315 m).
- Centres come from scene/tracks/red_ball.csv (cx and cy_corr; frames 12-17 are partly occluded by the table's back edge,
  so cy_corr is used). I checked the centres by drawing them on frames 9-19 (frames/strip*.png): they sit on the ball.
- Camera: f = 0.5959 × 1280 = 762.8 px, principal point (640, 360). Back-projection: P = ((u-cx)/f, (v-cy)/f, 1) · Z,
  with Z = distance / sqrt(1 + x² + y²).
- Depth per frame: the given distances interpolated four ways (linear, cubic through the 4 points, quadratic fit, and
  ball-diameter depth rescaled to the given values). The depth from the ball's diameter (7 cm prior) gives 0.93, 1.21,
  1.24 and 1.27 m at the given frames. This matches the given values at frames 5, 10 and 19, but gives 1.24 vs 1.372 m at
  frame 14, where the ball is occluded.
- Velocity at frame 14 (script vel.py), smoothed over about 5 frames:
  - linear: mean speed 12-16 = 173, |P16-P12|/4 = 152, |P17-P12|/5 = 150
  - cubic: 173 / 165 / 161
  - quadratic: 158 / 151 / 152
  - diameter-rescaled: 176 / 161 / 159
  - one-frame forward difference at frame 14: 151-173
- Second route: the image motion alone is about 35 px/frame at about 1.37 m, which gives ≈ 151 cm/s; the depth change adds
  the rest.
- Answer: 163 cm/s (the middle of the estimates). Confidence: moderate, about ±8%. The main uncertainty is the depth
  rate at frame 14, because only 4 depth samples are given.
