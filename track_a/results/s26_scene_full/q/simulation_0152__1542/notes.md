# Q1542 – speed of the yellow car at t = 1 s (m/s)

Time base: question_fps = 24, which is the same as the file's fps. t = 1 s is frame 24, so speed = |x(24) - x(23)| (px) x 24 x metres-per-pixel.

## Pixel displacement (disp.py)
- I fitted a circle sub-pixel to the white rim's outer edge of the yellow car's near-side front wheel. This works even though the wheel rotates.
  The rim centre stays at y = 798.5 ± 0.2 and r = 63.5 ± 0.2 in every frame, so the car keeps a constant depth and moves parallel to the image plane.
- Rim dx per frame: 22→23 99.73, **23→24 101.18**, 24→25 102.42 (smooth acceleration). Value used: **101.15 px/frame**.
- Check: the scene record's ref_x gives 101.7 and the raw hubs give 101.0. A body-patch template match gives 99.0, but that patch is the cabin, which is inboard and farther away, so I didn't use it.

## Scale at the car's near-side wheel plane (m/px, s_c)
The yellow tyre's outline can't be read cleanly. Above it is a dark wheel-arch gap, and below it a dark contact-shadow band on the floor. Edges read off the image therefore gave 184–206 px. Instead, I tied the scale to the cart (the blue car):
- **Cart tyre** (cartrim.py, cartrad.py): I fitted circles to the rims, then took the radius on the near-sidewall side.
  - The rear tyre near the image centre is symmetric: r = 54.1–54.7. The near side of the front tyre gives r = 53.3; its far side reads ≈ 60 because the obliquely seen tread is included.
  - r = 53.8 → d = 107.6 px. (The earlier 112.5 px horizontal chord included the tread.)
  - s_k = 0.369 / 107.6 = 0.003429 m/px.
- **Route A (hub heights, level camera, horizon y = 539.1 from the corridor vanishing point):**
  - camera height H = s_k (893.4 − 539.1) + 0.1845 = 1.399 m
  - s_c = (H − 0.382) / (798.5 − 539.1) = 0.003922 m/px, which implies a yellow tyre of 194.8 px.
- **Route B (floor-shadow edge rows, same convention for both vehicles, 948.5 and 894.5):** s_c = s_k × 409.4 / 355.4 = 0.003950 m/px, which implies a 193.4 px tyre.
- **Direct check:** the yellow tyre radius from the rim centre down to the floor edge is 96–97 px (d ≈ 192–194), which implies s_c ≈ 0.00395.
- Value used: s_c = 0.00393 m/px (±1 %).
- depth_info check: with f ≈ 2670 px (HFOV ≈ 39°), the cart tyre at 9.31 m is consistent. The yellow car's near side is then ≈ 10.5 m away, and the camera is 1.40 m high, which is plausible.

## Answer
v = 101.15 × 24 × 0.00393 = **9.54 m/s**. The range across the scale routes is 9.52–9.59.
Confidence: about ±2 %. The main uncertainty is the cart tyre's pixel diameter (107–108.5 px).
