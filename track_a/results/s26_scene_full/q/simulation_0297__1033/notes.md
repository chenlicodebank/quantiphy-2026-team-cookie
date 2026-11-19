# q_1033: jellyfish displacement from 0.5 s to 1.0 s

- 2D simulation, 24 fps (file and question_fps agree). t=0.5 s is frame 12 and t=1.0 s is frame 24.
- Track: the core-ball centre (scene/tracks/creature.csv), checked with check.py. It moves horizontally at a constant
  20.968 px/frame over frames 1–71 (linear fit; per-frame dx is 18–24 px, which is jitter). The floor-shadow track gives
  20.970 px/frame on its own, so the two agree.
- Scale from the prior: 1.75 m/s ÷ (20.968 × 24 px/s) = 0.003478 m/px.
- Displacement:
  - Fit route: 12 frames × 20.968 px = 251.6 px, which gives **0.875 m**. This is exactly 1.75 m/s × 0.5 s, because the
    speed is constant.
  - Raw route: the endpoint positions at frames 12 and 24 are 254.2 px apart, which gives 0.884 m (+1%, within the
    per-frame detection jitter).
- Answer: 0.875 m. Confidence is high, because the motion is constant-velocity and straight with no events in the window.
