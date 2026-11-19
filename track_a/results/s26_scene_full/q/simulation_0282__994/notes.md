# Q994: displacement of the dragon from 0.5 s to 1.0 s

- This is a 2D top-down render at 24 fps (question_fps is also 24). So t = 0.5 s is frame 12 and t = 1.0 s is frame 24.
- I used the torso/hip point from scene/tracks/dragon.csv. The overlay `frames/check.png` shows it on the hip at f12 and f24.
- The motion is nearly uniform: per-frame steps are 32–37 px, and the mean over steps 1→2 … 70→71 is 34.42 px/frame, which is 826.2 px/s.
- Scale from the prior: 1.29 m/s / 826.2 px/s = 1.5615e-3 m/px.
- The displacement from f12 to f24 is 409.9 px, which gives **0.640 m**.
- Second-route checks:
  - Using the mean speed that includes the near-zero 0→1 step gives 0.649 m.
  - Using the local mean speed over frames 12–24 gives 0.643 m.
  - Assuming exactly uniform speed, 1.29 × 0.5 = 0.645 m.
  - All of these agree within 1.5%.
- Confidence: high.

Script: check.py
