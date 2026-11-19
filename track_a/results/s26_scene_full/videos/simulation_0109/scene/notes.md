# simulation_0109: measurement record (pixels and seconds only)

Clip: 1080x1080, 72 frames, fps 24.008 (t = frame/24.008). Blender render, 3D scene.

## Contents
- Two **red spheres**, the same size and colour, on a plain light-grey backdrop (RGB about 204).
  - `sphere_left`: starts on the left at (523, 818) px in frame 0. Moves up and to the left, ending around x 336.
  - `sphere_right`: starts on the right at (653, 815) px. Moves almost straight up (x drifts only from 653 to 662).
  - Both are already moving at frame 0, rising the whole time, and leave through the top edge at the end.
- Nothing else is in the scene: no ground, props, markings or visible shadows. The `backdrop` is the only static "object".

## Files
- `scene.json`: inventory, camera, events, a per-frame list of the centre-to-centre pixel separation, and summary numbers.
- `tracks/sphere_left.csv`, `tracks/sphere_right.csv`: one row for each of frames 0–71. Columns:
  - `ref_x, ref_y`: the reference point. This is the centre of a least-squares circle fitted to the mask contour, skipping contour points on the image border. It equals the projected sphere centre, which is the object origin.
  - `centroid_x/y`: mask centroid. This is wrong once a sphere is clipped.
  - `bbox_x0..y1`: bounding box.
  - `circle_diam`: apparent diameter in px. Use this for size and depth.
  - `circle_fit_rms`: residual of the circle fit.
  - `mask_length`/`mask_width`: PCA extents of the mask.
  - `mask_height`, `mask_area`.
  - `clipped_by_frame` and `occluded`: equal to 1 when the sphere touches the image border.
- `scripts/`:
  - `track.py`: segmentation (R−G>60 and R−B>60, then a 3x3 opening), connected components, and the circle fit.
  - `check.py`: draws the overlays and measures background and halo values.
  - `enhance.py`: contrast stretch used to look for ground and shadow cues.
  - `write_scene.py`: builds `scene.json`.

## Key numbers (px)
- **Apparent diameter**:
  - Left sphere: 118.9 at frame 0, 107.5 at f36, 101.5 at f63.
  - Right sphere: 119.7 at frame 0, 106.8 at f36, 100.2 at f62.
  - Both shrink smoothly, so both spheres move away from the camera while they rise. The two spheres look almost the same size at every frame.
- **Image-plane step**: about 14.5 px/frame at the start, falling to about 10 px/frame at the end. Part of this drop is perspective, because the spheres are receding.
- **Centre separation**: 130 px at f0, 157 at f8, 182 at f16, 228 at f32, 271.7 at f48 and 312 at f64. It increases steadily.
- **Surface gap at f0**: about 11 px. The spheres never touch and do not collide.

## Events
- Frame 0: both spheres are already moving upward. The start of motion is not visible.
- Frames 0–5: a faint pink glow fades out.
- Frame 31 (t = 1.291 s): a pink glow (halo) switches on abruptly around both spheres. This is only a render or material effect: the trajectory does not change at that frame and the mask threshold ignores the halo.
- Leaving through the top edge:
  - The right sphere starts touching the top edge at frame 63 (t = 2.624 s), the left one at frame 64 (2.666 s).
  - By frame 71 only a sliver of each sphere remains visible.
- There are no bounces, impacts or direction changes. Both paths are smooth and almost straight in the image.

## Camera and perspective
- The camera is static: background corners stay at 204.0 in every frame. There is no texture, so no background-shift measurement is possible.
- There are no usable perspective cues: no horizon, ground plane, vanishing points or shadows. The enhanced frames only show noise below one grey level in rows 900–1080 and faint speckle below the spheres.
- Use depth_info together with `circle_diam` for scale. The focal length follows from f ≈ diam_px·Z/D for a sphere of true diameter D at centre distance Z. For a pixel ray, assume the principal point is (540, 540).

## Reliability
- Frames 0–62: the circle fit is about ±0.3 px for the centre and about ±1 px for the diameter (fit residual ≈1.1–1.3 px rms). Masks were checked visually on overlays at f0, 24, 48 and 66, and fit the sphere outline.
- Frames 63–71 (clipped):
  - The centre comes from the visible lower arc only, so the error grows to a few px.
  - By f68–71, ref_y is negative (the centre is above the frame) and the diameters drift (96–102 px), so these frames are less reliable.
  - The bbox, centroid and mask extents describe only the visible part.
- Ambiguity: the two spheres look identical, so tell them apart by their left/right position. Their x ranges never cross: the left sphere is always left of the right one.
