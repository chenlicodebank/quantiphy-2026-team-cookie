# simulation_0112 - measurement record

The clip is 55 frames at 24.006983 fps, 1080x1080 px, t = frame/fps. It is a Blender render labelled 2D. A red classic
sports coupe (Porsche 911 Turbo style, with a rear spoiler) drives left to right along the deck of a rusty beam bridge
over a stream. Behind it are a rocky hill on the left, grassy slopes, a thin bare tree in the middle and a big leafy
tree on the right. **The car is the only moving object.** The water ripples are animated texture, and the water shows
a faint red reflection of the car. Neither is an object.

## Files
- `scene.json`: inventory, static-object pixel extents, events, camera and perspective notes.
- `tracks/car.csv`: the main per-frame track (frames 0-54). Columns:
  - `axle_mid_x`, `axle_y`: midpoint of the two near-side wheel hubs. Use this as the reference point / vehicle root
    proxy. In frames where hubs could not be detected, the value comes from the linear fit (see `source`).
  - `axle_mid_x_fit`: a linear fit through all reliable hub frames.
  - `rear_hub_x`, `front_hub_x`: the raw Hough hub centres. These are quantised to about 1 px.
  - `bodycentre_x_est` = axle_mid_x - 10.5. This is the silhouette-bbox centre measured near the image centre, so use
    it if the root is taken as the body centre. It is a constant offset, so it does not change any displacement.
  - `centreplane_x_est`: parallax-corrected to the car's centre depth (see Perspective).
  - `tmpl_x`: a masked template-match check, frames 13-35 only.
  - `bbox_*`, `length_px`, `height_px`, `area_px`, `cut_by_frame_edge`, `occluded`: silhouette from background
    differencing.
- `tracks/car_mask.csv`: the raw silhouette data, which also has the hull centroid.
- `scripts/`:
  - `bg.py`: median background (`bg.png`) and the camera-shift check.
  - `track_car.py`: silhouette masks.
  - `refine_car.py`: masked template x. Run it before `build_track.py`, which reads `tmpl_x` from it and overwrites
    `car.csv`.
  - `wheels.py`: Hough hub detection.
  - `build_track.py`: final track.
  - `static.py`: bridge and tree edges.
  - `check_overlay.py`: draws the overlay. I checked overlays at frames 2, 9, 24, 40 and 47; the hubs and bbox hit the
    car correctly.

## Measurements and reliability
- **Camera:** static. The background shift is ≤0.02 px over all frames.
- **Car motion:** straight, horizontal, +x and uniform.
  - The near-side axle midpoint follows x = -148.14 + 28.227·frame px. The rms residual is 0.65 px and the quadratic
    term is 0.0025 px/frame², which is negligible. So there is no acceleration within measurement error.
  - y is constant: hub y = 505.5, tyre bottom about 539 = bridge deck top.
  - The hubs are measured in frames 2-47 (frame 15 was rejected as an outlier). Frames 0-1 and 48-52 come from the
    fit, because the car is only partly visible and no hub is inside the frame. Frames 53-54 are invisible
    (`visible=0`; the fit values there are extrapolation only).
- **Car sizes (px):**
  - Full silhouette length is 423.5, median over frames 13-36, range 421-430. It is slightly longer near the left
    edge, where the front face shows.
  - Height is 127 (y 412-539). The bumper-to-bumper silhouette, including the spoiler at the rear, was measured at
    frame 24: x 308-729.
  - Near-side wheelbase is 232 and the tyre radius is about 33.5.
  - Width is not observable, because this is a pure side view.
  - Silhouette bbox edges are accurate to about ±2 px. The bumper edges blend with the background, so the bbox-centre
    x is noisier (per-frame steps 20-30 px) than the hub track (28.2 ±1).
- **Events:**
  - The car is already moving at frame 0.
  - It is fully in view in frames 13-36.
  - The front bumper reaches the right edge at frame 37.
  - The last visible frame is 52.
  - The axle midpoint crosses the image centre (x = 540) at frame about 24.4.
  - There is no stop, release, bounce or direction change.
  - The car passes in front of the bare-tree trunk (x about 587-605) in frames about 20-35 and in front of the
    big-tree trunk (x 1006-1067) in frames about 36-52. It is never itself occluded.
- **Static objects:** the pixel extents in `scene.json` come from `bg.png`.
  - The bridge deck top is at y 539.5, the deck slab bottom at 556.5 and the girder bottom at 615. The bridge spans the
    full width and is cut by both edges.
  - The big-tree trunk is 60 px wide.
  - The tree crown and hill extents are approximate (±10 px). Bridge edges are ±1 px.

## Perspective (ambiguity)
Although the clip is labelled 2D, the camera is a perspective camera fairly close to the path:
- When the car is at the left edge you see its front face; at the right edge you see its rear.
- The far-side tyres peek out about 35 px from the near-side tyres when the near hub is about 415-440 px from the
  image centre. That gives a far/near depth ratio of about 1.09.
- The car's centre plane is therefore at about 1.045 × the near-side depth. Its image motion is about 0.957 × the
  near-side hub motion, about 27.0 instead of 28.2 px/frame. This is `centreplane_x_est`, which assumes the principal
  point is at x = 540. It is an estimate, uncertain by about ±1.5 %.
- Silhouette-based measurements mix both depths. Their per-frame bbox-centre step averages about 27.3 px.

If a question uses the 2D one-scale convention with the car's length as the prior, pair the prior with the silhouette
length (423.5 px) or the wheelbase (232 px), and pick the motion track that matches.
