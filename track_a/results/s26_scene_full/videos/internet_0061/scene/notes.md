# internet_0061 – measurement record

Video: 1920x1080, 30.012937 fps, 116 frames (t = frame / fps, frame 0 at t = 0), real internet footage, treated as 2D.
The view is handheld, looking straight down on a mesh office chair. The seat mesh fills the left two-thirds of the image (x < ~1290) and the
backrest fills the right third (x > ~1330). A vertical plastic rail at x ~1290-1325 separates them.
The only free-moving object is an **acorn-shaped toy**: a white dome plus a black textured cap with a stem. It is held in a hand at the
left with the cap pointing left, and thrown to the right. It hits the backrest, rebounds, and rattles around the lower-right corner of the seat.
It then travels up along the seat/back rail, slides back down and is grabbed by the hand.
Units are pixels and seconds throughout. No metric scale has been assumed.

## Files
| file | content |
|---|---|
| `scene.json` | inventory (objects, distinguishing features, visible frames, pixel sizes), events, camera, perspective |
| `tracks/ball.csv` | **final toy track**, all frames 0-115: `cx,cy` = visible centre of the whole toy (raw image px); `cx_stab,cy_stab` = the same point in frame-0 coordinates (camera drift removed); `bbox_x0..y1,bbox_w,bbox_h`; `length_px,width_px` (main-axis length / width of the mask, or max/min of bbox for manual rows); `axis_deg`; `source`; `occluded` (`hand`, `image_edge`); `note` |
| `tracks/ball_raw.csv` | automatic mask measurements, for reference only (also has mask area, white/black areas, and which colour seeded the mask) |
| `tracks/hand.csv` | coarse skin bounding box of the hand/forearm; use only rows with `valid=1` (frames 0-42 and 100-115) |
| `tracks/camera_shift.csv` | per-frame camera drift relative to frame 0: `dx_px,dy_px` (shift of the image centre), scale, rotation, the 2x3 affine (frame-0 px → frame-i px), and the individual landmark shifts and correlations |
| `scripts/` | every script used (camera_tm.py = camera drift, background.py, track_ball.py, manual_boxes.json, merge_ball.py, track_hand.py, gridcrops.py / check_overlay.py for visual checks, events.py, mesh_period.py, gridframe.py) |

## How the toy track was made, and how reliable it is
- **Automatic mask** (`track_ball.py`). The dome is the smooth, bright, unsaturated region; the stripy mesh is never smooth. The cap is the
  very dark region (V<50), with the static black gaps of the background excluded. The mask is the convex hull of the two, refined with GrabCut.
  The centre is the hull centroid. On clean frames the hull boundary was checked visually and matches the silhouette to within ~5-10 px.
- **Manual boxes** (`manual_boxes.json`, `source=manual_bbox`) replace the automatic mask in these frames: 0, 20, 38, 44-46, 58-62,
  67-78, 80-83, 85-99 and 108-115. These are frames with motion blur, the black cap over the black seat gaps or the dark rails, or the hand
  over the toy. Each box is the whole toy (cap + dome, stem excluded where it sticks out), read by eye from 1:1 gridded crops. The reading
  accuracy is about ±8 px per edge, so the centre is good to about ±5 px.
- **Held frames 0-38** (`manual_bbox_shifted`): the manual whole-toy box from frame 0, 20 or 38 is shifted by the automatic centre motion.
- **Frames 39-43** (`dome_mask_plus_cap_offset`): in flight the cap trails on the left and is smeared by blur, so the mask holds only the
  dome. The box was extended 95 px to the left (the cap thickness measured in frame 0). The centre is uncertain by ±20 px in x, and the box
  widths of ~290-320 px include blur.
- **Frames 44-46**: strong motion blur at the backrest impact. These are manual boxes around the blurred silhouette, uncertain by ±15 px.
- **Frames 60-63**: the toy touches the bottom image edge (y=1079). The box is truncated at the bottom by a few px, so `cy` may be a few px too high.
- **Frames 108-115**: fingers cover part of the toy. The box is the estimated whole-toy outline, ±10 px.
- Path check: `frames/path.png` (scratch) shows a smooth, physically plausible path. The `check_overlay.py` sheets were viewed for every frame.

### Toy size in pixels (for a size prior)
- Held, frame 0: the whole toy spans x 182-460 and y 405-672, i.e. **length 279 px** along its axis (cap end to dome end, horizontal, which is
  also the throw direction) and **width 268 px**. The stem adds ~25 px on the left. The dome alone is ~182 x 245 px.
  The median over the held frames 0-38 is 288 x 261 px.
- On the seat the toy is farther from the camera and appears smaller. Dome facing up, frames 47-57: median bbox 221 x 226 px (mask
  length/width ~232/209). Frames 79-85: ~199 x 188 px. Side view with cap at the top, frames 92-99: ~210-236 wide x 241-261 tall
  (cap + dome + stem).
- Because the toy tumbles, its apparent length changes with orientation. For a "length along the motion direction" convention, the
  cleanest frame is the held frame 0 (279 px, horizontal = throw direction). For an on-seat size, use 47-57 (~220 px).

## Motion summary (frame numbers; positions are the centres in ball.csv)
- 0-38: held, drifting < 60 px. 38: throw begins. **39: first free frame (release).**
- 39-45: flies right (x 342 → 1432, y ≈ 536 → 488). The image displacement per frame grows from ~37 to ~260 px with heavy blur.
- **45: impact with the backrest** (rightmost point). 46: reversal.
- 46-52: rebounds left and down to the leftmost point at 52 (x≈732, y≈735). It then curves right and down along the seat (53-57).
- 58-62: at the bottom rail (y≈920-970). x reverses at 58 and at 61. Lowest point is at 60 (y≈970).
- 62-65: moves right to the seat/back rail (x≈1317 at 65), reverses at 66.
- 66-75: bounces between the rail region and x≈1155-1180: 69 is leftmost, 72 is at the rail (x≈1332), 75 is leftmost again.
- 74-94: moves up along the seat/back junction (x≈1230-1290), from y≈780 to the top at y≈160 (frames 94-95, near the top seat rail).
  94-97: nearly stopped.
- 96-108: slides back down at ~15-20 px/frame (y 167 → 371).
- 100: the hand re-enters at the top-left. **108: fingers contact the toy.** 108-115: grabbed, the toy nearly still under the hand at
  (≈1230-1250, 430-460).
- The motion is not a single straight line. For speed questions over a time window, take the centres from ball.csv, preferably
  `cx_stab,cy_stab`. Per-frame jitter is ~5 px on manual rows.

## Camera
The camera is handheld but nearly static. Chair landmarks (`camera_tm.py`, 6 non-repetitive templates on the chair frame and rail, plus a
similarity fit) show the image content drifting left by ~23 px and down by ≤5 px between frames 0 and 100, with ~0.7° rotation and <0.5%
scale change. I did not trust ORB features (`camera.py`): the periodic mesh makes them lock to the wrong period, and they under-estimated the drift.
Frames 105-115: the hand covers the landmarks, so the frame-104 transform is held. `cx_stab/cy_stab` apply the inverse transform.
For toy motion the correction is small relative to the displacements.

## Static scene (frame 50, px)
- Seat mesh: x ~12 (left rail) to ~1290 (seat/back rail). The vertical span between the top and bottom rails is ~863 px at x=1000
  (y 125-988) and ~856 px at x=1200 (y 119-975). Near x≈600 it is nearly the full image height (the seat is waisted).
- Horizontal mesh stripes: period **24-25 px** (24 at the right/top, 25-26 at the left/bottom; `mesh_period.py`). This is mild perspective,
  so a single planar scale is a reasonable approximation.
- Seat/back rail: x ≈ 1290-1325 (≈1275-1310 near the top). Backrest mesh x > ~1330, tan, sunlit, with large moving shadows.
- Plastic clips: top centre (x≈925-1060, y 0-55) and bottom centre (x≈960-1240, y≈1010-1080). Black gaps behind the rails at the top right
  (x≈1080-1290, y<60) and at the bottom.

## Ambiguities / cautions
- The cap is black, as are the gaps behind the seat rails and the toy's own shadow. In frames 69-72 and 86-98 the cap edge against these is
  ±10 px.
- The toy's shadow (dark, below/right of it) is not part of the toy. It was excluded by eye in the manual boxes.
- Motion blur in 39-46 and 89. Blurred extents overstate the size along the motion direction.
- The held toy (0-38) is closer to the camera than the toy on the seat. Pixel sizes therefore differ by ~25% between the two phases;
  this matters if a size prior is applied to motion measured on the seat.
- `hand.csv` boxes include the forearm and are coarse (skin colour). Rows with valid=0 are false detections.
- The scratch images in `frames/` are only visual checks (not part of the record).
