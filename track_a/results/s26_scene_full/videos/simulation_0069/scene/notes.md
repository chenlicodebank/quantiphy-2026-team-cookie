# simulation_0069 – measurement record

2D simulation (Blender) clip, 72 frames at 24 fps (3.0 s), 2160x1080. The camera looks straight down on a
street intersection: a horizontal road (y 289–755, 467 px wide) crosses a vertical road (x 616–1081, 466 px
wide), with beige sidewalk blocks in the four corners. **The camera is static** (phase correlation shift < 0.01 px).
There is no visible perspective, so one m/px scale applies to the whole ground plane. All values here are pixels
and frames (t = frame/24). Pixel axes: x to the right, y down.

## Files
- `scene.json`: inventory, moving-object summary, events, camera, road geometry.
- `static.json`: static objects in frame 0, each with a pixel bbox [x0,y0,x1,y1], w/h, centre and min-area-rect length/width.
- `tracks/car.csv`, `tracks/pedestrian.csv`: one row per frame (0–71). Columns are frame, time, cx, cy (reference
  point), centroid_x/y (mask centroid), bbox, bbox_w/h, mask_len/mask_wid (min-area rect), area, occluded, touches_edge, note.
- `scripts/`: diff.py (finds the moving regions), track.py (background-median subtraction per crop),
  write_and_overlay.py (CSV output, car rear-edge fix, overlay images), static.py and copy_static.py (static extents),
  events.py (per-frame steps and camera check), peek.py.

## Moving objects (only two; everything else is static)
1. **car**: the white van/MPV, the only vehicle. It sits in the vertical road at x ≈ 832, front facing up. It is
   at rest for frames 0–2, starts moving at frame 3 (t = 0.125 s) and drives straight up (−y) while speeding up
   steadily until the end. The front edge moves about 1 px per frame early on and about 20 px per frame at the end.
   Its centre goes from (832.5, 929) at frame 0 to (832, 200) at frame 71. It is fully inside the frame
   throughout. Top-view size: **length 234 px** (along y; per-frame range 232–237) and **width 87 px**.
   Reference point = bbox centre, computed from the clean front edge as y0 + 116.5. Mask centroid_y sits about
   7 px lower because the van's shape is asymmetric; use cx/cy as the origin. In frames 37 and 39 the raw rear
   edge was corrupted by a background artefact. Those rows were repaired and flagged in `note`, and the per-frame
   steps are smooth afterwards. Reliability is about ±1 px per frame on position.
   The front enters the horizontal road (crosses y = 755) at frame 20 and passes its far edge (y = 289) at about frame 60.
2. **pedestrian**: a small person seen from above (white top), on the bottom-right sidewalk at y ≈ 845. They walk
   right (+x) at a roughly constant pace for the whole clip, about 2 px per frame: centre x goes from 1330 to 1473
   (centroid 1332 to 1475, about 143 px in 71 frames). Their blob is only about 13–36 × 17–22 px, and the x extent
   swings with the stride (legs/arms). So the per-frame position jitters by ±1–2 px; smooth over several frames
   before taking speeds. The reference point is the bbox centre of the blob (from above, the pelvis is under the
   head/shoulders). Standing height cannot be measured from this top-down view; the top-view width is about 13–18 px.
   They pass just below the street lamp at x ≈ 1412 around frames 34–42, with no real occlusion. The mask's
   bottom edge is constant at y = 854.

## Static objects (frame 0, see static.json)
- Four brown square planters/tree pits, about 80×80 px: top-left (410, 222), bottom-left (410, 849) and
  bottom-right (1218, 846). The top-right sidewalk has a dark grey square instead (86×90 px, centre (1278, 72)).
- A small white round object on the road at (2025, 433), about 20–29 px (blurred), static.
- A dark grey irregular object on the road at (2060, 624), about 66×54 px, static.
- Bench/chair clusters at the four intersection corners, and a round teal bin at (1342, 806), 22 px.
- Eight street lamps, four on each sidewalk, at x ≈ 200, 1412, 1732 and 2051, all with similar top-view shapes.

## Ambiguities
- Top-down view: "height" of anything is not observable; only plan length/width.
- The pedestrian is tiny, so size-based scales from it are coarse (±20%). The car (234 px) is the best scale reference.
- No lane markings or crosswalks are clearly visible.
