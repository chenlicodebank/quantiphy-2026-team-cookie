# simulation_0295 – measurement record (pixels, seconds)

2D simulation render, 2560x1440, 24 fps, 72 frames (t = frame/24, 0 to 2.958 s). **Static camera**: phase correlation of frames 35 and 71 against frame 0 gives a shift under 0.003 px.

## Scene
A fantasy mushroom meadow, filmed from low down. The **only moving object is a blue butterfly** with a black body. It flaps its wings and flies right to left across the whole frame at an almost constant image height (body y about 660 to 652 px). Everything else is static: many mushrooms (sizes and positions are in scene.json), rocks, grass and sky. There are no contacts, bounces or impacts, and the butterfly never changes direction.

## Files
- `scene.json`: inventory, camera, static-object extents, butterfly summary (body-path fit, wing extents, wing-beat frames) and events.
- `tracks/butterfly.csv`: one row per frame (0–71). Columns:
  - `cx,cy`: centroid of the wing+body mask.
  - `bbox_x0..y1`, `bbox_cx,bbox_cy`, `bbox_w,bbox_h`: axis-aligned bounding box of the mask.
  - `rect_len,rect_wid,rect_angle`: min-area rectangle (main-axis length and width).
  - `area`: mask pixel count.
  - `body_x,body_y,body_area`: raw detection of the black body blob.
  - `body_x_fit,body_y_fit`: robust quadratic fit of the body position. **This is the recommended origin proxy.**
  - `body_measured`: 1 if the raw body point was kept in the fit.
  - `edge_clipped`: 1 for frames 64–71, when the left wing is cut off by the image edge.
  - `occluded`: always 0, because the butterfly is in front of all scenery.
- `tracks/butterfly_raw.csv`: the same mask stats before the body columns were added.
- `bg_half.jpg`: median background, the per-pixel median of every third frame, saved at half resolution. The full-resolution `bg.png` used by the scripts was deleted to save space; rerun `bg.py` to recreate it.
- `scripts/`:
  - `bg.py`: background and camera-shift check.
  - `track.py`: segmentation by |frame − background| > 30, with morphology and fragment merging.
  - `body.py`: dark-blob body detection.
  - `fit_body.py`: robust quadratic fit.
  - `overlay.py`: overlay drawing for visual checks.

## How it was measured and how reliable it is
- **Mask / bbox**: background subtraction works well because the butterfly always contrasts with the scenery. Overlays at frames 0, 3, 8, 15–20, 22, 30, 36–43, 56–64, 66, 70 and 71 cover the full wings, body and legs.
  - The thin legs and antennae are included, so bbox_h in wings-flat frames is about 65–87 px.
  - Error is about ±3 px.
  - In frames 64–71 the bbox is truncated at x = 0, so do not use bbox_w or cx there.
- **Reference point**: the rig origin is probably the body (thorax).
  - The body is often hidden under the wings, so the raw body detection scatters by ±10–25 px. Some frames have no detection: 0–2, 18–22, 39–43 and 60–66 (when the wings are flat and cover the body).
  - The fit is x(f) = 2308.84 − 29.734 f − 0.01485 f² and y(f) = 659.94 − 0.2048 f + 0.0014 f², with RMS residual 13.7 px. This is almost uniform leftward motion of about 30 px/frame (about 720 px/s), increasing slightly to about 31.8 px/frame by the end.
  - Path length ≈ net displacement ≈ 2186 px over frames 0–71.
  - The wing-mask centroid `cx` gives similar mean motion (about −30.5 px/frame from frame 2 to 63) but oscillates ±10 px with the wing beat.
- **Possible held frame**: frames 0 and 1 are almost identical (the mask moves 0.1 px). The render may hold the first frame, which would make the speed at frame 1 about 0. The body fit ignores this.
- **Wingspan / width**: in a 2D scene the horizontal bbox width is the apparent wingspan.
  - Unclipped frames range from 389 px (frame 30, wings up) to 522 px (frame 63, wings flat).
  - In wings-flat frames: 495 (frame 0), 434 (18), 421 (39), 511 (60) and 522 (63). The flat-wing width changes over the flight because of body roll or yaw.
  - Wings-up frames: 389–411 px.
  - Height (bbox_h) ranges from 65 px (wings edge-on) to 336 px (wings up, frames 8, 30 and 51).
  - Wing-beat period is about 21 frames (0.875 s).
- **Static mushrooms**: extents were read by eye from a gridded frame 36, so they are only accurate to about ±20 px. Perspective is mild but present: foreground objects are larger. For questions about mushrooms, re-measure if precision matters.

## Ambiguities
- Origin vs visible centre: wing flapping moves the mask centroid and bbox centre relative to the body, so use the body fit for speed and acceleration. The fit is quadratic, so it implies a tiny constant acceleration of about −0.03 px/frame². Real per-frame jitter of the rig cannot be resolved below about 10 px.
- No other animals or moving props. Sun glare and lens flare spots near the top right are not objects.
