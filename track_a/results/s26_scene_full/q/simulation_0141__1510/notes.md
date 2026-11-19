# Q1510 — side length of the floor tile (m)

Prior: walking speed 1.693 m/s. depth_info: d(t=0)=4.15 m, d(t=0.5 s, frame 12)=5.03 m. The file rate and question_fps are both 24.

## Floor-plane geometry (camera static, optical axis horizontal)
- Vanishing point from 6 longitudinal tile seams fitted in a median background (`vp_fit.py`): (959.4, 539.5).
  The transverse seams are horizontal, so there is no roll and the horizon is at y = 539.5.
- For a floor point: X = h·s with s = (x−cx)/(y−cy), and Z = f·h·w with w = 1/(y−cy).
- Longitudinal seam spacing: Δs = 0.7066 (5 intervals, 0.7038–0.7095), so the lateral tile size is 0.7066·h.
- Transverse seam spacing (`tile_period.py`, rectified profile with comb fit): Δw = 2.50e-4. Eleven seams in a clean
  column give a mean of 2.505e-4, and the comb fit gives 2.498e-4. So the tile size along the depth direction is f·h·2.50e-4.
- The depth-direction size depends only on the product f·h, so it does not need the focal length.

## Scale from the man's steps (`steps.py`)
- Foot-plant plateaus (heel = lowest sole row): y = 1052, 972, 913, 868, 833. These start at frames 0, 10, 22, 34, 46,
  so the step period is exactly 12 frames (0.5 s).
- In w they are perfectly linear: Δw_step = 3.6433e-4 (residuals < 0.02e-4).
- Step length L = 1.693 × 0.5 = 0.8465 m, which gives f·h = L/Δw_step = 2323.
- **Tile (depth side) = 0.8465 × 2.50/3.6433 = 0.581 m.**

## Second route / consistency
- Change in the given depths: d12 − d0 = 0.88 m per step. Using that as the step length gives 0.604 m. It agrees with the speed prior within 4 %.
- Rate of 1/height_px at matched gait phases (frames 0–24 and 0–48): the body's Z grows by 0.1832–0.1845 of Z0 per step.
  With L = 0.8465 that puts the body at Z0 ≈ 4.6 m. The foot-plateau ratio gives the heel at 4.53 m, which is self-consistent.
- Conflict: the absolute d0 = 4.15 m does not fit the pixel perspective ratios. The pixel ratio per step is 1.185, but d12/d0 = 1.212.
  Taking d0 as the body depth would give f·h ≈ 2080–2140, i.e. a tile of 0.52–0.535 m. Two cues agree on the motion scale
  (the speed prior and Δd), so I trust that scale. The answer is 0.577, between 0.581 (speed) and the other readings.
- Square-tile assumption: f = Δs/Δw = 2826 (HFOV ≈ 37°). That makes the camera height ≈ 0.82 m and the man about 1.1–1.2 m tall,
  which is small for a human. If the man were instead about 1.75 m, the tiles would be about 0.87 × 0.58 m (lateral × depth).
  The question says "side length", which implies a square tile, and the depth side (0.58 m) is the one fixed without f in either case.

## Confidence
Moderate. The depth-side measurement is precise (about 1 %). The main risk is the inconsistent absolute depth_info
(it would give 0.52–0.535) and the square-tile assumption.
