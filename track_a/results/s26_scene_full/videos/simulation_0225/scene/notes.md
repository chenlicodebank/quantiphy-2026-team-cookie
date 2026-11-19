# simulation_0225: measurement record

Blender render, 2D scene, 1920x1080, 24 fps, 50 frames (t = frame/24, 0 to 2.042 s). **The camera is static**: phase correlation of the facade, curb and loungers against frame 0 gives a shift under 0.13 px in every frame.

## Scene
A modern house terrace seen almost head-on, with water in the foreground. A **black-and-white (tuxedo) cat** walks left to right along the stone deck in front of the sun loungers. It is visible in all frames 0 to 49 and is never occluded. It is the only moving object. The water ripples are an animated texture only. Nothing else moves.

## Files
- `scene.json`: inventory, static object pixel extents, camera, events and a cat summary.
- `tracks/cat.csv`: one row per frame (0 to 49) with these columns:
  - `cx_mask,cy_mask`: mask centroid. This is the reference point and the proxy for the rig origin.
  - `bbox_*`: bounding box, plus `bbox_cx,bbox_cy`.
  - `width_px`, `height_px`: bounding-box extents.
  - `pca_length_px`, `pca_width_px`: extents along and across the mask's main axis.
  - `body_*`: dark-fur pixels only.
  - `feet_y`, `area_px`, `occluded` (always 0).
- `scripts/`:
  - `probe.py`: builds the median background of the region of interest (`bg_roi.npy`).
  - `track_cat.py`: segmentation and tracking. It also writes the overlay to frames/cat_overlay.png.
  - `camera_check.py`
  - `summarize.py`: writes scene.json.

## Method and reliability
- **Mask:** the cat is separated by subtracting a median background (threshold 28) inside x 380–1100, y 780–960. Grey shadow pixels are removed, then morphology is applied and the components near the largest blob are kept.
- **Overlay check:** the overlays at frames 0, 12, 24, 36 and 49 show the mask covers the body, legs and white paws.
  - The thin raised tail and parts of the head or ear are sometimes partly missed.
  - So the bbox may be a few px short at the tail tip or nose. Count on about ±3 px for extents and about ±1 px for the centroid.
- **Gait wobble:** the centroid swings with the stride.
  - Per-frame dx averages 5.49 px/frame, with a standard deviation of 0.81.
  - A linear fit gives 5.45 px/frame (x ≈ 570.9 + 5.45·frame). A quadratic fit gives almost no curvature (−0.003 px/frame²), so the walk looks like constant speed.
  - cy stays within 885–891.
  - Smooth over several frames before taking differences.
- **Cat position:** the centroid moves from (569.8, 890.1) at frame 0 to (838.8, 888.8) at frame 49, a net change of +269 px. The motion is horizontal (+x), with no vertical travel.
- **Cat size (px):**
  - Bbox width (horizontal length, nose to rump or tail root): median 105, range 103–113.
  - Bbox height (paw bottom to tail tip or ear top): median 75, range 66–78. The tail tip is often the highest point.
  - Length along the main axis: about 104.
  - Body-only (black fur) horizontal extent: about 93–100.
- **Static objects:** read from a 2x zoom grid at frame 0, ±4 px.
  - Front loungers 1, 2 and 3: x 764–947, 1004–1189 and 1215–1432; y 735 (backrest top) to 900 (feet).
  - Back-row loungers: left one x 652–826, y 713–858; the other two have backrests at x 874–1016 and x 1062–1206, top y 713.
  - Deck curb top edge at y ≈ 925.
  - House glass box: x 563–975, y 0–358.
- **Events:** the cat is already walking at frame 0 and still walking at frame 49. There is no start, stop, turn, contact or bounce.
- **Ambiguity:**
  - The rig origin (likely the pelvis or root) is not visible, so the mask centroid is used. For speed and displacement it is equivalent up to gait wobble.
  - Pixel scale: in a 2D scene, a single metres-per-pixel scale comes from the prior, such as the cat's length (use bbox width ≈ 105 px) or its speed (≈ 5.47 px/frame ≈ 131 px/s).
  - The loungers sit slightly behind the cat's walking line, so their scale is only approximately the same.
