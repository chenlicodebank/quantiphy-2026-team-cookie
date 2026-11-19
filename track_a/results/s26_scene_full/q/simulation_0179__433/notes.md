# Q433 — side length of the orange floor tiles (m)

Prior: trolley (shopping cart) acceleration = 1.507 m/s². fps 24 = question_fps (no re-timing).

## Scale (fit.py)
Quadratic fit of the cart's x position vs t (scene/tracks/shopping_cart.csv; I checked the track: the cart
moves horizontally at a constant image row, residuals about 0.5 px):
- bbox_cx: a = 295.6–296.1 px/s²; wheels_cx: 294.6–295.0; bbox_x0 289, bbox_x1 302 (the apparent length grows
  off-axis, so the centre value is the one to use).
- I used a = 295.3 px/s², giving 1.507 / 295.3 = 0.005103 m/px at the cart's depth.

## Tile pitch (tiles.py, orange mask on frame 0)
- The orange row at y 852–873 lies right at the cart's depth. Wheel contacts: far wheels at y≈868, near wheels at
  y≈884, so the cart centre is over the floor at y≈876. Tile starts along y≈860–864: 1100, 1198, 1296, 1394, 1492, ~1590,
  1687, 1784, so the pitch is 97.7 px (orange part ≈88 px plus ≈10 px grout).
- Near row (y≈975): starts 670, 784, 900, 1015, 1130, so the pitch is 114.3 px.
- The pitch is linear in y on a ground plane: 97.7 + 0.147·(876−862) = 99.8 px at the cart's depth.

## Result
- Pitch at the cart's depth: 99.8 px × 0.005103 = 0.509 m.
- At the orange band centre (97.7 px): 0.499 m. The answer is very probably 0.5 m tiles; I answer **0.505 m**.
- Second route: the cart length is 223 px × 0.005103 = 1.14 m and its height 248 px gives 1.27 m. Both are large for a
  real cart, but they are consistent with the scene's own scale. The two pitch readings (band centre and
  wheel-centre depth) agree within 2%.
- Another reading: the orange area alone, without grout (≈88 px), gives ≈0.45 m. I used the pitch (tile module).
Confidence: moderate-high (±3%) for the tile pitch reading.
