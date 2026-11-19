# simulation_0223 – measurement record (pixels, seconds)

Video: 1920x1080, 24 fps, 45 frames (t = frame/24). Source: simulation (Blender), **2D** scene.
Content: a xiangqi (Chinese chess) board seen from almost straight above, on tatami mats. The camera is static.
**Only one object moves:** the red general (帥, the middle piece of the red back row at the top). It starts at
rest at (959, 156) px, then slides straight down the board's empty centre file (x ≈ 959.2 px throughout), speeding up
steadily. It crosses the bottom rim of the board at about frames 40–41 and leaves the image by frame 43.
The black side has no general: the gap in the bottom row at x ≈ 959 is part of the setup.

## Files
- `scene.json`: inventory (moving and static objects), camera, events, static piece positions, board and bowls.
- `tracks/red_general.csv`: one row per frame (0–44).
  - `cx, cy`: reference point = centre of the piece's silhouette bounding box. This is the best proxy for the object
    origin (the disc centre).
  - `x0..y1`: bounding box. `bbox_w`/`mask_width_px` are across the motion; `bbox_h`/`mask_length_px` are along the
    motion (image +y).
  - `mask_centroid_y`: sub-pixel centroid of the mask; it agrees with `cy` to within about 0.4 px.
  - `glyph_centre_y`: centre from template matching of the frame-0 piece. This follows the top face.
  - `occluded`, `clipped`: flags.
  - `duplicate_frame` and `cy_dup_interp`: see below.
  - `method`: how the row was measured.
- `scripts/`:
  - `track.py`: mask from the difference to a per-pixel median background (column x 820–1100) → `raw.json`.
  - `track_tm.py`: template matching.
  - `static.py`: Hough and disc masks for the static pieces.
  - `build.py`: writes the CSV, the board edges and `static_final.json`.
  - `write_scene.py`: writes `scene.json`.
  - `view_*.py`: check images.

## Moving object: red_general
- Size: the disc diameter is 86–87 px (mask bbox, frames 0–39), with no change in apparent size while it is on the
  board. Static pieces of the same type measure 83–85 px (their masks are a little tighter). Pieces are cylinders
  seen from above, so the height is not measurable.
- Reliability:
  - Frames 0–39: ±0.5 px (clean dark background, sharp edges, no visible motion blur).
  - Frames 40–41: ±2 px. The piece is over the orange rim and the tatami, whose colour is close to the piece, so the
    mask is unreliable. The centre there is the template (glyph) centre minus the fitted glyph-vs-silhouette offset
    (0.0038·y − 0.65 px; residual 0.33 px).
  - Frame 42: only the top 14 px are visible. The centre (1108.5) is top edge + 42.5 px radius, roughly ±3 px.
  - Frames 43–44: not visible.
- Perspective: the glyph (top face) centre drifts relative to the silhouette centre from −0.6 px (top) to +2.8 px
  (y ≈ 970). This is slight perspective from the camera above the board centre. I used the silhouette centre because
  it lies midway between the top and bottom faces, i.e. close to the origin. The difference is too small to matter
  except at the 1 % level.
- **Duplicated video frames (important for one-frame speeds):** the pairs (9,10), (11,12), (18,19), (20,21), (28,29)
  and (34,35) are identical images. The frame increments show that the first frame of each pair already shows the
  next frame's position, i.e. that frame's own position is missing. Examples:
  - 8→9 is +18.8 px, about two normal steps; 9→10 is 0.
  - 17→18 is +38.5 px; 18→19 is 0.
  - Normal increments grow smoothly: 0.8, 2.1, 3.4, 4.4, 5.6, 6.7, 7.9, …, 13.5, 14.6, 15.8, 16.6, 17.9, …, 23–29, …,
    32–35, …, 38, 39, 40, 40.4 px/frame.

  `cy_dup_interp` is a local quadratic estimate of the true position at the first frame of each pair (from the clean
  neighbours ±3 frames). Use it, or difference over clean frames, for speeds at those times. Raw one-frame
  differences there would give 0 or about double values.
- Positions are only along y. x is constant to ±0.1 px (mask centroid 959.1–959.3), so path length ≈ |Δy|.

## Events (frame / time)
- At rest: frames 0–1 (t 0–0.042 s).
- Motion starts between frames 1 and 2 (about frame 1.3, t ≈ 0.055 s). The first displacement is 1→2 (+0.76 px).
- Speed-up: steady over the whole clip, with no bounces or direction changes.
- Leaves the board onto the tatami: about frame 40–41 (t ≈ 1.67–1.71 s). The board's inner edge is at y ≈ 1008 and
  the outer rim at y ≈ 1017. Over the tatami the piece's apparent width stays about 86 px; there is no clear drop or
  size change, but measurements there are poor.
- Leaves the image: frame 42 is the last frame with anything visible; frame 43 (t = 1.792 s) has none.

## Static objects (pixel positions at frame 44; full list in scene.json)
- Board: inner edges (gradient) at x 449–1479, y 80–1008. The outer orange rim (visual) is at x 448–1490, y 73–1017,
  about 1042 x 944 px.
- Pieces:
  - 31 static pieces: 15 red-glyph (top half) and 16 black-glyph (bottom half), each about 84 px in diameter.
  - Files are spaced about 89.8 px apart: x ≈ 600, 690, 778, 869, (959), 1049, 1138, 1228, 1319.
  - Rows are at y ≈ 156 (red back row), 322 (red cannons), 412 (red soldiers), 664 (black soldiers), 753.5 (black
    cannons) and 917.5 (black back row).
  - Pieces in the back rows touch each other; their centres come from Hough circles (±1–2 px).
- Other objects:
  - White go-stone bowl: left of the board, centre about (392, 467), diameter about 175 px, partly hidden by the board.
  - Black go-stone bowl: lower right, centre about (1553, 915), diameter about 195 px.
  - Tatami border strips: a horizontal dark band at y ≈ 655–700 and a near-vertical strip at x ≈ 1780–1900.
  - Engraved river characters on the centre column (y ≈ 290–420 and 670–800).
  - The bowl and tatami figures are approximate (±10 px).

## Scale guidance for answering sessions
This is a 2D scene, so use one metres-per-pixel scale from the given prior. For example, if a piece's diameter is
given, use 86–87 px for the moving general, or about 84 px for a static piece. The 3 % difference comes from how
tightly each mask was cut; prefer the general's own 86.5 px for questions about it. Then convert the y track.
