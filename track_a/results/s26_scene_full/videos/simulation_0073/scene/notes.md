# simulation_0073: measurement record

Simulation, **2D** scene, 24 fps, 72 frames (t = i/24, 0 to 2.958 s), 2160x1080. The view is top-down onto a
four-way street intersection, and all motion is in the ground plane facing the camera. **The camera is static**: the
static region differs by at most 9 grey levels between frames 0 and 71 (99.9th percentile 4), so there is no pan or shake.
All values are pixels (x right, y down) and frames. No metric scale is assumed: use one m/px scale from the prior.

## Files
- `scene.json`: inventory (moving and static objects with descriptions, sizes and positions), road layout, events, camera.
- `tracks/van.csv`, `tracks/cyclist.csv`: one row per frame (all 72 frames). Columns: frame, t_s, cx_px/cy_px
  (mask centroid = reference point), bbox x0,y0,x1,y1, len_main_axis_px / width_across_px (PCA extents of the mask),
  main_axis_angle_deg (about 90 = vertical), mask_area_px, occluded_or_cut (always 0).
- `scripts/`: `motion_scan.py` (frame reader and first blob scan), `track.py` (clean background = frame 0 top half plus
  frame 71 bottom half, difference mask >22, closing 5x5, van = largest blob in x 760-895, cyclist = blobs in
  x 895-960), `static.py` (prop boxes on the clean background), `summarize.py` (sizes, fits, crossings),
  `write_scene.py`.

## Moving objects
- **van**: a white minivan in the left lane of the vertical road (x ≈ 833 ± 1, straight). It moves up (−y). Its centre
  goes from y 924.1 (frame 0) to 202.6 (frame 71), a net 721.5 px. It **starts from rest at frame 0 and accelerates
  uniformly**. The step from frame 0 to 1 is 0.2 px and from frame 70 to 71 is 19.5 px. A check fit gives
  y = 924.5 − 0.28 i − 0.139 i² (about 0.28 px/frame², rms 0.5 px). This is for checking only, not a model.
  Size: length along travel is 245 px (median bbox height, range 242–249). Width is about 101 px including the
  mirrors, or about 89 px for the body without mirrors. Per-frame centroid steps have about ±0.7 px noise, so
  differentiate over several frames if you can.
- **cyclist**: a person on a bicycle, seen from above, just to the right of the van (x ≈ 917). It moves up at **constant
  velocity, about 8.9 px/frame**. Frames 0 and 1 are identical, and motion starts at frame 1→2. Its centre goes from
  y 828.6 to 205.6 (net 623 px). Size: about 64 px long (wheel to wheel, range 60–67) by 21 px wide (handlebars).
  The centroid is the centre of bike plus rider. The rider's body/pelvis lies a few px from it along y. Noise is about
  ±1 px per frame.

## Events
- Frame 0: the van starts from rest.
- Frame 1: the cyclist starts moving.
- Frame ~32 (1.33 s): the van's speed equals the cyclist's speed, and the centre gap is at its maximum of 220 px (van behind).
- Frames 61→62: the van's front passes the cyclist's front.
- Frames 70→71: the van's centre passes the cyclist's centre.

There are no contacts, bounces or turns.

## Static objects (frame 0 / clean background; bbox in px)
- Roads: the vertical road's asphalt is x 616–1081 (466 px) and the horizontal road's is y 290–755 (466 px). There are
  no lane markings.
- On the horizontal road: a **white ball** centred at (2025, 432), about 22–29 px across (its shadow cuts the mask, so
  the bbox is 29x20), and a **rock pile** at (2060, 624), 66x54.
- Eight three-headed street lamps (about 58 px tall in y; x width 36–76 depending on rotation).
- Four brown square patches (about 81–83 px square) and one dark square slab at the top (86x90).
- Four table/chair sets (33–69 px) and one small round teal object (23 px).

All of these never move. Exact boxes are in scene.json.

## Reliability and ambiguities
- Track masks were checked on overlays (frames 0, 24, 48, 71): they cover the full van and the full bike.
- The van's mask includes its mirrors and a faint shadow fringe, so its sizes are ±3 px.
- Sizes of small props are ±2–3 px.
- The centroid is used as the origin, which is good to about 1–2 px for these top-down rigid objects.
- The van is the only vehicle. The ball is the only ball.
