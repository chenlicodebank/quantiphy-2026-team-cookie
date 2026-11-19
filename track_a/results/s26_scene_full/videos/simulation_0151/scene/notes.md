# simulation_0151 – measurement record (pixels, seconds)

3D Blender render, 1920x1080, 24 fps, 42 frames (t = frame/24). Underground car park "B1", static camera looking
horizontally down the garage axis. Two vehicles drive right-to-left across the view, parallel to the image plane:
a **yellow sports car** (near, large) and a **light-blue utility cart with a canopy roof** (farther, smaller).
Both emerge from behind the right foreground pillar (x >= 1831) at t = 0, starting from (near) rest.
The car overtakes the cart in front of it (passes between camera and cart) and leaves behind the left
foreground pillar (x <= 95) by frame 40; the cart ends near the image centre (x ~ 600-980) at frame 41.

## Files
- `scene.json` – inventory, static objects, camera/perspective, events, fixed boxes.
- `tracks/car.csv`, `tracks/cart.csv` – one row per frame the object is (partly) visible.
  - `ref_x, ref_y`: reference point = centre of the object's *side-view box* (box carried rigidly by the measured
    horizontal shift). `bottom_x, bottom_y`: ground-contact point below it (tyre bottom).
  - `shift_px`: horizontal shift vs. the template frame (car: frame 24, cart: frame 36). Vertical shift is 0 (+-1 px).
  - `box_*`: full side-view box (car 1148 x 354 px; cart 374.7 x 325 px) – may extend beyond the image/behind pillars.
  - `vis_*`: what is actually visible in that frame (colour/background-difference mask bbox; `vis_mask_len/wid`
    = min-area-rect sides of the visible mask). Noisy where occluded; the cart's `vis_*` mixes in car pixels when overlapped.
  - `occluded` + `note`: pillar / car occlusion. `method`: which measurement produced `shift_px`.
- `scripts/` – all code (`run_all.py` reruns the pipeline; `common.py` decoding; `masks.py` background;
  `track.py` raw masks/bboxes -> `raw_*.csv`; `car_tm.py`, `car_chain.py`, `cart_tm.py`, `cart_early.py` shifts;
  `build.py` final tracks; `verify.py` overlay; `vanish.py` vanishing point; `static.py` static objects).

## How measured
- Background = frame 0 (x<1300) + frame 41 (x>=1300) (each half is empty of vehicles there). Foreground = colour
  difference > 25. Car = yellow hue pixels; tyre bottom from the dark run below the body.
- Car position: grayscale template matching of side-panel patches from frame 24 (front patch: frames 11-27, rear
  patch: 22-36, average where both). Frames 0-10: frame-to-frame matching of the visible nose (masked SSD),
  divided by 0.960 (nose motion / side-panel motion ratio measured on frames 11-14). Frames 37-38: tail chain
  /0.982; frame 39: from the visible tail-edge step (low reliability, +-5 px).
- Cart position: template matching of its roof (the roof stays above the car's roofline): whole roof (frames 25-41),
  rear roof + handle (18-24), handle (14-17), and roof-front LED strip from frame 0 (frames 0-13) mapped linearly
  onto the handle track (fit on frames 14-18, residual < 1 px; the raw roof-front track runs ~6 % slower and
  ~20-30 px offset because the oblique front face changes appearance).
- Overlays (`frames/verify.png`, not part of the record) checked: boxes sit on the right object at every sampled frame.

## Reliability
- Car shift: +-1 px frames 11-36 (per-frame steps smooth to ~1 px); +-2 px frames 0-10; +-3-5 px frames 37-39.
- Cart shift: +-1 px frames 25-41; +-2-4 px frames 14-24 (roof partly hidden by the car's roof; step noise ~+-2 px
  per frame there); frames 0-13 +-3 px (mapping).
- Box sizes: car length 1148 px (frame 24 bbox; 1132-1149 over frames 22-27), height 354 (top 530, tyre bottom 884,
  +-3 px; the glossy floor shadow/reflection right under the tyres makes the bottom +-3 px). Cart 374.7 x 325 px
  (+-2), includes roof handle; bottom 817.

## Perspective / 3D
- Vanishing point of the garage axis (ceiling strips) = (959.6, 539.3) = image centre -> horizontal optical axis,
  principal point ~ image centre, horizon row ~539. Focal length unknown.
- Both objects keep constant apparent size and constant image row -> constant depth, motion parallel to image plane.
- Ground-contact rows: car 884, cart 817 -> by flat-ground geometry Z_cart/Z_car ~ 277.7^-1/344.7^-1 = 1.24.
- IMPORTANT: wide-angle perspective. The tracked point lies in each object's *near side plane*. The true origin
  (vehicle centre) is half a vehicle-width deeper, so its image displacement is smaller by Z_side/Z_origin and its
  image position is (ref_x - 960) * Z_side/Z_origin + 960. When an object is off-centre its front or rear face is
  visible, so the visible bbox is longer than the side box (car nose up to ~100 px ahead of the side box in frames
  10-11; tail ~70-100 px behind it in frames 33-36). Use the side box (fully visible, centred frames 22-27 for the
  car, 32-41 for the cart) for sizes.

## Motion summary (descriptive only)
- Car per-frame shift grows from ~3 px (frame 1) through ~60 (11), ~97 (24) to a broad maximum ~102-103 px/frame
  at frames 29-32, then decreases to ~92 by frame 38 (accelerates then brakes). Always leftward.
- Cart per-frame shift grows from ~1 px (frame 1) to ~20 (11), ~30 (20), maximum ~33-34 px/frame around frames
  26-34, then ~29 px/frame at frame 41. Always leftward. Visible until the end.
- Car centre passes the cart centre at frame ~19; silhouettes separate at frame ~31. No contact.

## Ambiguities
- Glossy floor: strong reflections of both vehicles below them and on the ceiling – excluded from boxes.
- Early frames: cart partly behind the car and the right pillar (rear hidden until frame ~12); car's rear hidden
  behind the right pillar until frame 21; car exits behind the left pillar from frame 28.
- "Visible centre" vs "side-box centre" differ by tens of px in partially visible frames – use `ref_*` for motion.
