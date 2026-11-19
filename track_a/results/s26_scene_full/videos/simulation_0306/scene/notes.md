# simulation_0306 – measurement record

3D Blender render, 2560x1440, 24 fps, 72 frames (t = frame/24). All values in original-resolution pixels; no metric scale.

## Scene
- One moving object: a **humpback whale** swimming over an infinite light-grey floor (studio backdrop), plus its soft
  **shadow** on the floor. No other objects, markings or props. Camera is **static** (camera_check.csv: background
  corner patches differ from frame 0 by <=0.51 gray levels in every frame) and looks obliquely down at the floor;
  no horizon or vanishing lines – the only perspective cue is the floor plane (darker toward the top = far).
- Frames 0 and 1 are identical; motion starts at frame 2.
- The whale moves steadily toward the upper-left (away from the camera, roughly parallel to the floor – the shadow
  shifts by nearly the same vector) while making one fluke stroke: tail moves down (frames 1–~28), reverses (hidden
  below the image border, estimated frame 27–30, minimum of the frame-difference curve at 27–28), then sweeps up
  through frame 71 (fastest around frame 46–52). At the end the body is nearly straight with the fluke at upper right.

## Files
- `scene.json` – inventory, camera, events, key extents.
- `tracks/whale.csv` – every frame: `cx,cy` mask centroid; bbox (`bbox_x0..y1`, `bbox_w`, `bbox_h`); `area_px`;
  `axis_len`/`axis_width`/`axis_angle_deg` (PCA main-axis extent of the mask, angle in image coords, y down);
  `span_px` + endpoints (largest tip-to-tip distance on the hull); `top_x,top_y` topmost mask point;
  `head_x,head_y` (copied from whale_head.csv); `tail_x,tail_y` (mask pixel farthest from the head point = fluke tip);
  `head_to_tail_px`; `occluded` (mask touches an image border) and `tail_cut` (touches bottom border).
- `tracks/whale_head.csv` – head-patch (200x140 px) template track, chained frame to frame with sub-pixel peak;
  match scores 0.96–0.99. Smooth: ~2.2–2.9 px/frame toward upper-left; (1140,500) at f0 → (977.05,383.57) at f71.
- `tracks/whale_shadow.csv` – shadow blob (gray<150, outside dilated whale mask, y>500): centroid, bbox, area.
- `head_scale.csv` – similarity-transform scale of the head/front body vs frame 0 (SIFT+RANSAC), every 5 frames.
- `camera_check.csv` – camera stability check.
- `scripts/` – track_whale.py (mask + whale.csv), head_shadow_cam.py (head track, shadow, camera), tail_tip.py,
  head_scale.py, framediff.py (consecutive-frame difference), probe/segtest scratch scripts.

## Method & reliability
- Whale mask: Canny (15/40) on blurred gray, 25 px closing, background = flood fill from the top-left corner,
  whale = largest remaining component. Verified visually on overlays (frames 0, 24, 62, 71...): covers the whole
  body, flippers and fluke, excludes the shadow. Bbox/extent accuracy ~±5 px. The head looks faded/semi-transparent
  in the render (near-camera/fog artefact) but is inside the mask.
- Frames 8–39: the fluke runs off the bottom border → bbox_y1=1439, axis_len/span/tail tip and centroid are
  truncated there (tail_cut=1). Frame 19 tail tip is an outlier (1676,1439) for that reason.
- **Reference point**: the whale's rig origin is not visible. Use the head track for the body's translation (rigid,
  smooth, unaffected by the tail beat); the mask centroid oscillates with the tail and is truncated in frames 8–39.
  The origin of a whale rig is usually near the body centre, i.e. somewhere between the head point and the
  dorsal-fin region; translation of the origin ≈ translation of the head point (small rotations ≤~3°).
- Apparent size: the whale shrinks as it swims away – head-region scale vs f0: 0.943 at f30, 0.886 at f45,
  ~0.84 at f71 (late values noisier, ±0.02, and partly due to body pitch). Whole-mask extents also shrink but are
  dominated by pose (tail position): max span 1605 px (f0) → 1302 px (f71); head_to_tail 1456 → 1016 px.
- Whale length proxies (frame 0, body curved, foreshortened): head-to-fluke-tip 1456 px, max tip-to-tip span
  1605 px (fluke tip to flipper/ head), bbox 1492x912. Frame 71 (body straightest): head-to-tail 1016 px, span 1302 px,
  bbox 1220x612. Left pectoral flipper at f0 ~475 px long (by eye).
- Shadow: soft edges, threshold-dependent (±20 px on extents), lower part always cut by the bottom border.
- Ambiguities: whale is seen obliquely from above and its body axis points partly along the view direction (head up/far, tail down/near), so pixel lengths
  are not true lengths; no ground contact; only one animal so no identity confusion.
