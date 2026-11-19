# q_1633 — thickness of the star (m)

Prior: height of the star = 0.2 m. Depths: 6.552 m at t=1.0 s (frame 24) and 8.345 m at t=2.0 s (frame 48), using question_fps 24. The file runs at 24.008 fps; I used frame indices throughout.

## Method
- `masks.py`: soft silhouette (alpha) of the star in every frame, measured as the colour distance from the beige background.
- `fit.py` / `refine.py`: a 3D model of a rounded extruded five-point star: a prism with outer radius R, inner/outer radius
  ratio k and thickness, dilated by a sphere of radius rho. It is placed in full perspective (principal point 540,540,
  focal length f fitted). The distance follows a quadratic in t pinned to the two given depths. The image position is
  matched to the silhouette centroid. The model is rendered with 4x supersampling and fitted by least squares on the
  alpha maps, from 16 random starting orientations, then refined on all 72 frames.
- Result: the star does NOT rotate (a fitted angular velocity came out about 0). Its apparent narrowing is caused by
  perspective. The face normal is about (0.90, -0.15, 0.41) in camera axes, so the face is seen about 66° off-axis, which
  makes the thickness visible as a side wall. The model matches every frame closely (overlay: frames/ov_lin5.png).
- Fitted f is about 1450 px. Fixing shape and orientation and fitting the depth freely per frame (`traj.py`) gives
  distances of 6.58 m and 8.40 m at frames 24 and 48 (given: 6.552 and 8.345, under 1% off). The model's vertical
  extent in camera axes is 0.204–0.213 m, against the 0.2 m prior (2–6% off), so the depth scale and the prior agree.
- The trajectory's 3D acceleration is only 0.8 m/s², so the motion is not ballistic and gravity cannot be used to fix
  the world up direction. I assumed the camera is level, with height measured along camera vertical.

## Thickness estimates (total thickness T = t*R + 2*rho)
| fit | loss | T (depth scale) | T scaled so the height is 0.2 m |
|---|---|---|---|
| refined lin5 (all frames) | 820 | 0.0268 | 0.0260 |
| refined c2 | 822 | 0.0297 | 0.0278 |
| refined c7 | 856 | 0.0258 | 0.0250 |
| profile over fixed T (even frames, `profile.py`) | min near T ≈ 0.0248 | 0.0248 | 0.0243 |

Second route: the loss profile over a fixed thickness (0.018–0.034) has a clear minimum near 0.025. This agrees with the
free fits, 0.025–0.030.

## Answer
Thickness ≈ 0.026 m (about 13% of the 0.2 m height). Confidence: moderate, about ±10%. The thickness trades off
against edge rounding and focal length, and the video compression blurs the star's side wall.
