# q_2429 — height of the book (cm)

File fps = question_fps = 24, so frame = round(t × 24). Lab camera: f = 0.5959 × 1280 = 762.8 px, principal point (640, 360).

## What is measured
Height = the book's vertical extent (its thickness) while it lies flat on the table (frames 37–48, t ≥ 1.54 s; depth given at t = 1.6 s, frame 38: 0.851 m).
The front face of the book (cover edge + cream page block + bottom cover) is a vertical strip below the top face.

## Pixel measurement (edges.py)
Columns x = 495–645, frames 37–48, grey-level gradients:
- end of the top face (front-top edge): v = 495.5 (sharp drop; a 2 px dark line follows, the cover edge and the shadow under it)
- bottom of the book: the strongest drop after the cream face is at v = 508.5–509.5, and the darkest contact row is at 510.0
- front-face height: 13.0–14.5 px, best value ≈ 14.2 px. The values are identical in every frame from 37 to 48.
- back edge of the top face (against the white board): v ≈ 482

## Geometry (geom.py)
- Back-projecting the board bottom (0.9555 m) and the book centre (0.851 m) puts both points at the same camera Y (0.149 m), so the camera's optical axis is
  about horizontal (pitch ≈ 0°). The pixel height of a vertical segment is then f·H / Z_c, where Z_c is the camera-axis depth of the front face.
- Book centre: Z_c = 0.851 × 763 / |ray(566, 497)| = 0.834 m.
- The front face is nearer than the centre. The top face spans v 482–495.5, so Z_back / Z_front = 135.5 / 122. That gives Z_centre = 1.055 Z_front,
  so Z_front = 0.790 m (top-face depth, i.e. book width, ≈ 9.6 cm).
- H = 14.2 px × 0.790 / 762.8 = 1.47 cm (1.35–1.50 cm over the 13–14.5 px edge range).

## Check (second route)
The ratio of the front-face edge rows (v_top − cy) / (v_bottom − cy) = 135.5 / 150, with the table height Y = 0.155 m from the same geometry, gives
H = 1.50 cm. This agrees.
If the plain method card is used instead (centre depth 0.851 × 14.2 / 762.8), the answer would be 1.58 cm. It overestimates because the front face is about 6 cm nearer than the centre.

Answer: 1.47 cm. Confidence: moderate (±1 px on a 14 px edge is ±7 %).
