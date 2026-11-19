# Q254: length of the dark grey square tray (m)

Prior: chess piece speed = 0.04 m/s. The scene is a 2D top-down render with no perspective (the board pitch is 33.6 px everywhere).

## Scale
- Moving dark piece, `circ_cy` track from scene/tracks: a linear fit over frames 0–35 gives 1.3984 px/frame, and the net displacement 0→36 / 36 gives 1.3969 px/frame. The motion is uniform.
- The file fps is 24.012 and question_fps is 24.0. They differ by 0.05%, which is negligible; I used 24.012.
- Pixel speed = 33.58 px/s, so the scale is 0.04 / 33.58 = 1.1912e-3 m/px.
- Sanity check: one board square (33.6 px) comes out at 0.0400 m, so the piece moves about 1 square per second. That is plausible.

## Tray (measure.py, frame 46, sub-pixel threshold crossings halfway between the table and tray grey levels)
- x: 433.2 → 680.7 = 247.5 px, the same on 5 rows.
- y: 233.2 → 491.8 = 258.6 px, the same on several columns. On the left side, near the board/statuette, the lower edge reads ~497; I excluded that.
- Length = longer horizontal extent = 258.6 px → **0.308 m**. The width (shorter side) would be 247.5 px → 0.295 m.

## Check
- Scaling through the board instead (square = 0.04 m → 33.6 px) gives 258.6 × 0.04 / 33.6 = 0.308 m, which agrees.
- Confidence: good, about ±2%.
