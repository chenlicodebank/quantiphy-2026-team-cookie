# simulation_0021_segmented — measurement record

3D segmentation clip (Blender render with the background replaced by white), 1080x1080, 29 fps, 89 frames (t = frame/29).
All values are image pixels (x right, y down) at full resolution. No metric scale is assumed.

## Scene
Three objects on a plain white background (no ground plane, horizon or vanishing lines):
- **man** (moving): only person; dark navy jacket, grey trousers, blank white face. Walks steadily to the right
  for the whole clip (already walking at frame 0, still walking at frame 88). He is behind both props.
- **lamp_post** (static): black street lamp, bbox x 159-235, y 330-893; height 564 px, lantern 73 px wide,
  shaft ~12 px wide (axis x ≈ 193), base 33-54 px wide. Bottom at y = 893.
- **fire_hydrant** (static): white/grey rusty hydrant with chain, nozzle to the right; bbox x 63-140, y 758-892;
  height 135 px, max width 78 px (with nozzles), body 41 px, cap 48 px, base flange 62 px. Bottom at y = 892.

The camera is static: the props don't move by a single pixel, and median-background subtraction leaves nothing on them.

## Files
- `scene.json`: inventory, static extents, events, camera and perspective notes.
- `tracks/man.csv`: one row per frame (0-88). Columns:
  - `pelvis_x, pelvis_y`: the estimated pelvis, which is the reference point.
  - `head_cx, head_L, head_R, head_top_y`: head centre and head edges.
  - `feet_bottom_y`.
  - `bbox_*`: bbox of the visible mask.
  - `mask_height_px, mask_width_px, mask_area`.
  - `torso_band_x`: column centroid of the mask 40-50 % down the body.
  - `visible_centroid_x/y`.
  - `occluded`, `occluders`: bbox overlap with the hydrant or lamp, or head touching the shaft.
  - `bbox_bottom_hidden`: lowest foot hidden, so mask height is too small.
- `scene/scripts/`: run in this order: `measure.py` (median background, static components, raw man masks),
  `refine.py`, `headedges.py`, `final_track.py`, `events.py`. Each script overwrites `man.csv`, so run the whole
  chain from the start. `_median.png`, `_static.json`, `_widths.json` and `_head.npy` are intermediate files.

## Method and reliability
- **Man mask:** each frame differenced against the per-pixel median of all frames (threshold 40), then a
  morphological open/close. The overlays (frames 15, 52, 64) cover the whole visible body and nothing else.
  The parts hidden behind the props are naturally missing from the mask.
- **Pelvis x:** taken from the head centre, because the head is the cleanest part. The torso band is disturbed by
  swinging arms and by the lamp base.
  - Formula: pelvis_x = head_cx − 4.7 px. The −4.7 px offset is the median of torso band − head centre over the
    clear frames 22-45 and 75-88.
  - Frames 49-70: the lamp shaft hides part of the head. There the centre is rebuilt from the visible edge plus the
    head width (≈24-26 px): the left edge for frames 49-60, the right edge for 61-70.
  - Error: about ±1.5 px per frame (head width varies 21-26 px as the head turns). Per-frame dx of pelvis_x is
    0.5-3.5 px, mean 1.89 px/frame.
  - Path: pelvis_x goes from 85.8 (frame 0) to 252.3 (frame 88). The motion is a slightly uneven forward walk,
    a bit faster in the last ~20 frames (≈2.5 px/frame against ≈1.5-2).
  - If a question needs a smoother path, fit it to `pelvis_x`.
- **Pelvis y:** head_top_y + 0.47 × 222 px (standing-height estimate), giving ≈ 754 ± 2.
  - Vertical motion is only gait bob: head top stays at y 649-654.
  - The 0.47 fraction is an anthropometric assumption, so absolute pelvis y is uncertain by about ±10 px. Its
    changes are reliable.
- **Man's apparent size** is constant (no approach or recession):
  - mask height median 217 px, max 224 (frame 0), min 208 when feet are visible;
  - standing height ≈ 222 px (head top ~650 to ground contact ~870-873);
  - frames 12-14 have low heights because his feet are behind the hydrant (flag `bbox_bottom_hidden`);
  - mask width swings 38-116 px with the stride;
  - head width ≈ 23 px.
- **Depth cues:** the man's feet rest at y ≈ 866-873, while the props' bases are at y ≈ 892-893. He is therefore
  a little farther from the camera than the props, which is consistent with him being occluded by both.
  - The clip has no ground texture, so the camera height and tilt cannot be measured.
  - With a given depth_info, use focal length = depth × pixel size / world size, and check it against the second
    object.
  - Note that the props are nearer than the man, so their pixel sizes are not on his scale.
- **Static extents:** from the median image, thresholding min(BGR) < 215. They are accurate to about ±1 px.
  - The lantern's pointed top is at y 330.
  - The hydrant's left nozzle edge (x ≈ 63-64) and right nozzle (to x = 140) set its max width.

## Events (see scene.json)
- He moves monotonically in +x throughout. There are no starts, stops, direction changes or contacts; he only
  passes behind the props.
- Pelvis passes the hydrant's centre x at frame 12 and the lamp axis at frame 63.
- His head is behind the lamp shaft in frames 49-70 (almost fully hidden around 59-62).
- He last overlaps the hydrant's bbox at frame 57.

## Ambiguities
- **Occlusion flag:** `occluded` is a bbox-overlap test, so it is conservative. For example, frames 67-68 flag
  the hydrant only because the rear foot is near x 139.
- **Masks:** shadows are absent (the background was replaced). Motion blur is negligible. There are no similar
  objects to confuse.
