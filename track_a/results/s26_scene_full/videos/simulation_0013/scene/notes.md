# simulation_0013 — measurement record

3D Blender render, 1920x1954 px, 21.75 fps, 54 frames (t = frame/21.75, 0 … 2.437 s). All values are pixels/seconds; no metric scale.

## Scene
Park lawn seen from beside a large tree (trunk at left edge, x 0–225). **Camera static** (no pan/shake; the background
subtracts cleanly in every frame). Two moving things:
- **nest** – dark, hairy bird's nest. It sits on the branch next to the trunk (upper left, bbox ~118–510 × 161–380 at frame 0),
  slides off toward the camera, falls/tumbles down the left part of the image, and lands on the lawn in the lower-left
  foreground (rest bbox 464–877 × 1589–1903 from frame 41 on). It grows a lot on screen because it falls toward the camera.
- **bird** – black-and-white bird (magpie-like) flapping, flying left→right across the middle of the image (centroid
  x 949→1819, y 777→738). Its **shadow** on the sunlit lawn (y 1082→1103) is tracked too (frames 0–44).
Static: tree trunk + branch, white flower bush (bbox 898–975 × 1005–1068, 77×63 px), wooden cart cut by the right edge
(x 1552–1920, y 965–1140), background trees, sunlit lawn patches. Details are in scene.json.

## Files
- `scene.json` – inventory, static object positions/sizes, events, camera/perspective notes.
- `tracks/nest.csv`, `tracks/bird.csv`, `tracks/bird_shadow.csv` – one row per frame: frame, t_s, mask centroid
  (mask_cx, mask_cy), bbox centre, bbox x0/y0/x1/y1 (inclusive), bbox_w/h, mask length along its principal axis,
  width across it, principal axis angle (deg, image coords, 0 = horizontal), mask area, `occluded` flag
  (nest: 1 = overlapping dark trunk/branch, edge uncertain; 2 = strong motion blur/deformation, extents inflated).
- `scripts/` – `background.py` (composite median background), `segment.py` (component listing), `track.py`
  (masks → tracks + overlays), `views.py`, `diffcheck.py`, `ovsheet.py` (viewing helpers).

## Method
Background = per-pixel median (upper-left nest area: median of frames 45–53; lower area y≥1300: median of frames 0–20;
elsewhere: all frames). Mask = max-channel |frame − background| > 30, opened/closed, connected components assigned by
position. Over the very dark trunk (x<240, frames 0–26) the nest is added with a lower threshold (12). Overlays of masks,
bboxes and centroids were drawn and inspected at frames 0–53 (every 3rd + 40, 41); they sit on the right objects.

## Reference points & reliability
- **nest**: origin ≈ bbox centre (≈ mask centroid; they differ by ≤ ~20 px). Frames 30–36 and 41–53 are clean
  (±3 px). Frames 0–29 (occluded=1): the nest overlaps the near-black trunk, so its left edge (x≈106–120 by eye at frame 0)
  is uncertain by ~±20 px and frames 24–29 may include a bit of trunk shading; frames 27–29 contain a thin trunk strip
  (x0=151). Frames 37–40 (occluded=2): heavy motion blur/stretching (streaky elongated shape), extents inflated along
  the motion; centroid still usable (±10 px). At rest the mask bottom includes ~10 px of contact shadow.
  Apparent nest size: ~395×220 in the tree → ~380×410 (ball shape, frames 30–33) → 414×315 at rest (main axis 447, width 314).
- **nest events**: creeps down 1–2 px/frame from frame 0; clear accelerating fall from ~frame 13; fully off the branch by
  ~27; last moving frame 40 (centre y 1644), at rest from frame **41** (t=1.885 s) — impact between 40 and 41, no bounce seen.
- **bird**: use mask centroid as the body/origin; bbox centre and size swing with the wingbeat (bbox_h 48–120 px,
  bbox_w 94–157 px; wing-up maxima at frames ~10, 28, 45 → period ~17–18 frames). Not occluded. Mean apparent length
  grows ~115→145 px over the clip and its shadow drifts down the lawn, so it moves slightly toward the camera.
- **bird_shadow**: sun-cast (oblique), so not directly under the bird; lost after frame 44.

## Perspective
Far edge of the lawn / base of the background trees at y≈1000–1045; true horizon hidden, estimated y≈950–1000 (image
centre row 977). Focal length unknown — derive from a question's depth_info plus a known size.
