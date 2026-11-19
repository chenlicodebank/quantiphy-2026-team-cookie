# simulation_0164 – measurement record (pixels, seconds)

3D Blender scene, 1920x1080, 24 fps, 66 frames (t = frame/24). Static camera, side view of a bowling lane.
A dark-blue bowling ball enters at the left edge already rolling (frame 4), rolls in a straight line along
the lane (to the right and away from the camera), hits a rack of 10 white red-striped pins at frame ~38
(t ≈ 1.583 s, ±1 frame), carries on through the pin deck and disappears behind the right pit side wall
(partly hidden from frame 51, last sliver frame 54, gone 55-65). Pins scatter from frame 38 to the end.

## Files
- `scene.json` – inventory (ball, pins, lane, gutters, neighbouring lane, pit/kickback, floor, wall
  screens, ball shadow), static pixel extents, events, camera/perspective cues.
- `tracks/ball.csv` – one row per frame 5-54: `cx,cy` = ball centre (circle fit, = object origin),
  `radius_fit/diam_fit` = apparent radius/diameter, `bbox_*` and `mask_w/mask_h/mask_area/mask_cx/mask_cy`
  = blue-mask extents, `visible_frac` = mask area / fitted circle area, `fit_inlier` = share of outline
  points within 2.5 px of the circle (low values mostly mean motion blur, not error), `touches_border`,
  `occluded` (1 = cut by image border or hidden by the pit wall).
- `tracks/pins_region_change.csv` – per frame, in the pin-deck region (x 1300-1920, y 380-640): number and
  extent of pixels changed vs frame 0, and the extent of red-stripe pixels (spreads out from frame 38 as pins fall).
- `scripts/` – `track_ball.py` (ball track + overlays), `pins.py`, `pins_static.py`, `pin_width.py`,
  `lane_profile.py`, `perspective.py` (lane lines + vanishing point), `draw_track.py`, `montage.py`, `probe.py`.

## Method and reliability
- Ball: HSV blue mask (H 100-135, S>60) → morphology → largest blob → least-squares circle fit to the
  outline points not on the image border. Overlays checked on every frame: the circle sits on the ball in
  frames 6-50, including 39-50 where fallen pins touch the ball's outline (the circle still fits; only small
  edge bites). Centre accuracy ≈ ±1 px (frames 6-50). Frame 5 is cut by the left border (centre ±3 px).
  Frames 51-54: the ball goes behind the grey pit side wall (straight vertical edge on its right), so there the
  radius is fixed to the linear trend of frames 30-50 (~30.5 px) and only the centre is fitted to the visible
  left arc. Centre ±3 px at 51-52, ±5 px at 53-54 (per-frame x steps there are noisy: 15, 19, 21, 13 px).
- Apparent ball diameter: 88.5 px (frame 6) → 64 px (frame 37) → ~63-64 (40-48) → ~61 (50). It shrinks
  because depth increases. Per-frame noise ±1.5 px (motion blur widens the mask along the motion).
  Smooth or average neighbouring frames if a size is needed.
- Ball path frames 6-37 is a straight image line y = -0.0832x + 678.6 (rms 0.9 px). After impact the
  ball keeps going in the same direction more slowly in pixels (x step ~31 px/frame before, ~17-20 after).
  Pixel steps also shrink before impact because of perspective (the ball moves away), so pixel speed alone
  does not show the ball slowing down. You need depth (depth_info) to convert to 3D.
- Perspective: lane/floor edge lines and the ball path meet at a vanishing point ≈ (5680, 205) ± (70, 10).
  The horizon is ≈ y 205 if roll is zero. Ball centre height above the horizon line scales with apparent
  diameter (diam/(cy-205) ≈ 0.19 at frame 6 and 0.184 at frame 37), which fits a ball at constant height
  moving away. Focal length unknown: estimate it from depth_info + ball size (pinhole: f = diam_px × depth /
  diameter_world).
- Pins (static until 38): seen side-on, they overlap into a cluster bbox ≈ x 1463-1612, y 474-586. Separate
  red neck stripes are centred at x ≈ 1488, 1509, 1529, 1562, 1597. The rightmost pin (x≈1597, clear against
  the dark backdrop) is 102 px tall (top y 484, base y 586), belly ≈30 px wide, neck ≈13 px (±2 px). Pin
  bases (y≈586) match the ball's bottom at impact (cy+r≈587). Individual pins are NOT tracked after the hit
  (heavy overlap, tumbling). Only the region change/red-stripe extents are recorded.
- First pin motion: the red-stripe pixel set first changes at frame 38. Frame-0 differences in the pin region
  before that come from the ball's reflection/shadow on the deck and backdrop, not from pin motion.
- Camera: static (background difference ≈ 0 apart from moving things).

## Ambiguities
- The ball's soft grey shadow (left/below) and faint reflections are not part of the ball mask.
- The ball's specular highlights are filled inside the outline before measuring area.
- Impact frame: in the image, the ball overlaps the head pin from about frame 36, but that pin is further
  away. Pin motion and the drop in the ball's pixel step both start at frame 38, so contact is frame 37-38.
- No second ball, no people, no other moving objects. The neighbouring (far) lane has no pins.
