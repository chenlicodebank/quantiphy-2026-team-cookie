# simulation_0008 – measurement record

3D Blender render, 1080x1080, 66 frames (0-65) at 22.802381 fps (t = frame/fps, 0-2.851 s).
A lakeside scene: a white wooden **rowboat** glides right-to-left across the foreground water in front of a small
**jetty** and a wooden **boathouse** on stilts; trees left and right, rock on the left bank, rocky hills behind.
The rowboat is the only moving object. **The camera is static** (shift < 0.02 px on the boathouse in all frames).
All values are pixels / frames / seconds; no metric scale has been assumed.

## Files
- `scene.json` – inventory (all objects, distinguishing features, static-object pixel boxes), camera, perspective cues, events.
- `tracks/boat.csv` – rowboat, every frame 0-65. Columns:
  - `ref_x, ref_y` – image proxy for the boat origin = centre of the full-boat box (x: bow_x + length/2;
    y: (top_y + waterline_y)/2). For frames 0-54 the stern is off-screen, so ref_x uses the length 647.9 px
    (mean of the measured lengths at frames 55-57).
  - `bow_x` – x of the bow stem tip (leftmost boat point); sub-pixel template tracking; **most precise point** (±1 px relative, ±2-3 px absolute).
  - `stern_x_meas` – measured stern end (frames 55-65 only); `stern_x_est` = bow_x + length.
  - `top_y` – top of the boat mask (top of stem/stern posts, ~618-624); `waterline_y` – hull/reflection boundary.
  - `vis_bbox_*` – box of the visible above-water mask; `vis_mask_cx/cy`, `mask_area_px` – visible-mask centroid/area (biased by clipping; do not use as origin for frames 0-54).
  - `length_px_est` (used for ref_x), `length_px_meas` (bow→stern, frames 55-65), `height_px` (top_y→waterline),
    `hull_h_at_bow40/100` (gunwale→waterline hull height 40/100 px behind the bow; apparent-size check).
  - `occluded` = 1 when the stern is beyond the right image edge (frames 0-54), note column says so.
- `tracks/_bow_template_ref65.csv`, `_bow_template_ref30.csv` – raw bow template matches (frame-65 template, used for frames ≥25; frame-30 template, used for frames 0-24 after shifting by its offset at frame 25 = +3.86 px).
- `track_overlay.jpg` – every 5th frame with mask (red), full-boat box (yellow) and ref point (magenta); checked: hits the boat, excludes the reflection.
- `scripts/` – camcheck.py (camera), segment.py/track_boat.py (mask development), bow_template.py + bow_template_early.py (bow tracking), size_check.py (apparent size), flow_boat.py (KLT test, not used – biased), final_track.py (writes boat.csv).

## Method
Background = frame 0 for x<960 (boat not yet there) and frame 65 for x≥960 (boat already left). Boat mask =
|frame − background| > 28, cut at the per-frame waterline (darkest row y 735-780 where the dark lower hull meets its
dark reflection), morphological open/close, largest component, cut left of the tracked bow (wake ripples). The bow
end of the raw mask was noisy because of wake ripples, so the bow is tracked by masked colour template matching
(SQDIFF, sub-pixel). Stern measured from the mask once it is inside the image (frame 55+).

## Motion summary (observational only)
- Bow x: 990.2 (f0) → 320.0 (f65), i.e. ~670 px leftward in 65 frames, nearly uniform (~10.0-10.8 px/frame,
  slightly larger early than late). Vertical drift tiny: waterline 751→760 (f0-25) → 755 (f65).
- Boat moving the whole clip: no start/stop, release, bounce, contact or direction change. Events in scene.json
  (bow at jetty right edge f~34, bow at image centre f43, fully visible from f55).

## Apparent size / depth (3D)
- Fully visible length (bow-stem tip to stern) 649 px (f55) → 639 px (f65); height top-of-posts→waterline ~133-138 px;
  hull height at bow+100 px ≈ 88 px, constant within ±2 px over all frames (84-90). So the apparent size is constant
  within ~2-3%: the boat moves essentially parallel to the image plane at nearly constant depth. The 1.5 % length
  decrease in f55-65 (stern moves ~10.9 px/frame vs bow ~10.0) may be a slight recession/yaw or stern-mask noise;
  not confirmed by the hull height. The full-length extrapolation for frames 0-54 (647.9 px) is therefore ±~2 %.
- The boat (waterline y~755) is nearer the camera than the jetty (legs at y~680) and the boathouse (base ~y590).
- Boat is seen side-on, so beam (width) is not measurable. Image centre (540,540) assumed as principal point.

## Reliability / ambiguities
- Reflection: the boat's mirror image below y≈757 is excluded; note waterline is the lower bound of the boat box.
- Frames 0-54: only part of the boat is visible – the origin (centre) is extrapolated from the bow (ref_x); its
  frame-to-frame differences are as good as bow_x's (constant length offset). Note ref_x has a small step pattern in
  f55-65 because it uses the measured (noisier, ±2 px) stern there.
- Frames ~37-43: the stem post top merges with the jetty behind it, so `top_y` drops (636-644); ref_y uses the median top (620) there.
- Wake ripples on the water behind the boat are not objects; minor mask noise.
- Static-object boxes (scene.json) read from a gridded frame-0 image, ±3-5 px; trees are cut by image edges.
