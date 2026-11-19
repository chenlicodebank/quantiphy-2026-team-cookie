# q2245 — ball diameter (cm)

Method (lab card): D = depth × pixel diameter / f, f = 0.5959 × 1280 = 763 px. File fps = question fps = 24.

Route 1 — t = 0 (frame 0–3, ball at rest on green background, depth 1.818 m):
- edges.py: half-max edge widths of |frame − frame48| across the ball rows: 25–26.8 px (widest rows ≈ 26).
- circfit.py: circle fit to the upper arc + sides of the mask: 24.6–25.9 px (threshold-dependent).
- The vertical extent (≈29 px) includes the shadow/contact at the bottom, so I did not use it.
- Using ≈26 px: D = 1.818 × 26 / 763 = 6.19 cm.

Route 2 — t = 0.6 s (frame 14, rolling on the white board, depth 1.7288 m):
- Horizontal half-max width (perpendicular to the motion blur): 26.3–26.9 px.
- D = 1.7288 × 26.7 / 763 = 6.05 cm.
- Frames 15–16 (≈27.2–27.7 px at depth ≈1.69–1.71 m) give ≈6.1 cm.

Answer: 6.15 cm, the mean of the two routes. The scene record's equivalent diameter (28–29 px) includes the shadow, so it is a little too big.
Confidence: moderate, about ±5 %. The main uncertainty is ±1 px in the edge position, partly from the segmentation edge.
