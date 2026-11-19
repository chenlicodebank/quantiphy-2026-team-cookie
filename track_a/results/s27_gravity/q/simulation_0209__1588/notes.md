# Q1588 – typewriter speed at t = 0.125 s (frame 3, question_fps = file fps = 24)

Prior: the typewriter falls with a constant acceleration of 9.8 m/s² before 0.45 s (it lands at about frame 10). Because the scalar speed
changes at exactly g, the fall is a pure vertical free fall: v(t) = g (t - t0). The backward-difference speed at frame 3 is
g (2.5/24 - t0), so the answer depends only on t0, the time when the speed would be zero.

## Measurement
- `track_keys.py`: intensity-weighted centroid of the cream key caps for frames 0-9. These caps are visible in every frame, including
  frames 0-1, where the top of the typewriter is cut off. The y diffs are 7.6, 19.4, 29.1, 40.5, 50.3, 60.9, 71.1, 79.7 and 89.5 px/frame.
- `fit3d.py`: pinhole fit of a vertical free fall with g = 9.8. The camera has no roll and is pitched down by θ. The start point
  lies at depth 4.32 m (depth_info at t=0). A rest constraint requires the point on the same vertical at depth 4.501 m (depth_info
  at t=0.5 s) to project onto the rest bbox centre (1230, 608). Free parameters: f, θ, t0 and the start pixel.
  - Result: f = 2738 px, θ = 15.8°, t0 = -0.186 frame. The fit residual is 0.28 px RMS over 10 frames.
  - The fall distance to the rest depth (0.91 m) agrees with the fall distance at the impact frame 10 (0.88 m).
- Speed at frame 3 = 9.8 × (2.5 + 0.186)/24 = **1.097 m/s**.

## Checks
- The fitted pitch puts the horizon at 540 - 2738·tan15.8° ≈ -235 px. This independently matches the horizon in scene.json, which
  was estimated from the desk vanishing points at about 200-280 px above the image.
- `fit_sens.py` varies the key-to-origin offset (10-35 px), the rest pixel (595-620) and the frame subset (all, 2-9, 0-6). t0 stays
  between -0.12 and -0.22 frame, giving a speed of 1.07-1.11 m/s.
- If the typewriter were released from rest exactly at frame 0, the speed would be 1.02 m/s (1.04 m/s with Bullet's substep
  offset). The data clearly show motion already under way at frame 0: the first diff is 7.6 px, not about 5.5 px.
- Answer: 1.09 m/s. Confidence: good, about ±3 %.
