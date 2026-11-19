# q_2258 – length of the pen (cm)

Lab video, 24 fps (file and question fps agree), 1280x720, f = 0.5959*1280 = 762.8 px, c = (640,360).
Pen depth (depth_info, t=0): 1.6725 m. The pen is static (frames 0-48); the ball prior is not needed for a size.

## Measurement (pen.py, pen2.py)
- Median of 7 frames (ball-free at the pen). Pen axis fitted to dark pixels: y = -0.080 x + 475.7 (almost horizontal).
- Profiles of grey level / saturation along the axis (offsets -2..+2 px):
  - right end (silver cap end) ends at x ≈ 502.5 (grey jumps to wood 165);
  - black body starts at x ≈ 441; a thin grey tapering tip extends left to x ≈ 434 (just at the table's
    left edge; checked on an 8x crop, frames/penmark.png).
- Pixel length ≈ 68.5-69 px along the axis → 69.2 px incl. slope. (scene/ record said 60 px: it missed the tip and cap end.)

## Scale
- Method card: L = d * px / f = 1.6725 * 69.2 / 762.8 = 0.152 m.
- Treating the depth as the ray distance (Z = d / 1.030 at u≈468, v≈437): 0.147 m.
- Answer taken between the two: 15.0 cm (both within ~2 %). Sanity: a typical ballpoint pen is ~14-15 cm.

Confidence: moderate; main error is the left tip end (±1-2 px ≈ ±2-3 %).
