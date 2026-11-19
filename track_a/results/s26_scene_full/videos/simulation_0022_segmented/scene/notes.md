# simulation_0022_segmented — measurement record

960x960, 25 fps, 75 frames (t = frame/25). 3D Blender scene, segmented: plain white background.
All values are pixels / frames. No metric scale was assumed.

## Scene content
- **boat** (only moving object): red-hulled fishing boat, white wheelhouse and railings, tall mast, "AH805" on the hull.
  Seen broadside, bow pointing left; moves leftward across the image the whole clip. Enters already cut off by the
  right image edge (x = 959) in frames 0–34; fully visible frames 35–74.
- **island** (static): pale beige sand/rock mound in the left half (x 31–557, y 529–655), darker brown cliff at its
  right tip. Its right tip is covered by the boat's bow from frame 63 (the boat is in front, i.e. nearer the camera).
- No people, no other props, no ground/water plane (background removed).

## Files
- `scene.json`: inventory, extents, events, camera.
- `tracks/boat.csv` (every frame 0–74), from `scripts/track.py`. Foreground = 255 − min(RGB) > 10; island pixels
  (frame-0 mask) are removed unless the pixel changed > 25 vs frame 0 (boat in front).
  Columns: `cx,cy` mask centroid; `x0,y0,x1,y1,bbox_w,bbox_h,bbox_cx,bbox_cy` full-boat bbox (mast top to keel/rudder);
  `len_main,wid_cross,axis_deg` PCA extents of the mask (for this boat the two are similar, so the axis flips: use
  bbox_w/bbox_h instead); `hull_*` = largest red/dark component (hull from gunwale y≈586 to keel y≈681, bow to stern);
  `cut_by_right_edge` (= `occluded`) 1 for frames 0–34; `overlaps_island_in_front` 1 for 63–74;
  `bg_shift_x/y` camera check.
- `tracks/boat_template.csv`, from `scripts/template.py`: the bow + wheelhouse part (120 px wide) of frame 50 matched in every
  frame with a scale search (0.94–1.06, step 0.004), sub-pixel. `tm_shift_x/y` = translation vs frame 50 (most precise
  motion signal, valid in all frames incl. the cut-off ones); `tm_scale_vs_f50` = apparent size relative to frame 50;
  `est_bbox_cx/cy`, `est_hull_cx/cy` = frame-50 centres carried to each frame (use for frames 0–34);
  `est_full_len_px/h_px` = scaled full bbox size.
- `island_extents.json`, `island_mask_f0.npy` (packed bits): static island, from `scripts/island.py`.
- `scripts/probe.py` first look at the foreground threshold.

## Key numbers
- Boat motion: template shift_x 232.07 (f0) → −105.35 (f72): mean −4.69 px/frame; ≈ −4.64 px/frame at the start and
  ≈ −4.9 px/frame near the end (the slight increase goes with the boat growing in the image). Bow tip x0: 832 (f0) → 484 (f74).
  Vertical drift is small: bbox_cy ≈ 539–543 the whole clip; tm_shift_y +4 → −4 px.
- Boat apparent size: full bbox 286×283 (f35), 289×292 (f50), 296×292 (f74); hull bow-to-stern 289 px and gunwale-to-keel
  96 px at f74; mast top y≈396. Template scale 0.98 (f0) → 1.02 (f72): ~4% growth, so the boat gets slightly nearer the camera.
- Island: width 527 px, peak at x=250, top y=529, base y 627 (left) to 655 (right tip), peak height above base 111 px,
  bbox height 127 px, main axis tilted 4.9°.
- Camera: static (background shift ≤ 0.12 px).
- Events: no start or stop of motion inside the clip (it moves at constant velocity throughout). Fully in view from f35
  (t=1.40 s). Bow overlaps the island's right tip in the image from f63 (t=2.52 s); this is image overlap with the boat
  in front, and it may not be 3D contact.

## Reliability / ambiguities
- Boat origin (Blender root) is not visible. Proxies: hull bbox centre (`hull_bbox_cx`, y≈633–640) or full bbox centre.
  Both move almost exactly the same way, and they differ mainly in y (≈ 90 px).
- Frames 0–34: the mask bbox/centroid is truncated by the image edge, so do not use `bbox_cx`/`cx` there; use
  `boat_template.csv` (its `est_*` centres carry ±1–2 px error from scale noise ±0.01).
- `hull_cx/hull_cy` (centroid) jumps by ~6 px between frames because the dark keel/shadow pixels are sometimes
  included, so use `hull_bbox_cx` or `tm_shift_x`. Mask edges are ±1–2 px (anti-aliasing; thin white railings and mast
  are faint against white, and the mast top is found only to ±3 px).
- From f63 the boat's bow covers the island's right tip, so island pixels there are taken as boat only where they
  changed from frame 0. The bow x0 stays reliable.
- No perspective references exist (no ground/horizon). Any depth question must rely on the given depth_info plus
  the known size: the focal length can be solved from those inputs and the pixel sizes above.
- Overlays checked: frames/ov_00, ov_40, ov_74 (boat mask blue/red boxes, island green) cover the full objects.
