# internet_0010_segmented — measurement record

Basketball jump shot, 97 frames at 30.0003 fps (t = frame/fps), 1280x720, 2D, segmentation version of
internet footage: everything except the player and the ball is replaced by white. All values in pixels/seconds;
no metric scale assumed.

## Files
- `scene.json` — inventory (ball, player, inferred floor and hoop), ball diameter and player height in px, events, camera.
- `tracks/ball.csv` — one row per frame 0-96: frame, t, mask centroid (cx, cy), bbox centre, bbox x0..y1,
  width_x, height_y, PCA main-axis length/width, area, equal-area diameter, flag.
  Flags: `free` (clean separate blob), `held_merged_with_player` (frames 12-44: no position),
  `in_hands_manual_estimate` (frame 45, read by eye from a 4x crop, ±3 px), `touching_hand_mask_includes_fingers` (frame 0),
  `artifact_elongated_mask` (80: height 30 px, cy biased ~+5 px), `small_partial_mask` (82), `clipped` (93-96, unreliable).
- `tracks/player.csv` — frames 0-96: mask centroid, bbox, width_x, height_y, feet_y (lowest pixel), PCA axis length/width,
  area, flag (`holding_ball_merged` 12-45 — bbox includes ball; `partial_mask` 85-96 — segmentation loses the body).
- `scripts/` — survey.py (connected components of non-white pixels, threshold 40), track.py (builds the CSVs and
  frames/overlay.png), crops.py (zoomed crops for checking), summary.py (stats quoted here).

## Method and reliability
Foreground = pixels with any channel < 215 (white background). Components were assigned to ball/player by size and
position; overlays (frames/overlay.png) were checked by eye: boxes sit on the ball and the full player.
- Ball diameter: 17 px (median bbox width over clean frames; height median 16, equal-area 16.6, PCA length 17.8).
  Edge anti-aliasing/compression makes single-frame sizes vary 15-20 px. Use ~17 px as "ball pixel size".
- Ball centre: ±1 px in clean frames. Flight 46-92 is clean except 80 and 82. Horizontal motion ~9-10 px/frame
  rightward during flight, near-parabolic vertical motion; apex frame ~66 (y ≈ 296).
- Player standing height: 112 px (frames 0-11, range 111-113, head top to soles). Standing width 34 px.
  Larger heights in 31-60 include raised arms/ball. Feet at y ≈ 586-590 = floor line (≈588).
- Player is nearly stationary: centroid x 387 → ~415 (frames 0-30, small steps/turn), then 414-430.
  Small jump: feet_y rises from ~586 to 581 (frames 46-52), lands ~55; only ~5-7 px, approximate.

## Events (see scene.json)
Dribble: ball leaves hand at frame 0, bounces on the floor at frame 9 (bottom y 586), caught at frame 12.
Gather 30-44, release at frame 46 (t 1.533 s; first separate frame), apex ~frame 66 (t 2.2 s), contact with the
(invisible) rim/backboard at frame 83 (t 2.767 s, centre (799, 384)) where horizontal motion reverses; then the ball
drops down-left (84-92). After 92 the ball mask is clipped (likely net/rim region), positions unreliable.

## Camera
Background removed, so camera motion cannot be measured. Player's feet stay at a constant y and nearly constant x
all clip, consistent with a static camera; treat as static (unverified for small pans).

## Ambiguities
- Hoop/backboard/court not visible; their positions only inferred from the ball path.
- Ball is held (merged with player) frames 12-44; release frame 45/46 boundary.
- For an internet-convention scale, the annotators would measure the prior object's pixel length (ball ≈17 px
  diameter, player ≈112 px standing height) and apply one scale to everything.
