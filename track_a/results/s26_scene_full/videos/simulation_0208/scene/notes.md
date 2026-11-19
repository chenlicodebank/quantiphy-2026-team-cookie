# simulation_0208: measurement record

2D simulation, 24 fps, 30 frames (1.25 s), 2124x1080. A black vintage typewriter falls straight down
from the top centre onto a desk mat, hits it, rocks/tips on it and comes to rest. The camera is static.
All values are in pixels (x right, y down) and seconds. Time t = frame/24.

## Files
- `scene.json`: inventory, static object extents, events, camera, key pixel sizes and fall distances.
- `tracks/typewriter.csv`: one row per frame (0-29). Columns: frame, t; cx_bbox, cy_bbox = centre of the mask
  bounding box (**the recommended origin proxy**); cx_mask, cy_mask = mask centroid; x0,y0,x1,y1 = bbox;
  bbox_w, bbox_h; minrect_len/wid/angle = minimum-area rectangle of the mask; area (px); occluded (always 0);
  phase (airborne 0-10, rocking_on_mat 11-22, at_rest 23-29).
- `scripts/track.py`: segmentation and tracking. `checksheet.py` builds the check images. `static.py` measures the mat edges.
  `probe*.py` hold the noise, shadow and prop checks.
- Overlay images were written to `frames/` (scratch) and checked by eye.

## Method
Background = frame 29 above row 600 (the typewriter has left that area) plus frame 0 from row 600 down (the typewriter
is not there yet). Mask = per-pixel max |diff|: > 10 on the wall (render noise ≤ 2) and > 28 on the mat, with
shadow-like pixels (darker, same chromaticity) removed. The static scissors/paper zone (x ≥ 1196, y 955-1015) is
excluded. In frame 10 the detached shadow below the object is cut at a row gap. The largest component is kept.
I checked the overlays on frames 0-29: in the air the masks cover the full typewriter, and on the mat they cover the
body without the shadow.

## Reliability
- Airborne (frames 0-10): horizontal extent 292-293 px every frame (±1 px). This is the most reliable size. Height is
  125 px in frames 0-2. From frame ~6 on, vertical motion blur makes the bbox taller (bbox_h 133→169 px at frames 6-9).
  The blur is roughly symmetric, so the bbox centre is still a good centre (±2-3 px). cx stays at 981-984 px, so the
  fall is purely vertical. The object turns slightly in the air (its appearance changes a little). The centre track
  y values for frames 0-10 are 254.5, 262.5, 283, 315, 359, 415.5, 484.5, 567, 664, 772.5, 887.5.
- Frame 0 is already moving (8 px drop between frames 0 and 1), so there are no stationary frames before the release.
- Impact: frame 10 is still airborne (lowest edge y≈975-982, about 45 px above its later contact line).
  Frame 11 (t=0.458 s) is the first contact frame, so the impact lies between frames 10 and 11.
- Frames 11-22: the typewriter tips and rocks on the mat. Its bbox top goes 853→793 (f15)→853 (f19-21) while the
  bottom stays at y≈1011-1028. That is a rotation, not a clean bounce. The bbox centre changes there mostly
  because of the shape change, so it is less reliable as an origin (±10 px). The right edge (x1=1195 in frames 17-29)
  hits the exclusion boundary. The true right edge at rest is ≈1192 (seen by eye).
- At rest (frames 23-29): bbox ≈ [861, 848, 1192, 1023]: 332 px wide, 176 px tall. It now shows the front/top of
  the machine in perspective, so this is not the same view as the airborne size. For a size prior, prefer the
  airborne length of 292 px. The resting width includes foreshortened depth.
- The Blender origin is not visible. The bbox centre is the best proxy. The vertical drop of the centre from frame 0 to
  rest is 681 px, from frame 0 to frame 10 it is 633 px, and the bottom edge drops 706 px from frame 0 to rest.

## Static objects (frame 0)
- Desk mat: back edge at y≈946, back corners ≈(276,946) and (1800,946), back edge ≈1524 px long. The right side edge
  runs (1808,952)→(2032,1075). The front edge is below the frame. Reddish-brown border, tan/green blotter surface.
- Paper card ≈[1191,983,1305,1001] (114 px long). Scissors on it ≈[1216,968,1330,1003]. Small dark block ≈[1325,980,1356,1012].
  None of them move. Only their shading changes while the typewriter is near.
- Wall: plain blue-grey backdrop.

## Ambiguities
Only one moving object. The shadow of the typewriter on the mat, and changing reflections on the scissors, are not
motion. The airborne and resting views show different faces of the typewriter, so sizes depend on the orientation.
