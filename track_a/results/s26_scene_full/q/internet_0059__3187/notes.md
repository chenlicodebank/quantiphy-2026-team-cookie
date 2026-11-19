# q3187 – average velocity of the ball, 2.50 s to 3.20 s

- Time base: the file and the question are both 30 fps. t=2.50 s is frame 75 and t=3.20 s is frame 96. The ball is in free flight with no bounce in this window (the bounce is at about 3.35 s).
- Scale comes from the prior (g = 9.8 m/s²). I fitted a parabola to the ball centre's camera-compensated y over frames 66-97 and left out frames 77-80, where the top of the ball is cut off.
  - Scene record: g = 4956 px/s², so 0.001977 m/px.
  - My own re-track (red/dark mask bbox centre, camera shift by phase correlation on the wall with the ball masked out): g = 4954 px/s², so 0.001978 m/px.
- Displacement from frame 75 to frame 96, in background coordinates:
  - scene record: (962.6, 748.7) px;
  - my re-track: (961.2, 748.1) px.
  - That is |d| ≈ 1219 px = 2.41 m over 0.70 s, so the **average velocity is 3.44 m/s**.
- Checks:
  - Taking the displacement from the fitted trajectory gives 3.48 m/s.
  - The two tracks agree to 0.1%.
  - The other reading, mean scalar speed (path length / time), gives 3.82 m/s. I answer with the vector reading (net displacement / time), because the question says "velocity".
- Confidence: good (about ±3%). The main uncertainty is the g-based scale. The fit residual is about 4-5 px rms.
