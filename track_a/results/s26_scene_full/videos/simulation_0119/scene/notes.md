# simulation_0119 — measurement notes

2D simulation (Blender), 1080x1080, 48 frames, fps 24.012007 (t = frame/fps). Static top-down camera looks at a
coffee table with a 10x10 glass chess set on a shaggy rug. **Only one object moves**: a dark smoky-glass chess
piece (`dark_piece`). At frame 0 it is in the board's top row, 9th column (centre x≈533.7, y≈521.3). It slides
straight down the image (+y, toward the bottom of the board) at a near-constant ≈1.40 px/frame and stops at frame 36 at
(533.8, 571.6). That is a net 50.3 px, about 1.5 squares. The piece is already moving at frame 0, so motion began before the clip. Frame
36 is the first rest frame and frames 36–47 are identical. The steps show no visible slowing before the stop.

## Files
- `scene.json`: inventory, camera, events, static object extents, summary of the mover.
- `tracks/dark_piece.csv`: one row per frame (0–47).
  - `circ_cx, circ_cy` = **reference point**, the centre of a circle of fixed radius 17.15 px fitted to the
    piece outline. Seen from directly above, this is the projection of the piece's vertical axis, which is the best proxy for the object origin.
  - `cx, cy` = mask centroid. `bbox_*`, `width_px`, `height_px`, `area_px` = background-subtraction mask.
  - `circ_free_diam_px` = free-radius circle diameter, `circ_inlier_frac` = fit quality, `occluded` = always 0.
- `scripts/`: `diff.py` (motion detection), `diff18.py` (noise check), `track_piece.py` (mask track),
  `circle_fit.py` (reference centre), `template_check.py` (failed cross-check, see below), `static_measure.py`
  (board, table, tray, step stats), `overlay.py`, `overlay_circle.py`, `rawzoom.py` (visual checks → frames/).

## Method and reliability
- Background = last frame above y=547 and first frame below it. The piece's start and end footprints don't overlap, so this
  background is clean. Mask = per-channel |frame − bg| > 30.
- **Mask bbox and width are unreliable in frames 0–~16.** The glass piece sits on a dark square there, so the rim
  merges with the background: mask width 30–33 px instead of ~35, centroid biased about 1.5 px up. Use `circ_cx/circ_cy`
  instead. The fit is checked visually on frames 0, 2, 9, 18, 27 and 36, and the circle matches the outline. Centre error is
  about ±0.3 px (±0.5 px in frames 0–3, where the inlier fraction is 0.66).
- Per-frame steps scatter between 0.9 and 2.2 px (frame-to-frame jitter of the fit). Means: 1.408 / 1.404 / 1.384 px per frame over
  frames 1–12 / 13–24 / 25–36. That is consistent with uniform motion; any acceleration is below the noise. Net displacement 0→36 = 50.29 px,
  sum of fitted steps = 50.35 px. For speed, use a fit over many frames rather than single differences.
- Apparent piece diameter: 34.3 px (median of rest frames). The free fit gives 33.6–35.4 px, with no systematic trend,
  so the depth is constant and this is truly 2D. The x position is constant at 533.5–533.8: purely vertical motion in the image.
- Board: x 248–584, y 504–841 (336 × 337 px), square pitch 33.6 px (±0.2) everywhere, so there is no perspective.
  The table top is 665 × 665 px (bbox 112–777, 212–877). The tray is about 247 × 259 px. Other static items are visual estimates
  (±4–5 px), listed in scene.json.
- Camera static: no differences outside the piece, apart from isolated single-pixel compression noise (e.g. frame 18).

## Ambiguities
- The pieces are transparent glass, so their appearance changes with the squares behind them. Template matching failed for that reason.
- Several other dark glass pieces stand on the board; only the one in column 9 (x≈533) that starts in the top row
  moves. The dark piece lower in the same column (533, 760) stays still.
- The piece's "length/width/height": top-down, only the circular footprint (≈34.3 px diameter) is visible. Its
  height is not observable.
- No shadows or motion blur are visible.
