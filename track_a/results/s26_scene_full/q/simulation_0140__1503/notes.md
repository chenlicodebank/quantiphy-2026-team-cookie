# q_1503 – width of the "BE DIFFERENT" neon sign

The prior is "window frame width = 1.48 m". The sign and the windows are both features of the same flat, static
backdrop facade, and the sign hangs directly above the second row of windows. So one metres-per-pixel scale taken from
the window width converts the sign width. The depth_info (bird distances, sign distance 34.5 m) does not give a size
scale here, because no object with a known size has a given depth.

The file runs at 24 fps and question_fps is 24. The camera is static, so I used frame 96.

## Measurements (scripts: measure.py, windows.py, extent.py, crop.py)
- **Sign letters:** I thresholded the white letter cores (min RGB > 150/180/220) to get x 641–1335, so the width is
  **695 px**. This matches scene.json (695×81). The red glow reaches x 628–1341 (714 px), but that is glow, not the sign.
- **Window frame width:** I measured the outer extent of the window opening/frame in the row just below the sign. I
  read the dark bands under the lintel and under the sill at two thresholds, and checked them on 4–5x enhanced crops:
  - Window 847–968: 119–127 px (about 125 px on the crop).
  - Window 1029–1146: 117–128 px.
  - Window 1209–1325: 116–121 px.
  - Window 668–784: 115–124 px.
  - The top row gives the same: one window spans 840–964, about 124 px.
  - Adopted width: **122 px ± 3**.
- **Scale:** 1.48 / 122 = 0.01213 m/px.

## Answer
695 × 0.01213 = **8.43 m**.

## Checks
- The bounds of the window reading give 1.48 × 695/118 = 8.72 m and 1.48 × 695/127 = 8.10 m.
- The sign covers 3.8 window pitches (pitch about 181 px). That is consistent with a sign of about 8.4 m and a window
  pitch of about 2.2 m.
- The photo looks slightly upward, but horizontal scale changes little between the sign row and the window row just
  below it.

Confidence: moderate. The main uncertainty is where the "window frame" edge is taken (about ±4%).
