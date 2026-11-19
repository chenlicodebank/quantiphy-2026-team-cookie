# simulation_0282 — measurement record

2D simulation (Blender) clip, 24 fps, 72 frames (t = 0 … 2.958 s), 2560×1440. All values are in px and frames/s; no metric scale is assumed.

## Scene
- **Only object:** one dark-grey winged dragon, seen from directly above. Its head (with a light-grey cone-shaped snout tip) points left and its long spiky tail points right. It flies right → left across the frame. It flaps from frame 0 to about frame 50, then glides with its wings held spread from frame 51 to the end.
- **Background:** plain light-grey ground with a strong vignette (darker corners). There are no static objects, markings or horizon. The dragon casts a soft shadow offset to its left; this shadow is not part of the object.
- **Camera:** static. Background patches match frame 0 to within 0.1 grey level in every frame (`scripts/framediff.py`).

## Files
- `tracks/dragon.csv` (main file), one row per frame:
  - `body_x, body_y`: the reference point, i.e. the torso/hip centre on the spine. It is the best proxy for the rig origin.
  - `body_src`: `torso_template` for frames 0–66, `tail_template` for frames 67–71.
  - `body_in_frame`.
  - `bbox_*`: full mask bounding box. `extent_x_len` is the length along the flight direction, wings included; `extent_y_wingspan` is the extent across the flight direction, i.e. the wingspan.
  - `mask_cx/cy` (mask centroid; it wobbles with the wing pose, so do not use it for speeds), `mask_area`.
  - `tail_tip_x`: left blank when the tail is cut by the right edge.
  - `match_scale`: apparent size relative to frame 52.
  - `cut_by_edge`, `occluded` (always 0).
- `tracks/dragon_body_template.csv`: torso template output for every frame, with the NCC score. Valid for frames 0–66 (NCC 0.73–1.0). Frames 67–71 are invalid because the torso has left the frame.
- `tracks/dragon_raw.csv`: raw mask measurements. Its `nose_x` column is unreliable (see below).
- `scene.json`: inventory, sizes, events and camera.
- `scripts/`:
  - `bg.py`: median background.
  - `track.py`: mask.
  - `body_track.py`: torso template.
  - `tail_track.py`: hips+tail template for the exit frames; run with argument 60. Its output files are `tail_track_out_*.csv`.
  - `assemble.py`, `check_body.py`, `framediff.py`, `montage.py`, `probe.py`.

## Methods
- **Mask:** the darkness ratio is (bg − grey)/bg, using the median background. A pixel is in the mask if its ratio is above 0.55 (dark bones and body). Pixels with a ratio above 0.22 are also kept when they lie inside the hole-filled 41-px closing of that dark mask; this restores the lighter wing membranes. The soft shadow (ratio ≤ 0.5, blurry) is mostly excluded. Overlays were checked by eye at many frames: the boxes reach the wing tips, tail tip and head. Expect about ±5–10 px uncertainty on the extents. Some light membrane patches are missing inside the wings at frames 24–28 and 40, but this does not affect the boxes.
- **Body point:** the darkness-ratio image of frame 52 is used as a template. It covers head, wing roots, torso and hips, box x 440–700, y 680–760. It is matched over scales 0.78–1.22 with subpixel peak refinement. The reference point is (600, 716) in frame 52. Visual checks (`frames/body_check.png`, not kept) show it sits on the hip bulge in every frame from 0 to 66.
  - For frames 67–71 the head and torso are off-screen. There, a hips+tail template from frame 60 (x from B+60 to B+310) gives the same point: it agrees with the torso template to within 1–1.5 px over frames 58–66.
  - Expected precision is about 1 px per frame. Per-frame steps are 34.4 ± 1.0 px.
- **Nose/tail tips:** the snout tip is a light-grey cone (grey ≈150 against a background of ≈200) and blends into the shadow, so automatic nose detection is unreliable. Measured by hand on frame 52: snout tip x = 418, tail tip x = 888, giving 471 px from nose to tail tip. Relative to the body point, the snout tip is −182 px and the tail tip is +288 px; the tail flexes slightly during flapping.

## Key numbers (px)
- **Motion:** the dragon is almost uniform and always moves left.
  - Per-frame step of the body point is 32.4–36.7 px; the mean over frames 1→71 is 34.42 px/frame (×24 → ≈826 px/s).
  - Frames 0 and 1 are nearly identical (0.5 px apart), so steady motion starts with the 1→2 step.
  - Net displacement from frame 0 to 71 is 2408 px; path length is 2410 px.
  - Vertical bob: body_y goes 721 → 735.6 (f15) → 708.4 (f41) → 716 (f52) → 714.8.
- **Wingspan (y-extent):**
  - Maximum 1033 at f0. Other peaks: 870 (f13), 1000 (f26), 915 (f37).
  - Minimum 292 at f42. Other troughs: 317 (f17, wings raised), 502 (f8) and 505 (f32), the last two with wings swept back in a V.
  - Glide (f51–70): constant 897–899.
  - Frame 71 (479) is cut by the frame edge and must not be used.
- **Length along the flight (x-extent, wings included):** 401–743. The glide value grows from 462 to 494 between f51 and f63, together with match_scale 1.00 → 1.04.
- **Edges:** the tail is cut by the right edge at f0–3, so x-extents there are too small. From f64 the dragon is cut by the left edge, so x-extents from f64 on are too small.

## Ambiguities / reliability
- **Rig origin:** the exact origin used in Blender is unknown. The torso/hip point is a rigid body point, so its displacements and speeds should match those of any rig root to about 1 px per frame. Absolute positions could be offset by tens of px if the root is elsewhere (for example the chest).
- **Size scale:** apparent size varies by about ±5% (template scale 0.94–1.06), mostly from wing and body pose. During the glide there is a small growth (+4%) as the dragon nears the left edge.
- **Which "wingspan":** if a question gives a wingspan prior, decide whether it means the maximum (1033 px, f0), the glide value (897 px) or the value at a given frame; the csv has every frame.
- **Shadow:** the soft shadow on the left side of the wings is excluded from the masks. If a size seems ~50 px too large, the shadow has been included.
