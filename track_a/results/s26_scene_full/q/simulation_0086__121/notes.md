# Q121 – distance car ↔ bike at t = 2.0 s (frame 48, fps 24 = question_fps)

**Scene.** 2D top-down render. The car moves left with constant acceleration. The cyclist moves right at a steady ≈16.0 px/frame. Both are on the same ground plane, so one metres-per-pixel scale applies to both.

**Scale from the prior (a = 4.03 m/s²).**
- I tracked the car centre by template matching against the frame-0 car (tm.py), with a subpixel parabolic peak.
- Quadratic fits to the car centre:

  | Frames | Acceleration (px/frame²) | Residual std |
  |---|---|---|
  | 2–30 | 0.5303 | 0.06 px |
  | 2–40 | 0.5313 | – |
  | 10–40 | 0.5316 | – |

- Past frame ≈45, near the left edge, the template and edge tracks disagree with each other and the apparent acceleration drifts. I left those frames out.
- a = 0.5313 × 24² = 306.0 px/s², which gives a scale of 0.013170 m/px.
- Sanity checks: car length 438 px → 5.77 m (a Cybertruck is about 5.7 m), and cyclist speed → 5.06 m/s.

**Positions at frame 48.**
- Car centre is 478.4 px. This is the mean of three estimates:
  - the quadratic model: 477.9–478.4
  - the template match: 474.8
  - front bumper + half the length: 482.5
- Car y = 651.75.
- Bike centre is x = 1702.5, the centre of the wheel-to-wheel box, checked on the frame. Bike y = 477.25.
- The distance is 1236.5 px, which gives **16.28 m**.

**Variants and checks.**
- If the rider pelvis is taken as about 11 px behind the bike centre, the distance is 16.14 m (−0.9%).
- Using the all-frame fit (a = 0.547) instead would give a scale 3% smaller, about 15.8 m. I rejected it because of the near-edge artefacts.
- Confidence: about ±2%.
