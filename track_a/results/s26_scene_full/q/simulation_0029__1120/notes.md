# Q1120: height of the boat (m)

The file runs at 25 fps, but question_fps is 24, so t=1 s is frame 24 and t=2 s is frame 48. All frame numbers below are file frame indices.

## Focal length, from the eagle prior (speed 12 m/s) and the eagle depths 139.70 / 147.16 m (solve.py)
- Eagle centroid from scene/tracks/bird.csv: frame 24 is at (235.6, 521.8) and frame 48 at (409.7, 527.75) (the frame-48 value is interpolated). The principal point is assumed at (480, 480).
- I back-projected these with the given depths and solved for the focal length that gives |p2 - p1| = 12 m over 1 s: f = 2644 px.
- With a quadratic fit of the pixel track (frames 10-62) the same solve gives f = 2659 px.
- Requiring the mean per-frame 3D speed to be 12 m/s (depth linear in time) gives f = 2660 px over frames 25-48 and 2654 px over frames 13-60.
- **f ≈ 2655 px** (horizontal field of view ≈ 20.5°).
- Sanity check: the boat hull is about 160 px long, which is 160 × 134 / 2655 ≈ 8.1 m, plausible for a small fishing boat. The boat's implied speed is about 4 m/s.

## Boat height in pixels (mast.py, rudder.py)
- I re-checked the top of the thin mast pole on the pixel columns: it is at y≈487 at frame 24 and y≈484 at frame 48. The scene fit gives 488.2 and 486.0.
- Waterline (bottom of the dark keel band): 679 at frame 24, 682-683 at frame 48.
- Height: 192 px at frame 24 → 192 × 133.957 / 2655 = **9.69 m**.
- Height: 198.5 px at frame 48 → 198.5 × 131.256 / 2655 = **9.81 m** (second route, at a different time and depth).
- The depth correction for the off-axis position is below 0.3%.

## Ambiguity
- The world bounding box also includes any part of the hull below the water, which cannot be seen.
- At the stern, the dark patch below the waterline (y 683-688) looks like the reflection of the rudder, not the rudder itself.
- The submerged draft is unknown; it is probably 0-0.5 m.
- Answer: **9.85 m**. The visible part measures 9.75 m; I pushed the answer slightly up to allow for a small draft.
- Confidence: moderate. The error is dominated by the focal length (±1%) and the unknown submerged part (0 to +5%).
