# simulation_0145_segmented: measurement notes

**Scene:** a 2D, static-camera side view on a white background (segmented). The video is 1920x1080, 24 fps, 29 frames (t = frame/24, 0 to 1.167 s). An olive 6-wheel launcher truck stands still, facing left. Its rear launch pod is raised about 39°. One grey rocket leaves the pod and flies in a straight line up and to the left, then exits through the top edge of the image. Nothing else moves. There is no bounce, impact or turn. All values are in pixels and seconds, with no metric scale.

## Files
- `scene.json`: inventory (rocket, truck and its parts), sizes, launch axis, events, camera.
- `tracks/rocket.csv`: one row per frame (0-28). Columns:
  - `centre_x/y`: the reference point, the estimated geometric centre of the rocket, a proxy for its origin.
  - `centre_method`, and `centre_along`: position along the launch axis, where position = (697.19, 228.77) + s·(-0.77758, -0.62878).
  - Nose and tail points (x, y, along).
  - Visible-mask bbox, visible length and width, mask pixel count.
  - `full_bbox_est_*`: estimated box of the whole rocket, including any hidden part.
  - Occlusion flag.
- `scripts/`:
  - `explore.py`, `viewdiff.py`, `viewemerge.py`, `viewmissile.py`: inspection.
  - `axis.py` and `track.py`: fit the axis and write `axis.json`.
  - `final_track.py`: writes the csv.
  - `static.py`: truck parts; writes `static_out.json`.
- Overlays used for checking are in `../frames/` (`track_overlay.png`, `static_overlay.png`).

## Method
- **Rocket mask:** |frame − frame 28| > 40 (frame 28 shows the truck alone), restricted to a ±14 px band around the launch axis, then a 3×3 opening and components of at least 30 px. In the overlay the mask covers the rocket fully, and the centres lie on the rocket's axis.
- **Rocket length:** L = 221.9 px (±3), the median nose-to-tail length over frames 15-20 and 22. Diameter ≈ 17 px.
- **Centre:**
  - Frames 15-22: the mask centroid along the axis plus a 3.9 px centroid-to-midpoint offset. This is the most stable estimator; frame-to-frame jitter is about 1-2 px.
  - Frames 3-14: nose − L/2, because the tail is inside the pod or merged with a plume blob.
  - Frames 23-25: tail + L/2, because the nose is out of the image.
  - The nose and tail ends jitter by about 2-5 px. The tail end carries a bluish nozzle/plume blob that is larger in frames 13, 14 and 21; those visible lengths (232-237) overstate the rocket.
- **Truck:** a single-frame measurement (frame 28) using the mask, Hough circles for the wheels and minAreaRect for the pod. Reliability is about ±2 px for the bbox, ±3 px for the wheels and ±3 px for the pod.

## Reliability and ambiguities
- **Frames 3-8:** low reliability. Only the nose tip is visible, next to the rail arm and the dark pod opening, so the nose position can be off by a few px. Frame-to-frame steps here are irregular (10, 20, 17, 19 px).
- **Frames 9-22:** good. Frames 15-20 are the best: the whole rocket is clear on white.
- **Frames 23-25:** fair. Only the tail is visible.
- **Hidden periods:** the rocket is hidden before frame 3, so the true start of motion inside the pod is not observable. It is gone from frame 26 on.
- **Rocket origin:** the Blender origin is assumed to be the geometric centre of the rocket. If a question's prior is the rocket's length, use 221.9 px.
- **Events:**
  - Nose emerges: frame 3 (0.125 s).
  - Tail clears the pod mouth (release): frame 12 (0.5 s).
  - Nose reaches the top edge: frame 22.
  - Last visible: frame 25. Gone: frame 26.
- **Truck "root":** not observable. Use the parts in scene.json: overall bbox 568-1288 x 380-867 (720 x 487 px), body length 672 px, wheel diameter ≈ 99 px, axle spacings 331 and 116 px, pod 382 x 85.5 px at 39°.
- **Ground:** none is visible. The ground line is at y ≈ 867 (wheel bottoms).
- **Edge noise:** the segmentation edge flickers by 1-2 px along the truck outline, but the truck does not move.
