# simulation_0297: measurement record

**Clip:** a Blender simulation in 2D, 24 fps, 72 frames (3.0 s), 2560x1440. All values are in full-resolution pixels (x to the right, y down) and seconds, with t = frame/24. No metric scale is assumed.

## Scene
This is an underwater set with a static camera. A rippled water surface fills the top (rows 0 to about 290), dark open water lies behind, and a sandy floor with animated light caustics has its far edge at y ≈ 775. Static props on the floor: a tall kelp on the left, a short kelp with purple flowers, a black branching coral fan, a large porous blue rock with a cave under it, a kelp behind the coral, a thin kelp, and a kelp right of the rock. Their bounding boxes are in scene.json. They were read by eye from the median background on a 50 px grid, so expect ±10–15 px, and more for the faint kelp tops.

**The one moving object is the "creature"**, a jellyfish-like animal seen side-on. It has three parts:
- A translucent white/blue mesh **bell** shaped like a half-dome, with pink dots.
- A **green core ball** about 50–60 px across, on the bell's left (trailing) side.
- Three tentacles that point right, in the direction of motion:
  - an upper tentacle that curves up into a pale-green hook;
  - a straight horizontal tentacle at y ≈ 762 that ends in two pale blobs;
  - a lower tentacle that curves down into a pale-green hook. Its middle is almost invisible against the floor.

The creature casts a small dark **shadow** on the floor at y ≈ 1040–1055, directly below the core.

## Motion (main facts)
- **Frames 0 and 1 are almost identical** (mean abs difference 0.14, against about 2.3 for every later frame pair). Nothing moves between them. From frame 1→2 on, the creature moves right at a constant speed.
- **Reference point:** the centre of the core ball (`ref_x`, `ref_y` in tracks/creature.csv). The fit is x = 573.7 + 20.968·frame (frames 1–71), with an rms residual of 1.25 px and a negligible quadratic term. y = 758.8 ± 0.9 px, so the motion is purely horizontal. Per-frame dx averages 20.97 px (about 503 px/s) with 1–2 px of jitter from the measurement. Over frames 0→71, net displacement is 1466.8 px and the summed path length is 1468.0 px.
- The floor shadow gives an independent check: its fit has the same slope, 20.97 px/frame, and it sits within ~2 px of the core in x.
- **The bell pulses** while it translates. Its top edge goes 591 (f0) → 629 (f22) → 563 (f45) → 610 (f71). Its height is about 280 px near frame 12 and about 390 px near frame 45. Its horizontal width is ~170 px for frames 6–30 and ~200–225 px for frames 40–60; that wider value includes a faint trailing layer of mesh.
- The tentacle tips move with the body. In image terms the upper-hook tip stays at y ≈ 514–530, the straight-tentacle tip at y ≈ 760–776, and the lower-hook bottom at y ≈ 991–1018.
- **Size of the whole creature:** about 600–700 px long (bell left edge to straight-tentacle tip) and about 470–500 px tall (upper hook top to lower hook bottom). Both are in the `whole_*` columns.

## Events
| Frame (t) | Event |
|---|---|
| 0–1 (0–0.042 s) | At rest (duplicate frame) |
| 1 (0.042 s) | Motion starts at full speed; no ramp is visible |
| ~12–36 | The bell passes in front of the coral fan and the rock. There is no contact, and the creature is never hidden |
| ~12 / ~45 | Smallest / largest bell |
| 66 (2.75 s) | The straight-tentacle tip reaches the right edge of the image |
| 71 | The clip ends with the creature still moving at constant speed |

There are no bounces, impacts or direction changes.

## Files
- `scene.json`: inventory, static boxes, camera, events, summary numbers.
- `tracks/creature.csv` (**main**), one row per frame:
  - `ref_x/ref_y`: core-ball centre;
  - `core_radius_px`;
  - `bell_left_x`, `bell_right_x`, `bell_top_y`, `bell_top_x`, `bell_width_px`;
  - `bell_bottom_y_eye` and `bell_height_px_eye`, only at frames 0, 6, 12, 20, 24, 30, 36, 42, 45, 60;
  - the tip points of the upper hook, the straight tentacle and the lower hook;
  - `shadow_x/y`;
  - the `whole_*` box;
  - `right_edge_clipped`.
- `tracks/core_ball_matched.csv`: raw output of the core-ball detector.
- `tracks/creature_features.csv`: raw bell, pink-dot and tentacle-tip extents.
- `tracks/shadow.csv`: shadow track. It is missing for frames 30–32, over the rock's shadow.
- `tracks/bell_bottom_profile.csv`, `creature_raw.csv`, `ball_raw.csv`: superseded first-pass attempts, kept for traceability.
- `scripts/`: every measurement script. They read the median-background images that bg.py and bg_full.py write to ../frames/; these are scratch files outside the record.

## Method and reliability
- **Camera:** phase correlation of the floor strip gives shifts under 0.3 px, so the camera is static. The caustics and the surface animate but do not move.
- **Core ball:** found in every frame by matched filtering of the greenness map (G−B) with a disk minus a ring, giving sub-pixel peaks. This is the most reliable item: x is good to about ±1–2 px per frame, and y to ±1 px. The ball is partly behind the mesh on its right, so its true diameter is uncertain (about 50–60 px).
- **Bell:** a mask from the difference against the median background, then closing and a 41 px opening to strip the tentacles, inside a window around the core.
  - The top and right edges stand against dark water and are reliable to ±3 px.
  - The left edge includes some of the faint trailing mesh (±10 px).
  - The **lower edge is faint against the bright floor**, so the automatic masks stop too high (~840–880). The bottom was therefore read by eye on contrast-enhanced difference crops, ±10 px, and only for the frames listed. The rock confuses the reading at frames 24–30.
- **Tentacle tips:** pale pixels (R>130, B−R<50) to the right of the bell, grouped by height. These are reliable to ±3 px.
- **Inventory caveats:**
  - The pink-dot extents in creature_features.csv are contaminated by plants and coral; do not use them.
  - In 2D, using one m/px scale for the whole frame is the intended convention. The floor recedes in perspective, though, so floor props near y ≈ 980 are slightly nearer the camera than the far edge of the floor.
  - Which point is the creature's Blender origin is not known for certain. The core ball is the best candidate, and because the body translates rigidly at constant speed, any attached point gives the same speed.
