# q81 – speed of the bike at 0.5 s (simulation_0080, 2D top-down)

question_fps = file fps = 24 -> t = 0.5 s is frame 12; speed = |p12 - p11| x 24.
Prior: bike length = 1.7 m -> one metres-per-pixel scale (2D, single plane).

## Measurements (measure.py)
- Bike length (cyan bicycle mask, x extent, frames 0-16): 378-382 px, median 380 px.
  SAM 3 "bicycle" mask: box width 376.2 px (f12), 376.4 px (f11); length_px 373/374 (PCA mask extent).
  scene record: 378 px. Differences are ~1 % (antialiased thin tyre tips at the ends; threshold dependent),
  below 3 %. Used L = 378.5 px (between mine and SAM's box) -> 0.004491 m/px.
- Displacement 11->12: my cyan-extent centre 453.5 -> 406.5 = 47.0 px; SAM box centre 454.2 -> 406.7 = 47.5 px;
  record root 454.0 -> 406.5 = 47.5 px. Motion is uniform: mean step frames 2-16 = 47.43 px/frame
  (record: 46.5-48.2). Used 47.45 px/frame (constant-velocity motion, per-frame step jitter is ±1 px pixel
  quantisation of the extents).
- Speed = 47.45 x 24 x 1.7 / 378.5 = 5.11 m/s.

## Second route
Cross-correlation of the cyan column profile between frames gives 48.4 px/frame (-> 5.19 m/s), ~2 % higher;
it includes faint bluish shadow/antialiasing and is less clean than the extent/SAM box centres, so not used,
but it confirms the value within 2 %. Range over length choices (376-380 px): 5.09-5.15 m/s.

Answer: 5.11 m/s. Confidence: high (±2 %).
