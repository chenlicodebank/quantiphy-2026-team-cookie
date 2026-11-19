# simulation_0102_segmented: measurement record

This is a 2D segmentation clip: the original simulation with its background replaced by plain white (RGB 255).
Frame rate 24 fps, 73 frames (t = frame/24, from 0 to 3.0 s), 1920x1080. All values are pixels (x to the right,
y downward) and seconds. No metric scale is assumed.

## Contents of the scene
- **boat**: a red and white fishing boat with "AH805" on the bow. The upper hull is red, the lower hull dark
  purple/navy, and there is a white wheelhouse with a mast. Side view, bow pointing **right**, in the upper part of
  the frame. It moves to the right.
- **shark**: a blue-grey shark with a white belly. Side view, head pointing **left**, in the lower part of the frame
  (y about 852 to 957), below the boat. It swims to the left.
- No static objects, ground, horizon or markings. Camera is static: the background is featureless, and both objects
  keep a constant y and a constant pixel size, so there is no sign of zoom or shake.

## Files
- `scene.json`: inventory, sizes, events, reference-point conventions, camera.
- `tracks/boat.csv`, `tracks/shark.csv`: one row per frame (0 to 72), with these columns:
  - `ref_x, ref_y`: origin proxy. `ref_source` says how it was obtained.
  - `bbox_*`: mask bounding box. `bbox_cx/cy` is its centre.
  - `mask_cx/cy`: mask centroid.
  - `length_px` (x extent) and `height_px` (y extent).
  - `mask_area_px`.
  - `template_dx/dy/score`: rigid template displacement relative to frame 0.
  - `clipped_by_frame_edge`.
  - `occluded`: always 0, because the objects never overlap.
  - `ref_dx_from_prev_px`: one-frame backward difference of `ref_x`.
- `scripts/`:
  - `measure.py`: first pass.
  - `check_bg.py`: background and threshold check.
  - `tracks.py`: final masks, template matching and CSVs.
  - `finalize.py`: shark tail anchor, dx column and scene.json.

## Method
- Mask: min(R,G,B) < 250, 3x3 opening, keep connected components of at least 30 px.
- Rows 0 to 739 are assigned to the boat and rows 740 to 1079 to the shark. The two objects never overlap.
- Masks were drawn over the frames and checked by eye. They cover the whole object, including the shark's pale nose
  and the boat's thin mast and railings.
- Reference point while the object is fully inside the frame: centre of the bounding box (the world AABB centre ≈
  rigid origin for a 2D side view).
- Reference point after the object is clipped by a frame edge:
  - **boat** (frames 48 to 72): sub-pixel position of the rigid hull/stern template (a frame-0 crop) plus the median
    offset to the bbox centre. Accurate to about ±1 px, because the boat is rigid and only translates.
  - **shark** (frames 59 to 72): tail-tip x1 minus 139.5 px, the median half-length. Accurate to about ±3 px,
    because the tail flaps.
- While fully visible, the shark's template match is also given, but its score falls to about 0.86 because the body
  bends. Bbox centre and template give consistent displacements.

## Sizes (px, median over frames where the object is fully in frame)
- **boat**: length 858.5 px, stern to bow tip (range 856 to 863).
  - The visible height is 646 px, but the **mast top is cut off by the top image edge in every frame** (bbox
    y0 = 0). The true height is therefore unknown (at least 646 px), and `ref_y` / `bbox_cy` are biased upward.
  - Frame 0 parts: hull spans x 229 to 1088; keel bottom y = 643; wheelhouse x 640 to 820, roof y ≈ 237; mast at
    x ≈ 712.
- **shark**: nose-to-tail length 280 px (range 278 to 286; the tail beat changes it by a few px). Height from dorsal
  fin to pectoral fin is 105 px (range 103 to 107).

## Events
- Frames 0 to 1: both objects are at rest.
- Frame 2 (t = 0.083 s): both start moving. The boat moves right at a nearly constant ~17.9 px/frame. The shark
  moves left, speeding up steadily from ~7.5 to 8 px/frame to ~15 to 16 px/frame by frames 55 to 60.
- Frame 48 (t = 2.0 s): the boat's bow reaches the right edge.
- Frame 59 (t = 2.458 s): the shark's nose reaches the left edge.
- Frame 70: the mast leaves the frame.
- Frame 72: about half of the boat is visible; only the shark's tail is visible.
- Neither object changes direction, and there are no contacts.

## Reliability and ambiguities
- Bbox centres have about ±1 px jitter from anti-aliasing and compression, so one-frame differences are noisy by
  about ±1 to 2 px/frame. Fit over several frames, or use `template_dx` for the boat (smoother).
- For the shark, the flapping tail adds ±2 to 4 px jitter to the bbox centre and to its x1. The nose (`bbox_x0`) is
  steadier while it is in frame (frames 0 to 58).
- Vertical motion of both objects is negligible (within ±1 px).
- For a 2D question, use one metres-per-pixel scale from the prior object. For example, boat length ↔ 858.5 px,
  shark length ↔ 280 px, or the prior object's pixel speed. If the prior is a height, note that the boat height is
  clipped.
