# q_2858 – orange ball diameter (cm)

Lab clip 1280x720, 24 fps (file fps = question_fps = 24). Orange ball = scene/ `basketball` track (rolled by the
crouching person toward the camera). f = 0.5959*1280 = 762.8 px, principal point (640,360).
depth_info: f12 (t=0.5) d = 2.3557 m, f24 (t=1.0) d = 1.8100 m (f24: ball cut by the bottom image edge).

## Method
- Mask = non-green pixels (chroma background), component at the tracked centre (`measure.py`, overlay
  frames/f12_fit.png – clean silhouette at f12).
- The ball is far off-axis (theta = 27 deg at f12, 25 deg at f24), so its image is the perspective ellipse of a
  sphere: tangential semi-axis b = f sin(a)/sqrt(cos^2 th - sin^2 a), radial a/b ~ 1/cos th. Verified in the data
  (`orient.py`): radial/tangential extent ratio 1.08-1.10 vs predicted 1.09-1.11 in f14-21, so the off-axis
  stretch is real and must be removed (the naive depth*px/f gives ~24 cm at f12 and ~22 cm at f24, inconsistent).
- `fit_boundary.py`: fit that exact sphere-projection ellipse, swept by a linear motion-blur segment along the
  tracked motion direction, to the contour points (soft-L1 least squares). The lower boundary is excluded in the
  final fit ("cut") because the mask bulges there (dark underside / floor contact shadow; residuals 1.3-2.6 px
  with it vs 0.7 px without). D = 2 d sin(alpha).

## Results
| frame | d (m) | sin(alpha) cut fit | D (cm) |
|---|---|---|---|
| 12 (t=0.5) | 2.3557 | 0.03938 | 18.55 |
| 24 (t=1.0) | 1.8100 | 0.05144 | 18.62 |
Second route: the two given depths at two different frames (different apparent sizes 0.039 vs 0.051, one
frame truncated at the image edge) give the same diameter to 0.4 %. Full-contour fit (incl. bottom): 20.2 / 18.7 cm.
Naive (no off-axis correction): ~23.8 / ~22 cm – rejected (inconsistent between the two depths).

Velocity prior (2.21 m/s at 0.5 s) check: back-projected centres give ~1.6-1.9 m/s around f12-16 (f11->f12 has a
jump of 31 px vs ~18 px elsewhere, giving 2.4 m/s for that step); the prior is not used for scale since depths are given.

Answer: 18.6 cm (consistent with a size-3 mini basketball, ~18 cm). Confidence: moderate-high.
