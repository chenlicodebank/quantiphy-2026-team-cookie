# q1450 – forklift length (fork tips to rear bumper)

Prior: a = 2 m/s^2. depth_info: |O(t=1)| = 16.7953 m, |O(t=2)| = 19.0980 m. The file and the question are both 24 fps (frame = round(24 t)).

## Method (3D, pinhole, cx, cy = image centre)
1. `track_pts.py`: KLT tracks of 175 corner features on the forklift body for frames 0–71, with a forward–backward check. 144 survive the outlier cut; spinning wheel features are removed by their residual.
2. `fit.py`: rigid straight-line motion Q_i(t) = Q0_i + d·(t − t0)^2, which is a = 2 m/s^2 from rest. The metric scale comes from the prior. Variable projection: Q0_i are solved linearly and (t0, d) are fitted.
   - Reprojection rms is 0.81 px over all 72 frames, so the acceleration is uniform. t0 ≈ 0.
   - The focal length cannot be recovered from the trajectory alone: rms is identical for every f. The depths fix it.
   - Bug I fixed: the fit could land on the mirrored solution behind the camera. It is now flipped automatically.
3. `extremes.py`: per-frame mask (sum|RGB − bg| > 40) and its extreme points along 72 image directions (overlays in frames/ext_*.jpg).
   - `recon.py` triangulates each extreme track across frames 15–71 as a body point, using the known motion.
   - Points are expressed in the vehicle frame: forward = d; up ⟂ d with zero camera roll; lateral.
   - Roll check: the front-wheel and rear-wheel ground contacts come out at the same height (within ~3 cm), so the zero-roll assumption holds.
4. Length = forward-coordinate extent from the fork tip (image directions 160–185°, all agree to 1 mm) to the rear counterweight/bumper (directions 15–25°). Track rms is about 0.5–0.8 px.
5. Focal length (`solve_f.py`): the origin is taken at the horizontal bbox centre, at height fraction h of the bbox. Each given depth then yields its own f:
   - h = 0 (ground): 3147 / 3173
   - h = 0.2: 3264 / 3263 (the two depths agree here)
   - h = 0.5: 3419 / 3383
   - The best consistency is f ≈ 3260 px (HFOV ≈ 43°).

## Results
| f (px) | L (m) | H (m) | W (m) |
|---|---|---|---|
| 3150 | 4.24 | | |
| 3260 | 4.21 | 2.63 | 1.53 |
| 3400 | 4.18 | | |

L changes only about 1.5% across the whole plausible f range. Even f = 2500–5000 gives L = 4.42–4.09.

Second route: f taken from the depth difference alone (|O2| − |O1| = 2.303 m against the 3 m path between t = 1 and t = 2, origin at the mask centroid) is f ≈ 3330. That gives L ≈ 4.20, which agrees.

Answer: **4.21 m**. Confidence is good, about ±3%. The main uncertainties are where the origin sits (it affects f only weakly) and the silhouette-extreme definition of the rearmost point.
