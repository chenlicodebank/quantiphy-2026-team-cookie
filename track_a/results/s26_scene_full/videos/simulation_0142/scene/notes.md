# simulation_0142 – measurement record

2D simulation (Blender) clip, 1920x1080, 24 fps, 80 frames (t = frame/24, 0 … 3.2917 s).
A single man walks from left to right across a hall, side view, parallel to the image plane.
The camera is static. All values are in pixels and seconds; no metric scale has been assumed.

## Files
- `scene.json`: the inventory (the man plus static structures and their pixel extents), the camera, and the events.
- `tracks/man.csv`: one row per frame (0–79). Columns:
  - `pelvis_x, pelvis_y`: the reference point (pelvis estimate, see below). **Use this for positions, speeds and distances.**
  - `head_cx`: horizontal centre of the head (top 56 mask rows, widest run per row). This is the raw smooth signal.
  - `hipband_x`: the direct, noisy hip-band centre (diagnostic only).
  - `bbox_x0..y1, width_px, height_px`: the full-body bounding box (horizontal width covers stride and arms).
  - `mask_cx, mask_cy, area_px`: the mask centroid and area.
  - `head_top_x/y`: the top of the head.
  - `occluded`: 1 when the right foreground wall clips the body.
- `scripts/`: `bg.py` (median background), `camcheck.py` (camera shift), `track.py` (first pass), `track_final.py` (final track), `static.py` (background profiles), `draw_track.py` (track overlay check).

## How it was measured
- **Segmentation:** the man was segmented by difference from a median background built from 17 frames. Above the floor line (y < 798) the threshold is 12; below it the threshold is 30, because the glossy floor reflects the man. Interior holes were filled, since the dark trousers are close in colour to the dark wall. I checked overlays at frames 0, 6, 12, 24, 36, 48, 61, 74 and 79: the mask covers the full body, with feet, hands and head included.
- **Pelvis x (reference point):** I computed the hip-band centre directly, but it jitters by ±15–25 px because the hands swing across the hips and the mask has holes. Instead, pelvis_x = head_cx + offset, where the offset is −19.75 px (the median of hipband_x − head_cx over all frames, from the forward lean and face). head_cx is smooth: the per-frame step is 16–24 px (mean 18.8 px/frame). In this side-view walk the pelvis stays under the head to within a few px.
  - Expected error: about ±3 px per frame, with no drift.
  - Avoid using hipband_x for speeds.
- **Pelvis y:** pelvis_y = head_top_y + 225, about 46 % of the 492 px standing height below the head top. It follows the vertical bob of 639–658 px. This is approximate (±10 px absolute); the vertical bob amplitude is ~19 px.
- **Height:** the standing (maximum) height is 492 px, from the head top at y = 414 to the sole at y = 905, at frames 0, 25 and 74–75. Mid-stride the bbox height falls to 468–474 px: the head drops by ~19 px and the back foot lifts at frames 8–10, 33–35 and 58–60 (bbox_y1 = 899).
- **Width:** the bbox width varies from 105 to 310 px with the gait. It is the span of the legs and arms, not a body size.

## Events and gait
- **No start or stop:** the man is walking at frame 0 and still walking at frame 79. There is no release, bounce or impact.
- **Speed:** the walking speed is nearly constant (pelvis ~18.8 px/frame ≈ 451 px/s), with small per-step modulation.
- **Steps:** one step every ~12.4 frames.
  - Widest stride at frames 5, 18, 30, 43, 55 and 67.
  - Legs together at frames 11, 24, 36, 49, 61 and 73.
  - Head highest at frames 0, 12, 25, 37, 50, 62 and 74.

## Static scene (median background, fully reliable to ±2 px)
- **Back wall:** dark wood panels, x 114–1799, y 494–800 (306 px tall).
- **Floor line:** y = 800. Below it is a glossy grey tiled floor whose joints converge toward x ≈ 910 (one-point perspective of the floor). The man's soles stay at y ≈ 905 throughout, so he is at constant depth.
- **Windows:**
  - black beam at y 288–302, blue strip at y 305–322, white openings at y ≈ 340–475, sill at y 476–494;
  - mullions at x 137–177, 905–946, 1290–1323 and 1674–1715 (the outer two are slanted).
- **Two white arches** coming down from the ceiling, behind the man. Their bottom ends are at x 497–640 and x 1306–1419, ending at y ≈ 560.
- **Ceiling:** wooden vault at y 0–288.
- **Foreground white walls:** at x < 114 and x ≥ 1800.

## Ambiguities and reliability
- **Occlusion:** in frames 77–79 the right foreground wall (x ≥ 1800) hides the front hand and foot. The bbox_x1 and width values there are truncated, but the head and pelvis are unaffected.
- **Frame 0 bbox:** a few pixels of window-sill highlight next to the face may extend bbox_x1 by ~5 px (279 vs ~273).
- **Floor reflection and shadow:** these are excluded by the floor-region threshold. Bbox bottoms are accurate to ±2 px.
- **Other objects:** there are no other moving objects, animals or props. Only the man can be the subject of a size, speed or acceleration question.
- **Scale for questions:** use one m/px scale from the given prior. For example, if the man's height is given, standing height = 492 px. If his speed is given, mean pelvis speed = 18.8 px/frame.
