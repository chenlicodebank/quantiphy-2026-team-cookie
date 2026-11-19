# internet_0073: parcels on a belt conveyor at a truck loading dock (2D, internet, 25.111529 fps, 138 frames, 1280x720)

## Scene
A night-time loading dock. A long blue belt conveyor crosses the image left to right. Its top running surface is
at y~405-412 and it continues into the open rear of a truck on the right. Parcels on the belt are carried to the
**right** at a steady rate for the whole clip: no start, stop, bounce or impact is seen. In image coordinates and
with the camera drift removed, every parcel moves about 1.9-2.0 px/frame. The yellow bag at the truck end moves
about 2.1 px/frame. Three workers stand behind the belt and only their upper bodies are visible. The camera is
hand-held or drifting slowly. There are no humans or vehicles in full view.

## Files
- `scene.json`: inventory (moving and static objects with descriptions, frame-0 or frame-137 boxes and pixel
  lengths), camera summary, events and the column definitions.
- `tracks/camera.csv`: per-frame affine from ECC, with frame 0 as the template, masked to static background (the
  belt band, people and parcels are excluded). `p_cur = A p0 + t`. The file also gives the image-centre shift,
  scale, roll and a median phase-correlation shift as a cross-check. The phase-correlation dy is noisy late in the
  clip, so use the ECC values. By frame 137: centre shift (-16.8, -6.8) px, scale 0.9967, roll 0.56 deg. The drift
  is smooth, about -0.12 px/frame in x.
- `tracks/<parcel>.csv` (10 parcels): `cx_img, cy_img` is the reference point, the centre of the full rigid bbox
  in image coordinates. `bbox_*` is the full bbox, which can extend past the left image edge or behind the truck
  pillar. `visible_x0/x1/cx` is clipped to what is visible. **`cx_bg, cy_bg`** is the same reference point mapped
  into frame-0 background coordinates, with the camera drift removed. Use these for motion, as the annotators
  measured against the background. `left_edge_bg/right_edge_bg` are the bbox ends in background coordinates.
  `length_px` is the extent along the belt (the motion direction, i.e. the "pixel length" of the object).
  `height_px` is the vertical extent. The files also have `ncc` (match score), `visible_frac` and `occluded`.
- `tracks/person_*.csv` (3 workers): coarse centre and box of the visible upper body, in image and background
  coordinates.
- `scripts/`: `camera_shift.py`, `track_parcels.py`, `track_people.py`, `events.py` (+`events_out.json`) and
  `compare.py`, which is a consistency check of the parcels' displacements. There are also viewers: `zoom.py`,
  `tiles.py`, `overlay.py` and `show.py`.

## How it was measured
- Parcel boxes were read by hand from 4x zoomed crops with a 10-px grid. Most were read at frame 0;
  brown_box and pink_pouch were read at frame 137. The reading accuracy is about ±1-2 px per edge.
- Parcel tracking used a fixed colour template from that frame and NCC. Each step was limited to -1..+5 px in x
  and ±4 px in y, with a sub-pixel parabolic peak.
- Template columns outside the image or behind the truck door pillar (x≈1205 at frame 0, moved with the camera)
  were left out of the match.
- A parcel's track ends when it is less than 30% visible or when NCC is below 0.5.
- The boxes are rigid templates, so `length_px` and `height_px` are constant per object (all parcels are rigid
  boxes or soft bags that keep their shape).
- I drew overlays at frames 0, 20, 22, 30, 45, 58, 60, 70, 80, 85, 90, 95, 105, 110, 118, 125, 126 and 137 and
  checked them. The boxes sit on the right objects and cover their full extent.
- Consistency check: over frames 30-120, the parcels' background-x displacement is 1.93-2.01 px/frame. They all
  ride the same belt, so a spread of about ±2% is the tracking error level. Frame-to-frame steps are noisy
  (±0.5-1 px), so difference over several frames.

## Pixel lengths along the motion direction (most likely prior objects)
| object | length_px | height_px |
|---|---|---|
| white_pouch_left | 86 | 29 |
| white_box | 89 | 44 |
| grey_pouch | 85 | 40 |
| flat_white_pouch | 82 | 20 |
| red_parcel | 93 | 48 |
| cardboard_box | 104 | 34 |
| blue_bag | 132 | 48 |
| yellow_bag | 173 | 121 |
| brown_box | 80 | 40 |
| pink_pouch | 113 | 47 |

These are 2D image extents, so the apparent length includes a little of the parcel's depth face; there is no
perspective correction. The camera scale changes by only 0.3% over the clip, so the sizes are effectively
constant in time.

## Reliability and ambiguity
- **Most reliable:** white_pouch_left, white_box, cardboard_box, red_parcel and flat_white_pouch. They are fully
  visible in frames 0-137 with NCC ≥ 0.6-0.8.
- **grey_pouch:** its left tail is tucked behind white_box, so its left end is uncertain by a few px.
- **blue_bag and yellow_bag:** these are soft and deform, and their outlines are fuzzy (±3-5 px).
- **yellow_bag occlusion:** it is fully visible only in frames 0-56. After that it slides behind the
  red-orange truck door pillar (x~1205-1232) and its track stops at frame 113.
- **Two yellow bags:** do not confuse the moving yellow_bag with the **static yellow bag inside the truck**
  (x~1095-1222, y~287-392). Late in the clip they overlap in the image.
- **brown_box and pink_pouch enter at the left edge.**
  - brown_box: right edge appears at about frame 16; fully visible from frame 58.
  - pink_pouch: right edge appears at about frame 74; fully visible only at frame 137, with its left end at
    x≈1.
  - While they are partly visible, positions come from the visible part of the template and are less accurate,
    especially cy.
- **People:**
  - Only the upper bodies of the workers show; they are partly hidden by the belt and parcels.
  - The boxes are a constant size and moved with an upper-body template, so they do not follow bending or
    turning. Their heights are visible heights, not full body heights.
  - The striped-shirt worker comes out from behind the dark-shirt worker at about frame 111–117. They are tracked
    over frames 113–137 and move about 50 px to the left.
  - The white-shirt and dark-shirt workers stay roughly in place.
- **Lighting:** it is a night scene with strong lights at the top left. There is mild motion blur on the
  parcels and no shadows of note.
- **Camera drift:** the camera drifts (about 17 px over the clip). Image-coordinate positions underestimate
  rightward parcel motion by about 0.12 px/frame (about 6%). Use the `*_bg` columns.
