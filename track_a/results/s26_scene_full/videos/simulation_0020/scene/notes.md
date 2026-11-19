# simulation_0020 — measurement record

The video is a 2D simulation (Blender render), 1080x1080, 131 frames at 29.997709 fps (t = frame/fps).
A basketball player stands in front of a concrete wall. He crouches with the ball, does a small hop, raises the
ball and shoots (release at frame 21). The ball flies left, arrives at the rim (frame 78), sinks through the hoop and
net, falls straight down at x ≈ 293, bounces once on the wet sidewalk (contact at frame 120, apex at 123, second
contact at 126) and comes to rest. The camera is static.
All values are in pixels (x right, y down, origin top-left) and frames/seconds. No metric scale is assumed.

## Files
- `scene.json`: inventory (every object with a short name, what tells it apart, whether it moves, visible frames,
  pixel extents and positions), events, camera.
- `tracks/ball.csv`: one row per frame (0–130). `x,y` is the ball centre, i.e. the rigid origin. Also: mask bbox,
  `diam_fit` (least-squares circle fitted to the mask contour), `length_px/width_px/height_px` (bbox w/h),
  `visible_area`, `occluded` (0 = clear, 1 = partly hidden, 2 = hidden and interpolated) and `note`.
- `tracks/player.csv`: one row per frame. `pelvis_x,pelvis_y` is the pelvis estimate. Also: full-body mask bbox,
  `height_px`, `width_px`, mask centroid, area, `feet_off_ground` (foot bottom ≤ 792), `hem_y`/`hem_strength`,
  `pelvis_method` and `occluded` (frames 0–20, where the ball covers part of the body).
- `scripts/`: all code. `bg.py` checks camera motion. `track.py` does the median background, ball and raw player
  tracking. `player3.py` makes the final player masks. `finalize.py` writes the ball and player tracks.
  `pelvis.py` estimates the pelvis. `static.py` measures the static objects. `events.py` prints per-frame steps.
  `write_scene.py` writes scene.json. `view*.py` draws the check overlays. `player_masks_all.npz` holds the
  per-frame player masks (ROI x 620–980, y 460–840, bit-packed). `player.py` and `player2.py` are earlier versions
  that the final record does not use.

## Methods
- **Camera:** static. The phase-correlation shift between the first and last frame is 0.02 px.
- **Ball:** orange HSV pixels that differ from the temporal-median background (this removes the orange rim).
  I fitted a circle to the contour; in free flight the fitted centre and the mask centroid agree within 0.3 px.
  I checked the overlays on frames 78–100.
  - Free-flight diameter (frames 25–77): median **29.64 px** (p10–p90 29.0–30.7). At rest on the floor: 29.1 px.
    The apparent size grows slightly, from about 29 px at frame 30 to about 31 px at frames 70–78. This is
    probably minor motion blur or depth; treat the ball as about 29.6 px.
  - Frames 81–93: the lower part is hidden behind the rim and inside the net, so `y` = visible top edge + 14.8 px.
    This is less reliable (±3 px).
  - Frames 94–95 are hidden and linearly interpolated (`occluded = 2`), so do not use them for speeds.
  - Frames 0–20: hands cover part of the ball (centre ±2 px).
- **Player:** the median background contains the standing player. In those pixels I replaced the median with a
  row-wise interpolation of the wall columns on either side. The player is then pixels with |frame − bg| > 32,
  minus the ball disc, cut below row 811 (the wet-floor reflection). I checked the overlays on frames 0–130.
  - Standing (frames 49–130): bbox **x 781–839, y 588–811, height 224 px**, width 59 px with arms down.
    The head top (588) is blurred against the dark window frame and could be off by ±3 px.
  - Bbox height ranges from 187 px (frame 10, crouched hop) to 257 px (raised arm/ball in the bbox).
  - **Pelvis** is an estimate, since no rig is visible: shorts leg-hem trim row − 28 px. Where the hem is not found
    (frames 15–23, 31, 38) it falls back to foot line − 116 px. The hem detector sometimes switches between two
    trim rows 5 px apart (e.g. 690 → 695 at frame 51). Pelvis y is good to about ±6 px; pelvis x to ±3 px.
    Standing pelvis ≈ (808.8, 695).
  - Feet are off the floor (foot bottom above 805; the floor line is 811) in frames 8–12 (min 782 at frame 10),
    18–24 (min 797, jump with the shot) and 31–38 (min 786 at 33). The 18–24 segment could partly be heels or toes
    rather than a full jump.

## Events (also in scene.json)
| What | Frame(s) |
|---|---|
| Crouch with ball | 0–7 |
| Hop | 8–12 |
| Set point (ball nearly still at about (790, 557)) | 16–20 |
| Release (first free frame) | 21 (t = 0.700 s) |
| Flight apex (y = 444.6) | 59 (y flat within 0.5 px from 55 to 59) |
| Ball reaches rim top; horizontal motion ends | 78 |
| Ball slowly sinks into hoop | 79–93 |
| Ball hidden in net | 94–95 |
| Ball out below net, nearly still at y ≈ 551 | 96–98 |
| Straight drop | 99–119 |
| Floor contact (bottom row 773) | 120 (t = 4.000 s) |
| Bounce apex (y = 729.6) | 123 |
| Second contact | 126 |
| Ball at rest at (293.1, 760.6) | 127–130 |

Frames 0 and 1 have identical ball positions; 129 and 130 are identical too.

## Static objects
Pixel bboxes and rows for these are in scene.json:
- Rim: orange, nearly edge-on, x 253–317, top row 492, centre x ≈ 293.
- Net: x 279–317, y 500–538.
- Backboard: oblique, x 223–280, y 407–517.
- Shot clock ("12:00"): x 144–225, y 323–393.
- Support truss.
- Four windows (the middle ones are about 207 × 206 px).
- Two vents.
- Drain pipe.
- Tiny static red dot at (293, 554).
- Ground rows: grass strip 740–758, wet sidewalk 760–843, curb 844–855, gutter 856–900, road line 910–914.

## Ambiguities and cautions
- **The ball's motion does not follow one constant pixel gravity across phases.** During the flight (frames
  21–78), dy changes by only about +0.17 px/frame² and the horizontal speed falls steadily (from −11 to −1
  px/frame). In the drop after the net (99–114), dy grows by about 0.65 px/frame². The fall also slows from
  frame 117, before visible floor contact at 120. Each answering session should measure only the segment its
  question names.
- The view of the hoop shows 3D perspective, but the main action plane faces the camera, so one px scale
  should apply. The player's depth may differ from the ball's.
- **Reflections:** the wet floor mirrors the player and ball, so I cut the masks at the foot line.
- **Motion blur:** the ball smears slightly at frames 8–12 and 115–118 (bbox up to about 33 px).
- **Similar objects:** there is only one ball and one person. The rim and the red dot share the ball's colour
  but are static.
