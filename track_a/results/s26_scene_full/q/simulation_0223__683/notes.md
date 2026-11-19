# Q683: speed of the moving red general at t = 0.5 s

- fps = question_fps = 24, so t = 0.5 s is frame 12. 2D top-down scene: one metres-per-pixel scale from the prior.
- Scale: the general's disc diameter is 86.5 px. My edge profiles at frames 14, 15, 24 and 30 gave 86–87 px across the motion, which matches the record's 86–87 px bbox. 0.097 m / 86.5 px = 1.121e-3 m/px.
- Duplicated frames: the pair (11, 12) shows the same image, and frame 11's true position is missing. So the raw one-frame difference at frame 12 is 0 and can't be used.
- Speed: I fitted a quadratic (uniform acceleration) to the record's mask centroids on clean frames.
  - Windows 2–17, 5–17, 8–16 and 10–14 give a backward difference p(12) − p(11) of 12.31–12.32 px/frame (residuals 0.06 px).
  - Clean check: (y13 − y10)/3 = 12.31 px/frame, which is the velocity at frame 11.5.
  - My own background-difference mask (measure.py) is cruder (includes shadow; residual 0.6 px) and gives 12.12–12.22 px/frame.
- Speed = 12.31 px/frame × 24 × 1.121e-3 = **0.331 m/s**.
- Confidence: good, about ±3 %. The main uncertainty is the pixel diameter (86–87 px).
