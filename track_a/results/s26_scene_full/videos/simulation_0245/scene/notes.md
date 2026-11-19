# simulation_0245 – measurement record

Video: 1080x1920 (portrait), 30 fps, 75 frames (t = frame/30, 0 … 2.467 s). Source: simulation (Blender), **2D scene**.
All values are in pixels (x right, y down) and seconds. No metric scale is assumed.

## Scene content
- **creature**: a large fantasy quadruped with a horse/antelope-like body. It has an orange-brown striped coat, a white chest ruff, one very long curved ribbed/feathered horn sweeping back over its back, a long thin tail with a tufted tip, dark hooves and a pale grey snout. It walks left→right through the whole clip and is fully in frame in all 75 frames.
- **rabbit**: a small orange rabbit on the floor just ahead of (to the right of) the creature's front legs. It hops left→right all clip long. It is fully in frame for frames 0–64. From frame 65 it is cut by the right image edge, and only the rear part shows by frame 74.
- Static: a seamless olive-grey studio wall with a soft spotlight glow, and a studio floor. The wall/floor crease (darkest row) is at y≈1483, and the brightest spotlit floor band is at y≈1564. There are no other props, markings or furniture.
- Soft cast shadows of both animals lie on the floor at y≈1480–1560 and move with them. They are excluded from the masks.

## Files
- `scene.json`: inventory, per-object size statistics, camera, perspective and events.
- `tracks/creature.csv`, `tracks/rabbit.csv`: one row per frame (0–74). Columns:
  - `frame`, `t`
  - `cx_centroid`, `cy_centroid`: mask centroid, the recommended reference point.
  - `cx_bbox`, `cy_bbox`: bbox centre.
  - `bbox_x0`/`bbox_y0`/`bbox_x1`/`bbox_y1`/`bbox_w`/`bbox_h`: bounding box (inclusive pixels).
  - `mask_len_major`, `mask_width_minor`, `major_axis_deg`: PCA-axis extents of the mask.
  - `area_px`
  - `occluded`: always 0. Nothing occludes either animal.
  - `touching_other`: 1 in frames 54–56, where the rabbit and a front hoof touch in the image.
  - `at_image_edge`
  - Creature only: `torso_x0`, `torso_x1`, `torso_cx`, `torso_len`. These come from the median of the longest horizontal mask run in rows 1330–1400 and run from the back of the rump to the front of the chest.
- `scripts/`:
  - `common.py`: decoding.
  - `background.py`: clean-background build. Composite of frames 0 and 74, patched, then a masked temporal median.
  - `segment.py`: masks, tracks and overlays.
  - `build_record.py`: writes `scene.json`.
  - `camcheck*.py`, `probe*.py`, `summarize.py`: diagnostics.
  - `background.py` must run before `segment.py`. Its `frames/bg.npy` is scratch and was deleted afterwards.

## Method
The camera is static: wall and floor profiles are identical across frames away from the animals, so there is no pan, zoom or shake, and the background shift is 0 in every frame. Foreground was found by difference from the clean background:
- Wall region (y<1470): max channel difference > 6.
- Floor (y≥1470): the pixel must also show a chromaticity change (>0.026), or be very dark or bright relative to the background, or be much darker than the horizontal 61-px running median of the darkening ratio. This keeps thin legs and hooves but rejects the broad soft shadows.
- Small floor blobs are dropped unless they are dark (hooves).
- The rabbit is the blob near its previous position, cleaned to the orange (R−B>55) region. In frames 54–56 it was split from the hoof by erosion.

Overlays at frames 0, 30, 40, 55, 60 and 70 were inspected. The masks cover both animals, including the horn, tail, legs and hooves.

## Sizes and positions (pixels)
- **creature**:
  - bbox height (horn tip y≈1123 to hooves y≈1549): **427 px** (422–432). It is very stable.
  - bbox width (tail tip to snout): median 474 px (443–514). This varies with gait, tail swing and snout detection.
  - torso length (rump to chest): **266 px** (mostly 258–276).
  - PCA major/minor: 556 / 452 px.
- **rabbit** (frames 0–64): bbox about 76 × 62 px, median. It ranges 68–98 × 52–72 with the hop pose: stretched vs. crouched, ears up or down.
- Ground/hoof contact line: y≈1547–1551 for both animals.

## Motion summary (for orientation only, no model fitted)
- **creature**: moves steadily right. Centroid x goes 354.2→832.7 (+478 px in 74 frames, about 6.3–6.5 px/frame). Centroid y stays ≈1315–1324, with a slight gait bob. Per-frame dx of the centroid is noisy (±2 px) because the leg, tail and head poses change. Smooth or difference over several frames when you use it.
- **rabbit**: centroid x goes 578.8→1005 by frame 63 (≈6.7 px/frame, varying 3.4–9.8 px/frame within each hop cycle). Centroid y ≈1518–1524.
- Both move parallel to the image plane. Apparent sizes do not change, so there is no depth change and one px→m scale applies to both.

## Events
- Motion starts before frame 0 and continues past frame 74: no start or stop in the clip.
- Rabbit hop cycle (period ≈12.5 frames):
  - Tall/stretched pose (bbox top highest) at frames 2, 14, 27, 40, 52 and ≈64.
  - Crouched pose at frames 6, 19, 32, 45, 58.
- Frames 54–56: the rabbit and the creature's front hoof overlap or touch in the image. It is not obviously a physical contact.
- Frame 65: the rabbit reaches the right image edge.

## Reliability and ambiguities
- The creature's **pale grey snout** almost matches the wall colour (difference 2–4 grey levels). The mask sometimes misses the front 10–30 px of the head, so `bbox_x1` and `bbox_w` jitter by up to about 20–30 px. Prefer `bbox_h`, `torso_len`, `bbox_x0` (tail tip) or the centroid for scale and motion.
- The creature's origin (rig root) is not visible. The mask centroid (mid-trunk, y≈1320) or `torso_cx` is the best horizontal stand-in. Horizontal motion is the same for any body-fixed point up to the gait wobble.
- Hooves in dark shadow are partly lost in a few frames. The bbox bottom is still at 1549–1551.
- The rabbit's bbox bottom drops to 1539–1545 in a few frames (55–56, 69–73) where its feet sit in shadow. From frame 65 its centroid is biased left because part of it is out of frame. Use frames 0–64 for rabbit size and speed.
- Frames 54–56: the split between rabbit and hoof is approximate (±5 px on the rabbit's left edge).
