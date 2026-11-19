# simulation_0024 — measurement record (pixels, seconds)

Video: 960x960, 25 fps, 75 frames (t = frame/25, 0 … 2.96 s). Blender render, 3D scene. Camera **static**.

## Files
- `scene.json` – inventory, static objects, camera/perspective, events, summary rows of the boat track.
- `tracks/boat.csv` – the only moving object, every frame 0–74 (columns below).
- `scripts/` – `common.py` (frame reader), `camera_check.py`, `segment.py` (boat masks → boat.csv; writes overlays to ../frames/),
  `check_tracks.py` (consistency), `static.py` (rock/shore), `write_scene.py` (scene.json), `seg_test*.py`/`dbg.py` (exploration).

## Scene content
- **boat** – red-and-white fishing boat "AH805": red hull with white sheer stripe, white wheelhouse with red roof, white mast
  (black light/antenna on it), black post behind the wheelhouse, white stern rail. Bow points left; it sails bow-first right→left,
  seen roughly broadside and from above, the whole clip. Only moving object. No people, animals or other vehicles.
- **rock** – large pale boulder on the sand, top centre/right, bbox ≈ x 327–955, y 25–308 (628 × 283 px; visual, ±5 px).
- **sand beach** (upper half; dry-sand edge polyline in scene.json) and **sea** (lower half, animated waves; boat wake/shadow right of the stern).

## boat.csv columns
- `hull_*`: red hull mask (R−G>60 & R−B>40, largest blob + hull fragments split off by the white stripe/name; cabin roof excluded).
  `hull_x0..x1` = bow tip … stern (the hull's length along its main axis in the image), `hull_y0` = top of bow, `hull_y1` = bottom of red paint
  (waterline area). `hull_cx, hull_cy` = hull-bbox centre (**recommended reference point** for the boat origin; the true origin is
  probably the hull centre — whether at deck or waterline height is unknown, so the vertical offset is ±~50 px). `hull_centroid_*` = area centroid.
- `bbox_*`: full boat incl. superstructure: x from bow tip to stern parts (rail/rudder, ≈5 px past the red hull), y from mast top to keel
  (`keel_y` = lowest dark pixel ≤14 px under the red hull). `bbox_w_px` ≈ boat length, `bbox_h_px` ≈ full height keel→mast top (perspective view, not a pure side elevation).
- `mask_centroid_*`, `mask_area`: background-difference mask (can include bits of shore foam above the deck; use only as rough).
- `mast_top_x/y` (`mast_top_y_raw`, `mast_fixed`=1 if replaced by a 7-frame running median; frames 10, 11, 14, 32, 43 were fixed, where the thin mast tip dropped out of the mask),
  `roof_x/y` (red wheelhouse roof centre), `bow_x/y`, `stern_x/y`.
- `clipped_right`/`occluded` = 1 for frames 0–1: stern touches the right image edge → `hull_x1`, `hull_cx`, `hull_len_px`, `bbox_*` biased there;
  use `bow_x` (+ ~197 px half-length) or `roof_x` / `mast_top_x` for those two frames.

## Measured behaviour (no speeds derived here)
- Horizontal motion steady right→left: hull_cx 753.5 (f2) → 291.5 (f74); per-frame steps are 6–7 px (integer mask edges), no stops or turns.
- Slight upward drift in the image (hull_cy 600.5 → 582.5; mast top 307 → 291; keel 663–667 → 643–647) and ~2 % shrink
  (hull length 396 → 388 px, full height 361 → 353 px): the boat recedes slightly from the camera. For 3D speed questions combine the
  given depths with focal length estimated from the prior size; motion is mostly lateral.
- Events: moving already at frame 0; fully in frame from frame 2; still moving at frame 74. No contact/bounce/release events.

## Camera / perspective
Static (phase correlation of the rock/sand area: ≤0.02 px drift over the clip, beyond a constant 0.5 px estimator bias). Elevated oblique
view down onto the beach; no horizon, no straight lines for vanishing points. Image y increases toward the camera.

## Reliability
- Hull edges ±1–2 px (codec makes them jump in 2-px steps); hull length 388–396 px consistent frame to frame.
- Mast top ±2 px (thin white mast on pale sand; diff threshold 14 on sand). Keel bottom ±3 px (dark keel merges with its shadow/reflection in water;
  a red reflection patch under the stern is excluded).
- Rock extents are visual ±5 px; its right end and base merge with foam/shadow. Dry-sand edge polyline is visual ±10 px.
- Checked by overlays (frames/ov*.png, traj.png) at frames 0, 10, 20, 37, 50, 60, 74: masks cover the hull, wheelhouse, mast, rail.
