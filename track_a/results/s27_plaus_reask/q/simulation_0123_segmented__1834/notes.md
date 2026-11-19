# q_1834 — toothbrush length (m)

The video is a top-down view of a planar scene at 24 fps. The file and question_fps are both 24, so the times agree. There is no depth_info. I treated it as a 2D scene with one metres-per-pixel scale.

- The "cup" is the teal block, the only object that moves. A linear fit of its mask centroid x over frames 2–71 gives 14.536 px/frame = 348.9 px/s. The mean per-frame dx × 24 = 348.8, which agrees with the fit. Its y does not change, and its speed is constant.
- Scale: 0.338 / 348.87 = 9.689e-4 m/px.
- The "toothbrush" is the yellow-green stick with a grey head in the middle, at about (792, 442). I measured its length on frame 0 (`measure_brush.py`) as the PCA long-axis extent of the non-white mask. With thresholds of 240, 235, 220 and 200 it reads 116.9, 116.2, 114.1 and 114.1 px. I took 115.5 ± 1.5 px.
- Length = 115.5 × 9.689e-4 = **0.112 m**. The range from the threshold spread is 0.110–0.113.
- Second check: a manual read of the endpoints on a zoomed grid crop gave (753, 403) to (836, 486), about 117 px, which is consistent.
- Plausibility: with the same scale, a sink basin is 479 px = 0.46 m, which is plausible. The cup is 4 × 7.6 cm and the toothbrush 11 cm, both on the small side; a real toothbrush is about 17–19 cm. Without depth info I cannot detect any perspective difference, so I kept the single scale from the prior, which is exact.
- Confidence: moderate. The pixel measurement is good to about 2%. The main risk is whether a single scale is right for this scene.
