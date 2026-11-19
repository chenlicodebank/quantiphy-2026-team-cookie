# q906 — long side of the bag (m)

2D scene, 30 fps (file and question rates are the same). Prior: the cup (red/pink-banded paper cup) falls at 9.8 m/s^2 before 0.5 s (frames 0–14).

## Scale (fit.py)
Quadratic fits of the cup's vertical position over the free-fall frames (0–14, 3–14, 5–14):
- top_y (lid edge, least affected by the underside-ellipse perspective): 6300–6325 px/s^2 -> 1.550–1.556 mm/px
- bbox centre / centroid: 6218–6266 px/s^2 -> 1.564–1.576 mm/px (pulled slightly by the shrinking underside ellipse)
- Used scale: 1.555 mm/px (from top_y).

## Bag
Camera bag on the right end of the table, frame 0. A zoomed grid crop (frames/bag.png) gives a horizontal extent of x ≈ 1309 to 1534,
so ≈ 225 px wide, including the side pockets. This agrees with the scene record's bbox [1308, 1533]. The height is 134 px.
A colour-mask attempt failed: the wall's hue range was too tight, so it was discarded.
Long side = 225 px × 1.555 mm/px = 0.350 m. Using the centroid-based scale instead would give 0.353 m.

## Checks
- A camera bag about 0.35 m wide and 0.21 m tall is realistic.
- Cup: 42.5 px rim -> 6.6 cm and 65 px tall -> 10 cm, a small coffee cup, which is plausible.
- The bag sits on the same table at about the same depth as the cup's landing spot, so the same scale applies.

Confidence: good (±4%).
