# simulation_0285 – measurement record (pixels, seconds)

2D simulation, 2560x1440, 24 fps, 72 frames (t = frame/24). Static camera. A single jet aircraft flies in a straight
horizontal line from right to left across the upper half of the image in front of a plain studio cyclorama. Its soft
shadow moves across the white floor below it. Nothing else is in the scene.

## Files
- `scene.json`: inventory, camera, extents, events.
- `tracks/jet.csv`: one row per frame (0-71). Columns:
  - `ref_x, ref_y`: the reference point (estimate of the origin).
  - `ref_source`: how the reference point was found.
  - mask `centroid_x/y`.
  - `bbox_x0,y0,x1,y1,w,h` (inclusive pixel bounds).
  - `mask_length_main_axis` / `mask_width_across` (PCA extents of the mask) and `axis_angle_deg`.
  - `height_px` (= bbox_h), `area_px`.
  - `occluded_or_truncated` (1 = cut by the image edge).
- `tracks/shadow.csv`: the same measurements for the jet's ground shadow, frames 5-61.
- `scripts/`:
  - `bg.py`: median background.
  - `segment.py`: background-difference masks; the jet is the part above y=800, the shadow the part below.
  - `finalize.py`: final tracks and the truncation-corrected centre.
  - `dupcheck.py`: frame-to-frame difference and camera-shift check.
  - `show.py`: prints a CSV.

## How measured / reliability
- **Jet masks.** Made from |frame − median background| > 22 with a morphological close. Overlays at frames 0, 12, 24,
  36, 48, 60, 66 and 71 confirm the mask covers the whole aircraft: nose probe, fins, landing gear. Edges are good to
  about ±2 px. The background is plain, so there is no occlusion; the only problem is truncation at the image edge.
- **Reference point.** Uses the bbox centre in frames 13-55, when the jet is fully visible. In the edge frames it is
  estimated:
  - frames 0-12: nose x0 + 356.2 px;
  - frames 56-71: tail x1 − 370.7 px.
  - ref_y is fixed at 417.5 in these frames.
  - The two offsets differ because of the view angle, so the estimated x is uncertain by about ±5 px.
  - The mask centroid sits about 5-17 px right of the bbox centre, because the fuselage and engines are bulkier than
    the nose. The true origin is unknown within that range.
- **Motion.**
  - Frames 0 and 1 are identical: the jet does not move between them.
  - From frame 1 on, ref_x moves left at about 36-43 px/frame.
  - The steps are about 40 px/frame in frames 2-12 and 13-25, about 42-43 px/frame in frames 26-55, and about
    40 px/frame in frames 56-71.
  - Part of this change may come from the edge-frame estimates and from perspective (the jet is nearest the camera
    axis in mid-frame). It could also be a genuinely gentle speed change; this was not determined.
  - Over the fully visible frames 13-55, ref_x goes from 2155.5 to 394.0: 1761.5 px in 42 frames, a mean of
    41.9 px/frame.
  - The vertical position is constant at 417 ± 1 px.
  - The per-frame nose (x0) steps change from about 39 to 44 px around frame 26, while the tail (x1) steps go from
    about 43 to 41 px. These are small view-angle effects. Fit the motion from ref_x yourself.
- **Jet size, as the length to use for a size prior.**
  - The horizontal nose-to-tail bbox length depends on the view angle. Values are bbox_w, inclusive.
    - It is 707 px at frame 13, falls to a minimum of 678 px around frame 27, then rises to 701 px at frame 36 and
      728 px at frame 48.
    - It reaches a maximum of 745 px at frame 55.
    - Its mean over frames 13-55 is 707.1 px.
  - Height from fin top to wheel bottom is 224 px, constant.
  - The view is slightly from below and the side, so the wingspan cannot be measured; the image shows length and
    height.
  - If a question gives the jet's length, use the bbox_w of the frame it refers to, or about 708 px on average
    (±3% ambiguity).
- **Shadow.**
  - Soft edges, threshold 14, so its extents depend on the threshold (±20 px).
  - Detections in frames 70-71 were dropped: they were a render artefact band near the bottom edge (y about
    1295-1354).
  - The shadow lies on the floor nearer the camera and moves about 70 px/frame against the jet's 42. It is at a
    different depth, so do not use it to scale the jet.
- **Camera.** Static. The background phase-correlation shift is 0.07 px or less in every frame. Black letterbox bars
  cover rows 0-80 and 1360-1440.

## Ambiguities
- The jet and its shadow are the only "objects"; a question about the plane means the jet.
- Positions in the edge frames (0-12, 56-71) are extrapolated.
- The duplicated first frame means motion starts between frames 1 and 2 (t = 0.042-0.083 s).
- There are no events besides entering and leaving the frame: no bounce, contact or direction change.
