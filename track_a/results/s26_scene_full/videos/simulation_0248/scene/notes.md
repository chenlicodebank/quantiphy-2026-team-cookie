# simulation_0248 — measurement record (pixels, seconds)

Video: 1920x1080, 24 fps, 50 frames (t = frame/24; last frame 49 = 2.042 s). Simulation (Blender), labelled **2D**.
Camera is **static** (background differs by < 0.13 grey levels between frames: no pan, no shake). Side view of a grey
studio (seamless wall and floor, bright floor band brightest at y ~638-640). All motion is rightwards (+x), parallel to the image x axis.

## Objects
| name | what tells it apart | moves | visible |
|---|---|---|---|
| horse_red | smaller chestnut/red-brown horse with dark mane and tail and white hind socks; leftmost | yes | 0-49 |
| horse_dun | larger light-brown (dun/buckskin) horse with black legs, mane and tail; middle | yes | 0-49 |
| rabbit | small orange-brown rabbit just ahead of the dun horse's front hooves, on the floor | yes | 0-49 |
| floor_backdrop | grey studio floor and wall, static | no | all |

Both horses have an **untextured, flat-grey face** (looks like a grey mask on the head). It is low-contrast, but it is
included in the masks (the snout tip is the front end of each horse's length).

## Files
- `scene.json`: inventory, camera, events, pixel summary (median/min/max length and height, ground rows, net x displacements).
- `tracks/<name>.csv`, one row per frame (50 each): `frame,time`; `cx_bbox,cy_bbox` = bbox centre; `cx_centroid,cy_centroid` =
  mask centroid; `cx_torso,cy_torso` = centroid of the mask rows between 25% and 60% of the height (the torso band, which follows
  the root more smoothly than the full centroid, because the full centroid wobbles with leg swing); `x_min,x_max,y_min,y_max` = mask bbox
  (inclusive px); `length_px` = x extent (nose/tail-tip to rear, the main axis); `height_px` = y extent (ear tip to hoof);
  `area_px`; `occluded` (always 0: the animals never overlap).
  Width (depth across the body) cannot be seen in this side view.
- `scripts/`: `bg.py` (per-row polynomial background), `bg2.py` (temporal-median background over the frames where each pixel is clear, row-wise
  interpolation for pixels that are never clear), `track.py` (segmentation and tracking; pass frame numbers to write overlays to frames/),
  `static.py`, `summarize.py`, `write_scene.py`, plus viewers `maskview.py` and `headview.py`. To reproduce, run bg.py, then bg2.py, then track.py, then write_scene.py.
  The background .npy files were deleted to keep the record small; bg.py and bg2.py regenerate them.

## Method
Mask = |grey − background| > 10 or chroma > 8, then a 5x5 opening, then an 11x1 vertical opening. The vertical opening removes the thin
contact-shadow strip on the floor, which otherwise joins the rabbit to the dun horse. The rabbit is the small, low component
(top below y 580, height < 60). For the horses, a weak threshold of |d| > 4 within 30 px of the body (excluding the bottom 12 rows)
adds back the grey face. Overlays at frames 0, 10, 20, 25, 33, 45, 48 and 49 were checked by eye: each mask covers the whole animal
and no shadow.

## Key numbers (px)
- horse_red (frames 0-48): length median 194 (182-216, varies with gait), height median 170 (165-174), hooves at y ~630.
  Torso x goes from 646.9 to 801.3 (+154 px in 48 frames).
- horse_dun: length median 229 (218-243), height median 183 (178-188), hooves at y ~634. Torso x goes from 900.1 to 1190.9 (+291 px in 49 frames).
- rabbit: length median 44 (42-53), height median 37 (31-42), feet at y ~636-639. Centroid x goes from 1030 to 1337 (+307 px).
  It moves in a crouch-and-stretch gait with a period of about 10 frames (crouches at frames 5, 15, 26, 36, 46), so its per-frame x step varies from about 4 to 9 px.
  Its feet stay near the floor; there is no clear airborne phase.

## Events
- Frame 0: all three animals are already moving.
- Frames 0-48: steady walking or running for all three.
- **Frame 49 (t = 2.042 s): horse_red jumps back about 154 px** (torso x 801 → 647, almost its frame-0 position). This looks like an
  animation-loop reset. Any speed or distance for the red horse that uses frame 49 would be an artefact; frames 0-48 are continuous.
  The dun horse and the rabbit continue normally.

## Reliability and ambiguities
- Edges are good to about ±2 px. Black hoof tips and the grey faces are the least certain, so length and height carry about ±3 px.
  Length and height change with gait phase (legs spread or together). Use the median for a "size", or the min/max when the question
  asks for them.
- The reference point is not visible. The rig origin (likely root/pelvis) is unknown in the image. For horizontal motion, bbox centre,
  centroid and torso centroid agree to within a few px over the clip; torso and centroid are smoother than the bbox centre.
- 2D assumption: the animals stand on slightly different floor rows (red 630, dun 634, rabbit 637). That is a small depth offset,
  so a single scale is reasonable. Sizes differ by a few percent at most.
- The three animals are easy to tell apart (colour and size), never occlude each other, and have no motion blur. Each horse has a faint contact shadow under its hooves, which is excluded from the masks.
