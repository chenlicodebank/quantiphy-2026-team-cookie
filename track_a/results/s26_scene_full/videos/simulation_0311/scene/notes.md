# simulation_0311 – measurement record (pixels, seconds)

Video: 2560x1440, 24 fps, 72 frames (t = frame/24). 3D Blender render. Static camera looking steeply down onto a snowy
rural road. The only moving object is a **red sports car** (red body, black roof/glass, Ferrari LaFerrari-like). It drives
along the road away from the camera: it enters at the bottom-right behind the near wooden pole and leaves toward the upper-left.
It is still moving in the last frame.

## Files
- `scene.json`: inventory (car, poles, fences, road, trees) with pixel positions and extents, camera info, events.
- `tracks/red_car.csv`: one row per frame (0-71). Columns: frame, t, cx_mask/cy_mask (silhouette centroid), bbox_x0/y0/x1/y1,
  bbox_w/h, bbox_cx/cy, main_axis_len and width_across (silhouette extent along/across its principal axis), main_axis_angle_deg
  (image angle of the principal axis, x right, y down), area_px, occluded (`frame_edge`, `pole` or `no`).
- `scripts/`: `bg.py` (median background + camera-shift check), `track_car.py` (segmentation and track), `check01.py`
  (frame 0 vs 1 check, background grid images), `write_scene.py` (scene.json and trajectory overlay).

## Method
Median background from 13 frames. Car mask = pixels that differ from the background and are red/pink, plus changed
pixels near them that are brighter than the background (sky-reflecting roof edges), plus changed non-bluish pixels. The car's
shadow is excluded because shadow pixels are bluish or darker. The final silhouette is the convex hull of these pixels. The
hull fills in the dark roof/glass and bridges the pole when the car is behind it. I checked the overlays (frames 6, 12, 24, 30,
48, 54, 71, plus the trajectory image): the mask covers the full car.
In a zoom of frame 54 the bottom, left and right edges are within about 2 px. The top edge (dark fender/mirror on dark
asphalt) can be up to about 10 px too low, so bbox_y0 is ±10 px. Frame 52 shows a 10 px jump in y0.

## Reliability
- **Frames 29-71 (fully visible): reliable.** The centroid track is smooth (per-frame step falls from about 32 px at frame 30 to about 15 px at frame 71 as the car recedes), and bbox/extents
  are within a few px except y0 as noted.
- Frames 0-22: the car is cut by the bottom edge and split by the near pole. Frames 23-28: its rear-right part is still hidden
  by the pole. Centroids, bbox centres and extents in these frames are biased and must not be used for motion. During occlusion
  the **front-left extremes bbox_x0 and bbox_y0** are unoccluded from about frame 9 and form a smooth series that can serve as a
  substitute reference point. Frames 0-8 show only a small part of the car.
- Frames 0 and 1 are pixel-identical (max difference 9 grey levels), so the car doesn't move between them. Visible motion
  starts between frames 1 and 2.
- Reference point: the Blender vehicle root is unknown (probably ground level between the axles, which projects near the
  lower middle of the silhouette). The CSV gives both the mask centroid and the bbox centre. Displacements depend little on
  this choice, but perspective makes the centroid sit slightly high relative to the ground point.
- Apparent size (perspective cue for depth): the main-axis length shrinks from 699.5 px (frame 29) to 608 (40), 544 (50),
  492 (60) and 448.5 px (71). bbox shrinks from 652x410 to 426x232. The car is receding, and its depth grows by about 1.56x
  from frame 29 to 71 (inverse of the size ratio). The heading angle drifts from about -158° to -166° in the image, a
  perspective effect plus a possible slight curve. No sharp turns, stops, bounces or contacts.

## Camera and scene geometry
Static: phase-correlation shift of the background is under 0.02 px in every frame. There is no horizon. The verticals (poles)
converge downward, giving a vertical vanishing point at roughly (1250, 13300) px (rough, ±30%), which means a steep downward
tilt. The road runs diagonally from the bottom-right (near) to the top-left (far).
Static objects (positions and widths in scene.json):
- Near utility pole: thick, spans the full height. x 1972-2100 at the top, 1900-2002 at the bottom (width 128 to 102 px),
  metal band at y about 365. It occludes the car.
- Far-left thin pole: top (245, 0), base (313, 900), width about 34-40 px.
- Thin pole in the right fence line: (1128, 0) to (1130, 370), width about 22 px.
- Right fence (post bases listed in scene.json) and left fence.
- Snowy trees, and faint dashed centre marks near (400-700, 290-520).
Static-object positions were read from 100 px grid images and are ±5 px.

## Ambiguities
The car shadow falls next to the car on the asphalt and is excluded. Reflections make the roof look bluish/white, which is
handled by the hull. There is no motion blur problem. There are no other moving objects and no similar objects.
