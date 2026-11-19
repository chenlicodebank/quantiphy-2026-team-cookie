# Q2705: height of the pink bottle (cm)

The file and the question are both 24 fps. The bottle is static. I measured it on the median of frames 30–38 (around t = 1.4 s) with `measure2.py`, and checked it on single frames 10, 20, 34 and 45 with `measure.py`. All gave the same edges.

## Pixel measurements
- Top edge (half-level crossing, sub-pixel): 328.0 at the lid centre (x 666–675), and 329–330 near the rounded corners.
- Bottom edge (where bright pink turns into the dark base line). It can only be seen left of the card stand, x 643–658. It slopes from 475.6 at x = 643 to 477.3 at x = 655, so it is the front arc of the base ellipse. Fitting that arc (centre x 664, radius 24 px) gives b ≈ 3.8 px and a lowest point of ≈ 477.6.
- Side edges: x 640 to 688, so the width is 48 px.
- The camera is close to level (cy ≈ 360). Evidence: if the camera were level, the base ellipse would have b = r·(477−360)/763 ≈ 3.6 px, and the measured value is 3.8 px.

## Height
- Axis length: the top centre is ≈ 329.0 (the silhouette top is the near rim, seen from about 1 px below), and the base centre is 477.6 − 3.6 ≈ 474.0. That gives **145 px**.
- z of the centre = 0.9998 m × cos(ray angle) = 0.998 m. With f = 0.5959 × 1280 = 762.8 px, H = 145 × 0.998 / 762.8 = **0.190 m**.
- A plain silhouette extent with no ellipse correction (328.0 → 477.6 = 149.6 px) would give 19.6 cm. This is an upper bound, because it includes the base-ellipse bulge.

## Check
- Credit card: at 0.6867 m, 85.6 mm should span about 95 px. The dark card's long edge measures about 88–98 px; the card is rotated and lying at a grazing angle. So the scale is roughly consistent.
- The answer, 19.0 cm, is a plausible height for a small insulated bottle.

Answer: 19.0 cm. Confidence: about ±3 %.
