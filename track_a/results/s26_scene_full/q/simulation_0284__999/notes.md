# Q999 — displacement of the plane, 0.5 s → 1.0 s

- 2D top-down render, static camera. The plane flies in a straight line to the left at a constant ~34.25 px/frame
  (scene/tracks/aircraft.csv, from template matching; frames 2–30 give 34.1–34.6 px/frame and dy ≈ 0). It is stationary
  only at frames 0–1.
- Scale comes from the prior, speed = 22.16 m/s: m/px = 22.16 / (34.25 px/frame × fps).
- Results (check.py):
  - fps 24 (file): frames 12→24 give 11.10 m. Frames 13→25 give 11.11 m. Plane length 15.3 m.
  - fps 25 (question_fps): frames 12→25 (Python round(12.5)=12) give 11.55 m. Frames 13→25 give 10.66 m. Plane length 14.6 m.
- Both rates are physically plausible, so the plane size cannot tell them apart. The motion is constant, so the
  analytic value speed × 0.5 s = 11.08 m matches the 24-fps result.
- Answer: 11.10 m. It is within about 4 % of every candidate convention (10.66 / 11.10 / 11.55).
- Second route: the analytic speed × Δt (11.08) agrees with the pixel-track route (11.10).
- Confidence: high for the 24-fps reading. If the reference used 25 fps with 13 frames, the error is about 4 %.
