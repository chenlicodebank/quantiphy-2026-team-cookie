# captured_0035ax – measurement record (pixels, seconds)

Lab capture, 3D, 1280x720, 24 fps, 49 frames (t = frame/24, 0–2.000 s). Background (floor, walls) has been
replaced with uniform green (watermark "Modified with Segment Anything 2 Demo" in box x>=1029, y>=690 – not a scene
object). Benchmark intrinsics for this camera: fx = fy ≈ 763 px, principal point ≈ (640, 360).

## Scene
- **soccer_ball**: the small white ball with black patches. At rest at the far person's image-left foot (frames 0–4).
  She kicks it toward the camera and to the right (motion starts at frame 5; it is blurred and merged with her shoe through frame 9 and separate from frame 10).
  It hits the basketball at frame 19 (contact 19–20), bounces back toward the far person while slowing down (16 to 4 px/frame),
  and touches her image-right foot at frames 47–48.
- **basketball**: the larger orange Wilson ball. The near person holds it still at her side (frames 0–7, centre ≈ (884, 615)).
  It is released at frame 8 and kicked by her kicking foot (contact frames 9–11; it is clear of the foot from frame 12).
  It rolls away from the camera toward the upper left at ~17–19 px/frame until the collision at frame 19.
  After that it moves slowly left (~5 px/frame) to the end of the clip and is still moving at frame 48.
- **far_person**: the woman in the light-grey T-shirt and dark trousers at the upper left (x≈300–510). Her head is cut off by the top edge,
  so only the region from the top edge down to the shoes (y 0–312/324) is visible. Her feet stay planted. Only her kicking leg moves, plus a slight sway.
- **near_person**: the woman close to the camera on the right, with long dark hair, a dark-grey printed T-shirt and black trousers.
  She is cut off by the right and bottom edges, and her head top is at y≈100. Her standing shoe is at the bottom edge near x≈880.
- There are no static objects or ground markings. The floor is not visible, so there is no horizon or vanishing points.
  The camera looks obliquely down. It is assumed static: the background can't be checked, but both people's planted feet stay put to within about 2 px.

## Files
- `scene.json`: inventory, events (frame and time), camera, apparent-size trends, ball centre distances around the collision.
- `tracks/basketball.csv`, `tracks/soccer_ball.csv` (frames 0–48): `cx, cy` is the centre of a circle fitted by RANSAC to
  the silhouette edge pixels that border green background, so edges hidden by a hand, foot or the other ball are ignored. `r` and `diam` come from that circle.
  The `mask_*` columns give the colour-mask bounding box. `mask_len_main` / `mask_wid_across` are PCA extents (length along the main axis and width across it).
  Masks run about 2–4 px larger than the circle because of soft keyed edges and blur. `outline_bg_frac` is the fraction of the circle outline that borders background.
  `occluded` = outline_bg_frac < 0.8. In soccer_ball.csv, `touching_other` = 1 means the ball is merged with the person's mask; in those frames the mask box is just the circle's box.
  `reliability` is high, medium or low.
- `tracks/far_person.csv`, `tracks/near_person.csv`: visible non-green mask (balls removed) – centroid, bbox, area,
  lowest_y (shoe bottom), and truncated_by_frame (always 1). These are visible-part measures, not body centres or full heights.
- `scripts/`: track.py (all tracks), overlay.py / cropsheet.py (visual checks), pts_check.py (timestamps and step lengths),
  make_scene_json.py, probe.py.

## Reliability and ambiguities
- **Basketball:** a well-fitted circle (±1 px centre, ±1 px radius) from frame 12 on.
  - Frames 0–7: its right side is hidden by the hand and body. The fit from the left arc gives diam ≈ 80 px, which matches the visible mask height of 84 px including soft edges.
  - Frames 8–11: blur and the kicking foot make it medium reliability.
  - Diameter: ≈ 80 px when held, shrinking to ≈ 69–70 px from frame 18 to 48 (nearly constant: after the collision it moves almost across the line of sight).
- **Soccer ball:**
  - Frames 0–4: a sharp circle, diam 42.0 px (best size measurement).
  - Frames 5–9: LOW reliability. Heavy motion blur and merging with the shoe inflate the fitted radius (diam 55–63), so the centre is only good to ±5 px.
  - Frames 10–20: medium reliability. Blur stretches the mask along the motion direction. Use `mask_wid_across` (≈ 49–56) or the circle (≈ 47–57) for size; the ball is also nearest the camera here.
  - Frames 21–47: high reliability. The diameter shrinks from ≈ 54 to ≈ 41.5 px as it moves away.
- **Collision:** the centre distance at frame 19 is 62.5 px, about equal to the sum of the radii (34.5 + 26.7), so contact is at frame 19.
- **Timing anomaly:** at frames 11→12 and 35→36, both balls jump about twice their neighbouring per-frame step at the same moment.
  The far person's lowest point also moves from 312 to 319 px at frame 36 (and to 324 px by frame 38). This is probably a dropped capture frame (container timestamps are uniform).
  Frame indices are kept as-is (benchmark convention), but single-frame differences across these steps are about doubled.
- **People:** only part of each body is visible, and the masks include hair and clothing edges. The near person's mask also includes a separate standing shoe at the bottom.
- **Depth:** no ground plane is visible. Depth must come from each question's depth_info, using the camera intrinsics above and the apparent ball sizes.
