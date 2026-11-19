# captured_0037: measurement record

Lab recording, 3D, 24 fps, 49 frames (t = 0 to 2.0 s), 1280x720. The camera is static. A person standing behind a
wooden table holds a white ping-pong-type ball over the white cup, then tosses it to the left (toward image-left and
somewhat toward the camera). The ball bounces 4 times: card tent, tape roll, near the glass jar, then the table top. It is
still moving left when the clip ends.

## Files
- `scene.json`: inventory (static object pixel boxes, person extents), camera info, events with frame and time.
- `tracks/ball.csv`: ball in every frame 0-48. Columns: frame, time_s, cx, cy (mask centroid = visible centre, px),
  bbox_x0..y1, bbox_w, bbox_h, mask_len_main_axis, mask_width_across, main_axis_angle_deg, mask_area_px,
  occluded_or_partial, note.
- `tracks/ball_raw.csv`: the same data without flags (output of the tracker).
- `scripts/`: `detect_ball.py` (first candidate search), `track_ball.py` (tracker; also writes frames/ball_overlay.png),
  `finalize_ball.py` (flags and trajectory plot), `camera_shift.py`, `probe.py` (colour sampling), `montage.py` (crop sheets).

## Method
- Ball mask = |gray - per-pixel median background| > 35, HSV V > 165 and S < 45, inside a 60 px window around a
  horizontal-only constant-velocity prediction, then a 3x3 opening. The reference point is the mask centroid. Extents
  come from the mask's principal axes: the main axis is stretched by motion blur, so use `mask_width_across` as the
  apparent diameter. The threshold sits about half way between the wall (~120) and the ball (~230), so the mask
  approximates the half-intensity edge.
- I checked the masks visually in frames/ball_overlay.png and frames/traj.png. All 49 frames hit the ball.
- Camera: phase correlation of the left wall/tripod and table-front regions against frame 0 gives a shift below
  0.15 px in every frame, so the camera is static and needs no correction.
- Static objects: boxes read off zoomed grid views of frames 0 and 48 (±2 px).

## Reliability and ambiguities
- Frames 0-11: the ball is in the hand and partly covered by fingers. The centroid is biased by about 1-3 px and the
  width (~17) is underestimated; the visible length is ~21-22 px.
- Frames 12-13: the ball is still touching the hand. Release is between frames 13 and 14 (t ≈ 0.56 s).
- Bounce frames 19-20 (over the white card tent), 28 (over the pale tape roll) and 35-36 (over the glass jar): the ball
  is low-contrast against the bright object behind it, so the mask is partial. The centroid can be off by up to ~5 px
  there (frame 20 is the worst: only the top of the ball is masked).
- Motion blur stretches the ball along its motion by up to ~20 px when it moves fast (frames 17-19, 26-28, 34-36,
  41-44). Centroids stay good; lengths do not.
- Bounce 3 (frame 36) happens right at the left edge of the jar top. It is unclear whether the ball hit the lid rim or
  the table just behind the jar; part of the ball seems to be seen through the glass.
- Depth: the ball's apparent diameter grows from ~21 px (frames 14-16) to ~26 (22-24), ~31 (31-33), ~30 (38-40) and
  ~33 (45-48), so the ball comes toward the camera as it moves left. With depth_info, the 3D centre is
  X = (cx-640)·Z/763, Y = (cy-360)·Z/763. The given depth is the range to the centre; convert it with
  Z = d / sqrt(1 + ((cx-640)² + (cy-360)²)/763²). Apparent diameter × range / 763 ≈ true diameter; check this against the
  ruler prior.
- Person: only the arm moves. Head top is at y≈22. The lower body is cut off by the image bottom and hidden by the
  table, so the full standing height is not measurable in pixels.
- No speeds or accelerations are given here by design.
