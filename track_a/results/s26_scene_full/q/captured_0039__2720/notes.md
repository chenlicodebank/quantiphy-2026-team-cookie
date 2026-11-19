# Q2720: height of the poker tower (cm)

The poker tower is the two-card tent standing on the table between the pink bottle and the white cup
(x ~655-712, y ~416-500 at f48). The camera does not move, so I used frame 48 (t = 2.0 s, ball gone).
The file and the question are both 24 fps.

## Measurements (crop.py, edges.py, frames/tower_48.png, frames/card_48.png)
- Apex (top edge of the tent): y = 415.5-416 px (strongest gradient in columns x = 688-692).
- Front card foot: y ~ 500 px. Back card foot: y ~ 492-494 px. The table point directly below the apex lies
  between the feet, at y ~ 496-497 px.
- Pixel extent: top to front foot = 84.5 px; apex to the table point below it = 80.5 px. The front foot is
  ~2-3 cm nearer the camera, so it sits ~4 px lower in the image.
- f = 0.5959 x 1280 = 762.8 px. Depth to the tower = 0.9035 m. The ray is ~8 deg off axis (cos 0.99), so Z = 0.8945 m.

## Values
- Method card, as written (d x 84.5 / f): 10.0 cm. With the off-axis cos correction: 9.9 cm.
- Using the apex-to-table extent (80.5 px), Z = 0.8945: 9.44 cm.
- Prior check: the credit card (dark blue with a yellow sticker, near the front edge) is ~100 px long at
  0.6867 m. That gives 9.0 cm without the cos correction and 8.72 cm with it, against the exact 8.56 cm.
  So the depth-based scale reads 2-5% high. Applying that factor gives 9.0-9.5 cm.

## Answer
9.5 cm. This sits between the purely geometric estimate of the physical height (9.4) and the value from the
method card's pixel extent (9.9-10.0). Confidence: moderate, about +/-6%.
