# simulation_0054 — measurement record

2D simulation (Blender), 1080x1080, 30.003 fps, 100 frames. Frames 91–99 are completely black (the render ends), so content covers frames 0–90 (t = 0–3.000 s). The view looks straight down on a vertical two-lane road and the camera is **static**. Every object on the road is in one plane, so a single px→metre scale from the given prior applies to all of them. All values are in pixels and frames; t = frame/30.003.

## Files
- `scene.json`: inventory (moving and static objects), sizes, events and camera.
- `tracks/orange_car.csv`, `tracks/black_car.csv`: one row per visible frame. Columns:
  - frame, time
  - `cx_bbox,cy_bbox`: bbox centre
  - `cx_mask,cy_mask`: mask centroid
  - bbox `x0,y0,x1,y1`
  - `len_px` / `wid_px`: min-area-rect length along the travel axis and width across it
  - `area`
  - `truncated_by_frame_edge`
  - `occluded`: always 0
  - **`cx_est,cy_est`**: best estimate of the origin/centre. In full view this is the bbox centre. When a car is cut by the frame edge it is the visible edge ± L/2, where L is the median full-view length. `cy_est_src` says which was used.
- `bg.png`: median background, with the cars removed.
- `scripts/`:
  - `bg.py`: background
  - `track.py`: segmentation and tracks, with overlays in `frames/chk_*.png`
  - `post.py`: cy_est
  - `static.py`: lines and lamps
  - `check.py`: sanity fits
  - `show.py`, `montage.py`: helpers

## Method
- Mask = |frame − median background| > 40 in any channel, followed by open 5×5, close 15×15 and hole filling.
- The largest component in the left half (x<570) is the orange car; the largest in the right half is the black car.
- I drew the overlays on frames 5–90 and checked them. The masks cover each whole car body, including mirrors, and do not include shadows; the renders have essentially no visible cast shadow.

## Objects
- **orange_car**: orange sports car with a grey cabin, in the left lane (x≈347–358). It drives down the image (+y) with its front at the bottom.
  - Visible frames 0–90; partly cut by the top edge in frames 0–15.
  - Length 293 px (291–295 when slow). Width ≈124 px including mirrors (117–127).
  - It **decelerates smoothly the whole time**: about 17 px/frame at f≤20 down to 3.5 px/frame at f88–90.
  - As a check only, a quadratic fit over f16–90 gives roughly constant deceleration of about 0.18 px/frame². The car has not stopped by the last frame.
- **black_car**: black car with white light strips, in the right lane (x≈675). It drives down the image.
  - Enters at the top at frame 24, is fully in view frames 37–70, leaves at the bottom (last visible frame 84).
  - Length 292 px, width 121 px.
  - **Constant speed** of 22.41 px/frame (≈672 px/s; std of the per-frame step is 0.5 px).
  - It overtakes the orange car (centres level) at frame 63 (t≈2.10 s).
- **Static objects**:
  - Road asphalt runs from x 297 to 845 (548 px).
  - White lines at x≈339, 570 (centre) and 802, so each lane is ≈231 px wide.
  - Curbs at x 280–297 and 845–862. Sidewalks of wet paving slabs on both sides; grass at the far left.
  - Two black lamp posts on the left sidewalk. Their hexagonal heads (≈36 px) are at (194,450) and (194,980). They are 530 px apart along y.
  - A small white globe and an orange-white item sit next to the lower lamp at about (240,950–965).
  - Dark asphalt patches (positions in scene.json), and a brown object at the top-left edge.
  - Positions of the patches and props were read off the image by eye (±5–10 px).

## Reliability and ambiguities
- **Full-view centres**: the positions in full-view frames are good to about ±1 px. Per-frame differences jitter by about ±0.5–1 px (bbox quantisation, mirrors entering or leaving the mask). For speeds, use differences over several frames or a fit.
- **Truncated frames** (orange f0–15, black f24–36 and f71–84) are less reliable, roughly ±3 px per frame. Motion blur at the cut edge makes the per-frame steps alternate there (16/21, 14/27).
- **Motion blur on the orange car**: it lengthens the orange car's mask to 303–306 px in frames 16–24 (fast). Use 293 px (slow frames) as its true length. The black car's length stays at 292 px even at 22 px/frame.
- **Reference point**: the car origin is taken as the centre of its top-view bounding box. A rig root at an axle would shift positions by a constant along y but would not change speeds or differences.
- **No contact or other events**: there is no contact, bounce, lane change or reversal. The only events are entries and exits, the overtake, and the orange car's continuous deceleration.
