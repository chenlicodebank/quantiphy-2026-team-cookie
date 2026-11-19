# captured_0024 – measurement record

Lab video, 3D, 24 fps, 49 frames (t = frame/24, 0–2.0 s), 1280×720. Static camera. By the benchmark convention,
fx = fy ≈ 762.8 px and the principal point is ≈ (640, 360). The background around the table is blurred or replaced
(SAM2 watermark), and the person behind the table is blurred.

## Scene
A light-blue notebook (cyan cover, white page edges) starts lying on the upper end of a white board. The board leans
from the table top (lower-left) up onto a stack of books (a dark green hardcover with a thinner light book on top,
right side). The notebook sits still for frames 0–18. It slides down the board in frames 19–30, lands on the wooden
table around frame 30, slides left for a short way and stops at frame 36. It stays still until frame 48. It is the
**only moving object**. A blurred seated person is behind and to the right of the table, with an arm raised near the
top of the ramp. No hand contact with the notebook is visible, so what caused the release is unclear.

## Files
- `scene.json`: inventory (notebook, ramp board, book stack, table, person, tripod/lights), static pixel extents,
  events, camera and perspective notes.
- `tracks/blue_notebook.csv`: **main track**, one row per frame (0–48). Columns:
  - `cx, cy`: centroid of the full-object mask (cover + page edges). This is the visible centre and the reference
    point.
  - `bbox_*`: bounding box of that mask.
  - `len_main, width_across, main_axis_deg`: min-area-rectangle extents and angle (image coordinates, y down).
  - `area_px`: mask area.
  - `cover_cx, cover_cy, cover_len_main, cover_width`: the same quantities from the colour-only (cyan cover) mask.
  - `frame_diff_mean`: mean absolute grey-level change from the previous frame, as a motion indicator. No duplicated
    frames were found.
  - `occluded`: set to 1 for frames 29–31, the ramp→table transition, where the mask is incomplete.
  - `note`.
- `tracks/blue_block_raw.csv`: the colour-only track (cyan cover), kept as a cross-check.
- `track_overlay.jpg`: trajectory overlay. Red = full-mask centroid, blue = cover centroid.
- `scripts/`:
  - `track_block.py`: colour mask.
  - `track_block_diff.py`: full mask by background differencing.
  - `ramp_check.py`: checks that the ramp is static and measures camera shift.
  - `finalize.py`: merges the tracks and draws the overlay.
  - `tile_crops.py`, `probe.py`: viewing helpers.

## Method
- **Full mask:** for frames 0–30 the background is frame 48 (notebook on the table), with the final-rest region
  excluded. For frames 31–48 the background is frame 0 (notebook on the ramp), with the start region excluded. Pixels
  that differ by more than 28 grey levels are kept, then warm (skin/wood) and dark pixels are dropped. Then a
  morphological clean-up is applied and the largest component is kept and filled. I drew the overlays on frames 0,
  18–36, 40 and 48 and checked them. They hit the notebook and cover its visible extent.
- **Camera:** phase correlation on the left wall region gives a shift of 0.1 px or less over the whole clip, so the
  camera is static.
- **Ramp board:** checked for motion through its bright-region extreme points. It does not move. Its top-right corner
  only appears to move at frame 19 because the notebook uncovers it.

## Key numbers (pixels)
- **Start rest, frames 0–18:** centre (787.8, 369.4), bbox x 718–852, y 330–396. The long side is about 135 px,
  seen obliquely on the ramp.
- **End rest, frames 36–48:** centre (572.7, 476.7). Mask bbox is x 502–648, y 461–493. By eye, the true extent is
  x 496–647, y 462–499: the mask misses about 6 px of the lower white page edge and about 5 px at the left end.
  Visible length about 151 px, apparent vertical extent about 37 px.
- **Net image displacement:** 240.6 px, mostly along the ramp direction (about 33° below horizontal, toward the
  image left).
- **Ramp board corners, frame 48:**
  - Upper-right (858, 361), upper-left (~757, 360), lower-left (611, 468), lower-front-right (700, 490).
  - Slope edges are about 182 px (left) and 204 px (right).
  - In the image the edges slope at about 36–39°. This is a projection, not the true incline angle.
- **Book stack, frame 48:**
  - Dark book: x 747–853, y 451–487 (left part hidden behind the ramp).
  - Light top book: x ~785–834, y 436–451.
- **Table:**
  - Corners: left (413, 467), front (640, 610), right (~1140, 505); back edge at y ≈ 450.
  - Top is about 20 px thick.
  - Pedestal: x 745–800, y 600–720.

## Events
| event | frame | t (s) |
|---|---|---|
| at rest on ramp top | 0–18 | 0–0.75 |
| motion start / release (first ~1 px move at 19, clear by 20) | 19 | 0.792 |
| sliding down the ramp | 19–30 | 0.79–1.25 |
| reaches table / leaves ramp foot (±1 frame) | ~30 | 1.25 |
| decelerating slide on the table | 31–36 | 1.29–1.50 |
| comes to rest | 36 | 1.50 |

## Reliability and ambiguities
- **Centroid:** ±1–2 px in the rest phases and frames 20–28. In frames 29–33 it is ±4 px: the notebook hits the table
  and passes the ramp foot, part of it blends with the white ramp, and motion blur is present. Frames 19–23 include a
  few px of blurred background above the notebook's right end.
- **Full mask vs cover centroid:** the full-mask centroid sits about 3–6 px from the cover-only centroid, because it
  includes the page edges. Use the full-mask value as the visible centre.
- **Apparent size:**
  - Changes over the clip come mainly from orientation, not depth. On the ramp the cover is tilted toward the camera
    (mask height ~55–70 px). On the table it lies flat (~32–37 px).
  - The long side grows from ~135 px to ~147–151 px. That is partly the change of view and partly a small move
    toward the camera / image left.
  - Depth is not known from the video. Use the depth_info the question gives together with fx = 762.8 px to
    back-project the centres.
- **Similar objects:** the light top book on the book stack is also pale but does not move. Only the cyan-covered
  notebook moves.
- **Motion and stillness:** there is no camera motion and no duplicated frames. Frames 37–48 show sensor noise only
  (centroid jitter < 0.2 px).
