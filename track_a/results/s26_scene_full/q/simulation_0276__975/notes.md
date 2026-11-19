# q_975: speed of the raccoon at 1.0 s (m/s)

- 2D top-down render with a static camera, 24 fps (file fps = question_fps, so no re-timing). t = 1.0 s is frame 24.
- **Scale:** the prior gives a length of 1.51 m, tail included. The nose-to-tail-tip bbox width has a median of 295 px over the frames.
  I checked it by eye at frame 24 (tail tip at x≈1073, snout at x≈1363, so ≈290–295 px). That gives 1.51/295 = 0.005119 m/px.
- **Pixel speed:** I fitted a line (`fit.py`) to the scene track. The x-velocity is nearly identical for every reference point and
  window: the centroid gives 20.39–20.92 px/frame, the tail tip 20.32–20.49, the snout tip 20.34–20.65 and the bbox centre
  20.41–20.49, over the windows 2–71, 8–40, 12–36, 16–32, 2–24 and 24–48. There is no acceleration, and the motion starts
  at frame 2. The per-frame centroid steps are noisy (15–28 px) because of the gait, so I used the smooth origin speed
  of 20.45 px/frame.
- **Speed:** 20.45 × 24 × 0.005119 = 2.51 m/s.
- **Second route:** the tail-tip and snout-tip tracks give the same 20.4–20.5 px/frame, which agrees to within 1%.
- **Confidence:** high, about ±3%. The main uncertainty is the pixel length (±5 px).
