# q_2182 — basketball diameter (cm)

File fps = question_fps = 24, so no time-base conversion was needed.

Method (lab card): D = depth × pixel diameter / f, with f = 0.5959 × 1280 = 762.8 px.
Pixel diameter comes from a circle fitted to the convex-hull contour of the orange HSV mask (calc.py). The hull makes
the fit robust to the hand cut-out at t=0. Overlays are in frames/check_0.png and frames/check_46.png, and the circle
matches the outline in both.

| frame | depth (m) | record diam px | own diam px | D naive (cm) |
|---|---|---|---|---|
| 0 (t=0) | 1.3210 | 135.8 | 137.2 | 23.5 / 23.8 |
| 43 (t=1.8) | 1.5835 | 106.6 | 108.4 | 22.1 / 22.5 |
| 46 (t=1.92, apex) | 1.5795 | 109.5 | 111.0 | 22.7 / 23.0 |

Second route: an exact off-axis sphere projection (the ellipse stretches with off-axis angle, 12–17°) gives 21.2–21.9 cm.
That route is more self-consistent across frames, but it is not the annotation convention, and it falls below a
regulation ball (about 23–24 cm).

Answer: 23.3 cm. This is the naive card method, averaged over t=0 and the apex, the two frames with the cleanest depth
and fit. Confidence: about ±5%.
