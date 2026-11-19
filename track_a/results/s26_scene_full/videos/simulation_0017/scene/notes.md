# simulation_0017 – measurement record (pixels, seconds)

Scene: 3D Blender render, 1080x1080, 33.038926 fps, 101 frames (t = i/fps, 0 – 3.027 s).
A single person walks through a living room. The camera is **static** and the image is
**rolled ~90°**: world "up" points to image +x (right). Feet are at image x≈355–382, the head
top at x≈705; the floor, rug and sofa are on the left, the white shelving wall on the right.
The person walks along image **+y** (top → bottom), roughly parallel to the image plane.

## Files
- `scene.json` – inventory (all objects with pixel boxes), camera, perspective cues, events.
- `tracks/human.csv` – final per-frame track, frames 0–100:
  `pelvis_x, pelvis_y` (recommended pelvis/origin estimate, smoothed), `pelvis_x_raw, pelvis_y_raw`,
  `head_top_x` (top of head, = mask x max), `head_y` (head centre across the body), `head_w_px`,
  mask bbox `bbox_x0..bbox_y1`, `height_px_head_to_lowest_foot` (= bbox width along x),
  `stride_extent_px_along_walk` (= bbox height along y), PCA `main_axis_len`, `across_axis_w`,
  `mask_area`, `occlusion`.
- `tracks/human_raw.csv` – unsmoothed per-frame output of the segmentation.
- `scripts/bg_mask.py` (median background → `scripts/_bg.png`), `scripts/track_human.py`
  (segmentation + raw track + overlays), `scripts/finalize.py` (camera check, smoothing → human.csv),
  `scripts/check_montage.py` (draws the track on crops for checking), `scripts/bg_crop.py` (gridded
  background crops used for the static boxes).

## How measured
- Background = per-pixel median of every 4th frame (clean, person fully removed).
- Mask = |frame − bg| > 30, minus cast shadows (darker, same chromaticity; only tested at x<480,
  where the shadow falls on the grey block/floor), plus a chroma test (d>12, chroma shift>0.02)
  for the dark jeans over the dark grey block; largest blob + nearby blobs. Masks were drawn on
  frames 0–100 and checked: they cover the whole body (head to sneakers) in all checked frames.
- Pelvis: along the body axis (image x) the pelvis is put 0.47·H below the head top, H = 350 px
  (standing height measured in frames 0–20, where the feet are clearly visible), i.e. pelvis_x ≈
  540 (shirt hem / belt line, verified visually). Across the body (image y) it is the centre of the
  hip band x∈[pelvis_x±12] with skin (hands) removed. Final pelvis_y = median‑5 then mean‑5 smoothing.
  pelvis_x is effectively constant (~540): the walk has no visible vertical component in the image.
- Static boxes read off gridded background crops, accuracy ±3–5 px.

## Key numbers
- Pelvis y: 20 (f0) → 748 (f100); ~7.3 px/frame on average (7.4, 7.6, 6.9 px/frame over the three
  thirds – roughly uniform walking, slight slowdown or noise at the end). Per-frame steps of the
  smoothed pelvis: mean 7.5, sd 2.5 px (gait bob + estimation noise) – fit a line or average over
  several frames for speeds.
- Apparent size: standing height ≈350 px early (f0–20), median 327 px for f25–100 (lowest foot at
  x≈380–382; part of this drop may be the sole sitting at the sofa-cushion edge x≈383). Head width
  ≈47 px constant, head-top x ≈705 constant → camera distance nearly constant during the walk (any
  depth change is small, at most a few %).
- Camera: static (shift < 0.03 px).

## Reliability / ambiguities
- Only one moving object; no similar people. The face is rendered as a flat grey patch (character
  texture, not an occlusion).
- Frames 0–4: the body is cut by the top border (pelvis_y there is less reliable, f0 pelvis partly
  outside the frame).
- Frames ~40–75: the person walks in front of the dark grey block and the grey chair/sculpture;
  dark jeans have low contrast there, so leg extents/bbox_y and the hip band are less reliable (±5 px).
- `height_px_head_to_lowest_foot` varies with gait (foot lifts) and hair noise (±5 px); for a rest
  standing height use ~350 px (early frames) or ~327 px (later median) and state which.
- pelvis position is an anatomical estimate (±5 px along x, ±4 px along y), not a rendered origin.
- No metric scale is assumed anywhere; depth/focal length must come from the question's prior.
