# simulation_0130 – measurement record

**Scene.** A 2D simulation (Blender) shown from straight above: an airport apron, 1920x1080 px, 24 fps, 72 frames (t = frame/24, 0–2.958 s).
A white airliner, nose up, is towed straight up the image (toward smaller y) along the lead-in line of parking stand "01" (x ≈ 475). A small dark tug with yellow-orange trim pulls it through a white two-rail towbar.
A camouflage helicopter is parked on stand "02" on the right. It does not move and its rotor does not turn.
The camera is static: the empty centre strip changes by at most 0.16 grey levels across the clip. There is no visible perspective (the ground grid is uniform), so one px→m scale applies to the whole ground plane.

## Files
- `scene.json`: inventory, the extents of every object in px, events, camera.
- `tracks/plane.csv`: one row per frame (0–71) with these columns:
  - `ref_x, ref_y`: the bbox centre, i.e. the midpoint of the wingtips in x and the midpoint of nose and tail in y.
  - nose/tail y, the full bbox (it may extend past y = 1079), the visible bbox bottom, `length_px` and `wingspan_px`.
  - `fully_in_frame`: the whole plane is inside the image.
  - `ref_in_frame`: the reference point is inside the image.
  - `occluded`: 1 = cut off by the bottom image edge.
  - the template-match score.
- `tracks/tug.csv`: one row per frame with the body centre, the body bbox, body length/width, the y of the front prongs and the length including the prongs.
- `scripts/`:
  - `track_tm.py`: template tracking.
  - `tips.py`: zoomed crops used to read extents.
  - `write_tracks.py`: builds the tracks and overlays.
  - `write_scene.py`: checks and writes scene.json.
  - `heli.py`, `extents.py`, `bg.py`: exploratory scripts. Their automatic masks were contaminated by moving shadows and were not used for the final numbers.

## Method and reliability
- **Motion.** Plane and tug are rigid and only translate (x drift < 0.2 px, no rotation). I tracked them by sub-pixel template matching (scores 0.93–0.98). The plane template is the nose section, which stays visible in every frame. Positions are frame-71 extents shifted by the per-frame displacement. Displacements are accurate to about ±0.1–0.2 px.
- **Plane and tug move together.** Their displacements agree to within 0.2 px, so the towbar gap (≈87 px from tug rear to nose) stays constant.
- **Frames 0 and 1 are the same image.** The difference is 0.05 grey levels, i.e. render noise. Motion begins after frame 1.
- **From frame 1 to 71** the motion is a steady ≈5.247 px/frame upward: 367.3 px in total. Single-frame steps range 5.0–5.46 px, which is quantisation and tracking noise; no trend shows. No motion model is stored.
- **Plane extents at frame 71** were read at 8x zoom (±1.5 px):
  - length nose→tail 423 px (y 543–966);
  - wingspan 386.5 px (x 281–667.5, tips at y ≈ 792);
  - horizontal stabiliser span ≈143.5 px;
  - fuselage width ≈48 px.
- **The plane is cut off by the bottom edge** before frame 49; the tail enters fully by frame 49–50. For earlier frames, the full bbox and `ref_y` (which can lie below the image) are extrapolated from the rigid shift. They are reliable, but the object is not fully visible.
- **The model origin is unknown.** The bbox centre is used as the reference point. For speeds and distances travelled, any point gives the same result, because there is pure translation.
- **Tug at frame 71:**
  - dark body 48.5 x 25 px;
  - 71 px including the orange front prongs;
  - body centre at (475, 431.75).

  Accurate to about ±2 px: the edges are dark and soft against shadow. If a prior gives a "tug length", it is unclear whether the prongs are included.
- **Helicopter (static).** These were read visually and are accurate to about ±5 px:
  - fuselage nose y ≈ 205 to tail y ≈ 600 (≈395 px long), axis x ≈ 1450;
  - main rotor hub (1448, 330), tips spanning x 1285–1620 (≈335 px);
  - the blades look unequal in length (158–186 px from the hub, probably droop or tilt), so rotor diameter is ambiguous: ≈335–345 px.
- **Stand markings:**
  - "01" border at about x 145–800, y 110–505 (≈655 x 395 px);
  - "02" border at about x 1118–1775, same y;
  - accurate to ±5 px.
- **Ambiguities:**
  - Strong diagonal shadow stripes cross the apron.
  - Plane and tug cast shadows up and to the left. These shadows move with them and fooled the background-difference masks, which is why I used template tracking and visual tip reading.
  - The fuselage passes through shadow stripes, so its brightness varies.
  - There is no motion blur.
