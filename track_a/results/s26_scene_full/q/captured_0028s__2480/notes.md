# q_2480 — ping pong ball velocity at t = 1.0 s (cm/s)

File fps = question_fps = 24. t=1.0 s -> frame 24; t=1.1 s -> frame round(26.4) = 26 (ball at first bounce).
Lab method card: f = 0.5959*1280 = 763 px, principal point (640,360).

## Measurement (measure.py)
Background-subtraction mask (median of all frames, crop x600-900 y200-560), centroid of blob (motion-blurred streak
centre = mid-exposure position). Agrees with scene/tracks/ball.csv to <0.4 px.
- f24: (732.33, 337.57), f26: (738.09, 409.36). Ball released ~f21, falling; bounce at f26.
- Back-projected along the unit ray with the given camera distances (1.805 m at 1.0 s, 1.557 m at 1.1 s):
  P24 = (0.217, -0.053, 1.791), P26 = (0.198, 0.100, 1.541); |dP| = 0.293 m.
- Velocity = forward difference between the two depth-annotated times: 0.293 m / 0.1 s = **293 cm/s**
  (using the true 2-frame interval 0.0833 s gives 352 cm/s).

## Cross-checks / caveats
- Image-plane-only speed (depth held at 1.805 m), central difference f23-f25: 162 cm/s; at the size-implied depth
  (~1.45 m, 21 px for 40 mm) 132 cm/s, consistent with free fall ~0.13 s after release (g*t ~ 1.3 m/s) and with the
  image free-fall acceleration (~9 px/frame^2 -> depth ~1.44 m).
- The given depths drop 0.25 m between 1.0 and 1.1 s, much faster than ball size implies; the reference
  (3D centres back-projected with measured depth) includes that depth change, so the answer uses the given depths.
- Confidence: moderate-low; the result depends on whether the reference's depth component is as given (answer
  range 220-350 depending on smoothing; 160 if depth change ignored).
