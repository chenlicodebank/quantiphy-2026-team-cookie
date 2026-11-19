# simulation_0007 – measurement record

**Scene.** A 2D simulation: a static overhead (top-down) camera looks at a pond shore. The video is 1080×1080 px, 24 fps,
74 frames (t = frame/24, from 0 to 3.0417 s). The only moving object is a white wooden **rowboat** on the green
water. Static objects are a grey wooden **dock/pier**, a weathered wooden **shack** (top-left, cut off by the
frame), tan **rocks** (right bank), trees and bushes, grass bank, and water.

## Files
- `scene.json`: the inventory, camera, static extents, boat size and motion summary, and events.
- `tracks/boat.csv`: one row per frame 0-73. Columns:
  - `cx, cy`: centroid of the filled boat mask. This is the reference point and stands in for the object origin.
  - `obb_cx, obb_cy`: centre of the oriented box. It differs from the centroid by about 1 px.
  - `bbox_*`: axis-aligned box, inclusive pixel coordinates.
  - `length_px, width_px`: mask extent along and across the principal axis.
  - `axis_angle_deg`: angle of the principal axis in the image (y points down).
  - `area_px`: mask area.
  - `occluded`: always 0.
- `scripts/`:
  - `bg_and_camera.py`: camera-shift check.
  - `track_boat.py`: segmentation, tracking and overlays.
  - `static_and_motion.py`: dock extents and motion summary.
  - `probe_colors.py`: colour probing.
  - `camera_shift.json`: per-frame camera shift.

## Methods and reliability
- **Camera:** static. Phase correlation of the land area against frame 0 shows a shift of at most 0.003 px.
  No perspective cues; the view is nadir, so one metres-per-pixel scale applies on the water plane.
- **Boat segmentation:** HSV value > 100 below y = 560, minus the static dock mask. Then a 7×7 close, the
  component nearest the previous position, and outer-contour fill (so the dark seats are included). Overlays at
  frames 0, 18, 36, 54 and 73 were checked visually: the mask covers the full hull and nothing else.
  - Centroid precision is about ±0.3 px.
  - Per-frame step: mean 3.244 px, std 0.13 px (this std is segmentation noise).
- **Boat size:**
  - Width is 70.7 px across its axis, very stable.
  - Length is 209.7 px at frame 0 but drifts to 203.5 px by the end. A thin stick or rudder tip at the lower-left
    end is bright at the start and falls into tree shadow later, so the mask loses a few pixels. The hull length
    without the tip is about 204–206 px. For a "boat length" prior, ~205 px (±3) is the best value; use 209.7 px if
    the tip should count.
  - Axis-aligned bbox at frame 0: 198 × 90 px. The axis is tilted −22°, so do not confuse the bbox with
    length × width.
  - Height cannot be observed from a top-down view.
- **Boat motion:**
  - Straight line, constant velocity: linear fit vx = −3.031, vy = +1.169 px/frame (3.249 px/frame ≈ 78 px/s).
    Quadratic terms are about 0 and residual rms is ≤ 0.13 px.
  - Heading is 158.9° in image coordinates (toward the lower-left), along the boat's own long axis, with no
    rotation.
  - Net displacement from frame 0 to 73 is (−220.9, +85.3) px, length 236.8 px. Path length is 236.8 px.
  - The 3-segment rates (3.22, 3.25, 3.26 px/frame) suggest at most a very slight speed-up, within noise.
- **Dock:** at frame 0 the minAreaRect is 324.5 × 94.3 px, centred at (485.7, 518.2). The width is slightly
  overestimated because of the shadowed edge; the deck is about 85–94 px wide. Its long axis runs from the bank
  (upper-left, about (420, 380)) to the water end (about (545, 680)), roughly perpendicular to the boat axis.
- **Shack and rocks:** only approximate bounding boxes, estimated visually (±10 px).

## Events
- The boat is already moving at frame 0 and still moving at frame 73: no start or stop is observed.
- There are no contacts, collisions or direction changes. The boat passes about 60 px below the dock's end.

## Ambiguities
- Which end of the boat is the bow is unclear: both ends are pointed. The boat travels toward the lower-left end,
  which has a small protruding stick.
- Tree shadows lie across the water and darken the boat late in the clip, which affects only the tip.
- The boat's own shadow falls to its upper-right on the water and is excluded from the mask.
- No metric scale was guessed.
