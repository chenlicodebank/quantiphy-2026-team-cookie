# internet_0039 – measurement record (pixels, seconds)

Video: 2160x3840 portrait, 72 frames, fps 18.537415 (t = frame/fps). The source is internet footage and the scene is 2D.
Content: a top-down (overhead) view of one swimmer doing front crawl (freestyle) in a lane between two lane ropes
(red/white/blue floats). The swimmer swims toward the top of the image (-y) the whole clip. There are no other people or objects.

## Files
- `scene.json`: inventory, static-object sizes, camera, events and summary numbers.
- `tracks/swimmer.csv`: one row per frame (0-71) with these columns:
  - `cx,cy`: visible-mask centroid
  - `bbox_*`, `bbox_w/h`: axis-aligned mask box; the swimmer's main axis is vertical, so `bbox_h` is the length along the motion
  - `len_main/wid_across/axis_deg`: PCA extents of the mask
  - `area`
  - `head_x/head_y`: swim-cap centre (template matching) and `head_score` (match score)
  - `hip_x/hip_y`: centroid of the black trunks, used as a pelvis proxy; also `trunks_area` and `trunks_bbox`
  - `head_to_feet`: cap top (head_y − 48) to the lowest mask row
  - `occluded`: always 0
  - `duplicate_of_prev`
- `bgshift_raw.json`: frame-to-frame phase-correlation shift (dx, dy, response) of 4 vertical background strips.
- `static_measure.json`: lane-rope centre lines, widths and float-pattern period at frames 0 and 71.
- `scripts/`: every script used (`bgshift.py`, `rope_red.py`, `segment.py`, `track_swimmer.py`, `static_measure.py`, `summarize.py`, `build_scene_json.py`).

## Method and reliability
- **Camera: static.** The rope strips shift less than 1 px per frame. The red-float groups move only about 7 px between frames 0 and 71, which is rope bobbing, not a pan. The float pattern repeats every ~202 px, but a per-frame shift that large is implausible, so aliasing was ruled out. Positions are image coordinates and need no background compensation. The edge-strip correlations (edgeL/edgeR) have low response and are unreliable; ignore them.
- **Duplicate frames 1, 11, 20, 30, 40, 50, 60 and 70** are exact copies of the previous frame (frame-rate conversion). On those frames every track shows about 0 displacement, and on normal frames about 19–24 px per frame. Fits over many frames are robust to this. One-frame differences that land on a duplicate are artefacts.
- **Swimmer mask:** water has G−R ≈ 55–65; swimmer pixels have G−R < 38. After morphology the largest blob is kept. I checked the overlays visually at 10 frames, and they cover the full body, including the extended arm and the partly submerged legs. Feet and toes underwater are faint, so the bottom edge is uncertain by about ±20 px. Splash next to a recovering arm can widen the box slightly.
- **Head (cap) track:** the smoothest reference point (template score 0.72–0.99; lowest around frames 28–30 and 46–47 when the head turns to breathe). It moves from y = 2079 at frame 0 to 775 at frame 71: net 1304.7 px, path 1342 px. A linear fit gives −18.64 px/frame (−345.6 px/s) with 10.6 px rms residual. The mean step over non-duplicate frames is ≈ 20.7 px. x stays between 937 and 1047.
- **Hip (trunks) track:** net 1262.5 px from frame 0 to 71, fit −18.1 px/frame. It wobbles ±10 px with body roll and splash. Splash splits the trunks at frames 68–69; there I merged the dark blobs.
- **Mask centroid:** net 1266 px, but it shifts with arm position, so it is less suited for speed.

## Sizes (px)
| Measure | Value |
|---|---|
| Body length, cap top to feet (excluding arms) | median ≈ 1041 (985–1082 over the stroke) |
| Full mask extent along motion, including extended arm | median ≈ 1295 (1122–1372) |
| Mask width | 285–504 (widest at arm recoveries, frames 10, 43, 66) |
| Hip to head centre | ≈ 455 |
| Cap | ≈ 110 × 125 |
| Shoulders | ≈ 280 (manual, blurry) |
| Trunks | ≈ 209 wide × 170 long |
| Lane width between rope centres | ≈ 1364 at y = 1920 (1350–1400; the ropes bow slightly) |
| Rope width | ≈ 44–60 |
| Red float group period | ≈ 202 (each red group ≈ 58 long) |

## Events
- The swimmer is already moving at frame 0 and still moving at frame 71; there is no start or stop.
- Right arm recovery (widest sideways sweep): frame ~10 and frame ~66.
- Left arm recovery: frame ~43.
- Right arm extended ahead of the head: frames 19–30. Left arm extended: frames 0–8 and 49–60.
- One stroke cycle takes about 56 frames (≈ 3.0 s).

## Ambiguities
- If "the swimmer's length" is ever asked, it is ambiguous: body (cap to toes) ≈ 1041 px versus the full extent with the arm stretched forward ≈ 1295 px. Annotators measuring along the motion probably used one of these.
- Which point is "the swimmer's position" also matters: head and hip agree on average speed within about 3%.
- Pool floor markings are faint and distorted by the water.
- No metric scale is assumed.
