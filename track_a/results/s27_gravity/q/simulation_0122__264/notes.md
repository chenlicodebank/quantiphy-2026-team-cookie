# q_264: length of the sword (m)

This is a 2D scene. The prior is gravity (9.8 m/s²). The sword falls straight down, tip first, and does not change apparent size. That gives one metres-per-pixel scale from the fall acceleration. question_fps is 25, the same as the file fps.

## Acceleration (px/frame²)
- From the scene record's tip_y, a quadratic fit over f0-16 gives 6.85 (rms 0.8 px).
- Blade template matching (`tm.py`) used the blade pixels of f12, f13 and f14 as templates, matched by vertical shift with sub-pixel refinement, against a per-row median background:
  - f9-16: 6.88, 6.74, 6.82.
  - f5-16: 6.83, 6.81, 6.85.
  - f0-3 failed (too few pixels at the top edge) and were ignored.
- Sub-pixel tip edge and cross-guard centroid (`sub.py`) were noisier (6.3-7.3) and only used as a rough check.
- Adopted value: a = 6.82 ±0.07 px/frame², which is 4262 px/s². The scale is 9.8 / 4262 = 2.30e-3 m/px.

## Pixel length
Pommel top to tip, with the sword sharp (no motion blur seen at 2x zoom):
- f15: 520 → 935 = 415 px.
- f16: 635 → 1049/1051 = 414-416 px.
- The record gives 417 ±3.

Adopted value: 416 px.

## Answer
416 × 2.30e-3 = **0.956 m**. A plausible longsword is about 1 m.

The spread over the acceleration and length estimates (6.74-6.88 px/frame², 414-417 px) gives 0.94-0.97 m. Confidence is good, to about ±2%.
