# Q1351 — height of the white car (simulation_0067)

Answer: **1.98 m**. The "white car" is the large white cargo van, which is `van` in scene/. The file fps (24) is the same as question_fps (24): t=0.58 s is frame 14 and t=1.58 s is frame 38.

## Camera calibration (3D scene, static camera)
- **Vertical vanishing point** (`vvp.py`): sub-pixel line fits to 10 poles (6 street lamps and 4 traffic-light poles) give VP = (1068.5, 2650). Dropping any one pole moves it by less than 20 px. Its x is close to the image centre, so roll is about zero and the principal point is at the centre.
- **Focal length** f² = -(VPa - c)·(VPb - c) for orthogonal directions:
  - horizon (y ≈ -45) with the vertical VP: 1109–1113
  - east-west road VP with the vertical VP: 1117
  - the two road VPs (if the roads are perpendicular): 1107
- **Independent check of f**: I fitted a 3D van model to the silhouettes at f = 1080, 1113 and 1180. The fit loss is lowest near f ≈ 1109 (parabola through 0.0984, 0.0958 and 0.1124).
- At f = 1113 the fitted van trajectory is a clean constant-acceleration path from near rest (rms 0.03 m, t0 ≈ -0.06 s). At f = 1080 and f = 1180 it is not: a changes with the frame window and t0 is wrong. I used **f ≈ 1110**.
- **Ground plane and camera height** (`ground_ped.py`, `ped_height.py`): I placed the pedestrian's pelvis at 0.53 of the bbox height and set it at the given distances. This gives camera height H ≈ 7.0–7.09 m, and the implied pedestrian height is 1.81–1.87 m (plausible, so the scene is roughly real scale).

## Van height
- **Masks** (`vanmask.py`, `posefit.py`): background difference minus shadows (and minus the taxi's yellow pixels).
- **Van model** (`boxfit3.py`): a body with a sloped windshield and a lower hood, plus four wheels, on the ground plane. I fitted the shape jointly over frames 22, 30, 38, 46 and 54, with one ground pose per frame. IoU is about 0.93 and the overlays (frames/fit3B_*.png) match the outline.
  - At H = 7.04 the fit gives h = 2.000 m at f = 1113 (L 5.46, W 1.97) and 2.084 m at f = 1080. Interpolated to f = 1110: h ≈ 2.008 × (H/7.04).
- **Per-frame poses** (`posefit.py`, frames 6–70) give the 3D trajectory. `summary_f.py` sets the scale in three ways:
  1. **Prior a = 4 m/s²** (free quadratic fit, f = 1113): a = 4.06 in H = 7.04 units, so scale 0.985 and **h = 1.97**. If I instead force the van to start from rest at frame 1: h = 1.85.
  2. **Given van distances** (frames 14 and 38), origin at the bottom centre of the van: scales 0.992 / 0.967, **h = 1.96**. Origin at the box centre: scales 1.054 / 1.005, h = 2.06. The two frames disagree more under this hypothesis, so it is less consistent.
  3. **Pedestrian ground plane** (H = 7.04): **h = 2.00**. With the pelvis at 0.9 m: 1.97.
- **Consistency:** the given van distances are reproduced to within about 1.5 % with the origin at ground level under the van centre (best fit residuals -0.16 m and +0.09 m). The other objects' distances are roughly reproduced too.

## Result and confidence
The routes agree on 1.96–2.00 m, with 1.85 and 2.06 as outliers under the less likely assumptions. Answer: **1.98 m**.

Confidence is moderate, about ±4 %. The main sensitivity is the focal length: the depth-based h changes by about 1 % per 1 % of f, and the acceleration-based h is much more sensitive. f is pinned to about ±1 % by both the vanishing points and the silhouette fit.

## Corrections to scene/
- The record's focal estimate (~1100) is close. The refined vertical VP is (1068.5, 2650), not (1075, 2604).
- The van's bbox centre is not the projection of its 3D centre, so I used the 3D model fit instead.
