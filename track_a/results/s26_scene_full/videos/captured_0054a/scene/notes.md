# captured_0054a – measurement record (lab video, 3D, 24 fps, 49 frames, 1280x720)

All values are pixels (x right, y down, origin top-left) and seconds (t = frame/24). No metric scale was assumed.
Lab conventions (from the task): focal length 763 px (0.5959 x 1280), principal point ~(640, 360). The reference
positions are visible object centres back-projected with the given depth, so `cx, cy` in the tracks are what you
back-project: X = (cx-640)·Z/763, Y = (cy-360)·Z/763 (Z ≈ depth for points near the centre; strictly, depth is the
Euclidean range, so Z = d / sqrt(1 + ((cx-640)² + (cy-360)²)/763²)).

## Scene
A room corner with grey padded wall panels and a carpet floor. **Camera static** (max background shift 0.08 px, `tracks/camera_shift.json`).
- **Seated person** (black clothes, long dark hair) sits cross-legged on the floor at the left. Her right hand (image right) pushes the
  **basketball** (orange), which rolls toward the camera and to the right and leaves the frame at the bottom. A little later her left hand
  pushes the **soccer ball** (white with black pentagons), which rolls toward the camera and to the left and leaves the frame at the bottom-left corner.
- **Standing person** (blue zip hoodie, dark trousers, white sneakers) stands against the back wall between two tripods holding a
  **yellow ball** (tennis ball, image-right hand) and a **pale ball** (white/pinkish-grey, image-left hand). She throws both together up and to the
  left. They peak, fall, each bounces once on the floor (yellow f37, pale f38) and fly on toward the seated person's head; the clip ends (f48)
  as they reach her face. Contact is not confirmed within the clip.
- Static items: left tripod, right tripod (taller, orange cable), black wall TV, ceiling camera, two wall outlets, floor tapes (white strip in
  front of the standing person, white line at the bottom edge, small yellow mark at the bottom right), cables on the floor.

## Files
- `scene.json`: inventory (what tells each object apart, whether it moves, visible frames, pixel sizes), events, camera and perspective cues.
- `tracks/<ball>.csv` for basketball, soccer_ball, yellow_ball, pale_ball: one row for every frame 0-48. Columns:
  `cx,cy` = reference point (visible centre of the mask; for border-cut big balls the centre of a circle fitted to the visible arc);
  `mask_cx,mask_cy` = raw mask centroid; bbox (inclusive px); `major_len/minor_len/major_angle_deg` = PCA extents of the mask
  (the long axis is mostly motion blur); `area_px`, `equiv_diam` = 2·sqrt(area/π); `circfit_diam` (border-cut frames only);
  `truncated`; `state`; `occluded` (1 = hand on or around the ball); `reliability`; `note`.
- `tracks/<ball>_auto.csv`: raw output of track.py (the same numbers without the state columns).
- `tracks/standing_person.csv`, `tracks/seated_person.csv`: rough automatic silhouette extents. **The bounding windows leak** (wall shadows, cables).
  Use the hand-measured values in scene.json instead: standing person head top y 207.5 (f0) / ~203 (f40), sole bottom y 542.5, so
  standing height ≈ 335 px (±3) at the back wall; shoulders ~97 px wide; feet at x 620-690.
- `scripts/`: common.py (decoder), background.py (median backgrounds, written to ../frames/ as scratch), track.py, finalize.py,
  people.py, camera.py, probe_*.py, cropsheet.py / ovsheet.py / zoom.py (visual checks), check.py.

## How measured
- Basketball: HSV orange mask, closed, then opened (31 px kernel until f11, 15 px later) to cut off the arm and the orange cable, then the component nearest the prediction.
- Soccer ball: pixels that differ from a background (median of f41-48 up to f26, median of all frames after that), are white or black (not skin),
  and lie in a window around the prediction. After morphology the mask is filled to its convex hull. If it gets taller than the last good height
  (arm or shadow leak on top), the top is trimmed.
- Yellow ball: HSV yellow mask. Pale ball: changed vs median background, low saturation, bright.
- Every track was drawn on the frames (contours + centres) and checked by eye (frames/masks/*.jpg, scratch, not part of the record).

## Reliability / ambiguities
- **Basketball**: f0-9 the hand touches the top of the ball (occluded=1, mask good). From f23 the ball is cut by the bottom edge. cx,cy then
  come from a circle fit, and the fit diameter (90→105) is inflated by horizontal motion blur, so treat cy for f29-33 as poor. Apparent size
  ~64-71 px (f0) → ~90 px tall (f22). bbox_w is inflated by blur once rolling.
- **Soccer ball**: at rest f0-23 under the hand, ~66 px diameter, centre ≈ (157, 613) ± 3 px. f0-7 the mask includes a little shadow at the lower left.
  While rolling (f24-35) it is heavily blurred. Centres are ±5 px, and the bbox is 70-90 px wide (blur). f36-40 it is cut by the border (poor).
- **Yellow vs pale ball**: same size class. Yellow is clearly tracked everywhere. Pale is faint (skin-like colour while held, merges with the hand f19-21,
  nearly invisible blur streak f36-37 where the detected point is only part of the streak). In flight the pale ball is a few px above and right of
  the yellow ball until the bounce, then right of / behind it. Both travel toward the camera on the way down, so their apparent size grows
  (13 → ~25-30 px, partly blur).
- Release frames are approximate (±1 frame): basketball ~f9-10, pale ~f21-22, yellow ~f22-23, soccer push starts ~f23-24.
- Bounce frames = lowest image y: yellow f37 (y≈656), pale f38 (y≈661). With 24 fps the true contact may lie between frames.
- An anonymisation blur patch (pixelated square) sits near the standing person's hands from ~f18. Faces of both people are blurred.
- Perspective cue numbers (corner points, wall lines, horizon y≈285) were read by eye from a 50-px grid, ±10-20 px.
