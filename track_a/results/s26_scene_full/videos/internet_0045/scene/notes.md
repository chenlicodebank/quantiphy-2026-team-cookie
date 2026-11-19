# internet_0045: measurement record

**Scene.** A real handheld video: 45 frames at 30.0133 fps (1.50 s), 1920x1080. A white cylinder lies on its side and rolls
from right to left across a glossy light-wood desk. It is the only moving object. It is a paper or foam roll with a hole
in its end face. Static objects, left to right:

- a white wavy bowl
- an iced-tea bottle with a yellow cap
- a dark-green glass bottle
- a red T-fal kettle
- a black desk lamp

There is also a black monitor behind them, plus a power strip and cables. Units are pixels and seconds only.
Time: t = frame / fps.

## Files
- `scene.json`: summary covering the inventory, visibility, orientation, apparent sizes, events, camera and perspective.
- `tracks/cylinder.csv`: one row per frame (0-44). The columns are:
  - `cx_mask, cy_mask`: silhouette centroid, the visible centre and recommended reference point.
  - `cx_stab, cy_stab`: the same centroid mapped into frame-44 background coordinates (camera drift removed).
  - `cx_bbox, cy_bbox`: centre of the bounding box.
  - `bbox_x0..y1, bbox_w, bbox_h`: the bounding box.
  - `mask_len_main_axis`, `mask_width_across`, `main_axis_angle_deg`: from cv2.minAreaRect of the mask hull.
  - `mask_area`.
  - `occlusion`: `visible`, `right_edge` or `left_edge` (cut off by the image border), or `not_visible`.
- `tracks/camera.csv`: per-frame similarity transform to frame 44 (ORB + RANSAC). It gives the shift of the image
  centre (px), the scale, the rotation and the inlier count.
- `static_objects.json`: extents of the static objects at frame 44 (corrected by eye). `static_objects_auto.json` holds
  the raw GrabCut output.
- `scripts/`: `track.py` (cylinder + camera), `static_objs.py`, and the helpers `crops.py`, `montage.py`, `dbg.py`,
  `pix.py`, `regstats.py` and `probe.py`. Run them from the `scene_ws` folder.

## How the cylinder was measured
1. **Registration.** Frame 44 is a clean background (the cylinder has gone by then). Each frame is registered to it
   with a similarity transform: ORB features + RANSAC, 2300-3000 inliers.
2. **Pixel test.** Frame 44 is warped into frame i. A pixel counts as cylinder when:
   - the max-channel difference is > 25, and
   - the blue channel rose by > 35 (the desk's B is 115-150, the cylinder's 170-250), and
   - either (B - R) > -27 (the cylinder is bluish-white) or saturation < 44 (its warm-lit side).
3. **Clean-up.** A 9 px opening, then the component nearest the predicted position (gated against the kettle label).
   Holes are filled, then an opening with a 41 px disk cuts away the desk reflection.
4. **Visual check.** Overlays were drawn on every frame and inspected. Bounding boxes were compared by eye with
   50-px-gridded crops at frames 6, 24 and 27 (values are in `scene.json`).

## Reliability
- **Top, bottom and leading (left) edges** match the by-eye edges within about 5 px.
- **`bbox_x0` (leading edge)** is the cleanest coordinate in frames 4-30.
- **Centroid:** good to about 5 px.
- **Trailing (right) edge** is under-segmented in frames 19-33. Motion blur mixes the trailing end with the
  bottles, the bowl and the desk, so `bbox_x1`/`bbox_w` are 10-20 px short there. By eye, the true horizontal
  width is 233 px at frame 24 and 250 px at frame 27, against 221 and 232 px from the mask.
- **Desk-reflection lumps:** frames 9, 13-17 and 19 keep a small lump of the desk reflection at the lower left.
  `bbox_y1` is inflated by about 20-40 px there, with a few px of bias on `cy`. Frame 9 is the worst (bbox_h 241 where its
  neighbours give 221-223).
- **minAreaRect fields** jump between frames when the silhouette is nearly square (frames ≥ 13). Use them only for the
  side-view frames 4-12.
- **Partial frames:** frames 0-3 and 31-33 are cut off by the image border, so their centroids are not the object
  centre. Frame 34 is a faint sliver and was not measured.
- **Camera:** the drift is slow and smooth, about 0.2-0.3 px per frame, and negligible next to the cylinder's motion of
  about 50-75 px per frame. It is still recorded, and the cx_stab/cy_stab columns remove it.

## Apparent size: what a question's "size" can mean
- **Side view (frames 4-8).** The silhouette is about 300 px long along its tilted axis (minAreaRect 296-312), and the
  horizontal bbox is 286-306 px. Across the axis it is about 183-187 px (the apparent diameter). The axis is
  foreshortened, so the true length is longer than it looks.
- **End-on view (frames ≥ 13).** The end face points at the camera. The silhouette is about 230-250 px wide (by eye) and
  250-270 px high.
- **Motion direction.** The cylinder moves mainly horizontally to the left, with a small downward drift in the image:
  cy goes from about 713 to about 832 over frames 4-30. So the pixel length along the motion direction is the
  horizontal extent. That extent is about 300 px in the side-view frames and about 230-250 px when end-on.
- **Changing depth.** The cylinder rolls slightly toward the camera, and its bottom edge drops from y 823 to y 956.
  Its apparent size therefore grows by roughly 10-20 percent over the clip, on top of the change from turning. One
  planar scale (the annotators' convention) ignores this. Take the prior object's pixel size from the frames the
  question concerns.

## Ambiguities
- **"White object":** the bowl is also white but static, so the cylinder is the only mover.
- **Shadow and reflection:** the cylinder casts a soft shadow on the desk to its lower left. The glossy desk also shows a
  bright reflection of it below its left end. Neither is included in the masks, apart from the small lumps listed above.
- **Overlaps:** the cylinder passes in front of the kettle (frames 6-14), the green bottle and the tea bottle (16-24),
  and the bowl (25-31). Nothing hides the cylinder itself; it is always in front.
- **Before and after the clip:** no release, bounce or collision is in the clip. Motion starts before frame 0 and
  ends after the cylinder leaves the frame at the left (last seen at frame 34, t = 1.133 s).
