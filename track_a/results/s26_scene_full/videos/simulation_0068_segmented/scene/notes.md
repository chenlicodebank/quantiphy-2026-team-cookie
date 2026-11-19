# simulation_0068_segmented – measurement record

2D, segmentation source (Blender render with background replaced by pure white), 2160x1080, 24 fps, 72 frames (t = frame/24).
Top-down view of two cars on one plane. No ground features, markings or static props. All values are pixels / seconds; no metric scale assumed.

## Files
- `scene.json` – inventory, sizes, positions, path lengths, events, camera.
- `tracks/white_van.csv`, `tracks/beige_car.csv` – one row per frame (0-71). Columns:
  `frame,time` ; `cx,cy` = mask centroid (recommended reference point ≈ object origin in a top view) ;
  `rect_cx,rect_cy` = centre of minimum-area rotated rectangle (alternative, quantised to 0.5 px) ;
  `bbox_*` = axis-aligned image bbox ; `length_px,width_px` = rotated-rectangle long/short side (along/across the car's axis) ;
  `axis_angle_deg` = main-axis heading, 90 = pointing up (-y), 0 = pointing right (+x) ; `area_px` ; `occluded` (always 0) ; `touches_edge` (always 0) ; `n_components`.
- `scripts/track.py` (segmentation + tracking), `scripts/overlay.py` (check images), `scripts/events.py` (steps, headings, sizes), `scripts/probe.py` (pixel-value check).

## Method
Mask = pixels with 255 − min(RGB) ≥ 6 (background is exactly 255; van body ≈ 243, so the white van is still separable), 3×3 open, 5×5 close, hole fill, components > 3000 px, assigned by nearest centroid to previous frame. Overlays (contours, bboxes, centroids, paths at frames 0/20/40/56/71) were inspected: masks cover each full car, the two cars never touch or overlap.

## Objects
- **white_van** – white minivan, left, faces up. Moves straight up (x ≈ 831.5), from rest at frame 0, speeding up steadily (per-frame step ~0.5 → ~19.5 px; looks uniformly accelerated). Length 240 px (range 236–246), width 91 px. Centroid (831.5, 926.6) → (831.4, 201.9); path 725.6 px.
- **beige_car** – beige/pink-tan car, starts right of the van, faces up, starts moving at frame 1 and drives at roughly constant speed (~6.8 px/frame ≈ 163 px/s) through a right-hand (clockwise) quarter turn: heading 90° until frame 2, 45° at frame 29, ~0° from frame 65, then straight in +x. Length 223 px (217–229), width 87 px. Centroid (991.6, 851.4) → (1371.4, 636.4); path 477.4 px, net 436.4 px.

## Reliability / ambiguities
- Centroids are good to ~±0.5 px per frame; one-frame differences therefore jitter by ~±1 px/frame (beige steps 5.8–7.8 px around a near-constant ~6.8). Fit or smooth over several frames for speed/acceleration.
- Lengths vary by ±4 px from soft anti-aliased edges and the van's grey front strip (roof/bumper edge at the top of the van); use the medians. Heights are not observable from this top view.
- Camera assumed static (simulation; blank background prevents a direct check). No perspective: one px scale applies to both cars.
- Which car a question calls "the car" vs "the van": white vehicle = white_van (straight, accelerating); beige vehicle = beige_car (turning, constant speed).
