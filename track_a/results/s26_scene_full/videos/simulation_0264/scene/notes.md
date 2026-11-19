# simulation_0264 — measurement record

**The video:** a 2D simulation, 2560x1440 px, 24 fps, 72 frames (3.0 s). One grey and white futuristic **hover car**, nose pointing left, hovers about 34 px above a seamless grey studio floor and casts a dark shadow below it. It starts at rest near the right edge, at frames 0–1. It then accelerates smoothly to the LEFT and has left the frame by frame 68. There are no other objects and no markings. The camera is static.

## Files
- `scene.json`: inventory, sizes, events and camera notes.
- `tracks/hovercar.csv`: one row for each of the 72 frames. Columns:
  - `visible`
  - `clipped` (right/left/none)
  - `ref_x`, `ref_y`: estimated car centre
  - `bbox_cx`, `bbox_cy`: centre of the visible bbox
  - `mask_centroid_x`, `mask_centroid_y`
  - `x0 y0 x1 y1`: visible bbox
  - `length_px`, `height_px`, `area_px`
  - `occluded` (always 0)
- `tracks/hovercar_shadow.csv`: the same columns for the floor shadow.
- `scripts/track.py` builds both CSVs. `overlay.py` draws boxes on frames (output goes to `frames/ov_XX.png`). `check.py` prints the per-frame steps. `explore.py` was the first look.

## Method
- **Background difference:** each frame is compared with frame 71, which is empty (|diff| > 15 grey levels, then a 5x5 open, keeping components larger than 200 px).
- **Car vs. shadow:** the car is everything above y = 1062 and the shadow is everything below it. Rows 1043–1075 are empty in every frame, so this split is clean.
- **Checking:** overlays at frames 0, 12, 30, 50 and 60 showed the boxes hugging the full car (antenna tips through the underbody) and the full shadow.
- **Reference point:** `ref_x` is the bbox centre when the car is fully visible (frames 9–52).
  - When it is clipped (frames 0–8 at the right edge, 53–67 at the left), `ref_x` is extrapolated from the visible edge using a linear fit of apparent length, L(f) = 1034.5 − 1.183·f px (residual sd 3.6 px).
  - `ref_y` is the bbox centre y, about 885 px and essentially constant, because the motion is horizontal.
- **Simplest positional reference:** the front (left) edge `x0` is visible in frames 0–52 and is the cleanest edge.

## Key numbers (px)
- **Car bbox when fully visible:**
  - Height: 315 px (y 728–1042, including the two rear antennas). The body alone, without antennas, is about 265 px.
  - Length: 1023 at frame 9, 1001 at frame 30, 975 at frame 52 (median 1002.5).
- **Shadow:** y 1076–1130, about 54 px thick. Its length is about 1047 px at frame 12 and about 980 px at frame 51.
- **Per-frame step of `ref_x`:** about −1 px (frame 2), −13 (frame 12), −27 (frame 24), −37 (frame 33), −48 (frame 43), −58 (frame 52), about −70 (frame 66). The steps grow nearly linearly, about 1.2 px/frame², so this looks like a uniform acceleration from rest.

## Events
| Event | Frame | t (s) |
|---|---|---|
| Car at rest | 0–1 | 0–0.042 |
| Motion starts (front edge moves 1 px) | 2 | 0.083 |
| Fully in frame | 9 | 0.375 |
| Front edge reaches left image edge | 53 | 2.208 |
| Last sliver visible | 67 | 2.792 |
| Gone | 68 | 2.833 |

There are no bounces, contacts or direction changes.

## Reliability and ambiguities
- **Mild perspective:** the apparent length shrinks by about 5% across the frame, and the side seen changes from rear-quarter to front-quarter view. Despite the 2D label, the pixel length depends on the frame.
  - For a size prior, use the length at the matching frame, or about 1000 px at mid-traverse (frame 30).
  - The centre is less affected than the edges.
- **Measurement noise:**
  - Positions in fully visible frames: ±1–2 px. Extrapolated `ref_x` in clipped frames: ±3–5 px. Frames 54–67 are the least reliable.
  - The rear edge flickers by a few px (thin antennas and fin tips, faint against the background), so per-frame differences of `ref_x` carry ±2 px of noise. The front edge `x0` is smoother.
  - `y1` jitters between 1033 and 1042 because of thin underbody parts.
- **Shadow:** the shadow is not the car. The shadow's length and x-position differ from the car's (it is offset slightly left and is longer).
- **Not measurable:** the true origin of the vehicle rig is not visible; the bbox centre is used. There is no depth information and no metric scale.
