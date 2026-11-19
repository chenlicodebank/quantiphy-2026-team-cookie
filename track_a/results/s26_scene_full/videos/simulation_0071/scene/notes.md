# simulation_0071 – measurement record

**Scene**: a 2D simulation (Blender) shot from straight above a 4-way street intersection. 2160x1080 px, 24 fps, 72 frames (t = frame/24, last frame 71 = 2.958 s).
The camera is static. Nothing indicates perspective: matching lamp posts are the same pixel size (~57 px) across the whole frame, so a single m/px scale applies to the ground plane.
All units are image pixels (x right, y down) and seconds. No metric scale is assumed.

## Files
- `scene.json`: inventory, size summaries, events, road geometry, static objects (bbox/centre/OBB), and camera.
- `tracks/car.csv`: one row per frame (0–71). Columns: centroid `cx,cy` (reference point), bbox, `length_px` (along the car's main axis, PCA of the mask), `width_px`, `heading_deg` (0 = +x/right, 90 = up), `area_px`, `front_x/y` and `rear_x/y` (axis end points), `occluded`, `cx_smooth/cy_smooth` (3-frame mean), and `step_px` (raw one-frame displacement).
- `tracks/pedestrian.csv`: the same columns without front/rear. `cx_smooth/cy_smooth` here is a 7-frame mean.
- `scripts/`: `motion_scan.py` (finds the movers), `track.py` (median-background subtraction at full resolution, masks, overlays), `static.py` and `road_edges.py` (static extents), `finalize.py` (flags and smoothing; writes scene.json), `summarize.py` (prints the tracks). `background.jpg` is the median background and `static_out.json` the raw static measurements.

## Moving objects (only two)
1. **car**: the only vehicle, a peach/cream sedan.
   - It is identical in frames 0 and 1 and starts moving at frame 2.
   - It drives up (−y) in the right half of the vertical road, makes a smooth right turn through the intersection, and ends driving right (+x) in the lower half of the horizontal road. It is still moving at frame 71 and never leaves the frame.
   - Heading: 89.6° → 45° at frame 29 → <1° from frame 61 on.
   - Step per frame is about 6.8 px (5.7–7.7 is mask noise), so the speed looks roughly constant.
   - Size: length 222.5 ± 1.5 px, width 88 ± 2 px.
   - Raw centroid path is 476 px and net displacement is 435 px. The raw path includes about ±0.5 px/frame of centroid jitter; use smoothed values for path lengths if needed.
   - Overlays (frames/ov_*.png) confirm the mask covers the whole car body. There is no visible shadow, and the mask may include a 1–2 px edge.
   - Reliability: centre ±0.5 px, length ±2 px.
2. **pedestrian**: one person (white top, dark hair) on the bottom-right sidewalk, seen from above.
   - Walks right (+x) at y ≈ 843 from frame 2 to 71: x 1331 → 1473, about 2.0 px/frame, still walking at the end.
   - The mask is tiny (~20–38 px along x, 13–24 px across) and its extents swing with the stride. Use the smoothed centroid as the pelvis.
   - Standing height cannot be seen from a top-down view.
   - Frames 25–61 are flagged `occluded=1` because the person's bbox overlaps the lamp post `lamp_bottom_2` (bbox 1395–1430, 784–841), so the mask may be partial (for example, the 4.5 px centroid jump at frame 51).
   - Reliability: centre about ±1.5 px raw, ±0.5 px smoothed.

## Static objects
Measured on the median background; bbox values are [x0, y0, x1, y1] in px. Full list in scene.json.
- **Roads**: vertical road x 615–1081 (466 px wide), horizontal road y 289–756 (467 px wide). The four beige sidewalk blocks fill the corners and have a darker tan curb rim.
- **Dark square** (manhole or grate) at the top right: 86×90 px, centre (1278, 71).
- **Brown square planters**: about 80×80 px at (410, 849) and (1217, 846). The top-left one, near (410, 222), is also about 80×80 px by eye, but its auto bbox merged with the curb.
- **Lamp posts** (two heads plus an arm): 8 in total, in rows at y ≈ 220 and y ≈ 807 and columns at x ≈ 192, 1416, 1740, 2062. Bbox height is 58 px; width varies with arm orientation (35–76 px).
- **Grey props** (benches or hydrants) at the four corners: about 52–70 × 31–56 px.
- **Green trash can** at (1342, 806): 22 px.
- **White ball** lying on the road at (2026, 433): about 20–26 px. It is static.
- **Grey rock or bush** on the road at (2063, 622): 66×54 px. It is static.

## Events
| Event | Frame | Time (s) |
|---|---|---|
| Car and pedestrian both start moving (both static in frames 0–1) | 2 | 0.083 |
| Car mid-turn (heading 45°) | 29 | 1.208 |
| Car turn finished (heading < 1°) | ≈61 | 2.54 |
| Pedestrian near or overlapping lamp_bottom_2 | 25–61 | |

There are no collisions or contacts. The car and pedestrian are never close to each other.

## Ambiguities
- The car's reference point is the plan-view mask centroid. It is assumed to be the rig root's x-y position; a rear-axle root would be offset by about 0.25 × length along the heading, and front/rear points are given in case that matters.
- In a 2D question, a single scale from the prior object (car length 222.5 px or width 88 px, or a pedestrian quantity) applies to the whole scene.
- The pedestrian's mask size is a poor size reference because it is small and changes with every stride.
