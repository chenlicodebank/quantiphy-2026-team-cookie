# Q1013: displacement of the fish from 0.5 s to 1.0 s (m)

Prior: the fish's speed is 0.67 m/s (no time given, so I read it as the fish's mean speed). This is a 2D scene and the fish stays at a constant depth. fps = question_fps = 24, so the interval runs from frame 12 to frame 24.

Method (`measure.py`, using scene/tracks/koi_fish.csv):
- Trunk texture track: the mean step over the moving frames is 543.3 px/s, giving a scale of 0.001233 m/px. The displacement from frame 12 to 24 is 273.1 px, or **0.337 m**.
- Bounding-box centre track: 535.8 px/s, giving 0.001250 m/px. The displacement is 272.5 px, or 0.341 m.
- Constant-speed check: 0.67 m/s × 0.5 s = 0.335 m.

The three routes agree to within 2%. The per-frame speed varies by about ±5% (it peaks near frame 25), and the 12–24 window is close to the mean. The motion is purely horizontal.

Answer: 0.337 m. Confidence: high (±3%).
