# simulation_0260: notes

**What happens:** this is a 2D simulation: 40 frames at 30 fps, 1920x1080, with a static camera. A cream-coloured mug (handle on its right, cartoon face printed on the front) falls straight down from above the top of the image along the column x ≈ 1241 px. It lands on a dark table near the wall, between a black phone (left) and a beige camera bag (right). It rebounds slightly and comes to rest. The mug is the only object that moves.

Units: pixels (x to the right, y DOWN) and seconds (t = frame/30). No metric scale was assumed.

## Files
- `scene.json`: inventory (mug plus static objects with pixel bounding boxes and extents), events, camera.
- `tracks/mug.csv`: one row per frame 0-39 (`visible=0` in frames 0-1). Columns:
  - `cx, cy`: centroid of the mask (the handle pulls it about 5 px to the right). After landing, the anonymisation patch (see below) biases it a further 4 px.
  - `bbox_cx, bbox_cy, x0, y0, x1, y1, bbox_w, bbox_h`: bounding box of the mask, handle included.
  - `rect_*`: minimum-area rectangle of the mask.
  - `area`: mask area in pixels.
  - `body_x0, body_x1, body_w, body_cx`: horizontal extent of the cylindrical body, handle excluded.
  - `top_y`: rim (top of the silhouette).
  - `y1_true`: bottom, corrected by hand for frames 16-18.
  - `height_px`: y1_true - y0 + 1.
  - `ref_x, ref_y`: **recommended position of the origin**. This is the body centre horizontally and the middle of the silhouette vertically. For an upright cylinder the top and bottom ellipse bulges cancel, so the mid-height is the axis centre.
  - `clipped_top_edge`, `bottom_cut_at_table`, `occluded` (never occluded), `ref_note`.
- `scripts/`:
  - `track_mug.py`: segmentation and track.
  - `postprocess.py`: ref point and manual fixes.
  - `probe.py` and `probe2.py`: pixel and column profiles used for the fixes.
  - `strip.py`: crop montages.
  - `camera_check.py`
  - `draw_track.py`: overlay check.

## How it was measured
- **Mask:** the difference from frame 0 (where the mug is out of view), more than 30 grey levels in any channel. Only "warm" pixels are kept (R − B > −12), because the mug is cream while the wall and its shadows are bluish. The mask is cut below y = 869 to remove the mug's reflection on the glossy table top, then morphology and hole filling are applied. Overlays (mask, bounding box, centroid, body span) were checked visually on frames 0, 3, 6, …, 39 and 17-20. A trajectory overlay was also checked.
- **Static objects:** extents were read from zoomed, gridded crops of frame 0. Accuracy is about ±3 px.

## Reliability
- **Free fall, frames 5-15:** ref_y is good to about ±1 px; ref_x is constant at 1241 ± 1.5 (no horizontal motion).
  - The per-frame drop of ref_y is 38, 46.5, 52.5, 61, 66.5, 73.5, 79.5, 87, 94, 101.5 px, increasing by about 7 px per frame.
  - Extrapolating back gives zero speed at about frame 0, so the mug was released from rest at t ≈ 0, above the image.
- **Apparent height changes during flight:** 71 px at frames 5-6, 65 at 8, 61 at 9, 58 at 12, 54 at 14, 53 at 15. At rest it is 56. This is perspective: the high mug is seen from below, so the visible bottom ellipse adds height. The rest size is the best "true" size:
  - height (rim to base): 56 px
  - body width: 48 px
  - width including handle: 67 px
- **Frames 2-4:** the top is clipped by the image edge. ref_y = bottom − 28, and frames 2-3 have negative ref_y (centre still above the image). Frames 2-3 ref_x is estimated from the bounding box. Low reliability.
- **Frames 16-18 (impact and rebound):**
  - Frame 16: the mug is drawn sunk about 4-5 px into the table top (bottom ≈ 873 vs 869 at rest).
  - Frames 17-18: it is lifted (bottom ≈ 865 and 863).
  - Bottoms come from column profiles (probe2.py) and are good to ±1-2 px.
  - Rim (top_y): 820 at frame 16, 811 at 17, 809 at 18, 812 at 19, 815 at 20, then 814 from frame 21 on.
- **Rest, frames 20-39:** the ref point is (1242.5, 841.5) and is constant to within 0.5 px.

## Ambiguities
- **Grey patch on the mug:** from frame 19 on, a flat grey patch covers most of the mug's front. It looks like an automatic face-anonymisation blur triggered by the cartoon face. Its colour is close to the wall's, so the mask loses part of the upper-left body. The bounding box and ref point stay correct because the rim and the base are still detected, but `cx/cy/area` after frame 19 are biased.
- **Reflection and shadow:** the mug's reflection on the glossy table (below y = 869) and its shadow on the wall to its left are excluded from the mask.
- **Rotation:** the mug turns slightly about its vertical axis on landing (the face print moves), so the handle's apparent width varies by a few px.
- **Origin:** whether the object origin sits at the body centre or the full-bounding-box centre (with handle) is unknown. The handle shifts the horizontal centre by about 9 px but does not change vertical motion.
- **Similar objects:** the mug is easy to tell apart from the red/white takeaway coffee cup (static, x ≈ 858) and the white plant pot (static, x ≈ 1106).
