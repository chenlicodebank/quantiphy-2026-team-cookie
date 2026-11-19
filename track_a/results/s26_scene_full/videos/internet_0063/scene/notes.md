# internet_0063: measurement notes

## What the video shows
The video is 1920x1080 at 30.016 fps, 94 frames (3.13 s). The camera is rotated by 90°. A hand at the left edge holds a clear plastic water bottle (blue cap, Evian-type label) horizontally against a grey wall, then lets go. The bottle **falls toward image +x**, so gravity points to the right of the image.
- Evidence: after release, the bottle's x displacement per frame grows linearly (12, 26, 38, 51, 64, 76, 90, 101, 114, 123, 135, 145, 150 px/frame for frames 41–53). That is a constant pixel acceleration of roughly 12 px/frame², while the hand stays behind.
- The black vertical strip at x ≈ 1370–1540 is the skirting board. The wood on the right is the floor.
- The bottle hits the skirting board/floor at about frame 52–53 and tumbles clockwise. It lands on the wooden floor around frames 60–66, then rolls slowly toward the image top-right until the end.
- inputs.json calls the scene "2D". The fall happens in the wall plane, facing the camera. The floor phase (frames ≳ 60) shows perspective (see below).

## Files
- `scene.json`: inventory, static object positions and sizes, events, camera summary.
- `tracks/bottle.csv`: one row per frame (0–93):
  - `center_x, center_y`: the **reference point**, the bottle's visible geometric centre. It is computed as `cap_end + 130 px` along the bottle axis (half of the 260 px bottle length). Frames 54–59 use the observed foreshortened length instead.
  - `center_x_stab, center_y_stab`: the same point minus the camera drift (frame-0 background coordinates).
  - `cap_x, cap_y`: centroid of the blue cap (directly segmented, the most precise point).
  - `cap_end_*`, `base_end_*`: the two ends of the bottle along its axis. `base_end_y < 0` means the base is outside the top of the frame.
  - `axis_angle_deg`: image angle of the cap→base direction (x right, y down, so positive angles are clockwise on screen). `axis_source` says whether it came from mask PCA or a hand-checked value.
  - `mask_bbox_*`, `mask_len_main_axis`, `mask_width_across`, `mask_centroid_*`: extents of the background-difference mask.
  - `occlusion`, `motion_blur`, `phase` (held / falling / impact_tumble / on_floor_rolling).
- `tracks/hand.csv`: bounding box of skin pixels connected to the left image edge, plus the rightmost skin pixel (≈ fingertip). Low precision.
- `tracks/camera_shift.csv`: per-frame Euclidean warp of the background relative to frame 0 (dx, dy in px, rotation in degrees).
- `scripts/`: run in this order: `camera_shift.py` → `track_cap.py` → `track_bottle.py` → `build_record.py`. The checking tools are `overlay.py`, `crops.py`, `check_axis.py`, `draw_path.py`, `profile.py` and `camera_affine.py`. Scratch images and intermediate `.npy` files are in `../frames/`.

## How it was measured
- **Camera:** I ran ECC Euclidean alignment of each frame to frame 0 at half resolution, masking out the hand/arm regions.
  - x is well constrained by the vertical black strip. Its edges independently drift from 1386 to 1365 px (row 150), matching dx ≈ −19 px by frame 75.
  - y is weakly constrained (the scene has almost no horizontal structure). The dy values of 4–6 px are approximate, and frame 85 (+16) is suspect.
  - There is no zoom: the strip width stays 132–137 px in every frame.
  - The drift is ~0.2 px/frame, negligible against the fall (≥ 12 px/frame). For floor-phase motion (~5–7 px/frame), x drift is ~0.2 px/frame and y drift is uncertain at about ±0.5 px/frame. Use the `_stab` columns if needed.
- **Cap:** I took the HSV blue blob (H 95–125, S > 90, V > 70) nearest the previous position at full resolution. It is reliable in every frame, ±1–2 px when sharp and ±4 px under blur (frames 44–60, where the blob is a streak and its centroid is the streak centre). Late frames: the bluish bottle body adds to the blob area, a few px of bias.
- **Bottle mask:** I subtracted a camera-aligned median background (half resolution), then removed skin pixels and attempted to remove shadow pixels.
  - **Bias:** On the grey wall the mask includes the bottle's soft shadow below/right of it and the motion blur. The mask bbox, mask length (~280–315 px) and mask width (~105–150 px) are therefore too large in frames 0–60, and the mask centroid is biased about +15–30 px in y.
  - On the wooden floor (frames 61–93) the mask fits the bottle well (verified visually).
  - Use the mask extents only as upper bounds in the wall phase.
- **Bottle axis and centre:**
  - Frames 0–39: angle ≈ 1° (checked visually).
  - Frames 40–60: hand-checked angles. I drew a 260 px axis with ±35 px edges on each frame (`check_axis.py`) and adjusted until it matched the blurred bottle.
  - Frames 61–93: mask PCA angle, ±5°.
  - Centre accuracy: ±3–5 px in frames 0–48 and 61–93; ±8–15 px in frames 49–60 (heavy blur, tumble).
  - Check: in frame 15 the visible bottle spans x 120–378, y 547–617, so the box centre is (249, 582); the record gives (250.9, 579.5).
- **Bottle size (manual, zoomed frames):**
  - Length cap end → base: **≈ 260 px**. Measured 258 ± 4 px in the held frames (cap end slightly hidden by the thumb) and 263 px in frame 72.
  - Diameter: **≈ 70 px** on the wall, where the lower edge is hard to separate from the shadow (range 62–78).
  - An annotator measuring "bottle length" would most likely get 255–265 px.

## Events (frame / time)
| Event | Frames | Time |
|---|---|---|
| Held at rest (cap creeps 14 px left) | 0–39 | 0–1.30 s |
| Release / start of fall (onset ≈ frame 39.5, from a constant-acceleration fit to cap x) | 39–40 | ≈ 1.32 s |
| Free fall toward +x; axis rotates 1° → 25°, centre y drifts 578 → 557 | 40–53 | |
| Impact on skirting board/floor (base end crosses the strip edge at x ≈ 1368) | between 52 and 53 | ≈ 1.75 s |
| Horizontal (fall-direction) motion stops after frame 53 | | |
| Tumble/bounce; axis 25° → 236° clockwise; foreshortened in 54–57 (tipped out of plane) | 53–60 | |
| Lands on the wood floor with axis ≈ 265° (cap toward image bottom) | ≈ 60–66 | 2.0–2.2 s |
| Rolls steadily toward image top-right (centre (1492, 242) → (1640, 111)); still moving at the end | 66–93 | |
| Arm swings into the lower-left of the frame | ≈ 85–93 | |

## Ambiguities and reliability
- **Scale.** The fall is in the wall plane. The bottle's 260 px length was measured in that plane (held frames) and is the natural ruler for "bottle length" priors.
- **Perspective on the floor.** In the floor phase the bottle appears bigger as it rolls toward the image top: length 255 → 273 px and width 85 → 108 px between frames 66 and 82. The floor is not seen face-on, so pixel motion there is not on the same scale as the wall plane.
- **Partly out of frame.** From frame 84 the base end is outside the top of the image. The mask bbox is clipped at y = 0 and `mask_len_main_axis` shrinks (294 → 257). The centre column still uses the cap plus the 130 px offset.
- **Shadow.** The bottle casts a soft brownish shadow on the wall below/right of it. It is the main source of mask bias, and in early tests it was mistaken for skin.
- **Motion blur.** Heavy in frames 44–60. The bottle is a streak of up to ~150 px per frame, and the cap blob is the streak centre (mid-exposure position).
- **Other objects.** There is only one bottle and one person (hand/arm). Nothing else moves.
- **No motion models, speeds or accelerations are recorded.** The per-frame displacements quoted above only document the direction of gravity.
