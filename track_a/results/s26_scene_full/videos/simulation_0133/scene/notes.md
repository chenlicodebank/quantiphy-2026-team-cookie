# simulation_0133: notes

Video: 2D simulation (Blender), 1080x1920 portrait, 30 fps, 90 frames (t = frame/30). The camera is static (frame 0 and frame 89 match outside the apple to within noise). It is a side view. The camera sits at about counter-top height, so the counter's top surface is not visible.

## Scene
A single **apple** (red, with one pale/whitish side that faces the camera from about frame 80) starts at rest on a thin dark **ramp board**. The board leans from a white **plate** (far right, partly out of frame) down onto the top of a dark grey **counter** block. The apple rolls left down the board, rolls along the counter top, rolls off the counter's left edge, falls, lands on the light grey **floor**, and rolls left until it reaches the left image border at the last frame. Nothing else moves except the apple's shadow.

## Files
- `scene.json`: inventory (pixel positions and sizes of the counter, board, plate, floor and wall), camera, and events.
- `tracks/apple.csv`: one row per frame (0-89). Columns:
  - `cx_centroid, cy_centroid`: centroid of the mask.
  - `cx_bbox, cy_bbox, x0, y0, x1, y1, bbox_w, bbox_h`: the axis-aligned bounding box.
  - `mask_len_major, mask_width_minor`: sides of the min-area rectangle.
  - `area_px`: mask area.
  - `occluded`: 1 when part of the apple is hidden or cut off.
  - `flags`: free-text reasons for the flag.
  - `cy_from_top`: y0 + 31.5 px (the apple's radius), a centre estimate that ignores the bottom edge.
  - **`cx_ref, cy_ref`: the recommended pixel position of the apple's origin.** This is the centroid, except that y uses `cy_from_top` in frames 26-34 and 48-89.
- `scripts/track.py`: makes the track. It subtracts a clean background (frame 0, with the apple's area patched from frame 89) and removes the grey cast shadow with a "darker, same hue" test. It then keeps the largest blob, fills it, and applies a 25 px opening.
- `scripts/finalize.py`: adds the flags and reference columns, and writes scene.json.
- `scripts/static.py`: measures the static edges from intensity profiles.
- `scripts/check.py`: draws overlays for checking. I checked overlays at frames 0, 10, 30, 44, 48, 58, 70, 80, 84 and 89 by eye; the mask covers the apple in all of them.

## Apple size (pixels)
- Unoccluded diameter is about 62 px (mask width 60-66, height 61-65). The apple is slightly non-round and rotates, so it varies by ±2 px.
- On the floor the mask height reads 68-70 because about 4 px of contact shadow stays at the bottom. The true height there is about 62-64 px. The floor area is about 8% larger than on the counter. This is probably shadow residue, possibly a small depth change; for a 2D treatment use 62 px.

## Events
| Event | Frame | Time |
|---|---|---|
| Release / start of motion (apple at rest at about (883, 854) on the board) | 0 | 0 s |
| Leaves the board onto the counter top | ~26 | 0.867 s |
| Rolls along the counter, centre y ≈ 883 | 27-33 | |
| Leaves the counter edge (counter edge x = 578) | ~34 | 1.133 s |
| Free fall, moving left | 35-47 | |
| Floor impact (first floor frame; frame 47 is still about 84 px higher) | 48 | 1.6 s |
| Tiny rebound of about 2-3 px | 49 | |
| Rolling left on the floor, centre y ≈ 1523-1525 | 48-89 | |
| Reaches the left border, still moving | 89 | 2.967 s |

## Static objects (pixels, frame 60)
- **Counter:** left edge x ≈ 578 (light side face at x 575-582), top y = 907, base y ≈ 1663. That gives a height of about 756 px. The top slab's front face runs from y 907 to 945 (38 px thick). The right side is cut off by the frame; about 505 px is visible.
- **Ramp board:** runs from about (705, 908) to (950, 877). Length is about 247 px, slope about 7° in the image, thickness about 5 px.
- **Plate:** x 925 to beyond 1080, y 881-906.
- **Floor and wall:** the apple touches the floor at about y 1556. The bright light patch on the floor has edges at y ≈ 1464 and 1630. The ceiling/wall line is at y ≈ 226.

## Reliability and ambiguities
- **Centre positions:** about ±1 px in clear frames.
- **Frames 26-34:** the bottom of the apple is hidden behind the counter's front top edge (y = 907), so mask height reads 52-58. Use `cy_ref` (from the top edge); expect about ±2 px because the apple is not quite round.
- **Frames 83-89:** the apple's pale side faces the camera and its left rim blends into the bright floor. The mask misses a few px on the left, so x may be biased right by about 2 px.
- **Frame 89:** the apple touches x = 0.
- **Motion blur:** small.
- **Shadow:** the apple's shadow falls on the floor to its right; it is excluded from the mask except for the bottom few px.
- **Scale:** no metric scale was guessed. It comes from the question's prior (for example the apple's 62 px diameter), using one m/px scale.
