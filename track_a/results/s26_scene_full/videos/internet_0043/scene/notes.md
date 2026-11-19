# internet_0043 - measurement record

Video: 1920x1080, 30 fps, 61 frames (t = frame/30). Internet footage, 2D scene. All values are in pixels and frames.
No metric scale was guessed.

## Scene
A desk with a row of objects. From left to right: a white wavy bowl, an iced-tea bottle (yellow cap), a tall green
glass bottle, a white ridged cylinder cup, and a red Tefal kettle. Behind them are a black monitor, a black desk lamp
(right) and red roses (far right edge). A hand at the right edge flicks a **white egg**, which rolls right to left along
the desk top in front of the objects. It slows down, does not bounce or hit anything, and leaves the frame at the left
edge. The egg is the only object tracked. The hand is mostly outside the frame and is described only.

## Files
- `scene.json`: inventory (description, moving or not, visible frames, pixel sizes, bboxes), events, camera and
  perspective notes.
- `tracks/egg.csv`: one row per frame from 19 to 58. Columns:
  - `ref_x, ref_y`: **reference point** = midpoint of the egg's left/right and top/bottom edges (the visible centre),
    in raw image coordinates.
  - `ref_x_aligned, ref_y_aligned`: the same point corrected for camera drift (frame-0 alignment).
  - `core_cx, core_cy`: centroid of the bright "white core" mask. It is biased ~4-6 px right of ref_x because the
    egg's right side is shaded.
  - `bbox_*`: bbox of the core mask. `mask_len/mask_wid`: min-area rectangle of the core mask. `area`: core mask
    area in pixels.
  - `edge_x0/x1/y0/y1, edge_width, edge_height`: egg outline. Horizontal edges are half-max crossings of a
    whiteness (V−S) profile through the centre. Vertical edges are the gradient peaks within 25-60 px of the centre.
  - `cam_dx, cam_dy`: camera shift vs frame 0.
  - `occluded`: 1 = in contact with or overlapped by the hand (frame 19), or cut by the left image border (57, 58).
  - `ref_src`: `edges`, or `core+offset` where the edge leaked into a neighbouring object (only frame 33). In that
    case ref_x = core_cx + the neighbours' median offset.
- `camera_shift.json`: [frame, dx, dy] from phase correlation of the wall/monitor region against frame 0.
- `static_objects.json`: raw GrabCut extents at frame 0. `scene.json` holds the cleaned values; for the iced-tea
  bottle and the cup, use the row-width p90 instead of the bbox width, because a thin cable or label leaked into the
  bbox.
- `scripts/`:
  - `camera_bg.py`: camera shift.
  - `track_egg.py`: egg track.
  - `static_objects.py`: static extents.
  - `overlay.py, path_overlay.py, tile_crop.py`: visual checks (images go to ../frames/).

## Egg: key numbers
- Visible from frame 18 (a sliver in the hand) to frame 58 (partial at the left edge). Released at frame **19**
  (t = 0.633 s, ±1 frame): it still touches the fingers at 19 and is free at 20. Fully in frame and free: 20-56. It
  starts leaving at 57 and is gone at 59.
- Path: ref_x goes from 1786.7 (f20) to 77.6 (f56), and from 1850.6 at f19 (occluded). ref_y drifts slowly from 786
  to 792. The motion is almost purely horizontal (−x).
- Per-frame Δx (drift-corrected ref_x):
  - f20-21: 64-72 px. f20 is affected by the release.
  - f21-28: drops steadily from ~72 to ~46 px. This is a strong early deceleration, probably the skid-to-roll phase
    just after release.
  - f29-52: almost constant at 43-45 px/frame.
  - f53-56: ~41-42 px/frame.
  - Noise is ±1-2 px per frame; smooth before taking second differences.
- **Pixel size** (if a question gives the egg's real size, scale with this):
  - Height (top to bottom edge, vertical gradient peaks): median **79 px** (77 on the right side → 80-81 on the left
    side; it grows slightly as the egg drifts towards the camera).
  - Width:
    - Half-max of the white core: ~73-75 px. This misses the darker shaded right side.
    - Zoomed visual inspection (frames 26, 40): full outline ≈ **79-80 px**.
    - Frames 20-25: 85-101 px, inflated by motion blur.
  - The egg looks nearly circular here, so **~79 px** is the best length along the motion direction (bumper-to-bumper
    analogue).

## Camera
Static, with a slow smooth drift: dx goes 0 → −8.1 px over 60 frames and dy stays within 0 to +2.6 px. That is
≤0.3 px/frame, compared with the egg's 42-72 px/frame, so it hardly matters. If you want it, use the drift-corrected
columns. Phase correlation has about ±0.5 px uncertainty (frame 0 against itself returned dy 0.5). No zoom was
seen. Near-frontal view; the egg's track is close to parallel to the image x axis. The annotators' convention is a
single planar scale, so no perspective correction is needed.

## Static objects (frame 0, pixels: bbox [x0,y0,x1,y1], width × height)
| object | bbox | W × H |
|---|---|---|
| white bowl | [127,601,516,771] | 390 × 171 |
| iced-tea bottle | [582,378,702,770] | 118 × 393 |
| green glass bottle | [794,253,934,771] | 138 × 519 |
| white cylinder cup | [990,555,1112,753] | 122 × 199 |
| red kettle (incl. handle) | [1165,476,1519,767] | 355 × 292 |
| monitor (top cut off) | ≈[460,0,1347,445] | ≈887 wide |

Accuracy is about ±2-3 px. Bases sit at y 753-771; the egg rolls lower in the image (bottom at y 825-832), i.e. a
little in front of the objects.

## Reliability and ambiguities
- Egg centre: ±1-2 px in frames 24-56. Frames 20-23 are heavily motion blurred, but the edge midpoint is still
  centred (±3 px). Frame 19 is overlapped by the hand. In frame 57 the left edge is cut by the border, so ref_x
  (32.9) is approximate; edge_x1 − 37 gives ≈36. Frame 58 is only partial; do not use its centre.
- The egg has a faint reflection on the glossy desk and a soft shadow below it. Both are excluded from the mask
  (checked visually).
- No other moving objects. The bowl and cup are also white; do not confuse them with the egg.
- The hand's motion (frames 12-19) is not tracked: it is mostly off-screen and blurred.
