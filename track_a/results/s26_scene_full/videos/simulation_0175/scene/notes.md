# simulation_0175 – measurement notes

2D simulation (Blender) at 24 fps, 40 frames (0–39, t = frame/24), 1920x1080 px. Units are pixels and seconds,
with x pointing right and y pointing down. No metric scale is assumed. The answering session applies one
m/px scale taken from the prior (for example the airplane's real length divided by its 466 px pixel length).

## Scene
A white regional/business jet flies right to left across the upper sky. It has rear-mounted twin engines, a T-tail
and a red/gold cheat line, its landing gear is down and it is seen exactly side-on. The background is static: a tall
rocky islet with trees on top (centre-left), a pale sand beach, a turquoise sea with animated ripples, and the
horizon at y ≈ 895. A faint dark patch, most likely the airplane's shadow, crosses the sea to the right of the
island. There are no people, animals or other vehicles.

## Files
- `scene.json`: inventory, pixel sizes, camera information, events and summary motion numbers.
- `tracks/airplane.csv`: one row per frame. `ref_x, ref_y` is the reference point (the centre of the nose-tip..tail-tip
  box, used as the origin). `mask_cx, mask_cy` is the mask centroid. `bbox_*` holds the visible box; for partial
  frames the nose or tail sits at the frame edge. `visible_length_px` and `visible_height_px` are the visible box
  sizes. `occlusion` is one of full / partial_entering_right_edge / partial_exiting_left_edge / out_of_frame.
  `dx_from_prev_px` is the leftward shift from the previous frame found by cross-correlation (the most precise
  per-frame motion value).
- `tracks/airplane_raw.csv`: the raw mask track (threshold 25). Its nose edge misses the faint glass nose by about
  15–25 px.
- `tracks/plane_shadow.csv`: the dark blob on the water (secondary feature, low reliability).
- `scripts/`: `track_plane.py` (median-background segmentation), `refine_plane.py` (low-threshold nose edge and
  cross-correlation shifts), `build_track.py` (final csv), `track_shadow.py`, `static_and_camera.py`,
  `check_overlay.py`. The `_*.csv` and `_*.json` files there are intermediate outputs.

## Key measurements
- **Airplane length**: nose tip to tail tip is **466 px** (median over the fully visible frames 9–31, range 458–474;
  ±5 px). Height from fin top to landing-gear bottom is **95 px** (y 91–185). The fuselage body alone is ≈ 38 px tall.
  The size is constant across frames, which confirms motion parallel to the image plane.
- **Airplane motion**: purely horizontal and leftward. Vertical drift is 0 px. The per-frame shift is
  **61.5 ± 0.2 px/frame**, constant over frames 4–38 (≈ 1476 px/s), with no detectable acceleration.
  `ref_x ≈ 2174.6 − 61.66·frame` (edge-based ±4 px). Example: at frame 18, ref = (1069.5, 138).
  - For partial frames (1–8 and 32–39), ref_x is extrapolated from the visible edge using L = 466 px; these values
    are accurate to about ±5 px. The cross-correlation shifts are also less reliable at frames 1–3 and 39.
- **Events**: the nose enters at the right edge at frame 1 (frame 0 has no plane). The airplane is fully visible
  from frame 9 to frame 31. The nose reaches the left edge at frame 32, and the last tail sliver is at frame 39.
  It passes over the island centre (x ≈ 922) at about frame 20.3. There are no starts, stops, bounces or direction
  changes.
- **Rock island** (static, frame 0): bbox x 624–1221, y 531–1030. Width ≈ 598 px; height from the treetops to the
  rock base ≈ 500 px (base ±10 px, because the vegetation and beach blend).
- **Sand beach**: x ≈ 460–1460, y ≈ 985 down to the frame bottom (approximate).
- **Camera**: static. Phase correlation of the rock region against frame 0 shifts by ≤ 0.5 px over all frames.

## Ambiguities
- The cockpit glass is pale blue against blue sky. A low threshold (diff > 8) is needed to catch the nose tip; the
  standard mask ends about 15–25 px behind it.
- The airplane's origin is assumed to be the centre of its bounding box. The mask centroid lies about 7 px to the
  right of it (mask_cx ≈ ref_x + 7) and about 3 px lower.
- The shadow on the water is weak and its interpretation is uncertain. Frames 16–29 are usable (y ≈ 973,
  ≈ −57 px/frame). Frames 30–33 in its csv are noise near the island's own shadow.
- The water texture animates, so the sea is not a reliable static reference. Use the rock instead.
