# simulation_0228 — measurement record (pixels, seconds)

Video: Blender render, 2D scene, 1920x1080, 24 fps, 50 frames (t = frame/24, 0 … 2.0417 s).
The camera looks straight down at a pool-side deck (top part of the image) and dark pool water (y > 623.5 px).
The camera is **static**: phase correlation of the static deck at frames 0, 25 and 49 shows no shift, and the grid overlays match.
Image axes: x to the right, y down. No metric scale is assumed anywhere.

## Files
- `scene.json`: inventory, static-object extents, sizes, events and the camera.
- `tracks/dog.csv`: one row per frame (0–49). `cx,cy` is the centroid of the full dark dog mask (tail included). `body_cx,body_cy` and `body_x0..body_x1`/`body_len_px` are the same without the thin tail (columns where the mask is ≥12 px tall). Also: bbox (x0,y0,x1,y1,w,h), PCA `length_px`/`width_px` along/across the main axis, `axis_deg`, `area_px`, `occluded`.
- `tracks/swim_ring.csv`: one row per frame. `cx,cy` is the centre of an ellipse fitted to the outer contour (= torus centre, taken as the origin). Alternatives are also given: `circ_cx/cy` (circle fit, within 0.2 px of the ellipse), `bbox_cx/cy` and `mask_cx/cy`. Also: ellipse major/minor axes, circle-fit outer diameter, bbox, `handle_angle_deg` (direction of the inner tube/handle seen from the centre; 0 = right, positive = clockwise on screen), `area_px`, `occluded`.
- `scripts/track.py` builds the tracks and overlays (in `../frames`). `scripts/static.py` measures the pool edge, deck joints, lounger edges and camera shift. `scripts/summary.py` gives the step lengths and writes scene.json. `scripts/ring_check.py` was used to choose the ring threshold.

## Moving objects (both visible and unoccluded in all 50 frames)
1. **dog**: the only animal, solid black and seen from above. It walks left to right along the deck just above the pool edge (cy ≈ 566–571 px), head to the right and a thin tail trailing left.
   - Length with tail is 105–112 px (median ~108); body without tail is 80–92 px (median ~82; a few frames read high, up to 92, when a leg or the tail base thickens). Width is 22–28 px (median ~25; it varies with the gait). Its height cannot be seen from this view.
   - Motion: steady, about 5.4 px/frame (per-frame steps of 4.3–6.8 px from gait jitter). Net displacement over frames 0→49 is +267.2 px in x and −3.6 px in y; path length of the centroid is 268.4 px. It is already walking at frame 0 and still walking at frame 49, with no stop or turn.
2. **swim_ring**: a pink inflatable torus with a short tube/handle inside the hole pointing right. It floats on the water.
   - Outer bbox is 143–145 px wide (x) by 133–135 px tall (y). The fitted ellipse is 139.6 × 131.7 px and the circle-fit outer diameter is 135.6 px. The inner hole is about 66 px. The horizontal extent is ~10 px larger than the vertical; this may be shading or tilt on the darker purple left rim, which is included in the mask. Use bbox_w (≈144.5) for "width/diameter along x" and bbox_h (134) for y. Extents are stable to ±1 px, except frames 6, 8–11, 13, 16 and 20, where a few spray/ripple pixels on the right widen bbox_w to 146–151 (the centre fits are unaffected).
   - Motion: drifts right. The step is ~0.5 px/frame at frame 1, rises roughly linearly (~1 px/frame per frame) to ~9–10 px/frame by frame 13–15, flattens to a broad maximum of 11.5–12.1 px/frame over frames 20–29 (peak 12.1 at frame 23, t = 0.958 s), then falls smoothly to 1.1 px/frame at frame 49. So it speeds up and then slows down, with no reversal. Net displacement 0→49 is +385.5 px in x and −1.6 px in y; path length is 389.5 px. cy bobs between 719.9 and 727.9 px. The handle direction turns slowly from ~17° to ~11° (a slight counter-clockwise rotation of a few degrees).

## Static objects (frame 0; ±2–3 px)
- **Pool edge** (deck → water) is a straight horizontal line at y = 623.5. The coping joint is at y ≈ 603 and the upper deck joint at y ≈ 341.
- **Deck tiles**: vertical joints at x ≈ 430, 575, 719, 864, 1007, 1154, 1298, 1443, 1588, 1733, 1876, a pitch of ~144.6 px.
- **Three front sun loungers** (wooden, slatted, backrest at the top end):
  - left: bbox x 742–944, y 123–462 (339 × ~202 px)
  - middle: x 1012–1215, y 123–462 (339 × ~203 px)
  - right: x 1272–1487 at the backrest, ~1272–1452 at the foot, y 123–462
  The backrest region (y < ~250) is raised, so it is brighter and slightly wider.
- **Three back-row loungers**, cut off by the top edge: x 580–778, 843–1035, 1100–1298 (y 0 to ~130).
- **Ornamental grass bed** at the left: x 0–430, y 0–660.
- **Dark water**: y > 624.

## Events
- **Dog**: walking at constant speed for the whole clip. There are no motion start/stop events.
- **Ring**: almost at rest at frame 0 and starts drifting right. It reaches its maximum speed around frames 20–29 (t ≈ 0.83–1.21 s; peak at frame 23) and slows to almost at rest by frame 49 (t = 2.04 s).
- There are no contacts, bounces or impacts. The dog stays on the deck and the ring stays in the water.

## Reliability and ambiguities
- **Dog**: the mask is a clean threshold (V < 45, grown to V < 70 near the dog) because it is black on a light deck. The centroid is good to ~±1 px, but it wobbles ±1–2 px from frame to frame with the leg and tail motion. The rig origin (pelvis/root) is not visible; the full-mask centroid (`cx`) or the body centroid (`body_cx`, ~4–5 px further toward the head) are the best proxies. For speeds, the per-frame jitter averages out over a few frames. The dog's shadow is not separable; it falls mostly under the body.
- **Ring**: the mask is R > 50 on near-black water (water R ≤ 13). The centre is good to ±0.3 px.
- **Depth**: the dog (on the deck surface) and the ring (on the water, slightly lower) are at slightly different depths below the camera. With a top-down view this scale difference is small and cannot be measured. Treat it as one plane unless a question gives depths.
- **Camera**: static, so no background correction is needed.
