# internet_0034 – measurement record (pixels, seconds)

Video: 3840x2160, 60 frames, 24.097768 fps (t = frame / fps). Internet footage, 2D. All coordinates are
full-resolution pixels (x right, y down). No metric scale is assumed anywhere.

## Scene
Static close-up of a white tiled wall with a white toilet-roll holder (suction disc at upper left, bracket,
horizontal rod pointing right with a small end post). A right hand brings a white toilet roll in from the
bottom-right corner (frames 0-12, fast up-left motion while the roll turns from a 3/4 view into a side view),
then slides it left onto the holder rod (from ~frame 18) and stops at frame ~56. The hand never lets go.

## Camera
Static. Phase correlation of the never-covered upper-left wall against frame 0 gives |shift| <= 0.3 px for
every frame (scripts/probe.py). No background compensation needed. The wall is nearly fronto-parallel
(grout lines tilt ~0.3 deg; tile widths 1548-1631 px across the frame, ~5 % perspective/lens variation).

## Files
- `scene.json` – inventory, static object positions/sizes, events, camera.
- `tracks/toilet_roll.csv` – one row per frame 0-59:
  - `TL,TR,BR,BL` (x,y): corners of the roll's side-view silhouette. TL/BL lie on the LEFT end face (the
    end that goes onto the rod first), TR/BR on the right end (held by the hand).
  - `center_x,center_y`: mean of the 4 corners = visible centre (the reference point to use). NaN in frames
    0-4 (roll cut off by the bottom/right frame edge).
  - `visible_bbox_center_*`, `bbox_*`: axis-aligned bbox of the corners clipped to the image (frames 1-8
    also include the left end-face ellipse extreme).
  - `left_edge_mid_x`: x of the middle of the left (leading) end – the cleanest edge, best for horizontal
    displacement of the roll.
  - `length_along_axis_px` (end face to end face, mean of top and bottom edges), `top_edge_px`,
    `height_diameter_px` (outer diameter, mean of left/right edges), `axis_angle_deg` (tilt of the roll axis,
    positive = right end lower), `occlusion`, `truncated`, `source`.
- `tracks/hand.csv` – frames 2-59: centroid, bbox, extents and area of the skin-coloured mask
  (R-B>18). The forearm in a dark green sleeve is NOT included, so from ~frame 30 the mask ends at the sleeve
  (bbox_x1 ~3420-3800) even though the arm continues to the frame edge; `truncated` only flags the image edge.
  The centroid is of the visible skin only (biased by frame-edge truncation in early frames).
- `scripts/` – probe.py (camera/colours), seg.py (hand mask; its roll mask failed and is not used),
  track_roll.py (ECC attempt, drifted, not used), anchors.py (manual corner readings), refine.py (edge
  refinement), tiles.py/crops.py (gridded viewing), holder.py, build.py (writes the tracks), verify.py.
  Intermediate JSON: roll_refined.json, seg_raw.json, static_raw.json, holder_raw.json.

## How the roll was measured
White roll on white tiles: intensity masks fail. Instead the 4 silhouette corners were read by eye from
gridded crops (frames 0-11, 13, 14, 18, 22, 26, 30, 36, 42-48, 51, 53, 55, 57, 59; +-10-15 px), linearly
interpolated for the other frames, and then each of the 4 edges was refined for frames 9-59 (except
43-48) by searching +-22-30 px along the edge normal for the strongest intensity step (skin pixels excluded),
robust line fit, corners = line intersections. Overlays (red = refined, blue = manual guess) were checked on
frames 12, 20, 34, 40, 46, 49 and hit the roll outline within ~5-10 px.

Reliability:
- Frames 49-59 (roll near rest, clear edges): corners +-3-5 px; centre +-3 px. At rest (56-59) the centre is
  (1911, 1411) +- 1 px.
- Frames 9-42: top and left edges +-3-5 px; the right edge is partly behind the fingers (only 5-15 edge
  samples), so TR/BR, the centre x and the length can jitter by 10-20 px (e.g. frames 34-41, where BR fell
  back to the manual guess in 36, 38-41). For horizontal motion prefer `left_edge_mid_x` or `TL_x`
  (smooth), or smooth the centre over several frames.
- Frames 43-48: roll yaws slightly (its right end face shows as a thin strip) and tilts; corners are manual
  readings only (+-10-15 px), right corners = outer silhouette including the end-face strip.
- Frames 0-8: roll is in a 3/4 view, motion-blurred and partly out of frame / behind the hand; manual
  readings +-15-25 px. BR in 5-8 is a parallelogram completion (TR+BL-TL) behind the hand. Frames 0-4 have
  only TL (+TR from 1) – use TL for the trajectory there.

Roll size (side view): length (end to end along its axis) 589 +- 3 px and outer diameter 697 +- 2 px at
frames 50-59; frames 13-34 give 590-600 and 698-707 px. This is the length to use if a question gives the
roll's real length/width (one planar scale = prior / pixel value). The apparent size is constant within
~2 % over frames 9-59, so the roll stays at about the same depth (in front of the wall, on the rod plane).

Roll trajectory (centre): f5 (3150,1775) -> f9 (2972,1469) -> f17 (2657,1321) -> f30 (2397,1367) ->
f42 (2137,1362) -> f50 (1979,1414) -> f56-59 (1911,1411). Net horizontal travel of the left end from f9
(2677) to rest (1616) is ~1060 px; most of the motion is leftward, with an initial strong upward component
(frames 0-15).

## Events (frame / time)
- 0 / 0.000 s: roll already entering at the bottom-right corner (blurred corner at ~(3280,2025)).
- 2 / 0.083 s: hand first visible.
- 0-12 / 0-0.50 s: fast up-left motion, the roll turns into side view and its tilt drops from ~14 deg to ~6 deg.
- ~15-17 / 0.62-0.71 s: highest position (TL_y min ~949 at f15; centre_y min ~1321 at f17); vertical
  motion reverses to slightly downward.
- 18 / 0.747 s: the roll's left end passes the free end of the holder rod (end post x ~2340) – start of
  sliding onto the rod.
- 42-48 / 1.74-1.99 s: slight yaw and tilt (~-4 deg).
- 48-50 / 1.99-2.07 s: roll drops ~20-45 px and levels off – core settles on the rod (contact).
- 56 / 2.324 s: roll stops (stationary 56-59). The hand keeps holding; no release.

## Static objects (frame 0)
- Holder: suction disc centre (1596,1049), diameter 288 px (Hough circle); rod x 1515-2340 (825 px long),
  y 1291-1411 (120 px thick); end post x 2325-2342, y 1233-1430; whole holder bbox (1452,905)-(2342,1435).
  The rod is hidden behind the roll from ~frame 20; at rest the roll covers x 1615-2210 (the end post stays
  visible just right of the roll at x~2330, y~1235-1300).
- Tiles: horizontal grout at y 687/1741 (left, x 100-900) and 682/1772 (right, x 2700-3400); vertical grout
  at x 262, 1810, 3441 (top row), 998, 2607 (middle row), 253, 1800 (bottom row). Tile ~1550-1630 px wide,
  ~1054-1090 px tall (running bond). Real tile sizes are unknown.

## Ambiguities
- "Roll size" could mean length (end to end, ~589 px) or diameter (~697 px); the roll is seen side-on so
  its length is horizontal and its diameter vertical.
- The roll's soft shadow on the wall (left/upper-left) and the white holder behind it are low-contrast against
  the white roll; edges were taken at the roll's silhouette, not the shadow.
- The hand's skin mask excludes the sleeve; the hand reference point is the centroid of visible skin.
- Motion blur is strong in frames 1-12 (roll moving ~50-150 px/frame), so edges there are uncertain by
  ~15-25 px.
