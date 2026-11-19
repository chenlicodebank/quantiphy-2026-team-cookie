# q_3165 – ball velocity at 3.00 s (internet_0057)

- Time base: file fps = question_fps = 30, so t = 3.00 s is frame 90. The ball is in free flight (release at 54, first bounce at 97).
- Track: scene/tracks/ball.csv, bg-fixed centre (camera drift removed). Frames 73–77 are degraded and left out.
- Scale from the prior (g = 9.8 m/s²): I fitted a parabola to y(frame) over the free flight from 54 to 96, which gives a = 2.063 px/frame² (rms residual 1.8 px).
  That makes the scale 9.8 / (2.063 × 900) = 0.00528 m/px. Other fit windows gave: 55–95 → 2.061; 60–90 → 2.063; 78–96 → 2.011; 54–72 → 2.125.
- The horizontal speed is constant at about 15.3 px/frame.
- Velocity is a forward difference (frame 90 → 91), evaluated from the fit at frame 90.5. This gives 6.72 m/s (window 54–96). The alternative windows give 6.72–6.82 m/s.
- Second route: the raw forward difference of the track from frame 90 to 91 is 43.3 px/frame, which is 6.86 m/s.
  The raw step from 89 to 90 is 37.4 px/frame (5.9 m/s), so raw single steps are noisy (±2 px). I used the fitted value.
- Answer: 6.72 m/s. Confidence: good, about ±3 %.
