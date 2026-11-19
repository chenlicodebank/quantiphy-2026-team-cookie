# simulation_0026 — measurement record (pixels, seconds)

Video: 960x960, 25 fps, 75 frames (t = frame/25, 0 … 2.96 s). Blender render, 3D scene: a red-and-white
fishing boat in shallow water at a beach below a sand cliff, plus one person walking on the wet sand to the right of
the boat. **The camera is static** (phase correlation of cliff patches vs frame 0 stays under 0.5 px in every frame,
`scripts/camshift.py`). No horizon is visible; the cliff hides it.

## Files
- `scene.json`: inventory (moving and static objects, what tells them apart, visible frames), static extents,
  camera, events, plus a frame 0/37/74 summary of each track.
- `tracks/boat.csv`: every frame 0-74. `bbox_cx,bbox_cy` = centre of the full boat bbox (mast top to keel, bow to
  stern). `hull_cx,hull_cy` = hull centre (gunwale to keel). `keel_cx,keel_y` = bottom centre of the hull.
  `x_min..y_max` = full bbox (mast top to rudder bottom). `length_px` = bow-to-stern length, `height_px` = mast top
  to keel. `scale_vs_f37` = matched apparent scale relative to frame 37 (on a 0.005 grid), `scale_fit` = straight-line
  fit of it. Also `match_score` and `occluded` (always 0).
- `tracks/person.csv`: every frame 0-74. `pelvis_x` = mean x of the torso rows. `pelvis_y` = y_min + 0.47*height.
  Also the bbox (head top to feet), `width_px`, `height_px`, mask area and an `occluded` flag (1 only in frame 0,
  where the boat stern is next to the person).
- `tracks/boat_raw.csv`: a background-difference mask of the boat, kept only as a cross-check. Its y_max is cut at
  641, so the hull bottom in this file mixes with water noise. Do not use it for heights.
- `scripts/bg_cache.png` is the clean background plate (it can be regenerated). `track.py` also writes a
  `person_raw.csv`, which I deleted because it was made with an older plate and is superseded by `person.csv`.
- `scripts/`: all the code. `common.py` (decoding and the clean background plate), `camshift.py`, `track.py` (raw
  masks), `boat_match.py` (template matching, writes `boat_match.txt`), `boat_track.py`, `extents_ref.py`,
  `person_probe.py`, `person_track.py`, `make_scene.py`.

## How it was measured
- Background plate: the camera is static, so I built the plate by pasting together regions of frames 0, 20, 40 and
  74 where neither moving object is present.
- Boat: the boat is rigid. I took its mask above the waterline in frame 37 as a template and matched it in every
  frame (masked normalised correlation, translation plus scale 0.90-1.10, sub-pixel peak). Scores are 0.989-1.0.
  Reference extents at frame 37: bow x=148, stern x=392 (length 244 px), mast top y=306, wheelhouse roof y≈470,
  gunwale y≈540, keel (dark hull to water) y≈623, rudder bottom y≈632. Every frame's values are these points mapped
  through that frame's translation and scale. I checked the overlays at frames 0, 20, 37, 55 and 74 and the box hugs
  the mast top, bow, stern and keel.
- Person: background difference summed over RGB, threshold 30, with a per-row seam correction. The feet are cut at
  the last row with a strong (>100) difference, because the legs' faint reflection on the wet sand continues below
  the feet. I checked the overlays at frames 0, 37 and 74; the mask covers head to feet.

## Observations (pixels)
- Boat: moves steadily left the whole clip. The full-bbox centre goes from x 415.9 to 134.5, while y stays at about
  465. Its image step shrinks from about 4.1 to 3.5 px/frame, and its apparent size shrinks too (scale 1.046 → 0.952;
  length 254 → 233 px; mast-top-to-keel height 330 → 303 px; keel line y 627 → 617). So it is receding from the
  camera while moving left (about 10 % farther away at the end). No stops, turns or contacts. It is fully visible in
  all frames; at frame 74 the bow is at x≈18.
- Person: walks slowly left, pelvis x 560 → 522 (about 0.5 px/frame, per-frame jitter ±0.5 px from the gait). The
  feet move slightly down (≈583 → 590), so the person is coming a little closer or the ground point is lower.
  Apparent height is 52-55 px (head to feet); frame 0 reads 51 px because the feet are less clear there. Width
  14-19 px depending on arm swing.
- Static objects (frame-0 / background-plate pixels):
  - Cliff: top y 250-290, base y≈495.
  - Beach: y 495-600. Shoreline y≈575 on the left (x<270) and about 600-605 on the right.
  - Fence posts at the cliff foot: x 185-470, y 465-502.
  - White rock/dune at the right edge: x 810-960, y 455-580.
  - Posts at its foot: x 880-960, y 558-582.
- Events: both objects move from frame 0 to frame 74 with no start, stop, bounce or impact. The boat stern is
  closest to the person in frame 0 (gap of about 7 px in the image); after that they separate.

## Reliability and ambiguities
- Boat x and y are good to about ±0.5 px and its scale to about ±0.4 % (rms residual of the linear fit 0.0037).
  The origin's exact image position is unknown; `bbox_c*`, `hull_c*` and `keel_*` give the choices. For a boat the
  Blender origin is probably near the hull centre or the waterline. All three move almost identically except for the
  scale-driven y drift.
- The keel/waterline boundary is soft (shallow water, reflections), so keel_y is uncertain by ±3 px. The mast top is
  thin (±2 px). The rigging wire runs from the mast to the stern davit and falls inside the bbox.
- The person's pelvis is estimated from proportions, not detected (±2 px). The head is low-contrast against the sand.
  The person's reflection on the wet sand was excluded.
- Nothing is occluded. The sea's surface animation and the boat's reflection in it are not objects.
