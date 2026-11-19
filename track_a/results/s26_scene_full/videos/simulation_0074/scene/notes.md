# simulation_0074 – measurement record (pixels, seconds)

Video: Blender render, 3D scene, 2160x1080, 24 fps, 72 frames (t = frame/24, frame 0 at t = 0).
Elevated, oblique, **static camera** (phase correlation of static regions vs frame 0: max shift 0.01 px
over all frames; no pan/shake/zoom). It looks down on a 4-way road junction: plain grey road with no lane
markings, four beige paved sidewalk corners, white backdrop at top centre, no horizon visible. Focal length unknown.

## Files
- `scene.json`: inventory (moving + static objects, with pixel boxes), events, camera, perspective cues
  (approximate kerb lines, apparent size of each mover at sample frames), and the track file list.
- `tracks/<object>.csv` (taxi, van, cyclist, pedestrian), one row per frame 0-71:
  `cx,cy` = mask centroid; `bbox_cx,bbox_cy` = bbox centre; `bottom_x,bottom_y` = lowest mask point (ground
  contact, approx.); `bx0,by0,bx1,by1,bw,bh` = bounding box; `main_len,cross_w,axis_deg` = mask extent along / across
  its principal image axis; `area` = mask pixels; `occluded` (0/1) and `note` (why). pedestrian.csv also has
  `*_coarse` columns (first-pass box) — use the main columns.
- `scripts/`: s1 frame differencing (finding movers), s2 background build, s3a cyclist template track (frames 0-30),
  s3 main tracker (background subtraction + mask propagation + colour rules), s4 camera check and static extents,
  s5 occlusion flags, s6/s7 pedestrian refinement + flags, s8 scene.json, s9 visual check overlay.
  Scratch images went to `../frames/` (not part of the record). To re-run, start with s2 (it rebuilds
  `frames/background.png`, which was deleted to save space), then s3a, s3, s5, s6, s7, s4, s8.

## Objects
Moving (all visible and moving in all frames 0-71; none starts or stops inside the clip):
- **taxi** – yellow sedan with roof sign. Starts at upper centre-right (bbox x 1202-1437, y 230-360 at f0) next to
  the van, drives image-left along the far road and ends at upper centre-left (bbox centre ≈ (737,264) at f71), in
  front of the far-centre signal pole. ~6-11 px/frame of image motion; heading turns slightly (bbox width 236 → 323 → 262).
- **van** – white cargo van. Starts at upper right (bbox 1445-1706 x 187-390 at f0), creeps slowly at first
  (~1-2 px/frame) then turns toward the camera and comes down-left with rapidly increasing image speed and size
  (bbox 265x203 at f0 → 430x326 at f60 → 575x418 at f71; ~45 px/frame at the end). Largest perspective effect.
- **cyclist** – rider in dark blue on a bicycle. Starts in front of the taxi's rear (x ≈ 1367-1422, y 252-360 at f0),
  rides diagonally down-left across the junction, ends behind the van near (620-700, 560-610).
- **pedestrian** – person in white top and jeans on the far sidewalk, walking image-left (feet x ≈ 958 → 840, feet
  y ≈ 256 → 227, i.e. slightly away). Bbox height ≈ 98-101 px at frames 0-9, ≈ 92-99 px at 58-68 (walking, gait
  oscillation few px). Width 24-36 px depending on stride.
Static (pixel boxes in scene.json, frame 0): purple parked sedan (408-664 x 268-404), green car cut by the right
edge, 4 traffic signals (the nearest one, lower centre-right with a pedestrian-crossing sign, x 1385-1529,
y 416-999), 4 street lamps (one double-headed on the left, three on the far sidewalk), green litter bin (904-929 x
214-259), grey bin cluster top-left, small grey box far left, two red-brown grates, four sidewalk corners/kerbs.

## Reference points / conventions
Simulation answers use object origins (vehicle root, human pelvis, rigid centre) which are not visible. The CSVs
give mask centroid, bbox centre and bottom point so the answering session can choose (e.g. vehicle root ≈ ground
under the body centre ≈ between bbox centre and bottom; pelvis ≈ 45-50 % of a standing person's bbox height above
the feet). Image motion includes strong perspective (the van approaches the camera); convert with depths if given.

## Reliability
- Camera static: certain.
- taxi / van masks: good (±3 px on edges). Van: thin dark wheel/underbody parts partly missed (bottom can be a few
  px high); frames ~22-55 its lower right part is behind the near signal sign (flagged) — bbox right/bottom may be cut
  there, which also causes the 17 px bbox jumps around frames 30-33. Taxi frames 0-20: cyclist in front of its rear
  quarter; split by colour, so taxi right edge/area uncertain (flagged occluded).
- cyclist: frames 0-20 position from a fixed-size template box (89x130) tracked backwards from frame 30 and non-yellow
  pixels inside it — box size and centroid are biased (bw ≈ 100 at f0 includes taxi tail pixels); centre motion is
  OK to ~±5 px. Frames 21-61 clean (thin white wheel rims partly missed: width ±10 px). Frames 62-71 increasingly
  hidden by the van (flagged; only head/upper body at 69-71: positions there are NOT the cyclist's centre).
  Frames 0→1 template shift is 0 (possibly not yet moving; uncertain).
- pedestrian: low contrast (white on pale sidewalk); refined mask (s6) is good for top of head (smooth 159 → 136).
  Feet are hidden by the green bin in frames ~19-33, 36-38, 43-46 (bottom too high, bh too small → flagged);
  frames 51, 52, 56, 57 have taxi-roof pixels merged (bottom 261 / bh 120 invalid → flagged); the lamp-post flag
  for 49-71 is based on bbox overlap with the thin pole (mild). Frames 10-12 and 34-35, 39-42 bottoms (256-261)
  may include a shadow — prefer frames 0-9 and 58-68 for height.
- Kerb lines in scene.json: visual, ±10-25 px; for orientation only.
- No contacts, collisions, bounces or releases occur; image overlaps between objects are depth overlaps only.
