# captured_0036x — measurement record (pixels, seconds)

Lab recording (Orbbec, 24 fps, 1280x720, 49 frames, 2.04 s), 3D scene. The background was replaced
by SAM2 segmentation: everything except the table and ball is pure white (255), and there is a grey watermark at the
bottom right (x >= 1030, y >= 690). Benchmark intrinsics: f = 0.5959*1280 = 762.8 px, principal point about (640, 360).
Time t = frame/24.

## Files
- `scene.json`: inventory, static-object pixel extents, perspective cues, events.
- `tracks/ball.csv`: per-frame ball track for frames 0-48. Columns: frame, t, visible, occluded, note, cx, cy (centroid of
  the filled mask = visible centre, the reference point for lab videos), bbox_x0/y0/x1/y1/w/h, mask_area,
  len_main_axis / width_across (PCA extents of the mask along and across its main axis), main_axis_deg,
  equiv_diam (diameter of the circle with the mask's area).
- `scripts/track.py` (tracking + overlay PNGs in ../frames), `scripts/static.py` (table extents),
  `scripts/probe*.py` (threshold checks), `scripts/montage.py` (overlay contact sheets).

## Scene / inventory
- **ball**: a small white/cream ball, the only moving object. At t=0 it sits on the far (back) edge of the table top near
  the back-left corner at about (421, 429). It is nearly still for frames 0-12, drifting about 5 px left over frames 4-10.
  It then rolls diagonally toward the camera and to the right across the table top (frames 13-35). Its centre crosses the
  table's right side edge at about frame 35 (871, 514). It falls beside the table with strong motion blur (frames 36-40)
  and leaves through the bottom of the image after frame 40. It is not visible in frames 41-48.
- **table_top**: brown wood-grain rectangle seen in perspective, with its long axis pointing away from the camera.
  Corners are about back-left (405,441), back-right (760,446), front-left (187,588) and front-right (1000,592). The back
  edge is about 355 px wide and the front edge about 814 px.
- **table_edge_band**: dark front face of the top, y 588-626 (about 38 px thick at the front).
- **table_leg**: dark grey central pedestal, x 534-589 (55 px wide), from y 627 down to the image bottom (cut off).
- There are no people, hands or other props; anything that launched the ball is not visible because the
  background was removed.

## Camera
Static: the table pixels do not change between frames beyond compression noise. The table side edges converge to a
vanishing point at about (570, 330), so the horizon is at y ≈ 330, which puts the camera about 2° pitched down. The
apparent ball size grows as the ball approaches the camera: diameter about 24-26 px at frames 0-12, 23-25 px at 15-21
(measured across the motion), about 30-34 px at 25-31, about 46-50 px at 33-34. Late-frame masks are blur-elongated.

## Method and reliability
Mask = pixels that differ from the clean last frame (48, ball gone). In white-background areas this means any pixel
with min(RGB) < 247. In table areas it means a difference > 16 and low saturation (ball is grey/white, table brown).
The largest component near the previous position is taken, then morphologically cleaned and filled as a convex hull.
I checked overlays (frames/ov_XX.png) for all frames.
- Centres for frames 0-35: good to about ±1-2 px. The ball's shaded underside on the wood is sometimes partly missed,
  and a thin white segmentation halo under the ball is sometimes included (frames 24, 29, 32, 34 have an inflated
  height and minor axis). For those frames, prefer the vertical extent of neighbouring frames for size.
- Size: horizontal motion blur stretches the mask along x. width_across (minor axis) or bbox_h is the best diameter
  measure while the ball rolls. At rest (frames 0-12) the ball is about 25 px wide and 22-24 px tall.
- Frames 36-40: heavy motion blur (streak 80-120 px long). The centroid is the streak centre (±5 px). Frame 39 overlaps
  the watermark. In frame 40 the ball is cut by the image bottom (occluded=1), so that centre is unreliable.
- Frames 13-16: the per-frame step alternates (≈10, 15, 19, 17 px) because blur and segmentation vary. Smooth over
  several frames.
- Ambiguous: frames ~16-23 show a dark spot (shadow) slightly below the ball. The ball may be bouncing a little rather
  than rolling, but its centre path is smooth. The start of motion (frame 12-13) and leaving the table (frame 35-36)
  are each uncertain by ±1 frame.
- 3D conversion for answering sessions: X = (cx-640)·Z/762.8, Y = (cy-360)·Z/762.8, using the given depth Z at the
  stated times. The apparent diameter d_px ≈ 762.8·D/Z can relate a known ball size to depth.
