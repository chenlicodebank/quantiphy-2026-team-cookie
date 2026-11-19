# internet_0003_segmented — measurement notes

Top-down handheld shot of a pepperoni pizza being cut with a rolling pizza cutter (right hand, white sleeve,
from the right). Background replaced by white (SAM2 segmentation). 2D scene, 24 fps, 48 frames, 1280x674.
All values in pixels / frames; t = frame/24.

## Files
- `scene.json` — inventory, static pixel sizes, camera summary, events.
- `tracks/pizza_cutter.csv` — the only moving object. Per frame: `cx,cy` centroid of the visible black-plastic
  blob (guard/handle), `front_x,front_y` = upper-left end of the black guard (wheel-hub side; mean of the 3 % blob
  pixels furthest back along the cut direction), `*_stab` = same points mapped into frame-0 image coordinates
  (camera drift removed), bbox / area / PCA length & width / angle of the blob, `duplicate_of_prev`, `phase`,
  `guard_partly_hidden_by_hand`, `blob_reliable`, and manual wheel-disc centre/size and handle end for frames 43-47.
- `tracks/pizza.csv` — ellipse fitted (RANSAC) to the pizza rim found by rays from the centre to the white
  background: centre (raw and stabilised), axes, angle, horizontal width, vertical height, bbox.
- `tracks/camera_shift.csv` — similarity transform frame 0 -> frame i from SIFT matches on the static wine glass,
  board and money (RANSAC, 250-800 inliers), image-centre shift, frame-difference and duplicate flag.
- `static_auto.json` — automatic wine-glass mask extents. `scripts/` — all scripts (track.py main tracker,
  camera2.py camera, finalize_cutter.py flags/manual values, static.py, steps.py, dump.py viewer).

## Key numbers
- Pizza: 471.8 px wide (horizontal) x 440.9 px tall (vertical), mean diameter ~456 px (median over frames; frame 0:
  470.4 x 442.2, centre (636.2, 397.3)). Stabilised centre constant to 0.7 px → pizza does not move.
  Which diameter an annotator used is unknown; the horizontal one (~472) is the full visible width.
- Cutter cut stroke frames 0-36: straight line, ~40° below +x (down-right in image). Guard front (stabilised)
  (505.8, 254.1) at f0 → (769.0, 481.1) at f35: 347 px net. Per-unique-frame steps 10-20 px early, 7-10 px around
  f21-29, then stops; frames 37-44 small up-right drift (2-5 px/frame); frames 45-47 the cutter is lifted and turned
  (blob merges wheel + handle, values unreliable — use manual columns).
- Cutter sizes (only fully seen f45-47, ±5 px): wheel disc ~96 px across (face-on, f47), whole cutter wheel-edge to
  handle-end ~270 px (f47), black guard ~84 x 30 px (f35-42).
- Wine glass (frame 0): bbox (129,89)-(326,304), length rim-to-foot ~242 px, width ~134 px, bowl ~153 px, foot ~100 px.
- Monopoly notes: top 500 note ~149 x 64 px, rotated 500 note ~146 x 71 px, 100 note ~158 px long.
- Camera: not static. Image drifts upward ~25-28 px over frames 0-28 then holds/partly returns (f47: -26.6 px),
  up to 0.8° rotation, scale change <0.7 %. For motion questions use the `*_stab` columns (background-referenced),
  or raw columns if an annotator ignored the drift (raw minus stab differs by up to ~28 px vertically).

## Reliability / ambiguities
- Duplicated frames 2, 6, 11, 15, 19, 23, 27, 32, 36, 40, 44 (exact repeats): one-frame differences are zero there
  and double at the next frame; averaging over several frames is advisable.
- The cutter wheel blade is seen edge-on during the stroke (thin line extending up-left from the guard, front tip
  ~30-40 px ahead of the guard front, e.g. ~(472,247) at f0); the hand covers the rear of the guard until ~f34, so
  the blob centroid `cx,cy` is biased forward early (blob length 31→55→84 px). `front_*` is the more consistent
  point (±2 px). Motion blur is mild.
- Pizza rim: the hand covers the lower-right rim and the bottom fingers touch the lower edge; RANSAC uses the free
  rim (120-150 inlier points), axes ±2 px. The pizza is slightly elliptical in the image (ratio 0.935).
- Monopoly/glass sizes are manual readings from gridded zooms (±3-5 px); notes overlap each other.
- No balls, vehicles or falling objects; no bounces/impacts. The second hand at the bottom and the pizza are static.
