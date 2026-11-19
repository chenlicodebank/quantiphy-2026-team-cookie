# captured_0053 – measurement record (lab video, 3D, 24 fps, 48 frames, 1280x720)

## Scene
Static, elevated camera looking down a carpeted room/corridor. The only moving object is a **blue toy/RC car**
(blue cover with white and yellow patches, dark wheels). It is already moving at frame 0 and is still moving at
frame 47. It drives away from the camera toward the upper-left (far end of the room), roughly in a straight line,
from image centre (894, 450) to (539, 225). Static props: an orange basketball by the right wall, a small white cup,
a thin white stick on the floor next to it, a white box/card near the bottom, a second white stick at the bottom edge,
a tiny yellow bit, a plate on the right wall. In the background (far end): two people (static), a table, a tripod, a
bag with a tennis ball, and orange cables.

## Files
- `scene.json` – inventory, camera, static-object extents, events, first/last car measurements.
- `tracks/blue_car.csv` – each frame 0-47: `cx,cy` = centroid of the full car mask (visible centre, which is the
  lab reference point); `bbox_cx,bbox_cy`; bbox `x0,y0,x1,y1,bbox_w,bbox_h`; `area_px`; `minrect_len/wid/angle`
  = min-area rectangle of the mask (length along the main axis / width across it, in the image); `bottom_y` = lowest
  mask pixel (ground contact); `occluded` (always 0).
- `tracks/camera_shift.csv` – phase-correlation shift of a wall patch and a floor patch relative to frame 0.
- `static_measure.json` – static-object pixel extents at frame 47 (the car is far from them in that frame).
- `scripts/` – `track_car.py` (background median + blue-hue mask, grown with background-difference pixels near the
  blob, then closed), `static_objects.py` (colour masks of the props, timestamp check, background-motion check),
  `write_scene.py`, `probe_hsv.py`.

## How measured / reliability
- Camera is **static**: shift is 0.08 px or less in every frame. Frame timestamps are uniform at 1/24 s.
- Lab convention for back-projection: fx = fy = 763 px, principal point about (640, 360). Use the given depth_info
  with the car centroid (cx, cy).
- I overlaid the car mask on frames 0, 6, ..., 42, 47 and checked them. The masks cover the whole car, including its
  white and yellow patches. Edges may be off by about 3-5 px because of motion blur, especially in early frames where
  the car moves fastest in the image, and the shadow under the car can add a few px at the bottom. An earlier,
  stricter threshold missed the shadowed left side in frame 46; the current version fixes this. Centroid jitter is
  about 1-2 px.
- The car's apparent size shrinks as it moves away. Min-rect length goes from 159 to 122 px, width from 124 to 86 px,
  and bbox width from 164 to 123 px. That is about 0.75x, so its depth grows about 1.3x over the clip. The car is seen
  obliquely from above, so its image "length" mixes its length and height, and the mask length/width are not clean
  body axes. Pixel image steps per frame fall from about 11-13 px at the start to about 5-6 px at the end; part of
  that drop is perspective.
- The image steps 11->12 and 35->36 are about twice their neighbours' and show in every bbox edge. Timestamps are
  uniform, so this is either a dropped capture frame or a real jolt. Smooth over 5 or more frames, as the reference
  does.
- Static extents come from colour thresholds. Basketball: bbox 69 x 60 px, equivalent diameter 64 px, centre
  (987, 369); the bottom is shaded, so use the width of about 68 px as its diameter. Cup: 27 x 37 px at (565, 430).
  Middle stick: 88 px long. White box/card: about 81 x 77 px at (666, 612). Bottom stick: cut by the frame edge.
- No events other than continuous driving: no start, stop, bounce or contact with other objects in the clip.
