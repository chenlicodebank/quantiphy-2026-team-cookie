# q3252 – velocity of the cup at 2.00 s

Prior: acceleration 2.00–2.30 s = 0.32 m/s². Internet video, so one scale: m/px = 0.32 / (pixel acceleration over the same window).
Answer = 0.32 × v_px(2.00) / a_px(2.00–2.30). No metric size is needed.

Time base: 30 fps (the file's rate is 30.013, basically the same). 2.00 s is frame 60 and 2.30 s is frame 69. The camera is static: the background drifts only a few px, while the mug moves 60–95 px/frame.

Reference point: the leading (right) edge of the mug body. It is the only edge visible at frame 60, because the left edge is cut by the image border until frame 62. I re-measured it myself (edges.py: difference from the empty frame 100, column runs in three y-bands). Bands y = 650–700 and 720–760 match scene/tracks/mug.csv to within 1–2 px.

Right-edge per-frame displacements (px, band 720–760), from frame 56: 58 58 60 62 [64 at 60→61] 65 66 68 69 71 72 74 76 [79 at 69→70] 81 84 85 88 92.

- v_px(2.00), forward difference = 64 px/frame = 1920 px/s.
- a_px, endpoint second-difference over 60→69 = (79 − 64)/9 = 1.67 px/frame² = 1500 px/s². This gives 0.32 × 1920/1500 = 0.41 m/s.
- a_px from a quadratic fit of the right edge over frames 56–74 = 1559 px/s². This gives 0.32 × 1920/1559 = 0.394 m/s. The same fit with the centred v at 2.00 s (1863 px/s) gives 0.38.
- A quadratic fit over all of frames 54–79 gives 0.36. Its acceleration is inflated by the faster-looking late frames: perspective makes pixel speed grow toward the right edge of the image.

Sanity check: with 0.32 / 1550 ≈ 0.21 mm/px, the 420 px body is about 8.7 cm wide, which is a plausible mug. So the scale is consistent.

Answer: 0.40 m/s. The plausible range is 0.38–0.41 m/s. Confidence is moderate to good; the main uncertainty is how the annotator took the acceleration.
