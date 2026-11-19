# q_3254 – velocity of the cup at 2.20 s

**Prior:** the cup's acceleration from 2.00 s to 2.30 s is 0.32 m/s². No depth_info.

**Time base:** the file runs at 30.013 fps and question_fps is 30, so they are effectively the same. 2.20 s is frame 66, and 2.00-2.30 s is frames 60-69.

**Scale:** this is an internet video, so I used a single planar scale taken from the prior's pixel acceleration, m/px = 0.32 / a_px. This gives v = 0.32 × v_px / a_px, and the scale cancels except as this ratio.

## Measurement
- **Reference point:** the centre of the mug body, the midpoint of the left and right body edges, taken from background differencing against frame 100. The body is fully in view in frames 62-79.
- **Why not an edge:** each single edge is biased by perspective. The apparent body width goes 455 → 420 → 460 px across the frame. The centre cancels this.
- **Camera:** the background drift is ≤ 7 px over the whole clip, so I treated the camera as static.
- **My own re-measurement (edges.py):** rows 640-800, sub-pixel 50% crossings. It agrees with scene/tracks/mug.csv to within about 1 px.
- **Centre fit, quadratic in t:**
  - frames 62-79: a = 1413 px/s²
  - frames 62-72: a = 1420 px/s²
  - frames 60-69, extrapolated: a = 1452 px/s²
  - The rms residual is < 0.5 px, so the acceleration is close to uniform.
- **Velocity at frame 66 (forward difference, 66→67):** 75 px/frame = 2245 px/s. The fit gives 2244 px/s.
- **Result:** v = 0.32 × 2245 / 1420 ≈ **0.505 m/s**. Across the fit windows the value ranges from 0.495 to 0.508.

## Second route and checks
- **Record track:** the scene/ record's centre track, fitted independently in fit.py, gives 0.500-0.510.
- **Edges alone:** they disagree (right edge 0.45, left edge 0.78) because of the perspective width change described above, so I rejected them.
- **Implied scale:** 0.32 / 1420 = 2.25e-4 m/px. That makes the mug body 420 px ≈ 9.5 cm wide, which is plausible for a real mug.

**Confidence:** moderate to high. The main uncertainty is which point the annotators tracked: if they used an edge, the answer could differ by about 10%.
