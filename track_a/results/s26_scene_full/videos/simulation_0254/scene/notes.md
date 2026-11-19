# simulation_0254 — measurement record

**Scene:** a 2D simulation rendered at 24 fps with 60 frames (2.5 s) at 1920x1080. The camera is static. A single small olive/yellow-green ball (about 23.5 px in diameter) rolls down a straight incline at 44.2° below horizontal, going down and to the right. It reaches the floor and then rolls right along it. Nothing else moves.

## Files
- `scene.json`: inventory, static geometry, events and camera.
- `tracks/ball.csv`: one row per frame (0-59). Frames 0-17 have `visible=0`. Columns:
  - `cx, cy`: mask centroid, used as the reference point (the sphere centre).
  - `bbox_*`: bounding box, inclusive pixel coordinates.
  - `area_px` and `equiv_diam_px`: mask area and equivalent-circle diameter.
  - `length_px, width_px`: extents along and across the mask's PCA axes.
  - `height_px`: bounding-box height.
  - `circle_*`: minimum enclosing circle.
  - `occluded_or_cut`: 1 when the ball touches the image border.
- `static_geom.json`: line fits of the ramp strip edges and samples of the floor-line edge, from frame 0.
- `path_fit.json`: line fit of the ball's path on the ramp (frames 19-46).
- `scripts/`:
  - `track_ball.py`: HSV colour mask with saturation > 110 and hue 20-45, keeping the largest component.
  - `overlay.py`: visual check of the tracks.
  - `static_geom.py`
  - `path_analysis.py`: per-frame step and direction.

## Reliability
- **Ball centre:** good to about ±0.5 px. The residual about the straight path line is 0.3 px. The colour mask covers the whole sphere, which I checked on the overlays.
- **Frame 18:** the ball is cut by the top edge, so its centroid is biased (about 5 px off the line, too low in y). Its step to frame 19 should not be used.
- **Diameter:** about 22-26 px; the best value is 23.5 px. The mask edge shading changes it by about ±1 px, so pixel diameter is a coarse scale reference. If a question gives the ball size as the prior, use about 23.5 px, but expect ±5% scale uncertainty.
- **Ramp:** a straight dark strip.
  - Upper edge: y = 0.9741x − 319.9.
  - Lower edge: y = 0.9693x − 248.9.
  - The ball path, y = 0.9727x − 300.5, lies between them.
  - The ramp foot is at about (1355, 1003).
  - The top of the ramp is out of frame, so the ramp's full length is not measurable.
  - It is ambiguous whether the dark strip is the ramp's top face or a shadow. The light region to its lower left is the ramp body.
- **Floor:** the line at y ≈ 1005 is the junction between wall and floor. On the floor the ball centre is at y ≈ 1048. The camera looks slightly down, giving a mild 3D impression, but the motion is planar. Use a single pixel scale.

## Events (frame / t)
| Frame | t (s) | Event |
|---|---|---|
| 18 | 0.750 | Ball enters at the top, already moving |
| 19-47 | | Uniformly accelerating down the 44.2° incline. Pixel step grows from about 33 px/frame (f20) to 66.4 px/frame (f47). |
| 47 | 1.958 | Last frame on the ramp |
| 48 | 2.000 | Floor impact at the ramp foot. The direction changes from 44° downward to horizontal. |
| 48-55 | | Small hop. The centre rises about 12 px and peaks at frames 51-52. |
| 55-59 | | Rolls right on the floor at about 43-44 px/frame, slowly decreasing |
| 59 | 2.458 | Clip ends with the ball at x ≈ 1888, still in frame |

No speeds or accelerations are given in physical units. Each answering session should derive them from `ball.csv` and its own prior.
