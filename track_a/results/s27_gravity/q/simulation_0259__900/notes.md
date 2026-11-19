# Q900: width (long side) of the table, in m. Answer: 1.36 m

The prior is that the red cup falls at 9.8 m/s² before 0.5 s. question_fps = file fps = 30.

## Scale at the cup's plane
- I fitted a quadratic to the scene track (`scene/tracks/cup.csv`, frames 0–14, free fall) in `measure.py`. The bbox centre and the mask centroid both give 6265 px/s². top_y gives 6324 and bottom_y 6200. Those differ because the rim ellipses change with viewing angle, and the centre point is almost unaffected.
- The scale is s = 9.8 / 6260 = 1.5655e-3 m/px at the cup's depth. The cup falls straight down (x is constant), so its depth stays the same, and it lands on the table near the back edge.

## Table pixel extents (`edges.py`, `edges2.py`, frame 0)
- The front of the tabletop and the front legs run from x = 517.5/518.5 to 1539, so the front edge is about 1020.5 px long.
- The back legs are clearly visible under the table. The back-left leg runs from x = 680.5 to 704.5, with a 24 px face against 29.5 px for the front legs. The back-right leg's left edge shows at x = 1499.5, just left of the front-right leg, so its outer edge is at about 1523.5. The back extent is therefore 843 px.
- So depth matters: Zf/Zb = 843/1020.5 = 0.826, and the leg face widths give 24/29.5 = 0.81. The vanishing point is at x ≈ 1450.
- Tabletop rows: back edge y = 865.5, front edge y = 895.5. The cup's base centre at rest is at y ≈ 870 (contact line 871).
  The row ratio gives the horizon: (865.5 − y_h) = 0.826 (895.5 − y_h), so y_h ≈ 723. The window sill line and the window frame line meet at about (1448, 717), which agrees. The cup's rim-ellipse sagitta (`sagitta.py`) is zero when the lid is near y ≈ 715, which also agrees.

## Result
- Back route: 843 px × Zb/Zc, where Zb/Zc = (870 − 720)/(865.5 − 720) = 1.031. That gives 869 px × s = **1.360 m**. Moving y_h anywhere from 700 to 740 gives 1.356–1.367.
- Front route: 1020.5 px × Zf/Zc, where Zf/Zc = (870 − 720)/(895.5 − 720) = 0.855. That gives 872 px × s = **1.365 m**. This route is more sensitive to y_h: 1.34–1.39.
- A plain single-scale 2D reading with no depth correction would give 1021 × s = 1.60 m. I rejected it because the back legs show a strong front-to-back perspective, and the table length must be converted at the cup's depth.
- Checks: the cup lid is 6.7 cm, the mug body 7 cm and the pen 10 cm. These are somewhat small but within about 25–30 % of real sizes. The table comes out at about 1.36 × 0.9 m.

Confidence: moderate-good, ±5 %. The main assumption is that the back legs are flush with the back corners of the tabletop, as the front legs are with the front corners.
