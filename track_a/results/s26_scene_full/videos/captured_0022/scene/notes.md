# captured_0022 – measurement record

**Scene.** This is a lab recording (3D, 24 fps, 49 frames, 1280x720). A small white ball sits at the back (upper, far) edge of a tilted
light-brown wooden board. It rolls down the board toward the camera, which in the image means down and slightly left.
It rolls off the front (near, lower) edge at the very end and starts falling. The camera is static. The background was blurred by a
"Segment Anything 2" edit, and a person (jeans, head blob), a stand, a tripod and some equipment are visible only as blur.

## Files
- `scene.json`: inventory (ball, board and the blurred background items), board corner pixels, events, camera and perspective notes.
- `tracks/ball.csv`: the ball in every frame 0-48. Columns:
  - `frame`, `t_s` (= frame/24)
  - centre `cx_px`, `cy_px`
  - bbox `bbox_x0..y1` (inclusive pixels)
  - mask length along its main axis, width across it, mask height, mask area
  - `occluded` (always 0)
  - `state`: rest 0-11, rolling_on_board 12-45, leaving_edge_falling_motion_blur 46-48
- `scripts/`:
  - `track_ball.py` produces the track.
  - `overlay.py` draws the track on crops so it can be checked.
  - `crops.py` makes zoomed tiles.
  - `check_pts.py` checks timestamps and camera motion.
  - `board.py` and `board_lines.py` measure the board quadrilateral.
  - `_board_corners.json` is the output of `board_lines.py`.

## Method and reliability
- **Ball centre:** the centroid of the mask. A pixel is in the mask if it is whitish (HSV S<45, V>165) **and** differs from a ball-free background by more than 20 grey levels. The background is the per-pixel median of frames 16-48. The background test is what rejects the whitish glare in the middle of the board.
  - The search window is 45 px around a constant-velocity prediction.
  - I checked overlays at frames 0, 5, 11-14, 20, 30, 36, 42, 45-48 and every one hits the ball.
  - **Bias:** the lower, shaded part of the ball (and its dark contact shadow) is partly left out of the mask, so the centroid sits about 1-2 px above the true visual centre. The bias is roughly constant, so differences between frames are good to about ±1 px.
  - Frames 0-11: the bbox also takes in a few halo pixels on the left (x0=426; the ball really spans about x 429-447).
- **Ball apparent diameter:** about 19 px wide and 17-18 px tall at rest (the bottom is shaded). It is about 19-20 px mid-ramp and about 21-22 px at the front edge, so it grows as the ball approaches the camera. In frames 46-48 the mask is stretched vertically by motion blur (27-36 px tall). There, use the width (~21 px) and not the height.
- **Irregular step:** the step from frame 35 to 36 is 11.5 px, against about 6 px for the neighbouring steps. The raw frames confirm it, and the frame timestamps are regular. It is probably a capture or encoding irregularity, such as a dropped sensor frame. The reference annotators' smoothing over 5 or more frames would absorb it. Be careful with per-frame speeds near t = 1.46-1.50 s.
- **Camera:** static. Phase correlation of the upper image against frame 0 drifts by ≤0.16 px. The lab convention is f = 763 px, principal point (640, 360), HFOV 80°; this is given by the task statement, not measured. To get 3D positions, back-project (cx, cy) with this f and the depth_info that a question supplies.
- **Board corners** (top surface): taken from straight-line fits to the board colour mask in the median background, then intersected. They are accurate to about ±4 px, because the corners are rounded and the blur halo adds roughly 2-3 px outward.

  | Corner | x, y (px) |
  |---|---|
  | back-left | 275.0, 413.4 |
  | back-right | 603.3, 356.8 |
  | front-right | 675.4, 512.3 |
  | front-left | 218.7, 615.1 |

  Side lengths: back 333 px, right 171 px, front 468 px, left 209 px. The darker thickness band below the front edge is about 8-10 px. The board is a tilted ramp: the back is higher and farther away, so the left and right sides converge upward.
- **Events:**
  - Rest in frames 0-11; motion starts at frame 12 (t = 0.500 s). The release happens between frames 11 and 12 and no hand is visible.
  - Frame 45 (t = 1.875 s) is the last frame with the ball fully on the board.
  - It rolls off the front edge around frames 45-46. The front-edge line is at y ≈ 576 where the ball crosses (x ≈ 392).
  - In frames 46-48 it is falling, with motion blur, and is still visible at the end.
- **Path in the image:** from (437.0, 378.4) to (392.5, 559.2) on the board, almost straight and slightly to the left (about 14° from image vertical).

## Ambiguities
- The board's whitish glare lies near the middle of the ball's path. The background-difference test handles it, but the centroid there may still be off by about 1 px.
- The ball has a dark contact shadow just below it, which is not part of the ball.
- The background items (person, tripod, equipment, stand) are artificially blurred, so their extents are only rough.
- Only one moving object exists. There are no other balls.
