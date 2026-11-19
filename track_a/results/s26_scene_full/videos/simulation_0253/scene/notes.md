# simulation_0253 – measurement record (pixels, seconds)

Video: Blender render, labelled **2D**, 1920x1080, 24 fps, 45 frames (0–44), t = frame/24.
Content: a small tan cardboard box (with tape) slides down a straight inclined ramp from upper-left to lower-right.
It is the only moving object. The camera is static.

## Files
- `scene.json` – inventory, camera, ramp geometry, path direction, apparent box size, events.
- `tracks/box.csv` – one row per frame (0–44). Columns:
  `visible`; `cx,cy` = mask centroid (reference point ≈ box centre/origin); `bbox_x0..y1,bbox_w,bbox_h`;
  `rect_cx,rect_cy,rect_len,rect_wid,rect_angle_deg` = min-area rectangle of the silhouette (len ≈ along slope,
  wid ≈ across slope); `area_px`; `cut_by_frame_edge`/`occluded` (1 = clipped by the top image edge);
  `s_along_path_px` = centroid projected on the fitted path line (0 at frame 15, positive downhill);
  `step_px` = centroid distance to previous frame; `cx_est,cy_est` = centre estimate (equal to cx,cy when
  unclipped; for clipped frames 5–14 estimated from the leading bbox corner minus the median offset 59.6, 58.8 px).
- `scripts/` – `track_box.py` (segmentation/tracking + overlays), `static_scene.py` (ramp lines, camera and
  duplicate-frame checks; writes `static_out.json`), `summarize.py` (path fit, scene.json), `clipped_centre.py`,
  probes and `montage.py` (overlay checking).

## How measured
- Box mask: Lab colour difference to frame 0 (box absent there): Δb* ≥ 5 or (Δa* ≥ 3 and Δb* ≥ 3), close 9x9,
  open 3x3, largest component, holes filled. This excludes the box's grey shadow and the dark ramp band (an
  earlier saturation mask leaked into them). Overlays at frames 12, 24, 32, 40, 44 checked visually: mask covers
  the whole box (top + visible side faces) and nothing else.
- Camera: phase correlation of a box-free region vs frame 0 → shifts ≤ 0.5 px (noise). Static.
- Ramp: band edges fitted on frame 0 (`static_out.json`). Lower/left edge y = 0.9697x − 249.3 (very clean,
  residual 0.7 px); upper/right edge y ≈ 0.9675x − 313.1 (noisier). Image incline ≈ 44.1° below horizontal;
  band ≈ 46 px wide perpendicular (≈ 64 px vertically). Ramp runs from the top edge (x≈260–330, y=0) to its lower
  end near (1360–1390, 1000–1080), where it meets the floor; ≈1490 px visible length. Box centroid path is a straight
  line at 44.36° below +x (unit vector in scene.json), perpendicular scatter ≤ 1.4 px.

## Box numbers (key)
- Visible frames 5–44 (enters at the top edge already moving); fully in frame 15–44. Absent frames 0–4
  (frame 4 shows only a few pixels; treated as absent).
- Apparent size (frames 15–35, little blur): min-area-rect ≈ 107.5 px along slope × 87.7 px across; axis bbox ≈ 119 x 116 px;
  area ≈ 7960 px² (medians). Silhouette includes top and side faces (render is slightly oblique), so these are projected
  extents, not a single face edge. Frames 38–44: along-slope length grows to ~115–125 px from motion blur, width
  shrinks to ~77 px – use frames 15–35 for size.
- Motion: per-frame step grows steadily from ~22 px (15→16) to ~60 px (43→44) — accelerating, no stop, bounce,
  impact or direction change within the clip. Last frame: box still on the slope near (1322, 965).

## Caveats / ambiguity
- **Duplicated frames**: frame 28 is identical to frame 27 and frame 11 to frame 10. At 26→27 the step is 83 px
  (≈ two normal steps), so frame 27 already shows the position that belongs to frame 28 (one frame dropped,
  then repeated). Per-frame differences around 26–29 (and 9–12) should account for this, e.g. by
  using 26→29 spans or a fit.
- Frames 5–14 are clipped at the top edge: raw centroids are biased; `cx_est,cy_est` are rough (±5–10 px,
  worst for 5–9, where steps are irregular). Prefer frames 15–44 for motion.
- The centroid is of the silhouette (top + one side face), so it may sit a few px off the true 3D centre; this
  offset is constant and cancels in displacements.
- Shadow of the box falls down/right onto the ramp band; excluded from the mask.
- Static scenery: large light-grey face of the incline block left/below the band, dark wedge in the bottom-left
  corner (x 0–240, y 860–1080), plain grey wall/floor (floor junction soft near y≈1000 at right). No markings.
