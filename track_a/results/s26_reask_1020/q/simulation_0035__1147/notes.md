# Q1147 – eagle speed (m/s)

File and question fps are both 24, so frame = round(t*24). Frames 24 and 48 correspond to t=1 s and t=2 s.

## Scale
- Person (prior: 1.75 m). Re-measured in `measure.py` (median-background mask): 41–42 px tall at frames 20–30 and 44–51 (walking pose).
  The person's depth is constant (139.10 m), and they sit at about (165,728) px.
- Focal length: f = H_px·Z/H_m, where Z is the depth component along the optical axis. The principal point is assumed at (540,540).
  This gives f ≈ 3230–3370 px over H_px 41–42 and an effective walking height of 1.72–1.75 m.

## Eagle
- The bird's mask centroid comes from `measure.py` (it matches `scene/tracks/bird.csv`): frame 24 at (274.1, 587.3), frame 48 at (477.35, 593.8).
  Frames 24 and 48 fall at the same phase of the ~24-frame flap cycle, so the wing-pose offset of the centroid cancels.
- 3D position = depth_info distance × unit ray. Displacement between t=1 and t=2 ≈ (8.4, 0.4, 7.9) m, so the speed is ≈ 11.5 m/s.
- The image x-step falls from 9.6 to 7.4 px/frame across the clip. That fits a bird flying at constant speed while receding (depth 139.7 → 147.2 m).

## Checks
- Sensitivity (`solve.py`): across the f range and with raw or cycle-smoothed centroids, the speed is 11.40–11.69 m/s. The radial component (7.45 m/s, straight from depth_info) dominates, so the result depends only weakly on f.
- Plausibility: about 11.5 m/s is a realistic eagle cruising speed.

Answer: 11.5 m/s. Confidence: good (±3%), assuming constant speed over the clip.
