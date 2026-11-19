# q_3099 – ball displacement 0.10 s → 0.30 s

- Time base: fps = question_fps = 30, so 0.10 s = frame 3, 0.30 s = frame 9, and the prior's 0.5 s = frame 15.
- The camera is handheld and looks down; it drifts ≤1.3 px/frame. I used the camera-stabilised centres (cx_stab, cy_stab) from scene/tracks/basketball.csv.
  - The raw centres give the same result within 0.2 %.
- Verification: `check.py` draws the recorded fitted circles on frames 3, 9, 15 and 16 (`frames/check.png`). They hug the ball well.
- Pixel displacement from frame 3 to frame 9: 470.5 px (raw 471.3 px).
- Pixel speed at frame 15 (prior 2.94 m/s):
  - forward difference (15→16): 2362 px/s
  - backward difference (14→15): 2321 px/s
  - smoothed (13→17): 2335 px/s
- Scale = 2.94 / speed_px, so the answer is:
  - 0.586 m with the forward difference
  - 0.596 m with the backward difference
  - 0.592 m with the smoothed speed
- Second route: the image speed is nearly constant, with a median of 78 px/frame. That gives 2.94 m/s × 0.2 s = 0.588 m, which agrees.
- Answer: **0.59 m**. Confidence is high; the spread between methods is about ±1 %.
