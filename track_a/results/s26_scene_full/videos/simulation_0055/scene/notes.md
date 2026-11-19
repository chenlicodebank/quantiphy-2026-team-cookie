# simulation_0055 – measurement record (pixels, seconds)

3D Blender render, 1080x1080, 30 fps, 78 frames (t = frame/30). **Static camera** (no pan/shake: lamp post,
hydrant and windows sit on the same pixels in frames 0 and 77). Side-on view of a wet street: white brick building
with 4 windows and a teal graffiti tag, road with a dashed centre line (y~775), near sidewalk with a black lamp post
and a white fire hydrant. Two moving objects:
- **car**: orange sports sedan, drives **left → right** in the near lane, enters at frame 21 and **slows down**
  the whole time (centre step ~29-30 px/frame around frames 22-26 down to ~8 px/frame at frame 77). It is still moving
  at the end; it never stops.
- **man**: pedestrian (navy jacket, grey trousers, black beanie) walking **right → left** on the near sidewalk the
  whole clip, ~3-4.5 px/frame. He is nearer to the camera than the lamp post, the hydrant and the car, and walks in front of
  the car from frame 52.

## Files
- `scene.json` – inventory (all objects, static pixel extents), events, camera/perspective cues.
- `tracks/car.csv` – frames 21-77: `centre_x, centre_y` (reference point), `rear_x, front_x` (full extent even where
  off-screen or hidden, = centre ± L/2), `rear_edge_meas / front_edge_meas` (the edge actually measured that frame),
  clipped `bbox_*`, `length_px` (739.7, constant), `height_px` (219), `ground_y` (865), `source`, `occluded`, `note`.
- `tracks/man.csv` – frames 0-77: `pelvis_x, pelvis_y` (reference point), `head_cx, head_x0, head_x1, head_top_y`,
  `feet_y` (lowest shoe-sole row), `bbox_*`, `height_px` (head top → sole), `width_px`, `torso_cx`, `hip_band_cx`
  (raw), `occluded`, `note`.
- `tracks/car_template_match.csv` – superseded, do not use (see below).
- `bg.png` clean background plate (frame 0 with x≥975 taken from frame 50); `occluders_mask.png` lamp+hydrant.
- `scripts/`: `bg.py` (plate), `statics.py` (occluder mask), `track2.py` (man + template car), `car_edges.py`
  (final car track; run after track2.py), `verify.py` (overlay sheet), `crop.py/look.py/vprof.py/probe.py/check_front.py`
  (viewing/diagnostics), `track.py` (first attempt, superseded).

## How measured / reliability
**Car** (`car_edges.py`): mask = |frame − bg| > 60 (BGR sum) in rows 600-865 (above the near curb, so the orange
reflection on the wet sidewalk is excluded). The rear and front edges are where the per-column mask count crosses
30/50/70/90 px, averaged, with sub-pixel interpolation. The rear edge is clear from frame 49 on, and the front edge
from 21 to 50 (after that it is behind the lamp post, hydrant and man, then past the right edge). Length L = 739.7 px
is the mean of front − rear at frames 49 (740.2) and 50 (739.2), the only frames with both edges clear. centre_x =
rear + L/2 (frames ≥ 51), front − L/2 (≤ 48), and the mean of both at 49-50. The car's image height is constant
(219 px, rows 647-865), so it moves parallel to the image plane at constant depth. Per-frame steps are smooth to about
±0.5-1 px from frame ~28. Frames 21-27 are less reliable (only the blurred nose is visible) and 21-22 are low
reliability. Motion blur is visible (front/rear edges smeared over ~10-15 px at the higher speeds). Because the blur is
roughly symmetric and the same edge is used throughout, this biases the edges by a few px but barely affects steps.
Template matching of the car body (`car_template_match.csv`) was rejected: the sliding specular reflections on the
glossy paint biased it by up to 25 px.
Vehicle root: presumably on the ground under the car centre. Horizontally it is centre_x. Vertically the ground
contact is y≈865 (centre_y 756 is the bbox middle). Only horizontal motion is visible.

**Man** (`track2.py`): diff to a background plate in which the car (frame-50 appearance plus its ground reflection,
shifted to the car's position) is pasted, so he is segmented also while in front of the car. The head (rows 540-640,
always above the car roof) is never occluded. When the head is cut by the right edge (frames 0-5), head_cx = head_x0 +
25 (head width 51 px). **pelvis_x = head_cx + 3 px**, where 3 px is the median torso-centre minus head-centre offset
over 33 clean frames. This is smooth and preferred over the raw `torso_cx`, which is broken by the car from frame 58.
pelvis_y = feet_y − 0.53·height is an estimate (no visible hip landmark), ≈ y 754-770. feet_y = lowest row with
near-black shoe pixels (V<35); wet-ground shoe reflections are V 55-90 and were excluded (checked on profiles). Noise
is about ±5 px, so height_px (361-380, median 370) carries that noise plus real gait bob (head top 573-580). Rest
standing height is best taken as about the upper values (~375-380 px) or the median (370). bbox x-extents/width are
good in frames 18-24 and 31-51. In 0-17 and 25-30 the trailing foot is cut by the right edge. In 52-77 (in front of the
car) bbox_x0/width are unreliable (car residue, up to ~100 px too wide on the left), so use head/pelvis/feet there.

**Static objects** were read off 2.5x/1.5x zoomed crops of frame 0, ±2 px: lamp post 777 px tall (y 121-898, lantern
111 px wide, upper shaft 16 px, lower column 45 px, base 73 px, axis x 813.5). Hydrant 188 px tall (y 708-896, body
56 px, base 84 px, 115 px incl. side nozzles, centre x 943). Windows 80-82 × 132/142 px. Graffiti 210 × 127 px.

## Perspective / 3D notes
No visible pitch/roll (verticals vertical, street lines horizontal), so the image plane is roughly parallel to the
street. Both movers keep constant apparent size, so they are at constant depth. The car (road, ground y 865) is farther
than the lamp/hydrant (ground y ~897) and the man (ground y ~945). If the horizon is at y≈540 (level camera, assumed),
depth ∝ 1/(y_ground − 540), which makes car depth ≈ 1.25× man depth. Questions mixing the car and the man therefore
need separate px→m scales (use depth_info/focal length). The focal length is unknown and must be estimated from the
given priors.

## Ambiguities
Wet ground gives strong reflections of the car and the man (excluded from all extents). The man occludes the
hydrant (frames ~0-40) and the car (52-77). The lamp post occludes the car front from 51, and the hydrant from ~56.
There is only one car and one person, so there are no look-alike movers.
