# q1289 – height of the streetlight (double-lantern lamp post, near-left corner)

File fps 24 = question_fps 24. 3D Blender scene, static level camera, horizon / principal point y ≈ 538–540
(road-edge vanishing point measured at y 537, record says 539; cy = 540 used, the main route is nearly cy-independent).

## Lamp pixels (final.py, frames 0 and 70 identical – static)
- Top (finial / lantern tops, sub-pixel half-level edge): y = 183.8
- Bottom of the base foot on the sidewalk: y = 685.1 → AABB pixel height 501.3.
- The foot is ~40 px wide (~0.28 m), so its front edge is ~0.14 m nearer than the pole axis; base at axis depth ≈ 683.8
  (−1.3 px). Used: 500 px tall, base 143.8 px below the horizon.
- H = 500 / 143.8 × h_sw = 3.477 × h_sw, where h_sw = camera height above the sidewalk the lamp stands on.

## Scale
- Van (white car, prior a = 4 m/s²): it moves parallel to the image plane at constant image scale. A quadratic fit of
  ref_x gives 307 px/s² (stable 306.8–308.9 over different windows), so Z/f at the van = 0.01303 m/px.
- Van depth pair (30.065 m at f14, 29.307 m at f38) solved independently gives Z/f = 0.01292 (0.8 % agreement) and
  the van origin Z = 29.17 m. The tracked side face is about half the van's width (~1 m) nearer than the origin →
  f ≈ (29.17 − ~0.9)/0.01303 ≈ 2170–2200 px (upper bound is 2258 if the half-width were 0).
- Sanity checks at f = 2185: taxi length 475 px → 5.3 m, bike 1.66 m, van 5.9 × 2.1 m, pedestrian 1.87 m.

## Route 1 (main): pedestrian on the same sidewalk
- Pedestrian pelvis depths 17.28 / 16.156 m at f14 / f38. Z = d / sqrt(1 + r²/f²) → 16.20 / 15.00 m (f = 2185).
- h_sw = (feet_y − 540) × Z / f = 1.023 at both times. Over frames 8–50 (Z interpolated) the median is 1.022 and
  the minimum is 1.009. The front foot is nearer than the pelvis, so the true value is ≈ 1.01.
- f = 2172 → 1.03; 2210 → 1.01; 2258 → 0.99.
- H = 3.477 × (0.99 … 1.03) = 3.43 … 3.57; central value (f ≈ 2200, h_sw ≈ 1.01) **≈ 3.5 m**.
- Equivalent check: pedestrian scaled to the lamp's ground row = 260 px tall → lamp/pedestrian = 1.92 →
  1.87 m pedestrian × 1.92 ≈ 3.6 m (walking height, lowest foot to head).

## Route 2: road-level camera height from the van and cyclist tyres
- Van tyre bottom at y 615.5 → h_road = 75.5 × 0.01303 × (1 + 0.15/28) = 0.984 m (f-independent).
- Cyclist tyre bottom at y 620, Z 27.03 → 0.99 m at f = 2185.
- If the sidewalk is at road level: H = 3.477 × 0.984 = 3.42 m. The near-left sidewalk shows a ~11–14 px olive band
  at its edge. Read as a raised curb (~0.09 m), it would give 3.1 m, but that contradicts the pedestrian (whose feet
  would then sit 0.1 m below where a raised sidewalk puts them, about 10 %). The pedestrian, van and cyclist are
  consistent within about 2 % only if any curb is small. So route 1, which needs no curb assumption, is preferred.

## Answer
3.5 m (routes 1 and 2 with no curb give 3.42–3.57). Confidence: moderate, about ±5 %. The main uncertainty is the focal
length (the van's origin offset) and the unexplained curb band.
