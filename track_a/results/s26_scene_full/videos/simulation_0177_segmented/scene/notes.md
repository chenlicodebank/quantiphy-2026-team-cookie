# simulation_0177_segmented — measurement notes

**Scene:** a 2D segmentation clip, 24 fps, 60 frames (0–59, t = frame/24), 1920×1080. The background is plain white and there are no other objects, no ground, no shadows and no perspective cues. The camera is static. The only object is one **elephant**, seen side-on and walking to the right for the whole clip. There is no start, stop, turn, contact or occlusion.

## Files
- `scene.json`: inventory, a summary of the motion in pixels, size ranges, camera and events.
- `tracks/elephant.csv`: one row per frame (60 rows). Columns:
  - `frame`, `time_s`.
  - `cx_bbox, cy_bbox`: centre of the bounding box.
  - `cx_mask, cy_mask`: centroid of the silhouette.
  - `cx_body, cy_body`: centroid of the mask after a 15 px erosion, which removes the trunk, tail and thin legs.
  - `bbox_x0..y1`: bounding box. `width_px` and `height_px` are its extents.
  - `main_axis_len_px` and `across_axis_px`: PCA extents along and across the main axis.
  - `area_px`, `occluded` (always 0).
  - `torso_x0, torso_x1, torso_len_px`: the x-range of columns where the mask is at least 60 px tall. This runs from rump to head and leaves out the trunk and tail.
- `scripts/track.py`: builds the mask, the tracks and the check overlays (written to `frames/check_*.png`). `scripts/extra.py`: checks for other objects, computes the torso extents and the step statistics.

## Method and reliability
- **Mask:** pixels with min(R,G,B) < 200, cleaned with a 3×3 opening, plus any components close to the main blob. Overlays at frames 0, 30 and 59 confirm the mask covers the whole elephant, including the light-grey ear, trunk, tusks, tail and feet, and nothing else.
- **Edge accuracy:** extents are good to about ±1–2 px.
- **No other objects:** no non-white pixels appear outside the elephant's box in any frame.
- **Reference point:** the rig root/origin is not visible in the image. Use the mask or body centroid as a proxy. Over the clip, the per-frame steps of the centroid range from 2.4 to 5.0 px; the extremes come from gait shifts of the silhouette, not from true changes in speed. The mean step is 3.43 px/frame, about 82 px/s.
- **Net motion:**
  - Mask centroid, frame 0 → 59: x 355.85 → 556.51 (200.7 px); y 740.8 → 737.6.
  - Bounding-box centre, frame 0 → 59: 366 → 549 (183 px). The difference from the centroid is caused by the trunk and tail swinging.
  - The motion looks like a steady, roughly constant-speed walk. For speeds, prefer a fit or average over several frames of `cx_mask`/`cx_body` rather than single-frame differences.
- **Sizes vary with the gait:**

  | Measure | Median | Range |
  |---|---|---|
  | Bounding-box width (trunk tip to tail/rump) | 313 px | 284 (frame 18) – 348 (frame 54) |
  | Height (top of back to lowest foot) | 185 px | 176 – 191 |
  | Torso length (without trunk and tail) | 236 px | 227 – 244 |

  - A world AABB "length" prior most likely corresponds to the full width: about 313 px median, or the value in the frame the question names.
  - A "height" prior corresponds to about 185 px.
  - The apparent size does not trend over time beyond the gait swing, consistent with a fixed depth.
- **Scale:** this is a 2D scene, so use one metres-per-pixel scale taken from the prior. No metric scale is guessed here.

## Ambiguities
- Which pixel length the prior's "length" refers to: the full bounding box including the trunk and tail, or the body alone.
- Where the origin sits: the centroid is offset from the bounding-box centre by up to about 20 px.
