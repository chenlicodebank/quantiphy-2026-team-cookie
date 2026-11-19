# captured_0053s – measurement record

Lab recording (24 fps, 48 frames, 1280x720, 3D) whose background was replaced by a smooth colour
gradient (SAM2 demo watermark bottom-right). Lab camera convention: fx = fy ≈ 763 px, principal point ≈ (640, 360).
All positions are in pixels (x right, y down), times t = frame/24.

## Files
- `scene.json` – inventory, camera, events, summary numbers.
- `tracks/blue_object.csv` – the only moving object, frames 0–47: `cx,cy` = mask centroid (the visible-centre
  reference point), `bbox_cx,bbox_cy`, bbox `x0,y0,x1,y1`, `bbox_w,bbox_h`, `area_px`, `equiv_diam`,
  `minrect_len/wid/angle_deg` (minimum-area rectangle of the mask; angle of the long side, OpenCV degrees),
  `pca_len/wid/angle_deg` (extent along/across the mask's principal axis), `occluded` (always 0).
- `static_objects.json` – basketball, cup, white card: centre, bbox, area, equivalent diameter, min-rect size/angle.
- `bg_median.png` – temporal median of 12 frames (clean, contains only the static objects).
- `scripts/` – `bg_median.py` (background), `track_blue.py` (track + overlays), `static_objects.py`,
  `motion_check.py` (per-frame steps), `camera_check.py` (camera stability / frame irregularity), `gap_check.py`.

## Objects
- **blue_object** – blue box-shaped toy (probably a toy car) with yellow/white rectangular print. Moves in a straight
  line up-left (heading ≈ −148° in image coordinates, along its own long axis) from (895, 443) at frame 0 to (538, 220) at
  frame 47; centroid path 422.5 px, net 421.6 px. Already moving at frame 0 and still moving at frame 47. The
  centroid step falls from ≈11–13 px/frame (frames 1–11) to ≈5.5–7 px/frame (frames 33–47). It moves away from the camera (image-up =
  farther), so its apparent size shrinks: bbox 144×128 → 109×88 px, area 11803 → 6673 px, mask short side 102 → 77 px.
  Long side stays ≈109–111 px from frame 16 on (it shrinks with distance while the oblique view lengthens it).
- **basketball** – orange Wilson ball, static at (985.8, 369.8), 68×62 px (equivalent diameter 65.5 px; slightly
  wider than tall from the oblique view or a soft mask edge).
- **cup** – small white tumbler with dark lid, upright, static at (564.2, 423.8), 28 px wide × 47 px tall.
- **white_card** – flat white printed rectangle (box/booklet/card) on the surface, static at (664.7, 614.1),
  min-rect 78.9 × 47.4 px, long side at ≈60°.

## Method and reliability
- Moving mask: |frame − median background| > 35 (max over BGR), open/close, the largest component near the previous
  position, holes filled. Overlays (frames 0, 12, 24, 36, 47) show that the mask covers the whole object. Centroid is
  accurate to about 1 px, but frames 0–10 have motion blur that smears the edges by a few px along the motion direction.
- Static masks: polynomial background fitted to the ROI border, residual > 30. The outlines were checked visually and are
  accurate to ±1–2 px.
- Camera: static (shift < 0.3 px all frames).
- Events: no contact, bounce, release or turn. The blue object starts ~28 px (mask gap) from the ball at frame 0 and moves
  away. **Timing irregularity:** the steps into frames 12 (19.9 px vs ~10) and 36 (13.4 px vs ~6) are about double,
  and the bbox jumps by the same amount. These are most likely dropped or irregular capture frames, not real
  motion jumps. Smooth over ≥5 frames (as the reference convention does) when deriving velocities.
- Perspective: the background replacement removed the floor, the shadows and any horizon, so there are no vanishing
  points. Depth must come from the question's depth_info, together with fx ≈ 763 px. The apparent-size shrink gives the
  depth ratio: sqrt(area) ratio of frame 47 to frame 0 ≈ 0.75, so the object is about 1.33× farther at the end.
  Back-project the centroid with (u−640, v−360)·Z/763.
