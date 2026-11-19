# simulation_0268 — measurement record

2D simulation, 24 fps, 72 frames (3.0 s), 2560x1440. t = frame/24.

## Scene
- One moving object: **vehicle** — white futuristic car/spaceship seen from above, nose pointing left, black
  fin/wheel parts at the rear (right side). It starts at rest at the right of the frame, accelerates steadily to the
  left along a horizontal line (y = 719.5 px constant), and leaves through the left edge (last visible frame 65).
- Background: cloud/sky image only; no ground, markings or other objects. Camera static (phase correlation
  < 0.03 px shift), no zoom.

## Files
- `scene.json`: inventory, sizes, events, camera.
- `tracks/vehicle.csv` (one row per frame 0-71):
  - `x_ref, y_ref`: **recommended reference point** (origin proxy) = silhouette bounding-box centre, expressed through
    the smooth template track: x_ref = 0.96614 * body_dx + 1538.65 (linear fit of the measured bbox centre against the
    body template displacement over the fully visible frames 8-50). Available frames 0-65; frames 60-65 derived
    from the rear (black fin) edge instead (`x_ref_source`). Centre is off-image (x<0) from frame 59 on.
  - `x_body_texture`, `body_dx_from_f30`: position of the vehicle's top-surface texture (template matching of 4 body
    patches cut from frame 30, NCC with sub-pixel peak; anchored at 1531 = frame-30 bbox centre). Very smooth
    (±0.3 px). Moves 3.5% more pixels than the silhouette centre (parallax: the top surface is nearer the camera).
  - `cx_bbox_measured`: raw bbox centre (fully visible frames 8-50), noisy ±10 px because the white nose blends
    into white clouds.
  - `front_x_nose`, `rear_x_fins`: silhouette edges (rear = black fin tips, reliable ±2 px; nose ±10 px).
  - bbox columns, `len_x_silhouette` (bbox width, fully visible frames), `truncated_by_frame_edge` = `occluded`
    (frame edge is the only occluder).
- `scripts/`: `bg.py` (camera-static check), `track.py` (background-difference mask, bbox; background = mean of
  frames 67-71 which are vehicle-free), `tmatch.py` (template displacement), `final_track.py` (combines, writes the
  csv), `verify.py`, `crops.py`, `compare.py` (visual checks). `_mask.csv`, `_disp.csv` are intermediates.

## Sizes (pixels)
- Silhouette length along x (motion axis): ~1021 px near the image centre (frames 23-24), 1031 at frame 30,
  range 970 (right side, frames 8-12) to 1066 (left side, frames 49-50) — the 3D vehicle is seen in perspective,
  so its silhouette changes with image position. Use ~1020 px (±15) if a length prior is given.
- Width across (y): 514 px (y 463-976), constant.
- No rotation (main axis horizontal, 0°).

## Events
At rest frames 0-1; motion starts at frame 1 (first step 1→2 = 1.9 px); fully in frame 8-50; centre crosses image
centre at frame ~36; nose reaches left edge frame 51; centre leaves frame 59; last visible frame 65; absent 66-71.
Speed increases steadily (per-frame x_ref steps 1.9, 11.6, 23.8, 35.8, 47.8, 59.7, 71.9 px at frames 2,10,...,60);
no bounce, contact or direction change.

## Reliability / ambiguities
- Pixel motion depends on which point of the 3D vehicle is tracked: silhouette centre (x_ref) vs top-surface
  texture (x_body_texture) differ by a constant 3.5% factor in displacement; the rear fin edge moves 5.6% less than
  the texture. The true Blender origin (body centre) probably lies between silhouette and top surface. If the
  prior is a speed/acceleration of this vehicle, use the same column for the prior and the asked quantity and the
  factor cancels. Length prior → pair with x_ref (both silhouette-based).
- Motion blur is mild; white-on-white nose makes the front edge and raw mask centroid unreliable (mask has holes;
  mask centroid not recorded for that reason).
- Frames 0-7 rear cut by ~10-20 px; frames 51-65 front cut; positions there come from the template/rear-edge track.
