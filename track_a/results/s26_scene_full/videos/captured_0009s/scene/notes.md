# captured_0009s — measurement record

**Content.** This is a lab capture (24 fps, 1280x720, 49 frames, 2.04 s). The background was replaced with a green gradient using SAM2; a watermark sits in the bottom-right corner. The only object is an **orange basketball**. It is held almost still for frames 0–26, with the holder's hand masked out, which leaves a cut-out notch in the lower half of the ball. It is released at about frame 26 (t = 1.083 s), falls down and slightly to the right in the image, and bounces off the floor at frame 37 (t = 1.542 s; lowest centre y = 657 px). It rises to an apex at frame 46 (t = 1.917 s, y = 481 px) and starts falling again. No floor, holder or other static object is visible, so there are no static-object extents to record. The camera is static: consecutive-frame background difference is < 0.5 grey levels, and container timestamps are uniform.

## Files
- `scene.json`: inventory, camera, events and anomalies.
- `tracks/basketball.csv`: one row per frame (0–48). Columns:
  - `cx_fit, cy_fit, r_fit, diam_fit`: a circle fitted to the outer contour points of the merged orange mask (only points on its convex hull, so cut-outs don't bias it). **This is the reference centre.**
  - `cx_mask, cy_mask`: mask centroid. It is biased while the ball is cut (frames 0–31).
  - `bbox_*`: bounding box of the visible mask.
  - `mask_len_main / mask_wid_across / main_axis_deg`: PCA extents of the mask.
  - `encl_*`: minimum enclosing circle.
  - `fill_ratio`: mask area divided by the fitted-circle area.
  - `pieces`: number of mask fragments merged.
  - `occluded`: 1 where `fill_ratio` < 0.95.
  - `motion_blur`: 1 for frames 33–37.
  - `diam_px_best`: the fitted diameter, except the bbox width in blur frames.
  - `Z_per_D, X_per_D, Y_per_D, R_per_D`: pinhole back-projection with the lab intrinsics (f = 762.8 px, principal point 640,360), in units of the ball's true diameter. Z is along the optical axis, X is image-right, Y is image-down, and R is the Euclidean camera distance. Multiply by the real diameter, or rescale so that R matches a given depth_info.
- `scripts/`:
  - `track_ball.py`: HSV segmentation, circle fit and overlay crops.
  - `enrich.py`: derived columns.
  - `check_timing.py`: pts and background stability.
  - `draw_track.py`: draws the whole track on frame 37.
- `../frames/`: overlays that were inspected.

## Reliability
- **Centre while held or free (frames 0–27, 32–48):** about ±1 px. Overlays confirm the fitted circle follows the ball outline.
- **Frames 28–31:** the ball is split into 2–3 fragments by the hand mask. The circle fit on the merged fragments still matches the outline (checked visually), but allow ±2–3 px.
- **Diameter:** about ±2 px. A depth from the diameter is therefore good to about ±2–3%.
  - While held, the diameter is 136 px, so the ball centre is about 5.6 diameters from the camera.
  - At the bounce it is 94–100 px (about 7.7–8.1 diameters), and at the apex 110 px (about 7.0 diameters).
  - The ball moves away from the camera as it falls, so pixel displacement is **not** proportional to metric displacement. Use 3D back-projection, with the given depth_info if supplied.
- **Motion blur (frames 33–37):** this stretches the mask vertically, by up to +16 px in bbox height. Use the bbox width for size in those frames.
- **Possible dropped frame:** the y-step from frame 35 to 36 is 114 px, against about 57 px before and after. The file's timestamps are uniform, so the original capture probably skipped a frame there. Per-frame speeds touching frame 36 will look doubled.
- **Release frame:** ±1 frame. The ball creeps up about 4 px over frames 21–26 (hand lift) and drops from frame 27 onward.
- **Bounce:** contact happens between frames 36 and 38. Frame 37 is the lowest sample, with the ball bottom at y = 713, so it is not clipped by the frame edge (720). A faint dark shadow or blur sits beneath the ball at frame 37.
- **Ambiguities:** there are no similar objects. The hand is invisible, so its position is only implied by the notch in the ball.
