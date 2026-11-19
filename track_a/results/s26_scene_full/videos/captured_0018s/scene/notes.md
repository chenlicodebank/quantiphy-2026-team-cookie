# captured_0018s – measurement record (pixels, seconds)

Lab video (Orbbec, 24 fps, 49 frames, 1280x720, t = frame/24) whose background was replaced by a static
synthetic blue-white gradient (SAM2 demo; watermark bottom-right). 3D scene. Camera static (background is
synthetic; people don't shift; mean |f0−f48| in pure background is 2 grey levels). Benchmark intrinsics: fx = fy ≈ 763 px,
principal point ≈ (640, 360).

## Scene
Two women stand facing each other with their arms held out. Each drops two objects, which fall, bounce and settle.
No floor or horizon is visible.
- **left_person**: light grey top, dark trousers, farther away. Height 405 px (y 173–577, shoe bottoms at y≈577), x 336–466.
  At about f29 she releases the **soccer_ball** (black/white, outer object, x≈541) and the **white_carton** (white upright
  box, inner object, x≈477).
- **right_person**: long hair, black t-shirt, nearer. Height 615 px (y 102–716, shoes at y≈700–716).
  At about f27 she releases the **green_ball** (small tennis-like ball at the fingertips of her extended arm, x≈770) and the
  **yellow_fruit** (yellow oblong object with a dark green leafy top, held near her body, x≈875).
- The objects reach the ground at different image rows (soccer ball bottom ≈577, carton ≈603, green ball ≈616,
  yellow ≈697). That puts them at different depths, so use depth_info for each object.

## Files
- `scene.json`: inventory, static extents of the people, camera, events with frames and times.
- `tracks/<obj>.csv` (soccer_ball, white_carton, green_ball, yellow_fruit), one row per frame 0–48. Columns:
  - `cx_bbox,cy_bbox`: bbox centre, the recommended "visible centre".
  - `cx_mask,cy_mask`: mask centroid.
  - `x0,y0,x1,y1,bbox_w,bbox_h`: bounding box.
  - `mask_len,mask_wid,axis_deg`: PCA extents along and across the main axis (axis angle from +x, y down).
  - `area,eq_diam`: mask area and equivalent diameter.
  - `occluded,note`.
- `scripts/`:
  - `build_bg.py`: clean background.
  - `track.py`: tracking. Held phase uses colour masks in a moving window; free phase uses components of |frame−bg| assigned by colour class and prediction.
  - `overlay.py`, `crops.py`: visual checks.
  - `static_measure.py`: people.
  - `finalize.py`: flags and scene.json.

## Events (frame / t)
- **Release**: green_ball and yellow_fruit at f27 (1.125 s); soccer_ball and white_carton at f29 (1.208 s). The objects are still through f26 and f28 respectively.
- **Bounces**:
  - green_ball: lowest at f36 (cy 598), apex f45 (cy 421.5), then falling again.
  - yellow_fruit: lowest at f36 (cy 670.5), rebounds tumbling to cy≈596 at f41–42.
  - soccer_ball: lowest at f39 (cy 543, bottom ≈577), still rising slowly at f48 (cy 405, near apex).
  - white_carton: lands f39, tips over to the left, lying on its side by f46–48.
- **Probable dropped camera frame between f35 and f36**: every falling object moves about twice its expected step (soccer ball
  26→63 px, carton 30→70 px, yellow 53→115 px). Timestamps still follow frame/24. Treat speeds across f35→36 with care.

## Pixel sizes (best frames)
- **soccer_ball**: diameter ≈46 px. Use bbox_w in flight (44–48), or f46–47 unblurred (46–47); held 42–46 px.
- **green_ball**: diameter ≈21–23 px (f0–3 held, f42–48 slow).
- **yellow_fruit**: width ≈29–31 px. Length about 45–55 px, uncertain because it is blurred while falling and tumbling after the bounce. The leafy top is dark and often left out of the mask.
- **white_carton**: held upright about 25 px wide × ≥50 px tall (top partly behind fingers); width in flight 30–33 px; lying at f47–48 the bbox is 58–61 × 33 px.
- **People**: left 405 px tall, right 615 px tall (frame 0).

## Reliability / ambiguities
- **Free fall (soccer/carton f30–39, green/yellow f28–36)**: masks are clean and separate. Vertical motion blur stretches bbox_h by up to about 25 px at the fastest frames. The bbox centre stays close to the true centre because the blur is symmetric; use bbox_w for size.
- **Held phases (occluded=1)**:
  - soccer ball and green ball centres are good to about 1–2 px.
  - carton is partly covered by fingers; its mask was partial in f3–9, which moves cy by about 7 px.
  - yellow_fruit is mostly hidden by the hand in f0–27, so only a yellow patch is tracked and its centre is unreliable. f28–29 are partial.
- **white_carton f33**: the mask merged with the forearm, so that row is unreliable. True centre is about (486, 325).
- **Similar objects**: soccer ball and carton are both grey/white and fall side by side (carton on the left). Green ball and yellow fruit are told apart by hue (green ball G≥R; yellow R≈G≫B).
- **Background replacement**: no real shadows. Mask edges come from SAM2, so object outlines may be off by 1–2 px.
