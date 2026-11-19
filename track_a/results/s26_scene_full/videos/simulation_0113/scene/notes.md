# simulation_0113 – measurement record

2D simulation (Blender render) at 1080x1080, 24.0048 fps, 120 frames (t = frame / 24.0048). The camera looks straight down at a square swimming pool.
All values are in pixels and frames. No metric scale is assumed.

## Files
- `scene.json`: inventory (ring, pool, deck, ground), sizes, positions, a summary of the motion, events and camera.
- `tracks/ring.csv`: the ring in every frame 0-119. Columns:
  - `cx, cy`: centroid of the filled outer outline, which is the reference point (the torus origin, i.e. the centre of the hole).
  - `ell_cx, ell_cy`: centre of an ellipse fitted to the outline (a cross-check).
  - `bbox_*`: bounding box.
  - `outer_diam_major/minor`: diameters from the ellipse fit.
  - `filled_area`, `ring_area`, `hole_area`: areas in px².
  - `occluded`: always 0.
- `tracks/bg_shift.csv`: background shift per frame, from phase correlation on the deck/ground strip below the pool.
- `scripts/track_ring.py`: the tracker. It masks saturated pink/red/violet pixels inside the pool, keeps the largest component, fills it, and also writes overlay checks to frames/.
- `scripts/static_measure.py`: pool extents, the deck-change frame, and step and linear-fit statistics for the ring.
- `tracks/.keep`: an empty placeholder (ignore it).

## Objects
- **ring** (the only moving object): a pink/red inflatable torus with blue-violet blotches, in the upper-left of the pool.
  - Visible and unoccluded in all frames.
  - Overlays at frames 0/30/60/90/119 show the mask outline on the ring's outer edge.
  - Outer diameter ≈ 73 px (ellipse fit 73.6–74.2 × 70.9–71.4; the bbox of 74–76 includes 1–2 px of antialiasing). This is the size to pair with a size prior.
  - Hole ≈ 32 px across; tube ≈ 20.5 px wide.
  - Its vertical thickness is not visible from above.
- **pool**: square basin of dark water.
  - Water region x 313–770, y 310–765 (458 × 456 px). The outer rim edge is about 464 px.
  - Centre ≈ (541.5, 537.5).
  - The right third of the floor is darker because of shadow; it is not a separate object.
- **pool_deck**: lilac paved surround with an irregular outer border.
- **ground**: rough brown terrain at the image edges.

## Motion and events
- The ring is already drifting at frame 0. It moves in a straight line toward the lower-right (+x and +y equally, about 45°) at constant velocity for the whole clip.
  - Linear fit: vx = 0.2848 px/frame and vy = 0.2841 px/frame, so speed = 0.4023 px/frame ≈ 9.66 px/s. The RMS residual is 0.08 px.
  - The quadratic term is about 1e-5 px/frame², so there is no measurable acceleration.
  - Net displacement from frame 0 to 119 is (33.75, 33.49), which is 47.55 px.
- Raw one-frame centroid steps average 0.406 px (std 0.094, range 0.15–0.62), and their sum is 48.3 px.
  - These steps are dominated by about 0.1 px of segmentation noise.
  - For per-frame speed, average speed or path length, the linear fit (0.402 px/frame; path length over 119 steps ≈ 47.9 px) is more reliable than summing raw steps.
- There is no bounce, contact, impact or direction change. The ring stays well away from the walls (its right and bottom edges reach about 465 and 457 px at the end).
- At frame 24 (t ≈ 1.000 s) the deck's rendered appearance switches abruptly: the tile grid vanishes and the deck becomes smooth lilac. Nothing moves; the camera is unaffected.

## Camera
- The camera is static: the background shift is ≤ 0.04 px in every frame.
- The view is top-down with no usable perspective. The pool looks square, so one px scale applies to the water plane.
- The ring's apparent size is constant (73–74 px throughout).

## Reliability and ambiguities
- Ring centre: about ±0.1 px per frame.
- Ring diameter: ±1 px (an edge-definition choice). The two axes differ by about 2.5 px, either from slight shading or from a tilt of the ring.
- Pool edges: ±2 px (the rim has a bevel).
- The only similar-looking thing is the ring's reflection and shading on the water, which is negligible.
- Only one moving object exists, so "the ring", "the float" or "the donut" all refer to it.
