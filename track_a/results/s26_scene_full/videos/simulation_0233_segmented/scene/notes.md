# simulation_0233_segmented — measurement record

2D segmentation clip, 1920x1080, 24 fps, 50 frames (t = frame/24). White background, static camera.
Two objects: a black cat-like **animal** walking right (the only mover) and a static brown **chair** on the right.

## Files
- `scene.json` — inventory, static chair extents, animal size summary, events, camera.
- `tracks/animal.csv` — every frame 0-49: `cx,cy` mask centroid; `body_cx,body_cy` centroid after a 25 px
  morphological opening (removes the thin tail); `body_x0/x1`; bbox `x0,y0,x1,y1`, `bbox_cx,bbox_cy`, `bbox_w,bbox_h`;
  `len_px,width_px,axis_deg` (PCA extents along/across the main axis); `area`; `cut_left_edge` (1 = touching x=0);
  `occluded` (always 0, nothing occludes it).
- `tracks/chair_check.csv` — chair mask bbox/centroid per frame (proves camera and chair are static).
- `scripts/measure.py` (segmentation + tracks + overlays in `frames/ov_*.png`), `scripts/summarize.py` (summaries).

## Method
Animal = non-white connected components that are mostly dark (gray < 90, low saturation) left of x = 1500; chair =
the component at x >= 1500. Overlays at frames 0,10,20,30,40,49 checked: mask covers the whole animal incl. tail and
nose tip, the chair mask the whole chair.

## Key numbers (pixels)
- Animal fully visible from frame 22: nose-to-tail-tip length median 336 px (324-354, varies with tail pose/gait);
  body width (vertical extent) median 67 px (64-75). Main axis horizontal.
- Animal motion: rightward along y ≈ 531 (528-535). Nose front x1: 66 px (f0) → 710 px (f49), mean 13.1 px/frame;
  centroid on frames 22-49 fit 13.36 px/frame. Per-frame steps fluctuate (gait: nose jumps ~30 px about every 9-10
  frames, centroid steps 9.5-17 px), so the pace is about constant with gait ripple; no start/stop inside the clip.
- Chair: bbox x 1538-1835, y 496-715 → 298 px wide, 220 px tall; centroid (1687, 615). No contact with the animal.

## Reliability / ambiguity
- Frames 0-21 the animal is cut by the left edge: centroid/bbox/length there are NOT the full body; use x1 (nose)
  for motion in that range. The true origin (pelvis/root) is not visible; the centroid of the full silhouette
  (frames 22-49) is the best proxy, it lies ~145-160 px behind the nose (x1 - cx).
- Mask edges ±1-2 px; the light-grey nose tip may be partly lost to thresholding in some frames (±5 px on x1).
- Species is ambiguous from the silhouette (most likely a cat). Length includes the tail; questions about "body
  length" without tail would be ~ body_x1-body_x0 (opening-based) — see csv.
