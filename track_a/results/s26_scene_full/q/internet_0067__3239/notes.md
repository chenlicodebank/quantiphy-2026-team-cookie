# q3239 — acceleration of the acorn at t = 0.17 s

- The "acorn" is the scene record's "cup": a black cap on a white body, pulled left to right across the floor by a cord. The camera is static and the motion is 2D.
- fps = question_fps = 30. t = 0.17 s → frame round(5.1) = 5.
- Scale: height prior 8 cm. Pixel height (cap top to base of body) is about 610–640 px on frames 3–5 (checked on a zoomed crop of f4 at about 1005→1620, a background-difference profile, and the scene record's 604–644). Using 625 px gives 1.28e-4 m/px.
- Positions (x, px). Cap half-max centre: f3 699, f4 1244, f5 1956, f6 2818 (measure.py). Cap band centres: f4 1239/1242, f5 1963, f6 2831/2834 (edges.py).
  Per-frame displacement: 545 → 712 → 862 px. f6→f7 is about 880 px (from the trailing edges, because f7 is clipped).
- Acceleration at frame 5 uses the central second difference x4 − 2x5 + x6: 150 (half-max centre), 144 and 149 (cap bands), 158 (white body). I took 148 px/frame².
  148 × 900 × 0.08/625 = 17.0 m/s².
- Other conventions: the backward second difference (f3, f4, f5) gives about 170 px/f², or 19.6 m/s². The forward second difference (f5, f6, f7) gives about 40 px/f², or 4.6 m/s², because the object stops speeding up after f6 and starts tipping. Frame 7 is also clipped, so that forward value is unreliable. I answered with the central difference.
- Confidence: moderate. The result depends on which difference convention the reference used, and motion blur adds ±15 px to each position.
