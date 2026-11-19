# simulation_0239_segmented — measurement record

2D scene according to inputs.json, 24 fps, 50 frames (t = frame/24, 0 to 2.042 s), 1920x1080. Segmentation video: the original Blender
render with the background replaced by white. Units are pixels (x right, y down) and seconds. No metric scale is given.

## Files
- `scene.json`: inventory, camera, static building extents, events, gait notes.
- `tracks/horse_brown.csv`, `tracks/animal_cream.csv`: one row per frame (0-49) with columns frame, t_s, cx_px, cy_px (mask centroid = reference
  point), bbox x0/y0/x1/y1/w/h, mask_length_px / mask_width_px (extent along / across the PCA main axis), main_axis_angle_deg, area_px,
  occluded (always 0).
- `scripts/segment.py`: segmentation and tracking. Foreground = non-white (min channel < 225 or saturation > 40), then open/close. The largest
  component is the building. The other components are assigned by image row (centroid y < 825 → brown animal, otherwise cream), so the white
  muzzle tip and small detached parts are included. Writes overlays to frames/ov_XX.png.
- `scripts/static_building.py`: building row/column extents and the camera-shift check. `scripts/show.py`: prints a track.

## Objects
- **horse_brown**: dark reddish-brown quadruped, the upper animal (row ~776) just below the building, seen from above. Its head (narrow end
  with a white tip) points right. It walks right almost horizontally: cx 753.7 → 876.3 over frames 0-48 (+122.7 px), with steps of 0.6-4.8
  px/frame because of the gait. Apparent length 143-166 px (median ~148), width 36-42 px.
  **Frame 49 is a reset artifact**: the animal jumps back to cx 750.4, about where it was at frame 0. Do not treat it as motion; use frames 0-48.
- **animal_cream**: cream/beige quadruped, the lower and larger animal (row ~865), head to the right. It walks right: cx 973.7 → 1196.5 over
  frames 0-49 (+222.8 px, dy −8 px), steps 2.3-7.5 px/frame. Apparent length 163-190 px (median ~176), width 49-55 px.
- **building** (static): bbox x 619-1423, y 24-744 (805 x 721 px). Main block is ~700 px wide (x 662-1361). The middle band/eave is ~803 px
  wide (x 620-1423). The vertical corner edge is at x≈1018 and runs y 24-744.

## Camera
Static: building-region phase correlation gives shifts < 0.06 px. The view looks down on the animals (no legs visible). The animals keep a
constant image row and apparent size, so each stays at a constant depth. Because the clip is 2D, use one px→m scale from the prior object.
Ambiguity: the two animals are at different image rows and may be at slightly different depths. Nothing in the image measures that.

## Reliability and caveats
- The reference point is the mask centroid, which stands in for the animal's origin (pelvis/root). Leg, head and tail motion moves the
  centroid by ±1-2 px per frame, so per-frame speeds are noisy. Smoothing or averaging over a gait cycle (brown ~20 frames, cream ~16-17
  frames) or using net displacement is more stable. bbox x0 (rear) and x1 (nose) are also in the tracks.
- Mask edges come from compressed video: ±1-2 px. Mask length changes by up to ~±10% with the gait (stride and tail), so median length is
  the best value for "body length". Mask width is the animal's width seen from above. Height above the ground cannot be seen.
- No occlusion, contact or bounce events. Both animals are already moving at frame 0 and never change direction.
