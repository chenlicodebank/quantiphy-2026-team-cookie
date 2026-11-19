# q_1551: shark acceleration at 0.5 s (simulation_0159, 3D, 24 fps; question_fps 24, the same as the file)

## Data
- Prior: turtle acceleration 2.639 m/s^2. Depths: turtle 15.232 m (t=0) and 14.968 m (t=0.5); shark 16.474 m (t=0) and 15.744 m (t=0.5).
- Tracks: scene/tracks core centroids (origin proxy). Shark core is cut by the edge in f0–19, so the fits use the shark core in f20–37 and the snout x (bbox_x0) in f0–37.

## Model
Both animals start from rest (image speed ~0 at f0) and move with constant acceleration along a straight 3D line: P(t) = P0 + ½·a·t²·d.
- P0 is back-projected from the image point at t=0 and the given t=0 distance, with principal point (960, 540).
- The t=0.5 distance (frame 12) is used as a constraint.
- The focal length f is unknown.

## Focal length
- **Turtle alone** (a = 2.639 given, from rest): f ≈ 2480 px, rms 6.8 px (noisy because of flipper strokes), reproduces D(0.5) = 14.966. The minimum is shallow, over 2400–2600.
- **Shark alone**, core in f20–37 plus its distances: f ≈ 2760, rms 1.07 px.
- **Joint fit** (turtle + shark core + shark snout with a constant 3D offset): f ≈ 2705. The snout residuals are mostly within ±8 px.

## Shark acceleration (constant, so the value at 0.5 s is the same)
| route | f (px) | a (m/s^2) |
|---|---|---|
| joint fit | 2705 | **7.20** |
| without snout | 2596 | 7.29 |
| without turtle | 2901 | 6.97 |
| turtle-down-weighted | 2794 | 7.09 |
| f fixed at 2480 (turtle-only f) | 2480 | 7.45 |

The per-frame speed difference at frame 12 from the fitted trajectory gives 7.20.

## Checks
- The model's Z20/Z36 ≈ 1.33–1.35 agrees with the shark's full bbox-height ratio of 1.35 (260 → 352 px). The core-height ratio (1.50) does not fit; it is likely skewed by the core opening, so it was not used.
- With a = 7.2 from rest, the displacement over 0–0.5 s is 0.9 m, of which 0.73 m is depth change (the shark heads toward the camera, off-axis to the right), which fits the given depths.

Answer: **7.2 m/s^2**. Confidence moderate: the answer spans 7.0–7.45 depending on f (±3%), and it relies on the from-rest, constant-acceleration assumption, which the 1 px fit supports.
