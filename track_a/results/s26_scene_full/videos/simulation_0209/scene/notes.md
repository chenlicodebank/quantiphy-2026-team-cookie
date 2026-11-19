# simulation_0209 – measurement record

Blender render, 3D scene, 2124x1080, 24 fps, 30 frames (t = frame/24, 0 … 1.208 s).
**Content:** a dark vintage typewriter starts at the top of the frame, falls nearly straight down onto a large
wooden desk with a green leather top, lands (≈ frame 10), rocks back and forth (frames 11-22) and is at rest from
frame 24. A revolver lying on a cream paper on the desk, to the right of where the typewriter lands, does not move.
**Camera:** static; no pan or shake (corner patches differ from frame 0 by less than 1 grey level).

## Files
- `scene.json`: inventory (typewriter, desk, revolver, paper, wall), static extents, events, camera/perspective cues.
- `tracks/typewriter.csv`: one row per frame (0-29). `cx,cy` = centroid of the mask (use this as the origin
  proxy); `bbox_cx,bbox_cy` = bbox centre; `x0,y0,x1,y1,bbox_w,bbox_h` = mask bbox; `minrect_len/wid` = min-area
  rotated rectangle of the mask (main axis length / width); `area` = mask pixels; `occluded` = 1 when cut by the
  top image edge (frames 0-1).
- `scripts/segment.py`: segmentation and track writer. `scripts/diff.py`: camera-static check and first diff.
  `scripts/static_check.py`: revolver/paper motion check. `scripts/crops.py`: crop-sheet viewer.

## Method
The background plate is frame 0, with rows < 200 taken from frame 29 (the typewriter has left them by then). Pixels
that differ from the plate by more than 22 grey levels are kept. On the desk top only, pixels that are a uniform
darkening of the plate are removed as shadow. The masks are then opened and closed, the largest component and its
neighbours are kept, and holes are filled. I checked the overlays for every frame (`frames/masks.png`, a scratch
file): the masks cover the whole typewriter, including its dark upper part against the wall.

## Reliability
- Frames 2-9 (in the air) and 24-29 (at rest): mask edges are accurate to ±2 px.
- Frames 0-1: the top is cut off by the image edge, so `cy` and `bbox_cy` are biased low (too high on screen). The
  bottom edge `y1` (108, 115) is reliable, so use `y1` for timing early in the fall.
- Frame 10 (impact): strong motion blur and a dark contact shadow, so ±8 px.
- Frames 11-23 (rocking): the mask may include a few px of contact shadow at the bottom; ±4 px.
- The centroid is the centre of the visible silhouette, not the true 3D origin. For a box-like typewriter it sits
  near the projected centre (to within ~10 px). During rotation the centroid and the bbox centre differ by up to
  ~20 px.
- Fall kinematics (bbox centre in px/frame for frames 2-9): 29.5, 39.5, 50.5, 60, 68, 77, 87. The roughly constant
  increase suggests release from rest at about frame 0. Perspective is mild: bbox_w shrinks from 303 to 293 px
  during the fall.

## Ambiguities
- The typewriter is the only moving object. The revolver region changes slightly in brightness after landing
  because of shadow and reflection from the typewriter; the revolver itself does not move (checked visually).
- The paper is partly covered by the typewriter at rest.
- Desk extents come from corners picked by eye on a grid (±10 px). The bottom of the desk is outside the image, so
  its height cannot be measured.
- Vanishing points and horizon are rough; the horizon lies above the image, so the camera looks down.
- The focal length is unknown. If depth_info is given, combine it with a known size; for example, a typewriter of
  known width W at depth Z gives f ≈ bbox_w·Z/W, using ≈ 300 px in the air or 273 px at rest (rest pose is rotated).
