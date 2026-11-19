# captured_0034bx — measurement record (pixels / seconds only)

Lab capture (Orbbec RGB, 1280x720, 24 fps, 49 frames, t = frame/24, 0 … 2.000 s). The background has been
replaced by black (segmented). Only the table top, its leg and the objects on it are visible. 3D scene.
Lab intrinsics from the benchmark convention: f = 0.5959·1280 = 762.8 px, principal point ≈ (640, 360).
No metric scale is assumed anywhere.

## Scene
A wooden table top seen obliquely from above. On it are a black-and-white soccer ball (static, left of centre), a
yellow/orange pencil case (static, diagonal, right of the soccer ball) and two tennis balls:
- **tennis_ball_A**: the deeper, saturated yellow ball. It starts at the left edge of the table at (466.6, 287.3).
- **tennis_ball_B**: the paler yellow-green ball. It starts at the far-right corner at (820.4, 255.9).

Both balls rest during frames 0–23. At frame 24 (t = 1.000 s) both are pushed. The pusher was removed by the
segmentation; only a dark wedge or notch is left next to each ball. By frame 25 both are clearly moving. A rolls right (+x, slightly up-image =
away from the camera), and from frame 31 it passes **behind** the soccer ball, so only its top cap is visible from frame 35 on.
B rolls left and slightly down-image (toward the camera). They **collide at frame 38 (t = 1.583 s)**: the
centre distance is 47.7 px at frame 37 and 32.9 px (≈ one ball diameter) at frame 38. After the collision, A reverses and drifts slowly left (−x,
about 1–3 px/frame, still behind the soccer ball). B reverses its x motion and moves down-right toward the camera (about 2–3 px/frame).
Both are still moving slowly at the last frame (48).

## Files
- `scene.json`: inventory, static-object pixel geometry, events, camera and perspective notes, and rest positions.
- `tracks/tennis_ball_A.csv`, `tracks/tennis_ball_B.csv`: one row per frame (0–48). Columns:
  `ref_x, ref_y` = the ball's visible centre (circle fit, the reference point to use); `radius_px`/`diam_px` = the radius used
  (free fit when unoccluded, fixed 15.5 px when occluded); `radius_free_fit` (NaN when occluded); mask centroid;
  bbox (`bbox_*`, `bbox_w`, `bbox_h`); `mask_area`; `mask_len_main`/`mask_wid_across` = mask extent along and across its
  principal axis; `main_axis_deg`; `occluded` (1 = partly hidden by the soccer ball or touching the other ball); `note` (events).
- `tracks/raw_tennis_ball_*.csv`: raw tracker output (same numbers, column names `cx, cy, r_used`).
- `static_raw.json`: raw static-object measurements at frames 0, 24 and 48.
- `scripts/`:
  - `track_balls2.py`: the final tracker; run it before `finalize.py`.
  - `finalize.py`: writes the final CSVs and `scene.json`.
  - `static_objs.py`: soccer ball, pencil case and table silhouette.
  - `framediff.py`: camera-motion and frame-timing check.
  - `overlay_tracks.py`, `crops.py`, `maskview.py`, `profile.py`, `hsvstat.py`: visual and pixel checks.
  - `probe.py`, `track_balls.py`: first attempts, superseded.

## Method
Colour mask: (hue 23–35, S>60, V>90) OR (hue 24–40, (G+R)/2−B>40, V>120) OR the pale highlight cap (hue 23–34, S≥25,
V≥235). Static pencil-case pixels are removed with a frame-0 mask. Components are assigned to the nearest predicted ball.
When both balls fall in one blob (frames 38–39), it is split by nearest centre and refined with fixed-radius circle fits.
The centre comes from a least-squares circle fit to the mask outline. Outline points on the soccer-ball circle or next to the other ball are excluded.
When a ball is occluded, the radius is fixed at 15.5 px and only the centre is fitted (soft-L1). The overlays (frames/ov2.png, ov1.png) were checked by eye: the circles sit on the
balls in all checked frames (0, 25, 27, 30, 33–42, 45, 48).

## Reliability
- **Ball B centre**: about ±1 px at rest and ±1.5 px while moving. Motion blur (up to about 15 px/frame at frames 25–27) widens the
  mask along x, but the circle centre stays central. At frame 48 a manual edge read gives (676, 299) against the track's (677.4, 300.7):
  the shadow under the ball can pull y down by about 1–2 px.
- **Ball A centre**: ±1 px at rest and while moving in the open (frames 25–30). From frame 31 on it is behind the soccer ball, and from 35 on only the
  top cap (about 10–20 px tall) is visible. The centre is then inferred from the cap's arc with r = 15.5, so y is uncertain by about 2–3 px
  and x by about 1–2 px.
- **Apparent ball size**: the visual edge diameter is about 30–32 px for both balls throughout. At rest, the free-fit radius (13.7–14.5) is biased
  low because the pale rim and the segmentation cut under the balls are missed. When moving, it is biased high (15–16.8) by motion blur. The
  apparent size change over the clip is within about 1–2 px, so it is not a usable depth cue. Use the given depth_info instead.
- **Frame-timing jitter**: between frames 35 and 36 both balls move about twice their normal per-frame step (A +22 px, B −19 px). Frame 35
  has a smaller frame difference. This looks like an irregular capture interval, not physics. Per-frame speed there will spike, so smoothing over 5 or more frames (as the
  reference does) is advisable.
- **Motion start**: the shift at frame 24 is about 1 px. Frame 25 is unambiguous.
- **Collision**: frame 38, ±1 frame. A's overlap with the soccer ball in the image (frames 31–48) is depth occlusion, not contact (A is
  farther from the camera).

## Static objects (frame 0; frames 24 and 48 agree within 1 px)
- Soccer ball: centre (601.5, 318.3), radius 48.3 px (diameter ≈ 96.6), bbox x 555–650, y 270–368.
- Pencil case: centre (695.5, 349.5), length ≈ 95 px, width ≈ 30 px, long axis at −27° (rising to the right), bbox x 656–739, y 320–379.
- Table top corners: far-left (502, 242), far-right ≈ (815, 250) (ragged, next to ball B), near-left (435, 418), near-right (852, 432).
  Far edge ≈ 313 px, near edge ≈ 417 px, sides ≈ 185–188 px. The front face band runs from y ≈ 418–445.
- Table leg: x 635–660 (25 px wide), visible from y 432 to 536, where the segmentation cuts it.

## Camera and perspective
The camera is static: the table/leg region shift against frame 0 stays below 0.2 px in every frame. The table side edges converge to a vanishing point at
(703, −287), above the image. The far and near edges are nearly horizontal. If the table is level and the principal point is (640, 360) with f = 763,
the camera is tilted down about 40°. Larger image y on the table means closer to the camera. B ends nearer to the camera than it starts (y 256 → 301).
A's y changes only from 287 to 272.

## Ambiguities
- The two tennis balls look alike. A is the more saturated yellow and starts on the left; B is paler and starts at the far right.
- A is hidden behind the soccer ball for most of its post-collision motion.
- Shadows under the balls are excluded from the mask only by the hue/V thresholds.
- The pusher is invisible because of the segmentation.
