# simulation_0296 — measurement record (pixels, seconds)

Video: 2560x1440, 24 fps, 72 frames (t = frame/24, 0 … 2.958 s). Blender render, **2D** scene.

## Scene
- **Camera**: static. Phase correlation of the top and bottom background strips against frame 0 gives a shift of 0.00 px in every frame. The view looks straight down at the ground, so there is no horizon or other usable perspective cue.
- **butterfly**: the only moving object, and there is only one. It is light blue (morpho-like) and seen from above. Its body axis is horizontal with the head to the LEFT (the larger forewings are on the left), and the wings spread up and down in the image. It flies leftwards across the frame, from x≈1836 to x≈742, at y≈720→733. It is visible and never occluded in all frames 0–71.
- **ground**: static rocky ground with mossy stones and grass covering the whole frame. There are no lines, markings or distinct props.

## Files
- `scene.json`: inventory, camera, summary pixel measurements and events.
- `tracks/butterfly.csv`: one row per frame (0–71) with these columns:
  - `ref_x, ref_y`: the **reference point** = centre of the wing-mask bounding box. On the overlays it sits on the body at the forewing/hindwing junction (thorax), so it is the best proxy for the rig origin.
  - `centroid_x/y`: centroid of the mask area.
  - `bbox_x0..y1`
  - `extent_x`: horizontal extent, along the flight and body axis.
  - `extent_y`: vertical extent, i.e. the apparent **wingspan** across the body.
  - `pca_len / pca_wid / pca_angle_deg`: extents along and across the mask's principal axes.
  - `area_px`
  - `occluded`: always 0.
- `scripts/track.py`: segmentation. A pixel belongs to the butterfly if it is bright blue (B>110, B−R>35, B>G) **and** differs from a median background by more than 30. The median background was computed from every 3rd frame over the band y 450–1000; it removes static bluish stones. Blobs are grouped by a 19 px dilation, fragments under 300 px are dropped, and overlays are written to `frames/ov_XX.png`.
- `scripts/analyze.py`: camera-shift check, duplicate-frame check, flap extrema, track overlay.
- `scripts/write_scene.py`: builds scene.json.
- `scripts/probe.py`: first colour probe.

## Key numbers (pixels)
- **Position, frame 1 → 71**: (1836.0, 720.5) → (742.5, 733.5). Net displacement is (−1093.5, +13.0) px.
- **Pace**: mean −15.6 px/frame in x. Per-frame steps are 12–18.5 px.
- **Path length, frames 1–71**: 1094.9 px from the raw sum of steps. The motion is almost straight, so path length ≈ displacement.
- **Wingspan (`extent_y`)**:
  - Maximum when the wings are flat: **254–261 px**, overall maximum 261 at frame 18. This is the plateau over frames 0–3, 17–23, 37–44 and 58–65.
  - Minimum when the wings are edge-on: **46 px at frame 9**, 52 at frame 30, 51 at frame 51.
- **Horizontal (flight-direction) extent of the wings (`extent_x`)**: 188–194 px when the wings are open, 169–206 px when folded. This is the wings' length along the body axis, not the body itself. The thin dark body could not be measured separately.
- **Apparent size**: it does not change systematically, so the butterfly stays at a constant depth, consistent with 2D. The extents only oscillate with the wing beat.

## Events
- Frames 0 and 1 are identical. Motion starts at frame 1→2 (t = 0.042–0.083 s).
- The wings are edge-on at frames 9, 30 and 51 (t = 0.375, 1.25, 2.125 s), and open or flat around frames 0, 18, 39 and 60. This gives a wing-beat period of about 21 frames (0.875 s).
- The flight is steady leftwards, with a slow downward drift of about 13 px in total. There are no stops, reversals or contacts, and the butterfly is still moving in frame 71.

## Reliability and ambiguities
- **ref_x/ref_y**: about ±2 px when the wings are open. When the wings fold (frames ~7–12, 28–31, 49–53, 69–71) the faint, semi-transparent wing tips are partly missed, so ref_x can be biased by up to about 5 px. For example, frame 10→11 shows a 22 px step between 12.5 px steps.
  - For speeds, a 3–5 frame smoothing or a fit over a window is more trustworthy than a single backward difference.
  - `centroid_x` is worse during the folds, so prefer `ref_x`.
- **Offset to the true origin**: the offset from ref to the true rig origin is unknown but roughly constant, so it does not affect displacements.
- **Wingspan maximum**: reliable to about ±3 px; the mask edge includes the dark wing border.
- **Scale**: no metric scale is inferred. In a 2D scene, use one metres-per-pixel scale from the question's prior, e.g. a known wingspan ↔ 254–261 px max, or a known speed ↔ the per-frame px step.
- **Not answerable from pixels**: the butterfly's height above the ground. The ground is static texture only, and there are no shadows of the butterfly worth measuring.
