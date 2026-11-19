# q3245 – velocity of the acorn at 2.10 s (m/s)

Prior: acceleration of the acorn from 2.00 s to 2.30 s = 0.77 m/s^2. No depth_info. Internet clip, 2D side view.
Time base: file fps = question_fps = 30, so t=2.10 s is frame 63, and the prior window is frames 60–69.

## Method (annotator convention: one scale = prior / pixel value)
- answer = 0.77 m/s^2 × v_px(63) / a_px(2.00–2.30), so only the ratio of pixel velocity to pixel acceleration matters.
- Camera: almost static (record camera.csv: x shift ≈ 4 px, nearly constant over frames 57–73). Used raw pixels,
  the way annotators measure; ref-stabilised values give about the same result (0.66).
- Reference point: the narrow stem knob. Own track (`track_stem.py`): a centroid of how much darker each pixel is than
  frame 90 (no acorn there), taken over three thin row bands (555–585) above the cap. A centroid like this does not
  move under motion blur. It agrees with the record's raw_stem_x to about 1–2 px, and frame 63 was checked visually
  (frames/f63.png: stem at x≈588).
- Stem x (raw, band 560–580): 60: 305.7, 61: 397.3, 62: 490.9, 63: 590.3, 64: 694.1, ..., 69: 1266.6, 70: 1395.6.
- v_px(63), forward difference = 103.8 px/frame = 3114 px/s.
- a_px over 2.00–2.30: (v69 − v60)/0.3 s = 3720–3770 px/s^2. A quadratic fit over frames 60–70 gives 3630–3750, and
  one over 61–69 gives 3530–3700.
- Scale ≈ 0.77/3740 = 2.06e-4 m/px, so the acorn's length (~330 px) is about 6.8 cm. That is plausible for a toy.
- v(2.10) = 3114 × 2.06e-4 ≈ **0.645 m/s**.

## Checks / spread
- Every route in the 2.0–2.3 window gives 0.63–0.68 m/s: endpoint acceleration on the stem (own track) 0.64, the
  record's ref_stem 0.66, quadratic fits 0.64–0.68.
- Using the bounding-box middle of the dark cap (`track_cap.py`, `combine.py`) gives 0.62 by endpoints but 0.53 by
  fit. The cap edges are smeared by motion blur, so this point is noisier.
- Wider fit windows (59–72 or 58–73) give a larger acceleration (~4100 px/s^2, because the acorn's acceleration
  increases over time) and so 0.57–0.58. The prior names 2.00–2.30 s specifically, so the window estimate is used.
- The pixel acceleration is the main uncertainty (frame-to-frame second differences of 2–7 px/frame^2). Confidence:
  probably within ±10%.
