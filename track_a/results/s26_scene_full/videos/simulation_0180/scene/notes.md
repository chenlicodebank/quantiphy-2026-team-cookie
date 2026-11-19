# simulation_0180 – measurement record

3D Blender render, 1920x1080, 24 fps, 60 frames (t = frame/24, 0–2.458 s). Static camera.
One moving object: a wire **shopping cart** that starts at rest at the left (by the door) and accelerates to the
right along the back wall, drifting slightly toward the camera, ending in front of the ride platform. Everything else
(pink/yellow helicopter kiddie ride, its platform, coin box, wall vent, door, mat, floor tiles) is static.

## Files
- `scene.json` – inventory (all objects, distinguishing features, pixel extents at frame 0), camera, events.
- `tracks/cart.csv` – one row per frame 0–59: `bbox_cx,bbox_cy` (bbox centre, recommended reference point),
  `mask_cx,mask_cy` (centroid of changed pixels – biased toward dense wire/wheel areas, less reliable),
  `bottom_cx,bottom_y` (bottom of wheels), `wheels_cx,wheels_cy` (centroid of lowest 18 % of mask = wheels),
  `x0,y0,x1,y1,bbox_w,bbox_h`, `axis_len/axis_wid/axis_angle_deg` (PCA extents of the mask in the image),
  `mask_px`, `touches_edge` (always 0), `occluded` (always 0).
- `scripts/bg.py` – median background (in strips) + camera-shift check; `scripts/track.py` – cart tracking +
  overlays; `scripts/static.py` – colour-mask extents of ride/platform; `scripts/view.py` – grid view of a frame.

## Method and reliability
- Background = per-pixel median of all 60 frames (clean, cart removed). Cart mask = max-channel |frame−bg| > 25,
  opened, closed with 25x25 kernel, nearby components merged. Overlays at frames 0,15,30,40,45,50,59 checked by eye:
  bbox covers handle top to wheel bottoms and handle-left to basket-front, ±2–3 px.
- Over the grey/blue platform (frames ≳45) parts of the basket wires have low contrast and drop out of the mask, but
  bbox limits (handle, basket front corner, wheels) remain detected; bbox_cy is good to ~±3 px, mask centroid worse.
- Cart origin location is unknown (Blender rig: could be bbox centre or floor-level root). bbox centre and
  wheel-bottom line are both given; for floor-level motion the wheel line/bottom-centre gives the ground track.
- Apparent size: bbox height 283 px (f0) → 290 (f30) → 311 (f59), i.e. the cart gets ~10 % closer to the camera;
  bbox width stays ~270–274 px (cart moves along its own long axis, seen side-on, slight foreshortening change).
- Motion: x step per frame grows smoothly from ~0–1 px (f1–3) to ~37 px (f59) – starts from rest at frame 0 and
  accelerates throughout; no stop, bounce, contact or reversal. Image direction: right and slightly down.
- Camera: phase correlation shift < 0.02 px for all frames → static. Perspective: back wall nearly fronto-parallel
  (base line y≈730 at x=300 to y≈790 at x=1900); floor tile grid gives a ground plane. Focal length unknown.
- Static extents (scene.json): ride and platform from colour masks (±2 px); coin box, vent, door, mat, ceiling band
  read from a 100-px grid view (±5–10 px).

## Ambiguities
- Only one cart, one ride – no similar-object confusion. Cart shadow is faint and not included in the mask.
- The cart passes in front of (not behind) the platform; no occlusion of the cart.
- Mask "length/width" in the image are perspective-projected; world sizes need depth_info/focal length.
