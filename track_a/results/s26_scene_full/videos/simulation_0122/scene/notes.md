# simulation_0122 — measurement record

**Scene:** a 2D Blender render, 1152x2048, 25 fps, 40 frames (0-1.56 s). It shows a forest. A longsword falls straight down, point first, and sticks into the top of a large mossy boulder in the centre of the frame. The sword is the only moving object. The camera is static: phase correlation of the ground region gives a shift of at most 0.2 px over all frames.

## Files
- `scene.json`: inventory (sword, boulder, small white rock, foreground mossy rock, trees, ground, light effects) with pixel sizes and positions, events, camera, quality notes.
- `tracks/sword.csv`: one row per frame (0-39). Columns:
  - `ref_x` / `ref_y_mid`: the midpoint of pommel top and tip, taken as the sword's origin/centre.
  - `tip_y`, `guard_y` (centre of the cross-guard), `pommel_top_y`.
  - The bbox of the visible part.
  - `length_px_full` = 417, `visible_length_px`, `blade_width_px`.
  - `occluded`: 1 if part of the sword is cut off by the top edge (f0-f9) or hidden in the rock (f17+).
  - `state`.
- `scripts/`:
  - `diff.py`: motion detection.
  - `track_sword.py` / `tip.py`: mask against a composite clean background (rows <700 from f39, rows >=700 from f0) and blade-tip detection.
  - `profile.py`: tip profile plus 2x zoom of the early frames.
  - `hilt.py`: 3x zooms of the hilt.
  - `crops.py`: gridded crop montages.
  - `build.py`: writes the CSV, the overlay check and the camera-shift check (`cam_shifts.json`).
  - `tip_raw.json`: raw mask output.

## How it was measured
- **Tip y:**
  - f9-f16: lowest row of the blade mask (±1 px).
  - f0-f8: read by eye from 2x zooms (±2-3 px; the f0-f3 tips sit over static sparkles at y 60-110, so the automatic values there were wrong and were replaced).
- **Sword x:** constant at 575.5 ±0.5. The sword only translates vertically.
- **Pommel and guard:** read by eye at f10-f17 and f30. Pommel-top-to-tip = 417 ±3 px; guard-centre-to-tip = 348 px; pommel-to-guard = 69 px.
- **Rigid offsets:** the sword is rigid, so the CSV gives pommel/guard/mid as tip + constant offset. These match the eye readings within 3 px.
- **Overlay check:** `frames/overlay.png`, frames 4/10/14/16/17/39. The marks land on the right parts of the sword.
- **Apparent size:** the same in flight and at rest (69 px pommel-to-guard), so there is no depth change and one px scale applies.

## Motion data (raw, no model fitted)
- Per-frame tip displacement, f0→f16: 11, 17, 25, 32, 37, 45, 52, 59, 66, 73, 80, 86, 94, 100, 104, 114 px.
- Second differences are steady at about 7 px/frame², which fits uniform acceleration.

## Events
- **f0:** the sword is already falling, entering from the top edge.
- **f10 (0.40 s):** the whole sword is in view.
- **f16 (0.64 s):** the last free-flight frame. The tip is at y 1049, about 6 px above the boulder top (y 1055).
- **Impact:** just after f16.
- **f17 (0.68 s) to f39:** at rest. Pommel top at 755. About 300 px of the sword stays visible and 117 px (incl. the tip, inferred tip y ≈ 1172) is inside the rock.
- **f16→f17 displacement:** 120 px. The sword stops abruptly within that frame interval, so the f17 "speed" by backward difference is about 120 px/frame and 0 afterwards.

## Ambiguities and reliability
- **Origin:** the Blender origin of the sword is unknown. The midpoint is assumed, but displacements are the same for any point because the motion is pure translation. Absolute positions or distances to a static object depend on the choice: use `tip_y`/`guard_y`/`pommel_top_y` as needed.
- **Sword sizes:**
  - Guard span changes slightly (≈95-105 px) because the sword spins a little about its long axis while falling. If a question gives the sword's length as the prior, use 417 px.
  - The hilt is dark and partly blurred or blocky (compression) in f7-f9.
  - There is a glint on the blade in f3-f8 and a glow after landing (f17+). These are light effects, not objects.
- **Static objects:** their extents were read by eye on a grid (±10-15 px).
