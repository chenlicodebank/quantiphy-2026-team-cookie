# simulation_0095 – measurement record

2D simulation (Blender render), 1920x1080, 24 fps, 72 frames (t = frame/24, 0 … 2.958 s).
The camera is static. The background is plain uniform grey (RGB 132,126,135) with no ground, horizon, markings or static objects.
All values are in pixels and frames; there is no metric scale.

## Objects
| name | what | moves | visible |
|---|---|---|---|
| airplane | White Air China airliner (A320-type, red phoenix logo on the tail fin), side view, nose to the left. It is the large upper object. | yes, leftward, constant pixel step | frames 0–32 (fully in frame 7–16; enters partly visible at the right, leaves at the left) |
| car | Silver angular pickup (Cybertruck-like) with black wheels, side view, front to the left. It is the small lower object. | yes, leftward, from rest, accelerating | frames 0–71 (always fully in frame) |

Nothing else is in the scene. The objects never overlap or touch. Plane rows are 170–497 and car rows are 604–659.

## Files
- `scene.json`: inventory, sizes, events and camera info.
- `tracks/plane.csv` (frames 0–32):
  - `ref_x, ref_y` = estimated centre of the full plane bbox. This is the origin proxy, valid even when the plane is partly off-screen; x can be negative.
  - `nose_x_fit, tail_x_fit` = nose-tip and tail-cone-tip x.
  - `bbox_centre_x` = directly measured bbox centre, only on full-visibility frames.
  - `vis_bbox_*`, `vis_len_px`, `vis_height_px`, `mask_cx/cy`, `area` = the visible mask.
  - `visibility`/`occluded` = 1 when cut by the image border.
- `tracks/car.csv` (frames 0–71):
  - `ref_x, ref_y` = bbox centre (origin proxy).
  - `mask_cx, mask_cy` = mask centroid; this is smoother, with ~0.3 px noise compared with ~0.5 px for the bbox centre.
  - `bbox`, `len_px` (bumper to bumper), `height_px` (roof to wheel bottom).
- `tracks/*_raw.csv`: per-frame mask statistics (bbox, centroid, PCA main-axis length/width/angle, border flags).
- `scripts/`:
  - `track.py`: segmentation with |rgb−bg| > 6, 3×3 opening; plane = y < 545, car = y ≥ 545.
  - `finalize.py`: template matching for the plane.
  - `write_scene.py`: scene.json and diagnostics.
  - `overlay.py`, `viewmask.py`, `blur_edges.py`, `check_start.py`, `probe.py`: checks.

## How the plane was measured / reliability
- Two templates from frame 10 (nose part, tail-fin part) were matched in every frame (score ≥ 0.99 for the tail). The nose shift was fitted with a line over frames 2–16 and the tail shift over frames 6–27; the residual RMS is about 0.02 px.
  - Nose moves 74.20 px/frame; tail moves 73.01 px/frame.
  - The plane's apparent length therefore shrinks by about 1.2 px/frame (mask length 1119 at frame 7 → 1094 at frame 16). This is a perspective effect on a 3D object, not a real change.
  - The centre (`ref_x`) moves by the average, about 73.6 px/frame. The directly measured bbox centre gives 72.5–75.5 per frame, with a mean of 74.3 over frames 7–16.
  - Expect about 1% uncertainty in the plane's pixel step, and a few px in its absolute position.
- Size at frame 10 (centre x≈1062): length nose-to-tail is 1106 px (bbox 510–1615). Height from fin top to engine-nacelle bottom is 328 px (y 170–497).
  - The fuselage alone spans roughly y 338–462 (about 125 px).
  - No wingspan is visible (pure side view).
- The plane's nose/cockpit is rendered semi-transparent (a faint "ghost") while it moves. The low threshold (6) is needed to capture the real nose tip, which was checked against the sharp frame 0: nose at x 1167 in frame 0 and 1095 in frame 2.
  - With threshold 15 the mask loses about 40 px at the nose.
- Frames 0–1: identical images. The plane is cut by the right border, and the nose tip is at x≈1167. The fit predicts 1178 there, so the fitted positions for frames 0/1 are about 10 px uncertain.
- From frame 17 the nose is off-screen. From frame 28 the tail template is gone too, so `ref_x` for frames 28–32 is extrapolated from the tail line; the measured `vis_bbox_x1` agrees within about 8 px.
- `ref_y` = 333.5 (bbox centre including the fin). The visible-mask centroid is at y≈382 (fuselage centre ≈ 400). Vertical motion is below 0.05 px/frame.
- The plane's true Blender origin is unknown; the bbox centre is used.

## How the car was measured / reliability
- The threshold mask is clean; the overlays (frames 3, 12, 24, 71) hit the full car including wheels.
- Static size at frame 0: 171 px long (x 1473–1643), 54 px high (y 606–659).
- The apparent length varies 166–173 px with image x. It is smallest near the image centre (frame 48, x≈955) and larger towards the edges, because of perspective on the 3D body plus slight motion blur at higher speed. Use about 171 px (frame 0, at rest) or the length at the relevant frame.
- Motion: purely horizontal leftward; `ref_y` stays at 631.5–632.5.
  - Frames 0 and 1 are identical, so the car is at rest. It starts moving at frame 2 (step about 1 px).
  - The per-frame step grows linearly to about 36 px at frame 71, which is consistent with uniform acceleration from rest starting near frame 1.
  - It reaches x≈249 at frame 71 and is still in frame and still accelerating at the end.

## Events
| frame | event |
|---|---|
| 0–1 | identical images (both objects unchanged) |
| 2 | both start moving: the plane at once at full constant step, the car from rest |
| 5 | top of the plane's tail fin enters |
| 7–16 | plane fully in frame |
| 17 | plane nose leaves on the left |
| 32 | last plane pixels |
| 33–71 | only the car is visible |

There are no bounces, impacts, contacts or direction changes.

## Ambiguities
- Plane length depends on frame (perspective) and on the threshold, because of the faint nose ghost and thin tail cone. Quote it with its frame: 1106 px at frame 10.
- Scale between the two objects: by the 2D convention, one m/px scale (from the prior's object) applies to both. Nothing in the image shows a depth difference: there is no ground or overlap, and both show similar mild perspective. The relative sizes (plane 1106 px vs car 171 px, a ratio of about 6.5) look plausible for a real airliner (about 37 m) next to a pickup (about 5.7 m). This is only a sanity check, not a scale.
- No metric scale was applied.
