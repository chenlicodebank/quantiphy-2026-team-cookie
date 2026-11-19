# simulation_0275 – measurement record

**Scene.** A 2D simulation (Blender render), 2560x1440 px, 24 fps, 72 frames (3.0 s). There is one object: a grey
raccoon with a ringed tail and a pale face. It runs in profile from left to right across a plain grey studio
cyclorama. The floor has no markings, and there are no other objects or props. The camera is static: phase
correlation of the top strip shifted less than 0.25 px. All values are in pixels and seconds. No metric scale is
assumed: use the question's prior to get a metres-per-pixel scale (2D video, so one planar scale).

## Files
- `scene.json`: inventory, camera, background lines, extent and motion summaries, events.
- `tracks/raccoon.csv`: one row per frame (0–71). Columns:
  - `frame`, `t` (= frame/24)
  - `cx_bbox, cy_bbox`: bbox centre
  - `cx_mask, cy_mask`: silhouette centroid. **This is the recommended reference point.**
  - `x0,y0,x1,y1`: bbox, inclusive pixels. x1 = nose tip, x0 = tail tip.
  - `bbox_w, bbox_h`, `area` (mask pixels)
  - `axis_len, axis_wid, axis_angle_deg`: PCA main-axis extents of the mask
  - `shadow_top_y`: ground contact line found in that frame
  - `tailbase_x_approx, body_len_no_tail_px, tail_len_px`: rough tail/body split
  - `occluded`: always 0
- `scripts/`:
  - `bg.py`: median background of rows 500–1099 over all frames
  - `track.py`: segmentation, CSV and overlays. Run with argument 7, the threshold used.
  - `summary.py`: per-frame steps and fits
  - `static_and_plot.py`: floor line, camera check, overview image
  - `probe.py`: pixel probing

## Method
- **Segmentation.** Absolute difference between the Gaussian-blurred grey frame and the median background, threshold
  7 grey levels. Then morphological open/close, keeping the largest component plus nearby pieces.
- **Snout.** The pale snout differs from the background by only about 10–15 levels. The threshold of 7 was chosen so
  that it is included.
- **Contact shadow.** A thin very dark line at y≈865–869 is removed: rows at y ≥ 855 with more than 60 mask pixels
  are dropped. A side effect is that toes standing on the ground lose about 1–4 px at the bottom, so y1 ≈ 864 means
  the feet are down.
- **Visual check.** Overlays were drawn every 6 frames, and a full-track overview image was made. Both were inspected:
  the mask covers the whole animal (tail tip to nose, ears, legs) and excludes the shadow.

## Results
- **Motion.** The raccoon runs steadily in the +x direction. The centroid moves 22.59 px/frame on average between
  frames 1 and 71: net 1581.2 px, from 711.94 to 2293.12. Per-frame steps range from 20.1 to 25.2 px, with a gait
  wobble of ±2.5 px.
- **Acceleration.** The quadratic term of a fit is 0.0014 px/frame², which is negligible, so the speed is
  essentially constant.
- **Vertical bob.** The centroid y moves between about 781 and 795 with the gait.
- **Duplicate first frame.** Frames 0 and 1 are identical, so motion starts after frame 1. The one-frame backward
  difference at frame 1 is 0; from frame 2 on it is about 22–24 px.
- **Gait cycle.** The stride period is about 15.3 frames (about 0.64 s). bbox_h peaks at 143 px (tail raised) at
  frames 0–1, 16–17, 32, 47 and 62–63.
- **Size.**
  - Nose-to-tail-tip length (bbox_w): median 328 px, range 310–333. It is shortest (about 316) when the body is
    compressed, at frames 7, 23, 38, 53–54 and 69–70.
  - Height (bbox_h, top of back/ears/tail to feet): median 124 px, range 116–143.
  - Body without tail: about 210 px. Tail: about 115 px. Both are rough, ±25 px.
- **Static features.**
  - Ground contact line: y = 865, horizontal.
  - Soft wall/floor lighting transition: y ≈ 859. This is not a true horizon.
  - The raccoon's apparent size stays constant, so all motion is in one plane facing the camera.

## Reliability and ambiguities
- Mask extents: about ±2 px. The faint pale snout tip and shadow-trimmed toes are the main error sources.
- Centroid: about ±1 px per frame.
- The Blender rig origin (root or pelvis) cannot be seen. The mask centroid sits roughly at the torso/hip centre
  (about 15 px ahead of the bbox centre, because the tail is thin). Its horizontal motion matches any body-fixed
  point to within the gait wobble.
- For speeds, use cx_mask differences, or for less wobble, a linear fit over many frames.
- For "length of the raccoon" questions, bbox_w includes the tail. If a size prior refers to body length without the
  tail, use the rough body_len value (about 210 px) and expect larger uncertainty.
- There is no occlusion, no other animal and no notable motion blur.
