# simulation_0067 — measurement record

All values are in pixels of the original 2160x1080 frames (x right, y down) and in seconds (t = frame/24). No metric
scale was assumed.

## Files
- `scene.json` — video meta, camera (static, duplicate first frame, vanishing points / focal estimate), inventory of
  moving and static objects with descriptions and pixel boxes, events.
- `tracks/van.csv`, `tracks/taxi.csv`, `tracks/pedestrian.csv` — one row per frame 0-71:
  `ref_x, ref_y` (reference point = centre of the visible mask's bounding box), `bbox_cx/cy`, `cen_x/cen_y` (mask
  centroid), `x0 y0 x1 y1` bbox, `bbox_w/bbox_h`, `axis_len/axis_wid/axis_angle` (min-area rectangle of the mask:
  length along main axis, width across), `area` (mask px), `top_x/top_y` (highest mask point), `bot_x/bot_y` (lowest
  mask point), `occluded`, `edge_clipped`.
- `tracks/cyclist.csv` — `ref_x, ref_y` = top of the rider's head (most reliable point), `head_interp`=1 where the head
  was missed by the segmentation and replaced by a local quadratic fit (frames 8,17,38-40,50,51,54,56,59,67);
  bbox/axis columns are rider+bicycle extents, valid only where `reliable_extent`=1 (frames 16-35).
- `tracks/*_raw.csv` — direct segmentation output before cleaning (cyclist_rider_raw = dark rider core only).
- `bg.png` — clean static background (frame 71 with the late movers' regions filled from frame 0).
- `scripts/` — bg.py (camera stability), bg2.py (background), track.py (segmentation/tracking), finalize.py (final
  tracks), verify.py (overlay check), lines.py (curb lines), crops.py / gridcrops.py (inspection crops).

## How it was measured
Camera is static (phase-correlation shift < 0.01 px), so foreground = |frame − background| > 25 minus cast shadows
(uniform darkening of grey road). Objects were split by colour: van = convex hull of the near-white foreground;
taxi = hull of orange foreground near its previous position (dilated 20 px to take in cream highlights), minus van;
pedestrian = foreground in the right-sidewalk window; cyclist = dark foreground (suit/jeans/hair) near its previous
position, using Farneback optical flow (cyclist moves left, taxi right) where it overlaps the taxi. Overlays were
inspected at frames 0,4,8,10,14,20,30,40,48,56,60,71 — masks hit the right objects and their full visible extent.

## Reliability
- Van: very good from frame 15 on. Frames 0-14 the van is cut by the bottom/right image edges (`edge_clipped`=1),
  so its bbox/centre there is biased toward the image interior. Wheels are included in the mask; a soft ground shadow
  is mostly removed (residual few px at the bottom).
- Taxi: good from ~frame 15. Frames 0-14 its lower-left part is hidden by the van and the cyclist, so the bbox
  centre is biased (frame-to-frame steps noisy, 7-34 px). `top_y` (roof sign / roof) is smooth all clip long and is a
  better vertical reference early. Flag also set 26-43 where the van's rear is close to/over its lower edge. The right
  traffic light's pole/ped signal stands in front of its rear in the last frames (static, so not in the mask; can
  split the mask slightly).
- Pedestrian: good; never occluded. Pelvis ≈ bbox centre (belt line at frame 0 ≈ y 398 vs bbox centre 401).
  Standing/walking pixel height 98-116 px (leg swing makes it vary). Moves only ~1-4 px/frame, so per-frame
  differences are noisy; smooth over several frames.
- Cyclist: head-top track has ±3 px jitter (alternating steps visible e.g. frames 13-16); smooth before
  differencing. Frames 0-15 the rider overlaps the taxi and its bike is hidden by the van; frames ~36-70 the van hides
  the bike and later the body (only head/shoulders above the van roof), frame 71 rider beside the van's rear corner.
  Head-top to wheel-bottom height in clean frames: 114 px (f18), 106 (f24), 103 (f30), 98 (f36). The simulation
  origin (pelvis, on the saddle) is roughly 40-45 % of that height below the head top; rider+bike length along the
  bike ~ axis_len in frames 16-35 (wheels are thin and partly missed, so lengths are slight underestimates).
- Static-object boxes in scene.json were read from gridded frames (±5-10 px), except the sedan (zoomed, ±3 px).
- Perspective: east-west road VP (2697,-43) is good (±10 px); vertical VP from only two poles is rough; the
  focal estimate f ≈ 1100 px (HFOV ≈ 89°) assumes a centred principal point but is cross-checked by the diagonal-road
  curbs. Prefer calibrating from given depths when available.

## Motion summary (pixels; no speeds fitted)
- Frames 0 and 1 are identical: positions at t=0 and t=0.042 s are the same; motion begins between frames 1 and 2.
- Van: starts near rest, image step 2 → ~19-20 px/frame by frames ~25-30, then decreasing to ~12 px/frame by 71 as it
  recedes up-left (ref (1570,838) f0 → (1247,666) f30 → (698,306) f71).
- Taxi: moves up-left until ~frame 36 (bbox_cx min ≈1418), then right/up as it turns into the right-hand road;
  ends ≈(1564,334).
- Cyclist: head (1418,534) f0 → (1052,372) f30 → (785,254) f71; ahead of and left of the van, same general direction.
- Pedestrian: (1847,401) f0 → (1935,355) f71, walking away up-right on the right sidewalk.
- No impacts, bounces or stops; the cyclist/taxi and cyclist/van overlaps are image-plane only (different depths).

## Apparent size vs time (bbox w x h, px)
| frame | van | taxi | pedestrian h | cyclist (head→wheel h) |
|---|---|---|---|---|
| 0 | 794x484 (clipped) | 497x231 (occl.) | 111 | – |
| 18 | 675x484 | 321x203 | 112 | 114 |
| 30 | 533x382 | 172x172 | 108 | 103 |
| 42 | 404x288 | 204x140 | 106 | occl. |
| 54 | 303x221 | 231x122 | 108 | occl. |
| 71 | 208x145 | 207x112 | 98 | occl. |
Van and taxi shrink as they move away (larger depth); the taxi's width changes also reflect its turn (orientation).

## Ambiguities
- "Car" could mean the taxi (moving), the purple sedan (parked far side) or the green convertible (parked, cut off at
  the left edge); only the taxi and van move.
- The cyclist is the only person on a vehicle; the pedestrian is the only walker.
- Shadows are soft; residual shadow pixels may add a few px to the bottom of vehicle boxes.
