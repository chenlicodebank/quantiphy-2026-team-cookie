# simulation_0042 – measurement record (pixels, seconds)

Video: 1080x1080, 24 fps, 72 frames (3.0 s), Blender simulation, 3D scene. t = frame/24.
Scene: near top-down (bird's-eye) view of a sand beach (upper-left), a rocky headland (top centre-right, cut by the
top edge) and green sea (bottom/right). A black **bird** flies left -> right across the beach; a red-and-white
fishing **boat** drifts bow-first to the left at the bottom. No people, vehicles or other animals.

## Files
- `scene.json` – inventory (objects, visible frames, size summaries, static extents), camera, events.
- `tracks/bird.csv` – frames 0-67. Centroid of the dark silhouette (cx_px, cy_px), bbox, PCA mask length/width
  (`mask_len_px` is the long axis, which here is the wingspan direction), bbox height, main-axis angle (deg, image
  coords, y down), area, `touches_edge`, plus `len_along_flight_px` (body length along local flight direction),
  `span_across_flight_px` (wingspan as seen) and `flight_dir_deg` (direction of centroid motion over 2 frames,
  positive = downward in image).
- `tracks/bird_shadow.csv` – frames 0-28, centroid/bbox of the bird's shadow on dry sand.
- `tracks/boat.csv` – frames 0-71. Centroid of the hull mask (mast/rigging removed by an 11x11 opening), hull bbox,
  hull length along its main axis (`mask_len_px`), width across (`mask_wid_px`), bbox height, axis angle, area,
  `touches_edge`, `mast_top_y_px` (topmost y of mast), `cx_ref_px, cy_ref_px` (edge-corrected reference, see below).
- `scripts/` – track.py (all tracks + overlays), camera.py (camera stability), static_and_post.py (static extents,
  boat edge correction, step checks), probe*.py (pixel-value probes), show.py, check.py. To regenerate, run
  track.py and then static_and_post.py (which adds cx_ref/cy_ref to boat.csv), from the scene_ws folder.

## Method and reliability
- Camera: **static** (background phase correlation max 0.08 px over the clip). No pan/shake correction needed.
- **Frames 0 and 1 are identical** (duplicated first frame). Per-frame displacement 0->1 is zero for everything;
  motion appears from frame 1->2 on. Keep in mind for speed at t=0.04 s.
- Bird: mask = pixels darker than max(30, 0.35 x local mean brightness), nearest-component continuity, nearby
  fragments merged. Overlays checked at frames 0,12,30,45,60,71 – contour hugs the bird. Centroid steps are smooth,
  16.5-17.6 px/frame (frame 2-66). Frames 0-1 and 67 are cut by the image edge (centroids biased; flagged).
  Wing flapping makes span vary 31.6-62.4 px; max-spread frames 5, 31, 54; min-spread ~11, 24, 46. Body length along
  flight ~25-30 px (noisy +-2 px). Peak spans grow (54.7 -> 56.3 -> 62.4 px) as the bird moves down-image, i.e.
  closer to the camera (perspective and/or descending) – apparent size is NOT constant; use depth info if given.
- Bird shadow: blob much darker than the local sand; tracked on dry sand only (frames 0-28). It lies up-right of the
  bird (e.g. f0 bird (5,360), shadow (363,315); f28 bird (435,477), shadow (810,417)). Don't confuse with the bird:
  the bird is pure black and sharp, the shadow is softer and brownish.
- Boat: mask = red hull (R > G+50) or neutral white/grey (min>110, max-min<40) below y=700, closed, largest
  component; hull = mask opened 11x11 (removes mast). Hull length 344-350 px, width ~148-150 px through frame 62.
  Centroid moves ~5.9 px/frame steadily (per-frame jitter +-0.5 px). From frame 63 the bow is cut by the left image
  edge, so raw centroid/length are biased; `cx_ref/cy_ref` shift the frame-62 centroid by the stern bbox motion
  (integer bbox -> per-frame step noise ~+-1.5 px, but cumulative positions are fine). Frame 0/1 hull bbox bottom
  (1079) includes a few stray pixels at the bottom edge – use frame 2 onwards for size.
- The reference point for the boat is the hull-mask centroid in the image; Blender origin may sit at the waterline /
  hull centre – the projected difference is small in this near-top-down view but unknown.
- The boat's height cannot be measured directly (top view); mast tip is ~47-51 px above the hull mask top in image y.
- Static extents (scene.json): sand beach and rocky headland from masks at frame 30 and visual reading of a gridded
  frame (±10 px). The sand mask includes the pale submerged-sand fringe (lowest point (436,799)); the dry-sand edge is
  higher (lowest ~ (400,720)).

## Ambiguities
- Shadows: bird shadow (on sand, then faint on water) and the large boat shadow (water, upper-right of boat, with a
  long thin mast shadow) are not objects.
- 3D: no horizon or vanishing point visible; perspective only from slight lean of vertical structures toward the
  top of the image and the size trends above. Pixel distances are not uniformly scaled across the image.
