# simulation_0081 – measurement record

Video: 1920x1080, 24 fps, 29 frames (0..28, t = frame/24, 0–1.1667 s). Blender render, labelled **2D**.
The camera looks straight down at a plain grey floor (~RGB 151). It doesn't move. There are no markings,
props or static objects. Units are pixels and seconds, with image x to the right and y down.

## Objects
| name | identity | motion | visible |
|---|---|---|---|
| pedestrian | man in a white T-shirt with dark hair and dark jeans, upper-left (y≈440) | walks to the RIGHT (+x), about 13 px/frame | frames 0–28, fully in frame |
| cyclist (bicycle + rider) | turquoise/cyan bicycle with a rear rack, rider in a black jacket, lower half (y≈641), front wheel on the left | rides to the LEFT (−x), steady about 47.4 px/frame | frames 0–28. In frames 0–1 the rear of the bike is cut off by the right edge |

There are no other objects. Each figure casts a soft dark shadow, and the shadows are left out of the masks.

## Files
- `scene.json`: inventory, camera, perspective cues, extents and events.
- `tracks/pedestrian.csv`: per frame. `ref_x, ref_y` is the centroid of the hair/head blob seen from above (equal to `head_x, head_y`). Also has the mask centroid, bbox (x0,y0,x1,y1, centre, w, h), principal-axis length and width of the mask, area, and an edge-cut flag (always 0).
- `tracks/cyclist.csv`: per frame. `ref_x, ref_y` is the centre of the bbox of the cyan bicycle pixels, a ground-level stand-in for the root. Also has the bike bbox and `bike_len_px` (front-wheel tip to rear tip), the combined bike+rider bbox and mask (principal-axis length and width), the rider mask centroid, the rider dark-blob (head/back) centroid, and `cut_by_frame_edge`.
- `scripts/`: `bg.py` builds the median background, `seg.py` does segmentation and writes overlays to `../frames/ov_XX.png`, `write_record.py` writes the CSVs and prints summary statistics, and `probe.py` does pixel probing.

## Method
- **Segmentation:** a pixel is foreground if it differs from the background by more than 30 in any channel, or is more than 7 grey levels brighter than it (needed for the white shirt). Holes are then filled. The background is the median over frames, with the region the pedestrian contaminated repaired to 151.
- **Separating the objects:** a horizontal line at y=545 separates them; the pedestrian stays at y 378–511 and the cyclist at y 584–703.
- **Bicycle:** HSV cyan mask (hue 80–105, saturation above 60).
- **Pedestrian head:** the dark component (grey below 95) with the largest inscribed circle; legs are thin, so this picks the hair blob.
- **Checks:** overlays at frames 0, 7, 14, 21 and 28 were inspected. The masks cover the full figures and the bike, and the head point sits on the hair.

## Key numbers (pixels)
- **Cyclist / bike**
  - Bike centre moves from x 1711.5 (frame 2) to 478.5 (frame 28): mean step −47.42 px/frame, per-frame steps 46–49.
  - Front tip x0 mean step is −47.23; rear tip mean step is −47.62. The speed is essentially constant, and y stays at about 641–643.
  - For frames 0–1, `ref_x` (1758) is estimated as front tip + 193 because the rear is cut off.
- **Bike length:** 376–386 px, mean 381 (frames 2–28). It shrinks slightly as the bike moves left, fitting len ≈ 373.2 + 0.0072·x. Use about 381 ± 5 px, or the value at the frame in question.
- **Bike width:** about 90–106 px for the cyan handlebar; about 118–119 px for bike + rider hands/elbows.
- **Pedestrian**
  - Head x goes from 64.9 to 414.5 (frames 0–28). Over frames 1–28 that is 349.6 px, a mean of 12.95 px/frame.
  - Per-frame steps are 9–15.5 px: a walking-gait surge, slower at frames 22–27.
  - Head y is 434–440.
  - Mask/bbox centres swing with the stride: steps of 6.5–22 px.
- **Pedestrian extents**
  - Along the motion (x bbox): 117–225 px. Smallest with legs together (frames 15–18), largest at full stride (frames 2–9 and 23–27).
  - Across (y): 127–134 px (shoulders and arms).
  - Head blob: about 45–50 px across.
  - From a top view the standing height can't be measured.

## Events
- **Frames 0 and 1 are pixel-identical:** neither object moves between them, and motion starts with frame 1→2. A backward-difference speed at frame 1 would come out as 0. Treat this as a held first frame.
- **No other events:** no direction changes, contacts, bounces, starts or stops.
- **They approach head-on in x on parallel lines** about 200 px apart in y. At frame 28 the bike centre (478.5) is still 64 px to the right of the pedestrian's head x (414.5). The bike's front tip passes the head's x near frames 23–24.

## Reliability and ambiguities
- **Bike centre and tips:** reliable to ±1–2 px per frame (the cyan rack and wheel ends are crisp).
- **Pedestrian origin (pelvis):** not directly visible. Head x is smooth and recommended for positions and speeds. The mask/bbox centre is noisier because of leg swing.
- **Perspective parallax:** tall parts are pushed outward from the image centre (960, 540).
  - The rider's head shifts relative to the bike by about 0.040 px per px of image x (offset +52 px at x≈1711, +3 px at x≈478).
  - So the image motion of a high point is about 4–5% larger than ground-level motion. The pedestrian's head is likely displaced ≈30–45 px toward the left edge relative to their feet and pelvis.
  - The 2D/one-scale assumption therefore holds to within a few percent.
- **Bike length change:** the small (~2.5%) change across the frame also points to slight non-nadir perspective.
- **Scale:** no metric scale is assumed anywhere. Answer sessions should take one metres-per-pixel scale from their prior: bike length ≈ 381 px, bike speed ≈ 47.4 px/frame = 1138 px/s, pedestrian ≈ 12.95 px/frame = 311 px/s (head).
