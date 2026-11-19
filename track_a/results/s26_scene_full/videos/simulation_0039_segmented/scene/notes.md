# simulation_0039_segmented: measurement record

3D Blender scene with the background replaced by white. 1536x1536 px, 25 fps, 75 frames (t = frame/25).
Camera is **static** and looks steeply down. There is no horizon and no visible ground plane.
All values are pixels or seconds. No metric scale was estimated.

## Objects
- **boat** (moving). Red-and-white fishing boat at the bottom of the image, bow pointing left. It moves in a straight line
  toward the image left and slightly up, at about 8.1 px/frame in x and 2.3 px/frame in y between non-duplicate frames.
  It does not rotate. Its bow is cut by the left image edge from frame 66.
- **person** (moving). One small human in the middle-left (white T-shirt, jeans), seen from above. They walk toward
  the image bottom at about 2.1 px/frame, drifting slightly right. They are never occluded.
- **rock** (static). Large brown/beige rounded boulder at the top centre-right, cut off by the top edge. Its bbox is
  [683,0]-[1450,314], so it is 767 px wide with 314 px visible height.
- There are no other objects, ground markings or furniture.

## Files
- `scene.json`: inventory, camera, events, frame-0 pixel sizes and distances, duplicate frames.
- `tracks/boat.csv`: one row per frame (0-74).
  - `ref_x, ref_y` (**recommended origin**): frame-0 filled-mask centroid plus a sub-pixel rigid shift. The shift
    comes from template-matching the stern half of the frame-0 boat, so it stays valid after the bow leaves the frame.
  - `bboxc_rigid_*`: the frame-0 bbox centre with the same shift.
  - Raw mask columns: centroid, bbox, length along the main axis / width across it, bbox height (includes the mast),
    main-axis angle, stern tip, bow tip, keel bottom point, and flags `dup_of_prev` and `occluded_or_cut`.
  - From frame 66 on, the raw mask centroid, bbox, bow and length are truncated by the image edge. Use `ref_*` and
    the stern there.
- `tracks/person.csv`: per frame:
  - `ref_x, ref_y` = filled-mask centroid, used as the pelvis proxy;
  - bbox and bbox centre;
  - mask length along the body and width across it;
  - head-top y and feet-bottom y;
  - mask area and the duplicate flag.
- `tracks/*_mask.csv`: raw output of `scripts/measure.py`, including the rock track (constant).
- `scripts/measure.py`: masks pixels whose minimum channel is below 225, picks a region per object, closes gaps and
  fills holes, then computes PCA extents.
- `scripts/refine.py`: frame differences, camera check by phase correlation on the rock, and boat template tracking.
- `scripts/build.py`: writes the final tracks and draws a trajectory check image.
- I drew masks and trajectories on frames 0, 37 and 74 and checked them by eye. They cover the full objects.

## Reliability and caveats
- **Duplicate frames 1, 26 and 51.** Each repeats the previous frame (0, 25 and 50) for every object. One repeat per
  25 frames suggests a 24 fps render resampled to 25 fps.
  - A backward difference at those frames gives about 0 px.
  - The true per-render-frame motion is the value between the neighbouring non-duplicate frames. The boat moves
    steadily at about 8.4 px per step.
  - Treat this when fitting speeds. For example, average over the clip: the boat moves 596 px (net and path, since its path is straight) in 74 video
    frames but only 71 actual steps.
- **Boat reference.** The template shift is accurate to about 0.3 px. The absolute origin point is an approximation
  of the hull centre: the mast and pipe pull the mask centroid up a few px. The rigid shift (the displacement) is
  what matters for speeds.
- **Boat apparent size.** The main-axis length goes from 512 px (frame 0) to 507 px (frame 65), a shrink of about 1%,
  so the boat moves slightly away from the camera.
  - At frame 0: length along the main axis 511.8 px, width across it 280.8 px.
  - Axis-aligned bbox at frame 0: 478 x 330 px; the height includes the mast (mast top y = 1201).
  - Hull only: bow tip (505,1316), stern tip (983,1486), keel bottom y = 1531.
- **Person.** The mask is small (about 25 x 60 px), so the centroid jitters by about 1 px because of leg swing. The
  mask length oscillates between 54 and 71 px with the stride. Because of the top-down foreshortening, pixel length is
  not standing height. Head top y goes from 520 to 674; the mask centroid moves 155 px in y overall.
- **Rock.** Its true size is unknown because the top edge cuts it off. Its depth relative to the others is unknown.
- **Camera.** The rock's shift relative to frame 0 stays below 0.6 px in every frame, so the camera is static. A focal
  length must come from the given depth_info and priors. The principal point is assumed to be at (768,768).
- **Events.** Both moving objects move for the whole clip, with no starts, stops, contacts or direction changes. The
  boat's bow reaches the left image edge at frame 66 (t = 2.64 s).
