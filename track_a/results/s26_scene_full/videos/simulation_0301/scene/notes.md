# simulation_0301 — measurement record

3D Blender render, 2560x1440, 24 fps, 72 frames (t = frame/24, frames 0..71, 3.0 s). Static camera.
All coordinates are full-resolution pixels (x right, y down, origin top-left). No metric scale is assumed.

## Scene content
- **forklift**: yellow/black counterbalance forklift (mast and forks on its left side in the image, overhead guard,
  seen from the rear-right and above). Nearer to the camera. Visible in all frames, never hidden by anything; its
  wheels are cut by the bottom image border in frames 0-12.
- **red_car**: red sports car (LaFerrari-like, black roof/windows, seen from the rear-left and above). Farther from
  the camera than the forklift. Cut by the right/bottom image border in frames 0-20; its silhouette first touches the
  forklift's at frame 23; from about frame 28 its front (left end) goes behind the forklift and from ~42 on it is
  heavily hidden (visible fraction ~0.3-0.5 in frames 53-66); at the end it shows above/behind the forklift's
  overhead guard.
- No other objects. The ground is invisible (same pale blue-grey as the backdrop); only faint soft shadows under the
  vehicles show a ground plane. No markings, no horizon, no texture.

## Motion / events (scene.json "events")
- Frames 0 and 1 are identical in both object regions: both vehicles at rest at t = 0.
- Both start moving between frame 1 and 2 (t = 0.042-0.083 s) and speed up (per-frame image step of the reference
  point grows: forklift ~1 px -> ~18 px/frame, car ~0.4 px -> ~38 px/frame around frames 30-50).
- Both move away from the camera towards the upper left along nearly straight image paths, shrinking as they go.
  The car is faster and overtakes the forklift (passes behind it in the image). No 3D contact/collision is seen.
- Image step of the car flattens/drops after ~frame 50 and of the forklift after ~frame 58 — this is (at least
  partly) perspective shrinkage, not necessarily deceleration.

## Files
- `scene.json`: summary, inventory, events, camera/perspective notes, sizes at selected frames.
- `tracks/forklift.csv`, `tracks/red_car.csv`: one row per frame 0..71. Columns:
  - `ref_x, ref_y`: reference point = centre of the amodal (full-object) 2D bounding box. Use this as the image
    position of the object's origin (vehicle centre). For a vehicle root at ground level, the bottom-centre
    (`(amodal_x0+amodal_x1)/2, amodal_y1`) is an alternative; `ground_x, ground_y` = lowest visible mask point.
  - `amodal_x0..y1, amodal_w, amodal_h`: full-object box including parts hidden by the other object or outside
    the image (may extend outside the frame, e.g. car x1 = 2920 at f0).
  - `amodal_centroid_x/y`: area centroid of the full-object silhouette (alternative centre).
  - `amodal_scale`: apparent-size factor relative to the reference frame (forklift f18, car f26) from the
    frame-to-frame image registration. Ratio of apparent sizes = ratio of inverse depths (approximately).
  - `bbox_*`: bounding box of the visible mask only; `vis_cx, vis_cy`: visible-mask centroid; `mask_area`;
    `mask_len_main_axis`, `mask_width_across`, `main_axis_deg`: extent of the visible mask along/across its
    principal axis.
  - `visible_fraction` (approx. visible area / full silhouette area), `free_sides` (box sides that are true object
    edges in this frame), `drift_shift_x/y` (car: correction applied to the registration chain),
    `truncated_by_frame`, `occluded` (car hidden by forklift: visible_fraction < 0.97 and not truncated),
    `car_touches_forklift_in_image`.
- `scripts/`: bg.py (clean background), segment.py (masks), carchain.py (car registration), measure.py (tracks),
  write_scene.py (scene.json), events.py (motion onset), overlay.py / zoom.py / show.py / look.py (checks).
  scripts/masks.npz, bg_full.png, car_chain.json are scratch intermediates.

## How it was measured
- Foreground = max-channel |frame − clean background| > 40 (background assembled from frames 0 and 71, where the
  objects do not overlap). Shadows are faint (difference < ~30) and excluded.
- Frames 0-18: the two vehicles are separate components. Later, the forklift (always in front) is the frame-18
  forklift mask carried by chained affine ECC registration, intersected with the foreground (+3 px); the car is the
  remaining foreground. Checked visually on overlays at many frames (masks hit the right object and its full extent;
  car pixels seen through the forklift cab are assigned to the car).
- Forklift box: visible mask sides (exact) except the bottom in frames 0-12, extrapolated from the registration.
- Car box: car silhouette of frame 26 (fully visible, inside the image) carried to every frame by a scale +
  translation registration chain (masked template matching on the visible car pixels); translation drift corrected
  with the visible free (unoccluded, not border) sides, smoothed over frames (Savitzky-Golay, 15 frames).

## Reliability
- Camera static (background change < 0.25 grey levels). Timing exact.
- Forklift: ref point and box ±2 px in frames 13-71; ±5 px (bottom) in frames 0-12. Forklift sizes reliable.
- Car frames 21-27 (fully visible): ±2 px. Frames 0-20 (cut by border): left/top edges exact, right/bottom and
  centre extrapolated, ±5-10 px. Frames 28-71 (behind forklift): centre ±5-10 px, worst ±15 px in frames 50-71;
  amodal width/height there are scale-propagated from frame 26 and may be off by up to ~5% in width and more in
  height (the visible top-to-bottom extent shrinks faster than the width as the car recedes and is seen more
  edge-on; e.g. f71 visible 336x162 vs propagated 359x197). Per-frame steps of the car ref point are smooth to a few
  px except a dip around frames 59-63 where very little of the car is visible.
- Sizes: prefer frames where the object is fully visible: forklift any frame ≥13 (e.g. f18 668x712 px), car frames
  21-27 (f26: bbox 770x422 px, visible-mask main-axis length 803 px at 18.5°, width across 387 px).
- Image extents are 2D projections of rotated 3D boxes; for 3D sizes combine with the given depths and a focal
  length estimated from the question's own prior.
