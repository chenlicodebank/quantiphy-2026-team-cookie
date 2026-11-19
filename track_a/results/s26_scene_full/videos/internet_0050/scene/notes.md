# internet_0050: measurement notes

**Scene.** Real footage, 3840x2160, 30 fps, 94 frames (t = frame/30, 0 to 3.100 s), labelled 2D. The camera looks across
an outdoor basketball court. One person stands on a black electric kick-scooter and rides **right to left** along
the far baseline for the whole clip. The rider is already moving at frame 0, is still moving at frame 93, and never
stops, turns or bounces. That rider is the only moving object. Everything else is static: two basketball hoops (a
bird sits on the left backboard and only turns its head), soccer goals, an Adirondack chair, court lines, grass,
buildings and trees.

## Files
- `scene.json`: inventory with descriptions and frame-0 pixel extents of the static objects, the rider's pixel sizes, events, camera and perspective.
- `tracks/rider.csv`: one row for each of frames 0-93. Columns:
  - `cx/cy_stab`: bbox centre of the rider+scooter mask, used as the reference point.
  - `bbox_*_stab`
  - `centroid_*_stab`: mask centroid.
  - `front_wheel_x_stab`: leading edge of the front wheel. `rear_end_x_stab`: back of the rear wheel or fender.
  - `ground_y_stab`: the wheel-contact line.
  - `cam_dx/dy`: camera drift.
  - Raw image coordinates: `cx_img`, `cy_img`, `bbox_*_img`, where `*_img = *_stab + cam shift`.
  - `bbox_w`: horizontal extent, along the motion axis. `bbox_h`: cap top to wheel contact.
  - `scooter_len`: horizontal extent of the mask in the 45-px wheel band.
  - `mask_area`
  - `occluded`: always 0.
- `camera_shift.json`: per-frame shift (dx, dy) of the background relative to frame 0. It comes from phase correlation of two bands the rider never enters: buildings at y 450-850 and the court at y 1260-1600. The reported value is the mean of the two bands.
- `scripts/`:
  - `bg_shift.py`: camera shift.
  - `track_rider.py`: background model, mask and track.
  - `scooter_parts.py`: Hough circles for the wheels.
  - `check_track.py`: sanity check and overlay.
  - `validate.py`
  - `camera.py`: an early coarse version of the camera check.

## Method
Each frame is shifted into frame-0 background coordinates. A median background is built from every 2nd frame, which
leaves the rider out completely; I checked this visually. The mask is pixels whose colour differs by more than 35,
cleaned with an open and a close. It keeps the components near the largest blob, because the cap is separated from
the body by the blurred face.

The cast shadow runs as a long dark strip to the right of and below the wheels. It is removed by cutting below the
lowest pixel of the front wheel and to the right of the rear wheel. I drew mask overlays at frames 0, 20, 47, 75 and
93 and checked them: the mask covers cap to wheels and front wheel to rear fender, with no shadow.

## Values (px)
- **Rider size:**
  - Scooter length (main motion axis): median **177** (176-178). Frames 0-3 read 182 px, probably because of slight blur.
  - Rider+scooter height (cap top to ground): median **299** (296-303).
  - Person cap-to-soles: about **275**, ±5. The soles are on the deck about 24 px above the ground.
  - Wheel diameter: about **37** (Hough radius 18.3-20).
  - Wheelbase (axle to axle): about **139**.

  The apparent size stays constant, so the rider moves at constant depth parallel to the image plane. The planar
  assumption is good.
- **Motion:**
  - The bbox centre goes from x_stab 2711.5 (frame 0) to 1235 (frame 93), roughly −16 px per frame.
  - Per-frame steps are about −17 at the start, about −15.5 around frames 30-55, and about −16 at the end, so motion is nearly uniform with a slight dip mid-clip.
  - The y position is constant to within ±2.5 px.
  - Integer bbox edges make single-frame differences jitter by ±0.5-1 px. Fit or smooth over several frames for speed or acceleration.
- **Camera:** handheld with a slow, smooth drift. By frame 93 it reaches dx +12.6 and dy −7.2 px; the top and court bands agree to within about 1 px. This is under 1 % of the rider's travel. Use `*_stab` for motion relative to the ground.
- **Static objects** (frame 0, read off grid zooms, ±3-5 px):
  - Left backboard: 255x175. Right backboard: 273x185; the right hoop sits slightly nearer the camera.
  - Rims: about 100 px wide.
  - Pole bases: y 1150 (left) and 1163 (right).
  - Lane-line tops at the far baseline: x 1827 and 2193, y about 1158, so the lane is 366 px wide there. That is behind the rider's ground line (about 1177), so its scale is slightly smaller than the rider's.
  - Soccer goal: 187x137. Chair: 114x103.
- **Events:**
  - The front wheel passes the right lane-line top at frame 27 and the left one at frame 51. The bbox centre passes them at frames 33 and 56.
  - There are no start, stop, release or impact events inside the clip.

## Ambiguities
- If a question gives "scooter length", use `scooter_len` (about 177). If it gives "person height", decide between cap-to-soles (about 275) and cap-to-ground (about 299). The rider stands with slightly bent knees, so it is not a full standing height.
- Court objects lie at depths different from the rider's. Using the rider's scale for them is only approximate (the hoops are close to the rider's depth).
- Shadow, motion blur and the blurred face have only a small effect. The cap edge against a bright background is reliable to about ±2 px.
