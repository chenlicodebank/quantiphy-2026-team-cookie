# simulation_0192_segmented — measurement record

2D segmentation clip (Blender render with the background replaced by white), 1920x1080, 120 fps, 200 frames (0–1.658 s).
t = frame/120. Pixel coords: x right, y down. **No metric scale was assumed anywhere.**

## Scene
A static camera looks straight at the rear of a white box truck (bottom centre of the frame). A brown cardboard box
(with one dark open flap sticking up at its top right) **falls straight down** from the top of the frame and lands
on the truck roof. At about the moment it lands, a dark **tail-lift platform** at the bottom of the rear door
starts folding up about its bottom hinge (y ≈ 1028) and is still rising, slowing down, at the end of the clip.
Nothing else moves. The camera does not move: the static truck pixels match between frames 0 and 199.

## Files
- `scene.json`: inventory (moving and static objects with pixel extents), events, camera notes.
- `tracks/box.csv`: all 200 frames. Columns:
  - `cx, cy`: reference point = centre of the box front face. `cx = (left_x+right_x)/2`. `cy = front_top_y + 205.3/2`, where 205.3 px is the front-face height measured at rest.
  - `front_top_y`: sub-pixel top edge of the front face, measured in flap-free columns x 820–900 (grey-level crossing at 200).
  - `visible_bottom_y`, `visible_h_incl_underside`: these include the greyish underside, which shows while the box is high in the frame.
  - `left_x, right_x, width`: sub-pixel side edges in a 40-row band at mid-height of the face.
  - `bbox_*`: brown body bbox, integer.
  - `full_*`: bbox of the whole non-white mask, including the dark flap.
  - `stalled`: 1 if `front_top_y` moved less than 0.2 px since the previous frame.
  - `diff`: mean grey change in the box region.
  - `occluded`: always 0.
- `tracks/tail_lift_platform.csv`: all 200 frames. Columns:
  - `top_y`: sub-pixel free (top) edge, from the column mean over x 860–1020 crossing grey 90.
  - `hinge_y`: bottom of the dark plate (constant 1028).
  - `visible_h = hinge_y + 1 - top_y`.
  - Widths of the top and bottom edges, the centre of the visible projection, and a `note` for the frames where it lies flat (edge-on).
- `scripts/`:
  - `track.py`: produces both tracks.
  - `statics.py`: static extents and the camera check.
  - `overlay.py`: draws the tracks on frames. It was checked visually at frames 0, 30, 40, 58, 59, 62, 100, 120, 150 and 199; the boxes fit the box face and the platform edges.
  - `view.py`: writes grid frames.
  - `probe*.py`: exploratory profiles.

## Key numbers (px)
**Box**
- Front-face size: 280.8 px wide × 205.3 px tall. The width is constant within ±0.5 px for the whole fall, so the box moves at constant depth.
- Including the flap, the box at rest is 284 × 220 px.
- Start, frames 0–4: centre (946.6, 165.1), front top 62.43.
- Rest, frames ≥ 74: centre (946.9, 424.05), front top 321.4, bottom 526.7.
- Vertical drop of the reference point: 258.97 px. Horizontal drift is under 1 px.

**Truck rear (static)**
- Body: x 661–1227 (566 px wide), roof edge y ≈ 533.5, bottom ≈ 1046 (≈ 512 px tall).
- Door frame: x 820–1066 (246 px), y 599–1026 (427 px).
- Yellow outline stripe: x 684–1201, y 558–1017.
- Chevron panels: 28 × 136 px each, at x 694–723 and x 1164–1191, y 872–1007.

**Platform**
- Width at the hinge: 248.5 px.
- Top edge: 1020.4 (flat, frames 0–~52) → 1016.0 (frame 60) → 980.7 (80) → 939.6 (100) → 898.1 (120) → 862.5 (140) → 835.3 (160) → 817.4 (180) → 808.4 (199).
- Speed of the top edge: about 2.0–2.2 px/frame over frames 85–125, falling to about 0.3–0.5 px/frame at the end.

## Events
| event | frame | t (s) |
|---|---|---|
| box held still | 0–4 | 0–0.033 |
| box released (first motion at frame 5) | 4 | 0.033 |
| box first contact with roof (between 60 and 62) | ~61 | ~0.508 |
| small rebound, ~2 px up | 67–71 | 0.558–0.592 |
| box settled | 74 | 0.617 |
| platform starts tilting (±5 frames) | ~52 | ~0.433 |
| platform top edge visibly rising | 59 | 0.492 |
| platform still moving at clip end | 199 | 1.658 |

## Reliability and caveats
- **Irregular box steps.** The box's per-frame motion comes in uneven steps. Some frames repeat the previous position (`stalled` = 1, e.g. frames 8, 16, 20, 24, 32, 35, 37, 40, 47, 61) and the next step is about double (e.g. 30→31: +8.6 px, 44→45: +12.3 px, 57→58: +16 px).
  - The platform moves smoothly in the same frames, so this is the box's baked simulation and not video duplication.
  - One-frame backward differences of the box are therefore very noisy. Fit over several frames, or average, when a question needs speed or acceleration.
  - The fall is clearly accelerating: about 1.0 px/frame near frame 10, about 3.3 near frame 28, about 5.7 near frame 42 and about 7.5 near frame 55.
- **Box position precision.** Sub-pixel edges are good to about 0.3 px. The reference point assumes the box origin is the front-face centre. In a 2D video only vertical translation matters and any constant offset cancels in displacements.
- **Box height measurement.** The underside (34 px at the top of the fall, shrinking to 0 at the roof) is perspective, not a size change. Use the 205.3 px front-face height, or the 280.8 px width, which is constant and the most reliable size.
- **Flap.** The dark flap adds about 13 px above the face at the right. Excluded from the face size, included in the `full_*` bbox.
- **Box resting height vs roof edge.** The box bottom at rest (526.7) is about 6 px above the truck's rear roof edge (533.5). The box sits slightly behind the rear edge, on the roof.
- **Platform reference point.** It rotates in depth, so its image height is a projection of its rotating length. Its true origin (hinge or plate centre) is unknown, so both the free edge (`top_y`) and the hinge line (1028) are given.
  - Top-edge widths of 290–330 at frames 72–78 and the bottom-width jump at frame 154 are from the side arm or shadow merging into the mask. The heights are unaffected.
- **Platform tilt start.** Before about frame 52 the platform is a thin dark strip (y 1020–1028) lying flat, merged visually with the dark chassis below. The tilt onset (about 52–58) is uncertain by ±5 frames.
- **Static extents.** These are integer-pixel at frames 0, 30 and 199 and agree within 1 px. Small details (top light, DOLL plates) are approximate (±5 px).
