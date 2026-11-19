# q_213 – width of the teacup with the plate (m)

2D render, 1080x1080, file fps 24 = question_fps 24. Prior: gravity 9.8 m/s^2; the falling sugar cube is the prior's object.

## Scale (measure.py)
- Cube centroid y, frames 22–45 (frame 21 clipped at the top edge, excluded), t = frame/24, quadratic fit:
  a = 682.4 px/s^2, rms residual 0.12 px (clean free fall). First / second halves separately: 682.0 / 682.8 px/s^2.
  Bbox top / bottom / middle tracks give 680.4 / 681.8 / 681.1 px/s^2 (consistent within 0.3 pct).
- Scale = 9.8 / 682.4 = 0.01436 m/px. The cube falls into the cup, so it lies in the same plane.

## Width (measure.py, edge.py)
- The cup+saucer bounding box is widest at the saucer rim (cup body max 140 px incl. handle).
- Saucer half-contrast edges at rows 1053–1055 (frame 5): x 450.5 → 636.5, width 185.5–186.0 px.
  Threshold mask on frames 0, 5, 12: x 451–636 = 186 px. Use 186 px.
- Width = 186 × 0.01436 = 2.67 m.

## Checks / caveats
- Second route: bbox-based accelerations (680–682 px/s^2) give 2.67–2.68 m; saucer width ±1 px → ±0.5 pct.
- The result is large for a real teacup (~0.15 m), but in a 2D scene the gravity scale has no geometric route to be
  wrong (perfect parabola, same frame rate); the scene objects are evidently built large, so the prior's scale is
  used as instructed. A real-size cup would require g ≈ 0.55 m/s^2, contradicting the exact prior.
- Other reading: the cup alone (with handle) 140 px → 2.01 m; rim 134 px → 1.92 m. Answer uses cup with plate.
- Confidence: moderate-high on the measurement (~1 pct); the main risk is the interpretation of the scene scale.
