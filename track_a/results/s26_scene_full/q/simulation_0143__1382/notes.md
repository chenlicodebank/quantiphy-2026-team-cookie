# q_1382 — side length of the floor tile (simulation_0143)

Prior: man height 1.8 m. Depth to the man: 7.21 m at t=0 (frame 0) and 7.91 m at t=0.5 (frame 12). File fps = question fps = 24.

## Floor geometry (frame 99, `floor.py`, `seams.py`, `transverse.py`, `radial.py`)
- I fitted the 5 dark lengthwise grooves to sub-pixel accuracy (rms 0.3–0.5 px). They meet at VP = (959.3, 539.8). So the camera
  is level, with the horizon at row 539.8 (≈ image centre).
- Groove spacing in px = 0.7074 × (y − 539.8), constant across all 4 tile columns (±0.3 %). A radial profile found
  no fainter grooves in between.
- The crosswise tile boundaries (texture changes plus thin bevel highlights) sit at rows 1064, 1003, 955, 916, 883, 856, (833, 812).
  Their spacing in 1/(y − yh) is a steady 0.000250 (±1 %). So they are evenly spaced on the ground.
- For a level camera: tile width across the corridor W = h × 0.7074, and tile length along the corridor
  L = 0.000250 × f·h, where h is the camera height.

## Scale from the man (`camh.py`)
- f from height_px × Z / 1.8: 1716 (frame 0), 1743 (frame 12), so f ≈ 1730. Z is the pelvis depth with the off-axis
  correction applied: 7.20 and 7.86 m.
- f·h = Z × (feet_y − yh): 2183 (frame 0) and 2245 (frame 12). This gives h = 1.26–1.30 m.
- Independent route, needing no f: h/H_pose = (feet_y − yh)/height_px over all 100 frames. The 0th–25th percentile gives
  h = 1.27–1.29 m for H = 1.8 m.
- Result: h ≈ 1.28 m. **W = 0.90–0.92 m (0.905)** and **L = 0.546–0.561 m (0.55)**.

## Ambiguity
The render shows rectangular tiles, not squares: about 0.90 m across the corridor × 0.55 m along it. A square tile
cannot fit the given depth and height. It would need f·h ≈ 3600 (the man at ~12 m) or h ≈ 0.78 m (the man ~1.1 m tall).
Following the named-size rule (length = the longer horizontal extent), I answer with the longer side, 0.905 m.
The other reading is 0.55 m.

Confidence: the longer side is good to about ±3 %. The main uncertainty is which side the question means.
