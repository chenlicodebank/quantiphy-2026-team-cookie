# simulation_0014 – measurement record

3D Blender render, 1920x1954, 24 fps, 73 frames (t = frame/24, 0–3.0 s). Static camera. Pixel coordinates: x right, y down, full resolution.

## Scene
A farmyard: timber barn (front facing camera), wooden hand cart with large spoked wheel on the right, rail fence, two barrels,
flower bush, ladder/steps at barn side, a foreground tree whose trunk runs down the left edge and whose leafy branch spans the top.
**One moving object: `fur_ball`**, a near-black, hairy, deformable (soft-body) ball. It sits lodged on the tree branch at upper left
(centroid ~(165, 394)), sags slightly, falls from ~frame 19, moving down, slightly right and toward the camera, hits the grass in the lower-left
foreground at frame 49–50, and stays at rest (centroid (461.8, 1760.2)) with no bounce until the end.

## Files
- `scene.json` – metadata, camera/perspective cues, inventory with static-object pixel extents (measured at frame 72), events.
- `tracks/fur_ball.csv` – every frame 0–72: centroid of mask (cx, cy = reference point for the ball's origin), bbox (x0,y0,x1,y1,w,h)
  and bbox centre, mask area, equivalent-circle diameter, PCA major/minor length and major-axis angle, edge/occlusion flags, notes.
- `scripts/track.py` (segmentation + overlays), `write_track.py` (CSV), `view.py`/`montage.py` (viewing), `check.py` (sanity check).

## Method
Clean plate = frame 72 (ball at bottom) with rows y >= 1000 taken from frame 0 (ball at top); the camera is static, so this is exact.
Mask = pixels that differ from the plate by > 30 (max channel, after a 5x5 blur) AND are dark (max channel < 80), opened 3x3, closed with a
41-px ellipse, largest component with holes filled. Overlays of all frames were checked visually (frames/ov_*.jpg, not kept).

## Reliability / ambiguities
- Frames 0–33: ball partly behind leaves; its left part lies over the dark tree trunk (x < ~50), where it can't be separated → left edge
  and centroid x slightly uncertain (±10 px). Frames 34–38: the mask merges with the trunk at the left image edge → bbox x0 = 0 there is
  not the ball's edge; the centroid is biased left by maybe 10–20 px.
- Frames 42–45: ball in front of the dark barn/doorway; mask edges slightly eroded. Frames 44–49: the soft ball is strongly stretched
  (and motion blurred), so bbox/axis lengths there show deformation, not the ball's size. Its centroid is still a good reference point (±5 px).
- Size: equivalent diameter ~218–220 px on the branch (frames 0–14) vs ~331 px at rest (frames 50–72). The ball ends closer to the camera
  (about 1.5x closer if its size doesn't change). Rest bbox 440 x 307 px, wider than tall: the ball is viewed from slightly above, sitting
  flattened on the ground, and its lower edge may include a little contact shadow.
- Per-frame centroid noise when static ~±1 px. Downward pixel steps (dy/frame): ~0–1 px for frames 0–14, 2–7 px for frames 15–26, then
  increasing to ~100–145 px just before impact. Landing between frames 49 and 50 (last moving step 49→50: dx 53, dy 91).
- Release is gradual (soft ball slides/sags off the branch): the clear fall starts at ~frame 19 (17–21), t ≈ 0.79 s.
- Static extents (barn, door, cart, wheel, barrels, fence) were read off a 100-px grid at frame 72: ±5–10 px.
- No metric scale or focal length is assumed; use the question's prior/depth_info.
