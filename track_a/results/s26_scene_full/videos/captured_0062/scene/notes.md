# captured_0062: measurement notes

**Scene.** This is a lab capture: 1280x720 at 24 fps, 49 frames (t = frame/24, from 0 to 2.0 s), in 3D. The camera is static and looks down a carpeted room floor. The main event: a **flat white board** (a white rectangular plastic board/tray with two small clear clips on its far edge) lies on the floor at the lower right. At frame 16 (t = 0.667 s) it is pushed in from below the frame; no pusher is visible. It then slides away from the camera toward the upper centre-left and is still moving at frame 48. It stays flat on the floor the whole time (it keeps a flat quadrilateral shape). A second, minor moving object is an **orange basketball** in the background, half hidden behind the blue bin. It rolls a little from about frame 17 onward. Everything else is static.

## Files
- `scene.json`: inventory, events, camera, and a summary of the apparent sizes.
- `tracks/white_board.csv`: one row per frame:
  - centroid of the board mask (`cx_px, cy_px` = visible centre)
  - bbox
  - minAreaRect long/short side and long-axis angle (degrees, image coordinates, y down)
  - mask area
  - `cut_by_frame_edge` (1 in frames 0-18)
- `tracks/white_board_corners.csv`: board corners with the clips removed (far-left, far-right, near-right, near-left; "far" = higher in the image) and the four edge lengths in px.
  - The far edge is the one with the clips. Corners are good to about ±3 px from frame 22 on, and about ±6 px in the motion-blurred frames 17-21.
  - In frames 0-18 the near edge runs off the bottom of the image. The near-left corner (≈823,680) is real, but the "near-right" point (≈1124,690) is only where the mask meets the frame bottom, not the true corner. The near edge and right edge are therefore unreliable in those frames.
- `tracks/basketball.csv`: basketball measurements.
  - Visible orange-mask centroid and bbox.
  - `diam_est_px`: vertical extent, roughly the diameter (top and bottom are usually visible).
  - `est_cx/est_cy`: estimated true centre = left edge + d/2 and the vertical middle.
  - Always occluded by the bin on its right side.
- `tracks/camera_shift.csv`: phase-correlation shift of a static wall region against frame 0. The maximum is 0.12 px, so the camera is static.
- `static_objects.json`: static items at frame 48: centroid, bbox, and minAreaRect length/width/angle in px.
- `scripts/`: run from `scene_ws`:
  - `track.py`: board, ball and camera tracks, plus overlays in `frames/`.
  - `corners_post.py`: edge lengths.
  - `static.py`: static objects.
  - `checks.py`: checks that props stay still and prints the board's per-frame steps.
  - `look.py`: crop montage viewer.
  - `hsvprobe.py`, `ballmask_test.py`: colour probes.

## Methods
- **Board mask:** HSV threshold (V>185, S<45) below y=225, with the watermark box at the lower right excluded.
  - The thin white tape line on the floor at the bottom (y>640) is subtracted. In frames 17-21 it would otherwise merge with the board.
  - The board mask is then the convex hull of the largest blob (the board is convex). The hull also repairs the notch where the tape line lies under the board.
  - I checked the overlays (frames 0, 6, 12, 16, 18, 20, 22, 24, 28, 32, 36, 40, 44, 48): the outline follows the board edge, and the clips are included in the bbox.
- **Basketball:** orange hue 2-15, S>120, inside the crop x180-310, y60-200; I took the largest blob. In frames 0-17 a little of the cabinet colour may leak in.
- **Static objects:** colour difference from the crop-border (floor) colour, or a colour class (blue, yellow, white). Each was checked on an overlay.

## Static objects (frame 48, px)
| object | what it is | centroid | bbox (x0,y0,x1,y1) | minAreaRect L x W |
|---|---|---|---|---|
| milk_carton | small white/red drink carton lying on the floor, centre-left | (516,496) | 490,461,544,531 | 76 x 34 |
| plush_bear | brown/orange teddy bear lying on the floor below the carton (box includes some shadow, ±5 px) | (631,632) | 580,578,690,682 | 115 x 87 |
| blue_tote_bag | dark-blue tote bag with a round orange logo, lying flat at the right | (836,330) | 769,294,896,371 | 127 x 77 |
| blue_bin | blue waste bin with a yellow/white pattern, background left | (338,153) | 290,104,384,210 | 95 w x 107 h |
| tennis_ball_near_tripod | yellow tennis ball by the left wall, near the tripod | (152,222) | 144,216,159,228 | ~15 diameter |
| yellow_speck_floor | tiny yellow speck on the floor; hidden under the board until about frame 21 | (913,569) | 908,564,919,575 | 11 |
| white_tape_mid_floor | white tape strip in the middle of the floor | (666,403) | 625,392,707,413 | 84 x 6 |
| white_tape_bottom_floor | white tape strip at the bottom; under the board at the start | (924,691) | 870,661,977,719 | 121 x 12 (cut by the image bottom) |
| wall_outlet_plate | small grey plate on the right wall | (1233,364) | 1215,347,1248,378 | 34 x 27 |

The other static items (pixel positions in `scene.json`) are: the tripod at the left, the wooden cabinet, the seated person and standing person in the background, the cables, and a small yellow tape mark at (995,385).

## Events
- **Board at rest** in frames 0-15.
- **Board starts moving** at frame 16 (1 px), then clearly at frame 17 (t = 0.708 s, 11.7 px step).
- **Centroid steps:** about 24-26 px/frame in frames 19-22. These are inflated while the cut-off part slides into view. They are then about 16-20 px/frame (frames 23-35) and about 12-15 px/frame (frames 37-48), at 11 px for frame 48.
- **No stop, bounce or impact** happens in the clip.
- **Anomaly:** the step from frame 35 to 36 is 31 px, about twice its neighbours. This is probably a dropped capture frame or timing jitter. Answering sessions should consider it when differencing.
- **Basketball:** starts moving at about frame 17. It comes out to the left (frames 17-22), moves down (frames 22-24), goes back right behind the bin (frames 25-35), and comes out left and down again (frames 36-48).

## Perspective and apparent size
The board moves away from the camera along the floor, so its image shrinks:
- minAreaRect long side: 321 → 204 px
- near edge: 301 → 179 px
- far edge: 283 → 162 px
- area: 44.7k → 14.0k px² (frames 0 to 48)

Use the given depth_info together with focal length ≈ 763 px and principal point ≈ (640,360) to back-project the centroids. The floor is the ground plane, and the right wall/floor junction is a strong receding line.

## Reliability
- **Board centroid:** ±1 px when the board is clear (frames 22-48). In frames 17-21 it is blurred (motion blur stretches the mask by about 5-10 px along the motion). In frames 0-18 the centroid is the *visible* centre of a board cut off at the image bottom, so it is biased toward the far edge. The true centre in frames 0-16 lies lower than (961.7,631.7), probably by tens of px.
- **Board sizes:** the clips (about 15 px) are included in the bbox and minAreaRect but excluded from the corners.
- **Basketball:** low reliability (about ±4 px) because of the bin occlusion and the cabinet colour.
- **Static extents:** about ±3 px.
