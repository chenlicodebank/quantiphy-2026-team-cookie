# simulation_0011 — measurement record

Simulation (Blender) render, 3D scene, 24 fps, 60 frames (2.5 s), 1920x1954 px. t = frame/24. All values are in
full-resolution pixels (x right, y down) and frames; no metric scale has been assumed.

## Files
- `scene.json`: the inventory (moving and static objects), events, camera notes and static pixel extents.
- `tracks/crow.csv`, `tracks/black_fuzzy_ball.csv`: one row per frame (0-59) with frame, t, mask centroid (cx, cy) =
  the reference point, bbox (x0, y0, x1, y1, centre, w, h), area_px, eq_diam (=2*sqrt(area/pi)), minAreaRect
  main_axis_len / across_width / angle, an occluded flag and a quality note.
- `scripts/`: survey.py (coarse difference survey), track.py (full-res ROI tracking and overlays), export.py
  (CSV writer), crops.py (zoom-crop viewer), camera_check.py (background shift), check_record.py, cleanup.py. _rows.pkl holds the raw track rows. The bg_*.png
  clean backgrounds were deleted to save space; running track.py makes them again.

## Method
For each object ROI, a clean background is built as the per-pixel median over the frames where that pixel is not
covered by the dilated preliminary mask. Mask = pixels darker than the background by a colour difference above a
threshold (60 for the ball, 35 for the crow), followed by morphological open and close. The tracker keeps the
blob nearest the previous position and, for the crow, merges fragments within 12 px (split wings). I drew the
masks on frames and checked them visually (frames/ov_*.png).

## Objects
- **crow**: the only bird. It is black and flies left→right in front of the house gable for the whole clip (x 1029
  → 1758, y 1034-1106, with up-and-down motion from the wingbeat). Its extents oscillate with the wing flaps. bbox_w is
  a wingspan proxy (about 100-150 px). The reference point is the mask centroid, which is roughly the body. The
  origin of the rig is not visible, so the centroid shifts by about ±10 px with wing pose. **Frames 5-15 are
  unreliable**: the crow is against dark foliage and the eave post, the mask is partial and the centroid is biased
  left by about 10-30 px. Over those frames x jumps from 1068 to 1110 between frames 10 and 11; interpolate if needed.
  A faint crow shadow moves right on the lawn at y ≈ 1370-1390. It is not tracked.
- **black_fuzzy_ball**: a black, furry/fuzzy, roughly round object near the camera on the left. It could be a
  fuzzy ball or a small dark animal; at rest on the ground it looks like a dome. It starts on a branch partly hidden
  behind the big tree trunk and leaves at about (219,1072) and stays almost still for frames 0-15. It drifts down
  slowly from frame ~16 and is clearly falling from frame ~24, with increasing downward pixel steps. It lands on the
  lawn by the trunk base at (294.6,1543.9) on **frame 50 (t = 2.083 s)**, with no bounce, and stays there until
  frame 59. Its mask area grows from frame 28 to 39 mainly because the trunk and leaves stop hiding it (it is not
  approaching the camera). The full apparent diameter is ≈120-135 px (frames 38-43), and the ground dome is 134 x 75
  px. Frames 0-31 are flagged occluded, so their centroid is that of the visible part only and biased right/down.
  Frames 44-49 are motion blurred (the mask is elongated along the motion by up to about 140 px). The start-of-motion
  frame is uncertain by ±4 frames.

## Camera and 3D cues
The camera is static (shift below 0.03 px). The ground plane is the lawn. Its depth ordering is: tree base y≈1550
(nearest, which is where the ball lands), then cart wheels y≈1435, then house base y≈1365. The horizon is hidden by
trees and is probably around y≈1000-1100. Vertical lines stay near-vertical, so the camera is roughly level.
Assumed principal point (960,977). The focal length must come from the depth_info + prior given with each question.
The crow is far (at about the house gable), and the ball is near (at the foreground tree).

## Static objects (from frame 0/59; ±5 px)
These are in scene.json. The house front wall is 460 px wide (x 1115-1575), its base is at y 1365, the gable apex
at y 890 and the crossed beam tips at y 775. Doorway 65x205. Door leaf 80x195. Two barrels about 70-77 x 90.
Cart (cut off by the right edge) with wheel diameter ≈172 px. Also the white flower bush, big left tree (trunk
x 100-185), small round tree, bright tree behind the house, pink shrubs in the foreground, and the lawn with
shadow patches.

## Ambiguities
- The identity of the "ball" (furry ball or animal) is uncertain.
- The mask edges of both objects are soft (fur, feathers, defocus, motion blur), so sizes carry about ±5-10 px of
  uncertainty.
- The crow's size varies with wing pose. Use the min/max over frames for wingspan questions.
