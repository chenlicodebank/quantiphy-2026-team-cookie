# captured_0040 – measurement record (lab video, 3D, 24 fps, 49 frames, 1280x720)

All values are in pixels and seconds (t = frame/24). No metric scale was guessed.

## Scene
A person at the far left edge (only the right forearm/hand and a jeans strip visible) holds a small white
ball, swings and throws it to the right. The ball flies over a wooden table, **bounces on the table at frame 33**
(between the tape roll and the card tent), flies over/just in front of the white cup rim (frames 36-37),
**bounces a second time on the right part of the table at frame 41**, and is still airborne (descending,
x≈1182) when the video ends at frame 48. Static props on the table, left→right: glass jar, tape roll,
playing-card tent with flat cards in front, white cup; a dark navy flat object with a yellow note at the front.
Tripod (blue top light) behind the table, TV screen top-right. The ball is the only moving object besides the arm.

## Files
- `scene.json` – inventory (descriptions, visibility, static-object pixel boxes/extents at frame 48),
  events, camera info, ball apparent-size summary.
- `tracks/ball.csv` – ball every frame 0-48: `cx,cy` (mask centroid = visible centre), bbox, `mask_len_main_axis`
  (PCA length, stretched by motion blur), `mask_width_across` (≈ diameter + blur halo), `mask_height_vertical`,
  `main_axis_deg`, `area_px`, `equiv_diam`, `occlusion` flag.
- `camera_shift.json` – per-frame phase-correlation shift of 3 background patches vs frame 0.
- `bg_median.jpg` – median background.
- `scripts/` – `track_ball.py` (tracker), `blobs.py` (candidate listing), `camera.py`, `draw_track.py`
  (overlay check), `strip.py`/`zoom.py` (viewing helpers).

## Methods
- Ball: median background of all frames; ball pixels = |gray−bg|>25, bright (V>140; V>150 in-hand frames) and
  unsaturated (S<80; S<70 in-hand) → morphology → connected component (nearest to predicted position in frames
  0-25, the single large white blob afterwards). Masks drawn on crops for every frame and checked by eye
  (all 49 hit the ball; in-hand frames exclude the covering fingers).
- Camera: phase correlation of wall/tripod, right-wall and floor patches: max shift 0.07 px → **static camera**.
- Static objects: read off zoomed, gridded crops of frame 48 (±2-3 px; table corners ±10 px).
- Benchmark lab convention: focal ≈ 0.5959×1280 = 762.8 px, principal point ≈ (640,360). Use given depth_info
  to back-project centres.

## Key numbers
- Ball centre: start (168,474); back-swing low (127,528) f20; release ~f24 (192,452); apex1 cy 327.3 f28-29
  (x 373-421); bounce1 f33 (628,484); apex2 cy ~355 f36-37 (x 753-785); bounce2 f41 (927,493); apex3 f45
  (1068,379); last f48 (1182,478). Horizontal image motion ≈ 35-50 px/frame to the right after release.
- Ball apparent diameter (cross-motion width / vertical extent in low-blur frames): ~34-36 px near x≈400
  (f28-29, also in hand), ~38-39 px at f36, ~44-46 px at f44-45, ~50+ at f48 (blurred). The ball therefore moves
  **toward the camera** as it goes right (depth decreasing) – image-plane distances alone underestimate 3D motion;
  combine with depth_info / size ratio (depth ∝ 1/apparent diameter).
- Static extents: cup 73 (rim) × 128 px tall; jar 60 × 82; tape roll 78 × 47; card tent front card ~85 long ×
  22 wide; flat cards 102 long; dark object 107 long; table front edge ≈ 928 px (corners (211,540)→(1138,588)).

## Reliability / ambiguities
- Centroids in flight: ±1-2 px; mask length is inflated by motion blur (up to ~85 px vs ~35-45 true diameter),
  use `mask_width_across` or `mask_height_vertical` at near-horizontal motion frames for size.
- Frames 0-22: fingers cover part of the ball → centroid shifted a few px toward the visible part, width ~34.
- Release frame is uncertain (23-26); 24 is the best estimate.
- Frame 33 (bounce1): mask partly mixes with the tape roll/table glare (centroid ±3 px). Frame 34: ball overlaps
  the card tent top (passes in front). Frames 36-37: ball overlaps the white cup rim (white on white; mask
  bottom clipped slightly, centroid may be ~2 px high).
- Bounce frames are the frames with the lowest image y; the true contact may lie between frames (±0.5 frame).
- "Modified with Segment Anything 2 Demo" watermark bottom-right and background slightly blurred – ignore.
- Hand/arm not tracked separately; its position ≈ ball track in frames 0-22.
