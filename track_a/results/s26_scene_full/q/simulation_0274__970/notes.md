# Q970 – raccoon displacement 0.5 s → 1.0 s (frames 12 → 24 at 24 fps; fps = question_fps, so no re-timing)

2D top-down render, static camera; one px→m scale from prior (length incl. tail = 1.51 m).

Scale: nose-to-tail-tip x extent measured in code (measure.py; band y 712–770, |frame − floor bg| > 12, longest run of columns).
Frame 0 (rest, stationary) 305 px; median over all frames 299 px (10–90 pct 292–303); scene record median 296.
Visual check of frame 0 zoom: tail tip ≈ 594, nose ≈ 892 → ≈ 300 px. Used L ≈ 300 px → 0.00503 m/px.

Displacement px (frames 12→24):
- root (template-registered body centre, scene record): 1002.5 → 1252.7 = 250.2 px
- bbox nose: 1116 → 1364 = 248; tail tip: 824 → 1073 = 249; my own extents: 1119→1365 = 246, 824→1073 = 249
- mean step 20.58 px/frame × 12 = 247
Adopted ≈ 249 px → 249 × 1.51 / 300 ≈ 1.25–1.26 m (range 1.24–1.27 depending on length choice).

Answer: 1.26 m. Confidence: good (±3%), main uncertainty is the pixel length used for the prior.
