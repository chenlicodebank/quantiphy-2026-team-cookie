# internet_0002 — measurement record (pixels and seconds only)

Video: 3840x2160, 36 frames, fps 19.612613 (t = frame / fps; frame 0 at t = 0, last frame 35 at t = 1.785 s).
It's a 2D internet clip: a near top-down (nadir) drone view of a multi-lane highway. All traffic moves left to right (+x),
along the lanes, which run horizontally. No metric scale is assumed anywhere.

## Files
- `scene.json`: the inventory (moving and static objects with descriptions, pixel sizes, the frames each is visible),
  the camera, perspective notes and events.
- `tracks/<object>.csv`: one row per frame in which the object is visible. Columns:
  - `cx_full, cy_full`: centre of the full car box. For cars cut by the image edge this is extrapolated from the known box size.
  - `cx_visible, cy_visible`: centre of the part that is inside the image.
  - `x_front, x_rear`: right (front) and left (rear) bumper x, extrapolated when off-image.
  - `bbox_x0..y1`: the visible bounding box.
  - `visible_length_px, visible_width_px`: size of the visible part.
  - `full_length_px, full_width_px`: constant car size.
  - `cut_by_frame_edge`: 1 when the car is partly outside the image. This is the only kind of occlusion; there are no
    car-on-car occlusions.
  - `visible_fraction`, `match_rms`: template-match residual (lower is better).
- `camera_shift.csv`: background shift of every frame relative to frame 0 (phase correlation on the full frame and on
  the lane dashes only, plus a frame-to-frame value).
- `static_markings.json`: every lane dash (x0, x1, y, length), the dash rows (lane dividers) and their spacing, and
  the two solid lines at the top.
- `scripts/`:
  - `camera_motion.py`
  - `background.py`: median background, saved as `bg_half.jpg`
  - `track.py`: template tracker; reference boxes are in `car_boxes.json`
  - `static.py`
  - `build_scene.py`
  - `overlay.py`, `crops.py`, `crops_enh.py`: verification images

## Camera
Static. The background drift is under 0.6 px in x and under 2 px in y over the whole clip, so no pan correction is
needed. The cars' own motion can be read straight off the image coordinates.

Perspective is near-orthographic:
- Dash lengths are 293–304 px in every row.
- Lane-divider spacing is 306–330 px.
- Car sizes stay constant along each track.

So the annotators' single planar scale applies.

## Moving objects
Sizes are bumper to bumper (along x) and side to side (along y, mirrors excluded). They were read from zoomed frames
and include the motion-blur fringe of about 10–20 px.

| name | what tells it apart | lane / y | frames | length × width px |
|---|---|---|---|---|
| red_pickup | red pickup, grey bed cover, big shadow | lane 4; centre y 1159→1312 (drifts ≈4.6 px/frame downward = slow lane change towards the divider at y≈1310) | 0–33 (sliver of tail at 34) | 532 × 180 |
| gray_sedan | blue-grey sedan, top lane, leading | y 180→168 | 0–12 | 430 × 146 |
| white_car | white sedan with dark sunroof, top lane | y 152→190 | 7–35 | 462 × 172 |
| silver_pickup | silver cab, black bed cover, lane 5 | y 1418→1465 | 20–35 | 505 × 180 |
| dark_car | dark charcoal sedan, top lane, last to enter | y 144→156 | 27–35 | 485 × 172 |

Reference point is the visible car centre, i.e. the centre of the full box (`cx_full`). For an object's pixel length,
use `full_length_px`, bumper to bumper. Lengths along the motion direction are the usual prior basis:
- **red_pickup:** best measured (±6 px).
- **gray_sedan, white_car:** ±8 px.
- **silver_pickup:** the rear sits inside its own shadow, so ±10 px.
- **dark_car:** heavy blur, ±12 px.

## Events (scene.json → events)
No starts, stops, contacts or reversals; all cars move continuously. Edge crossings (frame, interpolated):

| frame | object | event |
|---|---|---|
| 6.35 | white_car | front enters at left |
| 9.76 | gray_sedan | front reaches right edge |
| 10.28 | white_car | fully in view |
| ≈13.0 | gray_sedan | gone |
| 19.04 | silver_pickup | enters |
| 23.33 | silver_pickup | fully in view |
| 26.21 | dark_car | enters |
| 29.46 | red_pickup | front reaches right edge |
| 30.18 | dark_car | fully in view |
| ≈34.4 | red_pickup | gone |

## Static objects
- **Dash rows (lane dividers):** six rows at mean y ≈ 355, 663, 989, 1310, 1616 and 1945. Spacing between rows is
  308, 326, 321, 306 and 329 px.
- **Dashes:** mean length ≈ 297 px, thickness ≈ 10–14 px. The gap between dashes is ≈ 836–866 px and the period is
  ≈ 1140–1160 px, except one gap of 1114 px in row y≈1616.
- **Solid lines:** two white lines across the top, at y 4–36 and 42–76.
- **Top lane:** between the solid lines and the first dash row, about 280 px wide.
- **Other:** small raised pavement markers along the dividers, and oil stains at the left edge (x 80–260, y 920–950).

## Reliability / ambiguities
- **Tracks:** template matching (sub-pixel) on a static background. For fully visible frames the frame-to-frame x step
  is smooth to about ±2 px. Frames where a car is cut by the image edge are noisier, with step errors up to about
  10 px:
  - red_pickup: 29–33 (e.g. the 30→31 step is 116 vs ≈108)
  - gray_sedan: 10–12
  - white_car: 7–10
  - silver_pickup: 20–23
  - dark_car: 27–30

  Prefer fully visible frames for motion fits.
- **Shadows:** long shadows fall to the upper-left of each car (sun at lower-right). They are not part of the cars and
  were excluded from the boxes. Shadows of the red and silver pickups are large; plain background subtraction merges
  them with the car, so it was not used for sizes.
- **Motion blur:** cars move roughly 105–130 px per frame, with about 10–20 px of blur at both bumpers. The box
  includes it.
- **Similar objects:** three sedans share the top lane — gray_sedan (blue-grey, leaves at frame ≈13), then white_car,
  then dark_car (dark, enters at 26). There are two pickups: red (lane 4) and silver with a black bed (lane 5). The
  red pickup's downward y drift is real (a lane change), not camera motion.
- **Height:** not observable from this top-down view.
