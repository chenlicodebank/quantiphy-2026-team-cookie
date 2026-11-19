# Q1305 — average speed of the bicycle over the whole clip (m/s)

The file and the question both run at 24 fps, 72 frames. Frame 0 is the same as frame 1, and the bike starts moving between frames 1 and 2.

## Focal length (the main unknown)
- **Vanishing points** (`vp.py`): I fitted kerb lines in frame 0 with sub-pixel edges (rms < 0.2 px).
  - The near kerb and the bottom edge of the right island meet at VP1 = (-114, 525.5).
  - Two road edges that recede to the right (lines A and B) meet at VP2 = (4843, 532.7).
  - If the two directions are at right angles, with the principal point at (1080, 540), f = 2120 px.
- **Check against the prior** (`van_check.py`): I tracked the white van's rear edge (record, f28-71) along the road direction (VP2) and calibrated it with D(1.58 s) = 29.81 m.
  - At f = 2120 the fitted acceleration is **4.01 m/s²**; the prior says 4. At f = 2000 it is 4.17, and at f = 2400 it is 3.70.
  - The van's predicted distance at 0.58 s is 29.20 m; the given value is 29.24 m.
- **Bike consistency**: at f ≈ 2000-2200 the bike's 3D motion between its two given depths is parallel to VP2 (within about 1°) and at right angles to VP1.
  - The projective fit of the bike's pixel track also gives Z38/Z14 = 1.095, which matches f ≈ 2120.

## Bike speed
- **Route 1** (`speed.py`): I back-projected the bike origin (ref_x 494 at f14 and 889 at f38) with the given depths 27.754 m and 29.412 m.
  - |P38 − P14| over 1.0 s gives **5.39 m/s** at f = 2120 (5.33-5.43 for f = 2100-2150).
- **Route 2** (`bike_route2.py`): I fitted a constant-velocity straight line in 3D to the projective head-x track (frames 1-71, rms 1.8 px) and scaled it with D38.
  - This gives **5.374 m/s**, constant, and it reproduces D14 = 27.748 m (given 27.754 m).
- The speed is constant at about 5.38 m/s.
- The mean of the per-frame speeds over frames 1-71 depends on frame 1:
  - With the zero step at frame 1 (frame 0 = frame 1) it is 5.30.
  - Without that zero step it is 5.38.
  - **Answer: 5.32 m/s**, between the two. The f uncertainty of about ±50 px gives about ±2%.

Confidence: fairly high (±3%).
