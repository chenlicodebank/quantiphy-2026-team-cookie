# simulation_0179 — measurement record (pixels, seconds)

2D Blender render, 1920x1080, 24 fps, 60 frames (t = frame/24). Static camera, side view of a
shop entrance. One moving object: a **shopping cart** (wire basket, red handle/seat, black castors)
that starts at rest and rolls to the right (+x) with steadily increasing speed, purely horizontally
(bbox top y=637 and bottom y=884 in every frame). No bounces, impacts or direction changes; the cart is
still fully visible and moving at frame 59.

## Files
- `scene.json` — inventory (moving + static objects with pixel boxes), events, camera.
- `tracks/shopping_cart.csv` — every frame 0–59: `bbox_cx, bbox_cy` (centre of the full-cart pixel bbox,
  recommended proxy for the object origin), `centroid_x/y` (mask pixel mean; biased toward dense parts, not
  recommended), `bottom_y`, `bbox_x0..y1`, `len_px` (x extent, handle tip → basket front), `height_px`
  (y extent, handle top → wheel bottom), `npix`, `wheels_x0/x1/cx` (castor/base extents for y>=840,
  an alternative reference), `occluded` (0 always), `note`.
- `scripts/bg.py` — median background (every 3rd frame; written to ../frames/bg.png, outside the record) + camera-shift check (phase correlation, <0.01 px).
- `scripts/track.py` — background difference (max channel diff >30), open 2x2, close 25x25, largest blob plus
  all diff pixels in a window around it (to include the thin wire basket/handle); writes CSV and overlays
  in `frames/ov/` (checked visually at frames 36, 54: mask covers whole cart incl. basket and handle).

## Key numbers
- Frame 0 bbox [740,637,962,884]: length 223 px, height 248 px; centre (851.0, 760.5).
- Frame 59 bbox [1640,637,1874,884]; centre (1757.0, 760.5). Net x displacement 906 px.
- Per-frame dx of bbox_cx: 0 (frame 0→1), 1, 1, 2, 2.5, ... ~18.5 at frame 36, ~30 at frame 59
  — increments roughly linear in frame number (looks like constant acceleration from rest), but no model is
  stored; answerers should fit from the CSV.
- Apparent length grows slightly 221→235 px toward the right of the frame (more of the cart's end visible
  off-axis); height constant 248 px. Use frame-0 values (223 x 248) or the value at the question's time.

## Reliability / ambiguities
- Box edges ±1 px; bbox_cx and wheels_cx agree on per-frame displacement within ~0.5 px (single-frame dx
  jitters ±1 px from integer edges, e.g. frames 30/31, 49/50, 56/57; smoothing over 2–3 frames helps).
- Frame 37: red handle tip blends with the orange coin machine; x0 set to 1099 by interpolation (noted in CSV).
- Cart passes *in front of* the ride platform from frame ~22 (overlap only, no contact, never occluded).
- Cart length in a size prior is probably the 3D bbox length; the pixel x extent includes the handle tip.
  Width (depth into scene) is not measurable from this side view.
- Static object boxes in scene.json were read off a 100-px grid at frame 0 (±5 px). The floor has perspective
  (converging grout lines); the cart moves at a constant depth so a single px scale applies to its motion.
