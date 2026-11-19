# captured_0035b: measurement record

**Video:** lab recording (Orbbec Femto Mega RGB), 3D scene, 1280x720, 24 fps, 49 frames (t = frame/24, 0 to 2.0 s).
All values are in pixels and seconds. No metric scale is assumed.
By the benchmark convention the intrinsics are f = 0.5959 x 1280 = 763 px, with the principal point near (640, 360).

## Scene
A high camera looks down into the corner of a grey-carpeted room. There are two people and two balls.
- **person_A** is on the left: a girl with long brown hair, a dark-grey T-shirt, black trousers and white sneakers (face blurred). The bottom border cuts off her feet, and from about frame 13 the left border cuts off her left side.
- **person_B** is on the right, by the back wall: light-grey top, blue-grey loose jeans and white sneakers with black stripes. Their head and shoulders are above the frame, so only the chest down is visible.
- **basketball**: orange. It rests at about (829, 281) beside person_B's feet.
- **soccer_ball**: white with black pentagons. It rests at about (439, 680) at person_A's right foot and touches the bottom border.
- At frame 11 both people kick at the same time:
  - person_A kicks the soccer ball up and to the right (away from the camera).
  - person_B kicks the basketball down and to the left (toward the camera).
- The balls meet at frames 24-26 (impact at about frame 25). The soccer ball is deflected to the lower right and slows from about 12 to about 6-7 px/frame. The basketball hardly deviates and keeps moving at about 12-13 px/frame.
- From frame 45 person_A's hands reach the basketball, and by frame 48 she holds it. The soccer ball is still rolling at the end.

## Files
- `scene.json`: inventory, events, camera, static-object and perspective data, and a frame-by-frame check of ball-ball contact for frames 20-31.
- `tracks/basketball.csv` and `tracks/soccer_ball.csv`: every frame 0-48.
  - `cx_px, cy_px` = the ball's visible centre (reference point). `diam_px` = fitted circle diameter, and `bbox_*` = that circle's box.
  - `diam_px_smooth5` = 5-frame running mean of `diam_px`.
  - `mask_*` = box and major/minor extents of a region mask. These include the white segmentation halo and the contact shadow, so they are about 5-15 px too large. Use them only as an upper bound.
  - `method`:
    - `circle` = edge-based circle fit
    - `interp` = fit rejected, centre interpolated from neighbouring frames
    - `manual_static` / `manual` = read by eye
    - `mean_circle_mask` = average of the circle fit and the mask centroid
  - `occl_or_contact` and `flags` mark contact with a foot, hand or the other ball, truncation by the border, and occlusion.
- `tracks/person_A.csv` and `tracks/person_B.csv`: keyframes only (0, 11, 12, 18, 24, 36, 42, 48). They give the bounding box, an estimated pelvis/visible centre, person_A's head top, and notes on foot positions. All were read by eye from 50-px grid renders and are good to about ±10 px.
- `tracks/*_final.json` hold the same ball centres and diameters for scripts. `basketball_raw.csv` is the first-pass orange-mask centroid. `soccer_ball_raw.csv` is superseded and should not be used.
- `scripts/`: every script. Run order: `track_balls`, `probe_soccer`, `refine_balls`, `circle_fit`, `finalize_balls`, `halfmax_size` (check only), `static_soccer`, `bball_profile`, `frame_diffs`, `room_lines`, `people_and_overlay`, `make_scene`.

## How the measurements were made and how reliable they are
**Camera.** The camera is static: phase correlation on the upper wall region finds less than 0.5 px of shift in every frame.

**Ball centres.** Each centre comes from a circle fitted with RANSAC to the steepest colour-contrast edge along 72 rays from the ball, seeded from colour masks. I checked them visually on montages (`frames/circle_*.png`) and on a full-frame overlay (`frames/overlay_tracks_26.png`).
- Accuracy is about ±1.5 px on free-rolling frames and about ±3-5 px on the flagged frames.
- Basketball frames 45-48: hands are over the ball, and frames 47-48 were read by eye (about ±5 px).
- Soccer ball frames 11-13: foot contact and heavy blur (about ±6 px).
- Rejected fits, filled by interpolation: soccer frames 14, 17, 26, 32 and 43; basketball frame 40.

**Diameters.**
- **Best values are on the static frames 0-10:**
  - Basketball: 53.1 px (horizontal 50 %-contrast width 54 px).
  - Soccer ball: 68.9 px. This was fitted by hand to edge points because the bottom of the ball is at y ≈ 715, at the image border, and a shoe touches its left side.
- In moving frames, motion blur (a smear of about 10-25 px/frame) inflates the fit by roughly 1-3 px along the motion direction, and single frames scatter by ±2-3 px. For an apparent-size or depth estimate, prefer `diam_px_smooth5` or a median over several frames.
- A half-contrast area measure (`halfmax_size.py`) was tried as a check but rejected. On the basketball it misses the shaded lower half, and on the soccer ball it misses the black panels.

**Apparent-size trend (perspective).**
- Basketball: grows steadily from 53 px (rest, far) through about 60 (f20) and 67 (f30) to about 72.5 px (f44-46). It is coming toward the camera.
- Soccer ball: 69 px at rest (very near the camera), about 52-54 px at frames 21-31 (farthest), then about 57-59 px at frames 39-48.
- Under a pinhole model Z ≈ f·D_true/D_px, so these give relative depth directly.

## Ambiguities and caveats
- **Dropped frame:** frame 36 follows a dropped source frame. Both balls move about twice their normal step from 35 to 36 (basketball 26 px against about 12.7, soccer ball 11.6 against about 5.9), and the inter-frame difference doubles. The step from 11 to 12 is also large (kick onset, possibly another irregular frame). Per-frame speed computed across 35→36 will be about twice the true value. The video timestamps are uniform, so frame index / 24 is still the time convention.
- **Background effect:** the background is blurred by a "Segment Anything 2 Demo" effect, with a watermark at bottom right (x > 1030, y > 690). The balls and people have a faint white halo, and region masks pick it up.
- **Image overlap at impact:** at frames 25-26 the two ball discs overlap in the image (negative gap) because the soccer ball is nearer the camera. Image contact runs from frame 24 to 27.
- **Kick timing:** the soccer ball first moves at frame 11 (by about 5 px, with the foot on it). The basketball first moves at frame 12. Both balls are free of the feet by frame 14.
- **People:** neither full height is measurable, since person_B's head is out of frame and person_A's feet are cut off. Their boxes are keyframe estimates, not per-frame tracks, because the automatic people segmentation failed on the blurred but textured background.
- **Room geometry (ground-plane cues):**
  - Wall/floor baselines: left wall y = -0.537x + 518.0 (x 280-590); right wall y = 0.1998x + 70.6 (x 620-1270).
  - Floor corner at (607.6, 192.0).
  - The vertical wall corner tilts from x ≈ 562 at the top to x ≈ 600 at y = 160, which indicates camera roll plus a downward pitch.
