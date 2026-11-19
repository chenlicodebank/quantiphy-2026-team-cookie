# Q330 – speed of the cup at t = 2.25 s (m/s)

- fps = question_fps = 24 → frame 54; speed = |p(54) − p(53)| × 24.
- 2D video, cup slides left→right along the counter; camera static.
- Frame 54 the cup is cut by the right image edge (x1 = 1919), so the record's cx_est there is a linear
  extrapolation — not used. Instead I measured the cup's LEFT edge (HSV blue mask, largest component), which is
  fully visible: `measure.py` (line fit of left edge, value at the centre row y = 649.5) and `measure2.py`
  (left edge at rows 560/600/650/700/740).
  - 53→54 displacement: line-fit 21.6 px; rows 600-740: 22, 23, 23, 23 px (top row 560: 18, rim near edge).
    Adopted 22.7 ± 0.7 px/frame. Cup tilt changes only ~1° between these frames (effect < 1 px at centre height).
  - Earlier frames 46-53 give 24-25 px/frame then ~23, so the slight slowing is consistent.
- Scale: prior diameter 0.087 m = rim (top) width of the upright cup, 117-122 px over frames 8-28 (mean ≈ 119.5 px)
  → 7.28e-4 m/px.
- Speed = 22.7 × 24 × 7.28e-4 = 0.397 m/s → answer 0.40 m/s.
- Check: steady phase 28-51 (24.6 px/frame) gives 0.43 m/s; frames 52-53 ~23 px/frame (0.40 m/s) — consistent with
  slight deceleration at exit. Frame 55 mask anomaly (edge shading) doesn't affect frames 53-54.
- Confidence: moderate-high (main uncertainty: which diameter the prior means, rim vs. base; rim assumed).
