# simulation_0152 – measurement record (pixels, seconds)

Video: Blender render, 3D scene, 1920x1080, 24 fps, 42 frames (t = frame/24, 0 … 1.708 s).
Scene: an underground car park corridor seen straight down its axis from a static, level, wide-angle camera.
Two vehicles drive left -> right ACROSS the corridor (parallel to the image plane), both at constant depth:
- **car** – yellow sports coupe with rear spoiler; farther from the camera (wheel contact row y≈890).
- **cart** – small light-blue open utility cart with a roof canopy and a backward visor tip at the top-left, white
  rear box, blue seat; nearer to the camera (wheel contact row y≈949). In the image it passes in front of the car.
They never touch (different depths). They only overlap in the image (about frames 3-31).

## Files
- `scene.json` – inventory (moving + static objects with pixel extents), camera, events, size constants.
- `tracks/car.csv`, `tracks/cart.csv` – one row per frame the object is in view. Columns:
  - `frame`, `time` (= frame/24)
  - `ref_x`, `ref_y` – reference point = midpoint of the two near-side wheel hubs (x), at hub/axle row (y)
    (car y=797, cart y=893.5). Smooth estimate: frame-to-frame body tracking (sub-pixel) + a quadratic correction
    fitted to the Hough-detected hub positions. Use this column for positions/speeds.
  - `ref_x_hubs_raw` – the same point straight from the hub detections (integer-ish Hough centres, ±1-2 px noise;
    a single hub ± half the wheelbase where only one hub is visible). Empty where no hub is detected.
  - `front_hub_x`, `rear_hub_x` – raw near-side hub centres where detected.
  - car only: `front_edge_x` (frames 0-27), `rear_edge_x` (frames 28-39) – measured silhouette (yellow paint) edges.
  - `bbox_x0, bbox_y0, bbox_x1, bbox_y1` – silhouette box. Car: x-edges measured where `bbox_note` says so,
    otherwise estimated from ref_x with fixed offsets (rear edge = ref − 364.75 − 241.5, front = ref + 364.75 + 164.5);
    values may lie outside the image (object partly out of view, see `in_view_*`, `clipped_by_image`); bbox_y0 is
    the top of the VISIBLE yellow (roof top is 528 when the roof is in view); bbox_y1 = tyre ground contact 890.
    Cart: left/top/bottom measured from the foreground mask (left=0 means clipped by the image edge, frames ≤20);
    right edge measured when free of the car (frames 33-39), otherwise predicted from the track
    (`right_edge_source`).
  - `length_px`, `height_px` (cart, when fully in view), occlusion flags (`occluded_by_cart` for the car: rear part
    hidden behind / seen through the cart frames ≤31).
- `scripts/` – all code: `common.py` (decoding, background composite = frame 41 for x<900, frame 0 elsewhere),
  `masks_probe.py`, `diff_view.py` (diff/colour masks), `track.py` (first template attempt, superseded),
  `chain.py` (frame-to-frame masked template chaining, translation+scale), `car_yellow.py` (car paint
  extents), `hubs.py`, `hubs_track.py` (Hough wheel hubs), `tyres.py` (tyre radii / contact rows), `extents.py`
  (cart silhouette), `vp.py` (vanishing point), `statics.py` (static objects), `build.py` (writes the CSVs),
  `check_overlay.py`, `overlay_chain.py`, `inspect_tracks.py` (visual / numeric checks). Scratch outputs live
  in `../frames/` (not part of the record).

## Key numbers (pixels)
| item | car | cart |
|---|---|---|
| near-side wheelbase (hub to hub) | 729.5 (728-730, frames 22-29) | 338.5 (335-340, frames 22-41) |
| rim radius / tyre outer radius | 63 / ~93 | ~36 / ~56 |
| hub row y / ground contact y | 797 / 890 | 893.5 / 949-951 |
| silhouette length | ≈1136 bumper-to-bumper (composed, ±15) | 549-551 (visor tip to front tyre, frames 34-39) |
| silhouette height | ≈362 (roof 528 to contact 890) | 485 (visor tip 466 to 951); canopy roof ~500 |
| visible frames | 0-40 (front 0-27, rear 28-39, sliver 40) | 3-41 (tracked 5-41; fully in view 22-41) |

The car is never entirely in the image: its length is composed from front-edge→front-hub (164.5 px at frame 27),
the wheelbase and rear-hub→rear-edge (241.5 px at frame 28).
Apparent sizes do not change over time (hub radii, wheelbases, template scale 1.000±0.005) – both vehicles keep a
constant camera distance; their image paths are horizontal (hub rows constant to ±1 px).

## Camera
Static (no background shift). Vanishing point of the corridor (ceiling-light lines) at (959.3, 539.1) = image
centre → optical axis level and along the corridor, principal point ≈ (960, 540), horizon y≈539. Focal length
unknown (wide angle). Ground-contact rows sit 351 px (car) and 410 px (cart) below the horizon; for a level camera
over a flat floor depth ∝ 1/(y−539), so the car's near-side contact line is ≈1.17× farther than the cart's.

## Events (frame / time)
- 0 (0.000 s): car front already in view at the left edge, essentially at rest (front edge +1 px to frame 1, then
  +11, +15, +20, +26 … px/frame: accelerating from rest).
- 3 (0.125 s): cart front clearly appears at the left edge (a few pixels may touch the edge in frames 0-2), already moving (~20 px/frame at frames 5-8).
- 22 (0.917 s): cart completely inside the image.
- 28 (1.167 s): car front leaves the right edge; car rear becomes measurable (x=742).
- 32 (1.333 s): vehicles stop overlapping in the image.
- 40 (1.667 s): last sliver of the car; frame 41 car gone. Cart stays in view to the end.
- Image step of ref_x: car ~56 px/frame at frame 10 → ~105-106 at 27-31 → ~97-99 at 36-38 (slight slowing at the
  end); cart ~20 at 6 → ~49-50 at 26-33 → 43 at 41 (accelerates, then slows). No reversals, bounces or contact.

## Reliability / caveats
- Cart ref_x frames 13-41: ±1 px (hubs and body chain agree within ~2-5 px with a smooth drift that is corrected);
  frames 5-12 no hub visible → chain + extrapolated correction, ±5 px.
- Car ref_x frames 10-36: ±2 px. Frames 0-8 and 37-39: extrapolated from the silhouette edge with a hub/edge
  motion ratio (1.117 early, 1.127 late) – ±20 px or worse, the hubs are outside the image there. Frame 0-1
  values are dominated by the front-edge motion (car nearly at rest).
- Reference point vs. the true object origin: ref_x is the NEAR-SIDE axle midpoint. The Blender origin of a
  vehicle lies on its centre line, half a track width farther from the camera. Because the motion is parallel to the
  image plane, origin image x ≈ 960 + (ref_x − 960)·Z_near/Z_origin (a few % closer to the image centre), and
  origin pixel speed ≈ ref pixel speed·Z_near/Z_origin. The car's silhouette front edge (far-side corner while the
  car is left of centre) moved ~9 % less than the near-side body, suggesting Z_far/Z_near ≈ 1.09 → origin ≈4 % farther
  than the near side. The vertical position of the origin (axle height vs ground vs body centre) is not observable;
  hub row and ground row are both given.
- Silhouette edges are affected by the wide-angle perspective (the car's front face is visible at the left, its rear
  face at the right), so edge-to-edge lengths vary by a few % with position; the front bumper at the right is dark
  and may extend ~15 px beyond the measured yellow edge.
- Floor is glossy: mirror images of both vehicles and bright light reflections appear below the wheels; all masks
  were cut at the ground-contact rows. The cart is open: the car is visible through its cabin frames ~22-31.
- The yellow 'B1' wall paint is static and was excluded by background differencing.
