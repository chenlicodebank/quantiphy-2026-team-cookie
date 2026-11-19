# internet_0041 - measurement notes

Video: 3840x2160, 52 frames, 23.979144 fps (2.169 s), internet footage, 2D. t = frame / fps.
All values are pixels at full resolution and seconds. No metric scale is assumed.

## Scene
A sandstone two-storey arcade building seen straight on (front columns at about 404 px spacing), with a paved
walkway (y 1425 to 1555) and a green reflecting pond (y > 1560) in front. Three brown ducks are in the pond
near the bottom of the frame:
- **duck_middle**: swims steadily LEFT on open water (y about 1880), head to the left. It is the main mover.
- **duck_right**: right-most, inside concentric ripple rings, with its head down or blurred (dabbling or preening),
  drifting LEFT slowly.
- **duck_rock**: left-most, sits on a submerged rock and stays still.
The ducks are at roughly the same distance from the camera (all on the pond surface, y 1850 to 1970). Under the
planar convention, one scale applies to all of them.

## Files
- `scene.json`: inventory (names, how to tell objects apart, static extents, column positions, events, camera).
- `tracks/duck_middle.csv`, `tracks/duck_right.csv`, `tracks/duck_rock.csv`: one row per frame (0 to 51, all visible,
  occluded = 0). Columns:
  - `ref_x, ref_y`: mask centroid (the visible centre).
  - `bbox_cx, bbox_cy`: centre of the bounding box.
  - `bbox_x0..y1, bbox_w, bbox_h`: mask bounding box. For the swimming ducks, x0 is the bill/front end and x1 the tail.
  - `len_main, wid_across, axis_deg`: PCA extents of the mask along and across its main axis. Bodies are horizontal,
    so `len_main` ≈ `bbox_w`.
  - `mask_area`.
  - `bg_dx, bg_dy`: global background shift relative to frame 0.
  - `ref_x_bgcorr, ref_y_bgcorr`: centroid minus that shift.
- `tracks/camera.csv`: per-frame facade shift relative to frame 0 (phase correlation on y < 1400, half-res), plus the
  correlation response.
- `scripts/`:
  - `track.py`: camera shift + template propagation + GrabCut masks + overlays.
  - `finalize.py`: merges the camera shift into the tracks.
  - `static.py`: columns and horizontal edges.
  - `camcheck.py`: checks the sign and uniformity of the camera shift.
  - `probe*.py`, `summ.py`: exploration.

## Method
For each duck, the box is propagated from frame to frame by normalized template matching (±40 px search). GrabCut
then runs inside the box (with slack) and the largest component is kept. The masks were drawn on frames 0, 13, 26,
39 and 51 and checked by eye: they sit on the correct ducks.

## Key numbers (pixels)
- **duck_middle**
  - Length bill to tail: median 127 px; range 124 to 130 in frames 12 to 51. A visual grid read at frame 0 gives
    130 px.
  - Frames 0 to 9 under-segment the pale tail tip (116 to 121 px), so for a length prior use about 127 to 130 px.
  - Height above the waterline: about 42 px.
  - Motion: ref_x goes from 2338.8 to 2164.8 (-174 px in 51 frames, mean -3.43 px/frame). It is slower at first
    (-2.9 px/frame over frames 0 to 10) and faster at the end (-4.0 px/frame over the last 10 frames).
  - bbox_x0 (bill) goes from 2283 to 2106 (-177 px).
  - Vertical: +10 px in the image (+16 px against the background).
  - Per-frame centroid jitter is about ±1 px because the mask shape changes. Smooth over several frames, or use
    bbox_x0, before taking differences.
- **duck_right**
  - Body length: median 135 px (131 to 146). Height: about 48 px; it was 54 to 66 px in frames 0 to 24, when part of
    the head or neck was included.
  - Motion: ref_x goes from 3295 to 3182 (-113 px, about -2.2 px/frame). This track is noisy because the posture
    changes (head dipping). The jump in ref_y around frame 24 to 27 comes from the head going down, not from the body
    moving.
- **duck_rock**
  - Width: 103 px. Body height: about 72 px (frames 0 to 8). In later frames the mask leaks onto the rock, so heights
    of 84 to 88 px there are inflated.
  - Stationary: the 7 px centroid drift is a posture change.
- **Rock** under duck_rock: about 275 x 70 px, at x 1682 to 1957 and y 1939 to 2010. This is a rough figure.
- **Front columns**
  - Centres: x ≈ 269, 682, 1089, 1498, 1897, 2298, 2698, 3105, 3508 (spacing about 404 px).
  - Example column at x 1890: shaft 80 px wide; capital 120 px wide; height from capital top (y 1040) to base
    (y 1425) about 385 px.
- **Walkway**: top at y ≈ 1425, coping edge at y 1540 to 1555, water from y ≈ 1560.

## Camera
The camera is nearly static, with handheld drift. Against frame 0, the facade moves by dx -0.2 to +0.9 px and by dy
from 0 to -6 px at frame 51 (negative = image content moves up). Patch checks at frame 51 give dy -2 px on the left
walkway and -10 px at the right pond edge, which suggests a slight roll. This is negligible next to the ducks'
horizontal motion (< 1% of duck_middle's displacement). The vertical component matters only for small vertical
motions. The `_bgcorr` columns subtract the global shift.

## Events
There are no discrete events: no release, bounce, impact, entry or exit. duck_middle and duck_right are already
moving at frame 0 and still moving at frame 51. duck_rock never moves.

## Reliability and ambiguities
- **Mask edges**: reflections and ripples blur the waterline, so mask edges are good to about ±3 to 5 px. The bodies
  are cut at the waterline, so heights are only the part above water.
- **duck_right head**: it appears as a pale, semi-transparent, motion-blurred blob above the body (frames 0 and 51)
  or is underwater. It is excluded from the mask, so duck_right's length means body plus tail.
- **Reflections**: the pond shows strong reflections of the columns, but the ducks have no confusing look-alikes.
  The three ducks are told apart by position: left on the rock, middle in open water, right in the ripples.
- **Motion blur**: little on the bodies.
