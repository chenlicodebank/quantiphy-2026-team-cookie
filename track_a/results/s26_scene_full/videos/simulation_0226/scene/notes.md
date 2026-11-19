# simulation_0226 – measurement record

**Scene.** A 2D Blender render, 1920x1080, 24 fps, 50 frames (t = frame/24, 0 to 2.042 s). A fixed top-down camera looks at a paved promenade: a grass bed at the left, two rows of wooden sun loungers at the top (3 complete in front, 3 cut off by the top edge), and dark water below y = 623. The **only moving object is a small black animal** (a dog or cat silhouette seen from above, head to the right, thin tail to the left). It walks straight to the right (+x) along the pavement just above the water edge, at y ≈ 567–571. It is visible and unoccluded in all 50 frames. It is already moving in frame 0 and still moving in frame 49.

## Files
- `scene.json`: inventory, camera, static-object pixel extents, animal summary and events.
- `tracks/animal.csv`: one row per frame (0–49) with these columns:
  - `frame`, `time`
  - `body_cx, body_cy`: centroid of the body mask with the tail removed. **This is the recommended reference point (origin proxy).**
  - `body_bbox_cx/cy` and the body bbox `body_x0..y1`
  - `body_len_px`: length of the tailless mask along its main (PCA) axis. `body_wid_px`: width across that axis.
  - `full_*`: the same measurements for the full mask including the tail.
  - `axis_deg`: main-axis angle (0/180 = horizontal).
  - `area_full`, `area_body`
  - `occluded` (always 0)
- `scripts/`:
  - `motion_scan.py`: camera-shift and moving-region scan.
  - `track_animal.py`: segmentation, the csv and the overlay check.
  - `static_measure.py`: groove positions, water edge and step statistics.
  - `zoom.py`: crop viewer.

## Method and reliability
- **Camera:** phase correlation on the pavement gives 0.00 px shift in every frame, so the camera is static. Frame differences show only the animal, plus faint grass sway at the far left.
- **Animal mask:** gray < 45 inside the ROI x 440–1000, y 500–612, keeping the largest component. The ROI stops above the water because the water is also dark. The tail is removed with a 9x9 elliptical opening.
- **Overlay check:** overlays at frames 0/10/20/30/40/49 show that the mask covers the whole silhouette, the tail is correctly split off and the centroid sits mid-body.
- **Shadow:** the soft shadow is grey and is not included in the mask.
- **Position accuracy:** about ±1 px.
- **Gait wobble:** the body centroid steps 5.46 ± 0.71 px/frame (range 4.1–7.6) because the silhouette shape changes with the gait. A linear fit of x(frame) gives 5.47 px/frame with no measurable acceleration (quadratic term −0.0005 px/frame²), so the animal walks at constant speed. Net displacement is +266.4 px in x and −3.5 px in y over frames 0→49.
- **Sizes (px):**
  - body without tail: 85.3 long (83–89)
  - with tail: 107.5 long (105–110)
  - width: 22.1 (21–23)
  - Height cannot be measured from a top view.
  - A size prior for "length" is ambiguous: with the tail it is about 107 px, without it about 85 px. A world bounding box of the rig normally includes the tail, so prefer about 107 px when a length prior or question refers to the whole animal.
- **Static objects (±5 px, read off a grid overlay of frame 0):**
  - Front loungers are about 338 px long (y 124–462) and about 202 px wide:
    - left: x 742–944
    - middle: x 1012–1215
    - right: x 1270–1487 at the flared backrest, 1272–1452 at the seat
  - Raised backrests look slightly wider (perspective).
  - Pavement slabs are 144.7 px apart in x (grooves at x = 430, 575, …, 1876). Horizontal grooves are at y ≈ 75, 341 and 604, and the pavement edge/water line is at y = 623.
- **Scale:** this is a 2D scene, so use one metres-per-pixel scale from the given prior: its pixel size, pixel speed (≈ 5.47 px/frame = 131 px/s) or pixel acceleration (≈ 0). Ground-plane perspective is negligible.
- **Events:**
  - No start or stop of motion within the clip, and no direction changes, contacts or bounces.
  - The head tip crosses the groove at x = 719 at about frame 19 (≈ 0.79 s).
