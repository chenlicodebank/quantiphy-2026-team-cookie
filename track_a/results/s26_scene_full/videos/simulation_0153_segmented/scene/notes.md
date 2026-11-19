# simulation_0153_segmented — measurement record

Video: 1920x1080, 24 fps, 42 frames (t = frame/24, 0 … 1.7083 s). Source: segmentation (a Blender
render whose background has been replaced by pure white, RGB 255). Labelled as a 2D scene. Pixels: x points
right, y points down, full resolution.

## Scene content
- **cart** (the only object): a light-blue golf-cart / utility cart seen from the side, facing and driving
  to the RIGHT. It has a flat roof on a rear pillar, a thin slanted roof extension sticking up and to the left
  at the rear, a blue seat, a grey sill with **three small white squares** between the wheels, a grey rear box,
  and black tyres with grey hubs. In the early frames the lighting makes it look dark teal.
- There are no other objects, no ground, no shadows, no markings and no props. A question can only be about
  the cart: its size, wheel or wheelbase, position, displacement, distance travelled, speed or acceleration.

## Camera
The camera is static. The background is plain white, so it cannot be checked against background texture. The
evidence is that the wheel-hub y stays constant (front hub 894.3–895.1 px) and the apparent size barely changes.
The render is in perspective. At the left edge (frames 0–16) the cart's front face, both headlights and the
far-side front wheel are visible. Late in the clip (frames ≥30) the grey rear box shows. The cart moves in a
straight horizontal line at constant depth: the wheelbase shrinks only 339.9 → 334.3 px (≈1.6 %) from frame
20 to frame 41. Treat the scene as planar, with one px→m scale.

## Files
- `tracks/cart.csv` — **the main file**, one row per frame (0–41):
  - `fully_in_frame` / `occluded`: occluded=1 for frames 0–21, where the left image edge cuts the cart.
  - `bbox_*`, `length_px`, `height_px`, `bbox_cx/cy`, `centroid_*`, `area_px`: the mask (pixels with min channel
    < 243, after a 3x3 opening). Valid as whole-object values only for frames 22–41.
  - `body_x0/x1/length_below_roof`: mask x-extent using only rows y>600, which excludes the roof and its extension.
  - `front_hub_x/y` (frames 11–41), `rear_hub_x/y` (frames 20–41): centres of the near-side wheel hubs, from
    template matching (NCC) with ONE fixed hub template cut from frame 30. The match is drift-free and
    sub-pixel; front and rear are assigned by x. Precision about ±0.5 px.
  - `wheel_mid_x/y`, `wheelbase_px`: midpoint of the two hubs and the distance between them (frames 20–41).
    **The midpoint is the best proxy for the vehicle root/origin.**
  - `marker_x/y` (frames 17–41): the three white sill squares, from a fixed template matched in every frame
    (drift-free, ±0.3 px). This is the cleanest motion track.
  - `front_chain_dx`, `front_chain_x_cum`: frame-to-frame shift of the cart's front 220 px (rows 760–960),
    chained from frame 0 and anchored at frame 0's front edge x=51. **This is the only motion measure for
    frames 0–10.** It reads ~2–3 % low compared with the hub/marker tracks: frame 20 gives 42.7 against
    44.2 px/frame, frame 30 gives 48.4 against 49.5. Over frames 11→41 it shows 1311.6 px of travel, while
    the front hub shows 1339.7 px, a shortfall of 28 px.
  - `top_above_*_hub_y`, `bottom_below_*_hub_y`: topmost and bottommost mask pixel in the column through each
    hub. The bottom value is where the tyre touches the ground (y≈947–949). The top above the front hub is the
    hood top (≈722), not the roof.
- `tracks/cart_features.csv`: raw feature matches with their match scores.
- `tracks/cart_shift.csv`: raw chained shifts. It includes `body_dx` (whole-body patch, frames 23–41), which
  agrees with front_dx to within about 0.5 px.
- `tracks/cart_mask.csv`: the first-pass mask measurements, with Hough wheel circles that are noisy (±5 px).
  Superseded by cart.csv.
- `tracks/cart_sizes.json`: size statistics over frames 22–41.
- `scripts/`: run order `track.py` → `shift.py` → `features.py` → `build.py` (`probe.py` is an exploration
  helper). Overlays were checked visually in `frames/` (ov_*, feat_*, check_*): the hubs, the marker and the bbox
  all land on the cart.

## Sizes (pixels, frames 22–41 where the cart is fully visible)
- Bounding-box length including the slanted roof extension: median 546.5 (range 535–564; the larger values
  come in frames 22–24).
- Body length below the roof, from the rear box/fender to the front bumper: 471–477 in frames 29–41. In frames
  22–28 it is larger (479–507) because the front face shows in perspective.
- Height:
  - Ground (tyre bottom, y≈949) to the top of the roof-extension tip (y≈466–470): 480–485, median 484.
  - Ground to the flat roof top (y≈498): ≈451.
- Wheelbase (hub to hub): median 337.2, range 334.2–339.9.
- Tyre diameter: ≈112 px (113 horizontal, 111 vertical, front tyre, frame 30). Hub centre to ground: ≈51.5.
- No world-space AABB is available. The pixel length/height above are the side-view extents. The cart's width
  (depth across the image) cannot be measured.

## Motion summary (for locating events; no fitted model)
- Frame 0: the cart is already moving slowly; only its front 52 px are visible at the left edge.
- Per-frame x-shift:
  - Frames 0–20: grows from about 1.5 to 44 px/frame, i.e. it accelerates. Chained front shifts are
    1.5, 4.9, 8.2, 9.8, 12.9, 15.6, 17.8, 19.7, 22.8, 25.0, 27.1, …
  - Frames 28–32: peaks at about 49.5–50 px/frame (t ≈ 1.17–1.33 s).
  - Frames 32–41: falls to about 43 px/frame (it decelerates, roughly −1.1 px/frame per frame).
- Vertical motion: none. Hub and marker y are constant to within about ±0.3 px.
- Visibility events:
  - Front hub appears at frame 11.
  - Marker appears at frame 17.
  - Rear hub appears at frame 20.
  - From frame 22 the whole cart is in frame.
- At the end of the video (frame 41) the cart is still moving right, with its front edge at x≈1488.

## Reliability and ambiguities
- Reference point: the simulation origin is presumably the vehicle root. Its position is unknown, but the
  cart is rigid and does not rotate, so every point (hub, marker, wheel midpoint) gives the same displacement.
  For frames ≥17 the marker and front-hub tracks agree within about 0.5 px/frame. Use the hub or marker tracks
  for speeds; use wheel_mid as the position.
- Frames 0–10: only the front edge is visible.
  - `bbox_x1` lags the true motion by ~3 px/frame because perspective changes the visible front face.
  - `front_chain_x_cum` lags by ~1–1.5 px/frame.
  - Any early-time speed or acceleration therefore carries a few % of uncertainty.
- Segmentation flicker:
  - The roof appears at frame 7 and then vanishes until frame 15.
  - The roof extension is missing at frame 20, so bbox_x0 reads 23 there although the cart is still cut.
  - The mask area drops at frame 30 (108k against ~120k px).
  - Mask extents can therefore jump by a few to tens of px. The template tracks are not affected.
- Hough wheel radii in cart_mask.csv are noisy; do not use them.
