# internet_0007 — measurement record

**Scene.** Top-down drone shot (portrait, 1080×1920, 29.943 fps, 298 frames, 9.95 s). A straight two-lane road runs
vertically through the middle of the frame (x ≈ 524–595, 71 px wide), with a dashed white centre line at x ≈ 560. Two cars
move on it, and nothing else moves (the trees sway a little in the wind, which doesn't count):
- **blue_car**: dark/metallic blue, left lane (x ≈ 537–545), drives toward the image top. It is visible in frames 0–133,
  fully in frame 0–127, and leaves through the top edge in frames 128–134. Frames 86–108 it passes under a large pale
  tree that overhangs the left lane and is mostly hidden.
- **white_car**: white, right lane (x ≈ 577–585), drives toward the image bottom. It enters at the top (front bumper at
  about frame 91–92, first measurable frame 94, fully in frame 99–290) and is leaving through the bottom edge when the video ends (291–297).
- The cars pass each other (same image y ≈ 190) between frames 114 and 115 (t ≈ 3.83 s).

## Files
- `scene.json`: inventory (moving and static objects), pixel sizes, events, camera summary.
- `camera.csv`: per-frame similarity transform of the background, frame 0 → frame i (scale, rot_deg, tx, ty in
  full-res px). It comes from ORB features with the road strip masked out and a RANSAC partial-affine fit.
- `tracks/blue_car.csv`, `tracks/white_car.csv`, one row per frame:
  `frame,t,cx,cy` (reference point = visible centre of the car in raw image px),
  `cx_stab,cy_stab` (same point in background-stabilised frame-0 px; use these to measure motion relative to the ground),
  `bbox_*` (box of the median car length × width centred on the reference point, clipped to the image),
  `mask_len` (bumper-to-bumper extent of the difference mask along the road, i.e. the motion direction), `mask_wid` (across), `mask_height` (= mask_len; top-down view, so
  the image only has the two ground-plane extents), `visible_edge_y` (in-frame bumper y when the car is cut by the border),
  `in_frame` (full/partial), `occluded` (1 = under the tree), `source` (how the centre was obtained, see below), `ncc`.
- `scripts/`: survey.py (first motion survey), camera.py, track_cars.py (median-background difference blobs),
  track_final.py (NCC template tracker), build_tracks.py + fix_edges.py (the final CSVs; run in that order),
  static_events.py, verify.py, crops.py/show.py/compare.py (viewing helpers). export.py and fix_partial.py are earlier
  versions that build_tracks.py replaced.

## How the tracks were measured
I warped every frame into frame-0 coordinates and differenced the road strip against a temporal median. The bbox of the
car blob gives the centre (`source=mask`, about 280 of 338 rows; reliable to about ±1 px).
A template tracker fills the frames without a clean mask (`tmpl+off`). The template alone drifted by up to 8 px along the
road, so I corrected it with the interpolated mask–template offset.
`interp`: blue car under the tree (86–108), linear interpolation between clean frames. It is reliable because the blue
car's speed is nearly constant (±2 px).
`edge`/`edge_fixed`: car cut by the image border. Centre = visible bumper edge ∓ the local clean length/2 (blue 77,
white 65). One outlier edge (blue 133) was replaced by a straight-line fit. Accuracy is ±2–3 px; the very last partial frames (white 296–297, blue 133) are the
least certain.

## Sizes (pixels; for the single-scale convention)
- blue_car: length along the motion **74 px** (frames 0–85, p10–p90 73–77), width 35 px including mirrors. After the tree
  (109–127) the mask reads 77–78 px because the car is darker there and blur/rear lights get included. 74 is the better bumper-to-bumper value.
- white_car: length **63 px** median (p10–p90 60–65), width 30 px. The length depends slightly on image position: ≈65–66
  near the top, ≈60–61 in the middle (y 800–1100), ≈63–65 near the bottom. This looks like mild lens or perspective
  variation, so a ±3 % scale uncertainty is inherent.
- Static: road width 71 px; centre-line dash ≈88 px long, repeating every ≈132–145 px; "SLOW" marking in the right lane bbox
  x 565–607, y 1150–1240 (90 × 42 px). Trees and the side track are only coarse (see scene.json).

## Motion character (orientation only, not a fitted model)
- Blue car: about −11.35 px/frame over frames 0–20, then a steady −11.9 to −12.0 px/frame.
- White car: about +10.1 px/frame at entry, falling gradually to about +8.9 px/frame by the end. It is gently decelerating.
- Neither car stops, reverses or turns. Both stay in their lanes, drifting at most ±4 px in x.

## Camera
It is almost static: drift of up to about 13 px and a scale change of up to 1.3 % over the clip, both slow (camera.csv). Raw and
stabilised coordinates differ by at most about 12 px. Annotators who measured in raw pixels would get nearly the same numbers.

## Ambiguities
- Blue-car occlusion by the tree (86–108): the positions there are interpolated, and the mask extents are blank.
- The white car's difference mask can pick up the "SLOW" letters and the centre dashes when exposure changes. Those blobs
  are filtered by size and colour.
- There are no visible shadows (overcast light), so the masks are the car bodies.
