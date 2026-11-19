# internet_0068 – measurement record

Video: 1920x1080, 30 fps, 100 frames (t = frame/30). Internet clip, 2D (side view). A toy **acorn** (black knitted cap with a stem, on a white cup) is pulled across a wooden floor by a **string**, moving left → right in front of a grey wall with a white baseboard rail that has two black **brackets**. Nothing else moves.

## Files
- `scene.json` – inventory, static feature positions, events, camera summary, size summary.
- `tracks/acorn.csv` – one row per frame where the acorn is visible (53–74). Columns:
  - `ref_*` = coordinates in the **reference frame (frame 99)**, i.e. background-stabilised (use these for motion).
  - `ref_bbox_cx, ref_bbox_cy` – centre of the bounding box (= visible centre; the default reference point).
  - `ref_mask_cx, ref_mask_cy` – mask centroid (biased left/up because the shaded right side of the cup is partly missing from the mask – prefer bbox centre).
  - `ref_x_min..ref_y_max`, `bbox_w` (along motion = length), `bbox_h` (stem top to cup bottom = height), `max_row_width` (widest mask row ≈ cap width), `body_height_no_stem`, `area_px`.
  - `ref_stem_x` – centre x of the stem knob (narrow, best horizontal marker; ≈ bbox centre +-5 px).
  - `raw_bbox_cx, raw_bbox_cy, raw_stem_x` – same points in raw frame pixels.
  - `truncated_at_edge` – 1 when cut by the frame edge (53–58 left, 73–74 right); bbox/centre are then of the visible part only. `flag` – `anomalous_frame` for frame 61.
- `tracks/camera.csv` – per-frame similarity transform ref→raw (`a00..a12`), shift at image centre, rotation, scale, inlier count, residual.
- `scripts/` – `track2.py` (registration + segmentation + tracks + overlays), `static.py` (static features), `events.py` (string activity), `probe*.py`, `sheet2.py`, `montage.py` (viewing helpers), `track.py` (first attempt without registration, superseded).

## Method
- Camera: Shi-Tomasi features in frame 99 tracked into each frame by pyramidal LK, RANSAC partial-affine fit (30–230 inliers, mean residual ≈0.4–0.6 px). **The camera is not perfectly static**: hand-held drift, the raw image is shifted ≈ +12–14 px in y relative to frame 99 for frames 0–60, decaying to 0 by frame ~90; x shift 0 → +6 px (max near frame 68); rotation 0.33° at start → 0 by frame 45. Over the acorn's passage (53–74) the camera x shift changes by only ~2 px, so raw and ref tracks differ by 3–8 px roughly constant offset.
- Acorn mask: each frame warped to ref, compared with a median background (frames 80–99 warped), pixels kept if (changed >30 and dark V<50 or unsaturated S<45) or (blue channel rose >12 and changed >15); open 9x9, close 25x25 and 41x41, largest tall blob. Overlays (frames/ov_*.jpg, not kept in the record) were checked: the outline follows the cap and stem exactly and the cup's left/lower edge; the **shaded right half of the cup** is often missing from the mask, but the bounding box is still right because the cap is the widest part and the cup bottom is captured on its left side. Shadow (lower-left) is excluded.

## Key numbers (pixels)
- Acorn fully visible frames 59–72: bbox width (along motion) 329–367 px, median ≈346; height (stem top → cup bottom) 418–427, median ≈420. Height constant → constant depth; the width growth 329→367 (frames 65→72) is motion blur (object moves faster). A sharp-frame length is best taken as the lower end (~330 px); the blur-free cap width is ≈ 320–330 px.
- Acorn ref y of bbox centre ≈ 741 ± 2 (horizontal motion). Ref stem x: 57: 65.7, 58: 137.8, 59: 217.1, 60: 302.2, 61: 392.6, 62: 487.5, 63: 586.1, 64: 690.7, 65: 796.2, 66: 904.1, 67: 1015.3, 68: 1132.3, 69: 1256.2, 70: 1383.2, 71: 1522.7, 72: 1666.2, 73: 1812.2 – per-frame steps grow from ~80 to ~146 px (the acorn speeds up throughout; no bounce/reversal).
- Static (ref = frame 99): baseboard rail top y≈483–486, lower dark edge y≈503 (x=150) to ≈513 (x=1850); left bracket body x 324–363, y 457–500; right bracket body x 1636–1673, y 479–517; bracket centres ≈1311 px apart.

## Events
string twitch frames 1–3; string tugged up toward baseboard frame 44 (t=1.467 s); acorn enters left edge frame 53 (t=1.767); fully in frame 59–72 (t=1.967–2.400); touches right edge 73; last visible 74 (t=2.467; frame 75 shows only its shadow); string gone from 76.

## Reliability / ambiguities
- Edge positions ±2–3 px in sharp areas, but motion blur smears the left/right edges by tens of px at high speed, so x_min/x_max carry ~±10 px uncertainty; stem x and bbox centre are the most stable (±3 px). Vertical extents ±3 px.
- Frame 61 looks different (cup suddenly shows a leaf pattern, cap smoother) – probably an edited/interpolated frame; its position fits the sequence but treat with care.
- Partial frames (53–58, 73–74): bbox centre is NOT the object centre; use x_max (entering) / x_min (leaving) or stem x (57, 58, 73) instead.
- Annotator convention: one scale from the prior's pixel size; if the prior is the acorn's length, the measured pixel length is ~330–367 px depending on frame (blur); its height ~420 px.
