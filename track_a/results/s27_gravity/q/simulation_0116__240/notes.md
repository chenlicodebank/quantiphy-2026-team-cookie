# Q240: speed of the football at 0.5 s

- This is a 2D scene. The football falls straight down. The scale comes from the prior g = 9.8 m/s^2.
- The file runs at 24.006 fps and the question at 24.0 fps. I used 24.0, so t = 0.5 s is frame 12.
- I fitted a quadratic to the centroid track `cy` from scene/tracks/football.csv, leaving out the frame-17 outlier (`fit.py`):
  - The acceleration is 3.123 px/frame^2, which gives 0.005448 m/px.
  - The fit puts the moment of rest at frame -0.01, so the ball starts at rest at frame 0.
  - The residual rms is 0.43 px.
- Speed by the backward difference at frame 12, from the fit: 4.699 m/s. This agrees with the analytic value g x 11.5/24 = 4.696 m/s.
- Checks:
  - Fitting the bbox centre gives 4.705 m/s.
  - Fitting only frames 3 and later gives 4.697 m/s.
  - The raw one-frame differences give 4.65 m/s (centroid) and 4.78 m/s (bbox), which is noisier.
  - The ball measures about 61 px, or about 0.33 m, which is plausible for a football.
- Answer: 4.70 m/s. Confidence is high.
