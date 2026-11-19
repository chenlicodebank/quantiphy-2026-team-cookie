# simulation_0189 — measurement record

2D simulation (Blender), 120 fps, 401 frames (t = frame/120, 0–3.333 s), 1920×1080. Static side view of a
white airport catering truck in a hangar. A brown cardboard box ("FRAGAIL" symbols) sits on the white cargo
body; over the clip the cargo body is raised by a scissor lift and the box rises too. All motion is vertical.

## Files
- `scene.json` – inventory, frame-0 pixel extents, events, camera.
- `tracks/cardboard_box.csv`, `tracks/cargo_body.csv` – every frame: centre (cx, cy), bbox, length/height
  (constant, rigid), raw shift vs frame 0, occlusion flag. Width column blank (2D).
- `scripts/track.py` (template matching vs frame 0, sub-pixel parabola fit; writes `scripts/raw_shifts.csv`),
  `edges.py` (frame-0 edges from colour/gradient profiles), `write_tracks.py` (builds tracks, gap, bg check),
  `overlay.py` (overlay images checked by eye in frames/).

## Measurements
- **cardboard_box**: frame-0 box body x 530–938, y 181–368 → 408 px wide, 187 px tall (204 px including the
  open flap at top-right, flap top y=164). Centre (734.0, 274.5) at frame 0. Rises at a near-constant
  ~0.160 px/frame (≈19.2 px/s); total −63.95 px in y by frame 400. Horizontal drift < 0.06 px.
- **cargo_body** (white container): frame-0 x 128–1457, y 368–804 → 1329 × 436 px. Centre (792.5, 586.0).
  Static for frames 0–4, then rises with increasing speed: mean 0.070 px/frame over frames 0–40, 0.12 (80–120),
  0.165 (160–200), 0.206 (240–280), 0.245 (360–400). The speed increase per 40 frames shrinks (≈0.03 → 0.01),
  so the acceleration is not constant. Total rise 67.6 px. Shift = mean of the roof-edge and bottom-edge templates
  (they agree to ~0.1 px).
- Gap between box bottom and roof: 0 at frame 0, max ~8.2 px at frame 163, back to 0 at frame 359; afterwards the
  box bottom is hidden behind the roof edge (−3.6 px at frame 400). The box is NOT carried by the body: it moves on
  its own at constant speed.
- Static (frame 0, approximate ±3 px, read off grid images): truck overall x 122–1840 (≈1718 px incl. mirror),
  cab x ≈1480–1812, ground contact y ≈1025; wheel centres ≈(705,945) rear and (1582,945) front, tyre diameter
  ≈162 px, wheelbase ≈877 px; stabilizer legs at x ≈487 and ≈1282; front railing platform x ≈1480–1830,
  y ≈308–520 (static). Tall white post at x≈1465 belongs to the cargo body and rises with it.
- Camera static: background patch shift < 0.3 px (compression noise), cab template < 0.01 px.

## Reliability / ambiguities
- Shifts are sub-pixel accurate (~±0.1 px, template scores ≥ 0.97). Per-frame differences are noisy
  (box per-frame std ≈0.07 px against a mean of 0.16 px), so smooth over several frames before using
  instantaneous speeds or accelerations.
- Absolute edges ±1–2 px. The reference point is the bbox centre. For a rigid object the centre's frame-to-frame
  motion equals the measured shift, so speeds don't depend on where the origin is.
- Occlusion flag is 0 everywhere. After frame 359 the bottom ≤3.6 px of the box is behind the roof edge; the
  bbox is propagated from frame 0, so it stays full size.
- "Cargo body" vs "truck": only the container (+ scissor lift) moves. Cab, chassis and wheels are static.
- No metric scale is assumed: use one m/px scale from the question's prior (2D planar scene).
