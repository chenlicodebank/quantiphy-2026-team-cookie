# simulation_0041 – measurement record

Simulation (Blender) video, labelled **2D** in inputs.json. 1080x1080 px, 24 fps, 72 frames (t = frame/24, 0 to 2.958 s).
Everything is in **pixels** (x right, y down, origin top-left) and seconds. I did not guess any metric scale.

## Scene
A high, nearly top-down aerial view of a beach. The camera is **static**: the rock region shifts by less than 0.01 px over the clip.
- **boat** (moving): fishing boat with a white/grey deck, red hull bottom and red cabin roof, a mast, and lettering like "AH808" on the hull. The bow points left. It is the only vessel. It sails in a straight line toward the left and slightly up (image direction −164.3°, about dx −5.7, dy −1.6 px per frame), at a steady ~5.9 px/frame. It does not rotate (|rot| < 0.06°). Its apparent size stays constant.
- **person** (moving): the only human, in a white T-shirt and dark trousers, walking on the sand toward the bottom of the image (direction +86°, down and very slightly right) at ~1.5 px/frame. They cast a long dark shadow to the upper right; the shadow is **not** part of the mask.
- Static: the rock outcrop (top centre-right, cut off by the top edge, bbox about x 478–1010, y 0–220), the dry pink sand beach (lowest tip near (400,722)), a darker band of wet sand or shallow water, and green water. Outlines are given in scene.json. They were read by eye on a 100 px grid, so expect about ±10 px.

## Key facts / events
- **Frame 1 is a near-duplicate of frame 0** for the whole image: the mean grey difference is 0.04, against 1.3–1.4 for every other pair of consecutive frames. Both objects therefore show 0 px displacement from frame 0 to 1 and move from frame 2 on. A backward-difference speed at frame 1 is 0. Keep this in mind when a question asks about t = 0.04 s, or about averages that include frame 0 to 1.
- Boat, frames 0→71: net displacement 412.7 px, path 412.9 px (a straight line). Mean step is 5.93 px/frame over frames 2–36 and 5.86 over frames 36–71, so the speed is constant within noise (per-frame steps scatter ±0.3 px).
- Person centroid, frames 0→71: from (359.4,387.8) to (366.5,493.8), net 106.3 px. The raw centroid path is 110.6 px because it includes ±1–2 px gait jitter. With a 9-frame smoothing the mean is 1.50 px/frame.
- The boat's bow reaches the left image edge at **frame 63** (t = 2.625 s). From there on the mask bbox and centroid are truncated (`occluded`=1), but the template track `ref_x/ref_y` stays valid.
- There is no contact, impact or direction change. The boat–person distance is 625 px at frame 0 and 457 px at frame 71.

## Files
- `scene.json`: inventory, camera, sizes, static features and events.
- `tracks/boat.csv` (frames 0–71):
  - `ref_x, ref_y`: the reference point. It is the centroid of the frame-30 boat silhouette (cabin and mast included; template centroid (354.6, 945.0)), carried by a rigid sub-pixel template match.
  - `tm_dx, tm_dy`: the shift relative to frame 30. `tm_rot_deg` is the fitted rotation (≈0). `tm_rmse` is the match residual in grey levels; it grows away from frame 30 because the water texture changes.
  - `mask_cx, mask_cy`: centroid of the per-frame colour mask. It is noisier (±0.5 px).
  - `hullfill_cx, hullfill_cy`: centroid of the mask's convex hull. It jumps when stray water highlights join the mask, so do not use it for speeds.
  - `bb_*`: the mask bounding box, mast included.
  - `mask_len_px, mask_wid_px, axis_deg`: PCA extents of the mask.
  - `occluded`: 1 when the boat touches the image edge.
- `tracks/person.csv` (frames 0–71):
  - `ref_x, ref_y`: mask centroid, shadow excluded.
  - `pelvis_est_x/y`: bbox centre x and y0 + 0.48·bbox height. This is a hip-level guess.
  - `head_top_y`, and `feet_x, feet_y` (the lowest mask row).
  - `bb_*`, PCA extents, and `occluded` (always 0).
- `scripts/`: `bg.py` (camera check), `seg.py` (segmentation and overlays), `tracks.py` (integer template track and CSVs), `refine_boat.py` (sub-pixel and rotation refinement), `static.py` (boat width profile and the automatic static attempt), `summary.py`, `dupes.py`, `probe.py`.

## Sizes (px)
- **Boat** (frame 30, fully visible):
  - bbox including the mast: 330 x 236. The median over frames 0–61 is 330 x 237.5, and the width stays within 327–333, so the size is stable.
  - Bow tip (184,881) to stern (513,974): **341.9 px**, along an axis of 15.8°.
  - PCA length of the silhouette: 353 px.
  - Width across the bow–stern axis: about 100–110 px on the bare after hull, up to about 130 px at the cabin, and about 197 px when the mast is included (the mast projects sideways in this oblique view).
  - Mast tip at frame 30: (327,793).
- **Person**: apparent head-to-feet height median **45 px** (10th–90th percentile 39–48, range 37–50). Width median 18 px (16–20). The view is from above, so this height is foreshortened. The legs are as dark as the shadow, so the lowest foot is sometimes cut off or merged by ±3 px, which is why the height varies frame to frame with the gait. For a reference height, use the median or upper percentiles.

## Method and reliability
- **Person**: I subtracted a median background. Pixels that changed and fall inside the vertical column spanned by the light shirt/skin pixels (±2 px) are kept, which removes the shadow because it extends to the right. Checked on overlays at frames 0, 24, 48 and 71: the mask covers head to feet with no shadow. The centroid is good to about ±1 px.
- **Boat**: a median background cannot be used because the boat ghosts into it. Instead I used a colour mask (white/grey low saturation, or saturated red), excluded the sand, and filled holes. Checked on overlays at frames 0, 24, 48, 66 and 71. The dark cockpit deck behind the cabin is partly missed by the mask. The template track is the most reliable position; I estimate about ±0.2 px.
- **Ambiguities**:
  - The boat's world origin is unknown. Use `ref_x/ref_y` for displacements and speeds; any fixed point on this rigid, non-rotating boat gives the same motion.
  - The person's pelvis is approximated (see `pelvis_est`).
  - The view is slightly oblique, so the boat's visible side and the person's foreshortened height are not true top-view extents.
  - Boat shadow and person shadow are excluded from all masks.
