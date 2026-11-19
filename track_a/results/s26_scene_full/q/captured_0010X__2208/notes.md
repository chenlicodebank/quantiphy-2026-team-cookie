# Q2208: acceleration of the ball at t = 0.6 s (frame 14 at 24 fps; the file is also 24 fps)

**Scene.** A pendulum (ball on a string, pivot at about (637,229) px), swinging mostly toward and away from the camera.
At frame 14 the ball is about 3 frames before its near turning point (frames 16–18), so it is slowing down.
Camera: f = 0.5959·1280 = 763 px, principal point (640,360).

**Track check.** I checked the centroids in scene/tracks/ball.csv on zoomed crops of frames 9–17 (frames/crops.png).
They sit on the ball, including across the switch from red to pale mask at frame 12.

**Why a model.** Per-frame depth from the apparent diameter is too noisy (±2 px out of 35 px) to take a second
difference. Smoothed diameter depths give 2–8 m/s² depending on the window (route2.py), so that route is unusable.
Instead I fitted a physical pendulum to all 49 frames: the pixel centroids, the six depth_info distances and
(weakly) the diameters.
- pend.py: planar pendulum, g left free.
- sph.py: spherical pendulum with damping. Fitted parameters: pivot depth, camera pitch and roll, L, initial state.
  g is either fixed at the prior's 9.8 or left free.

**Fit results.**
- g fixed at 9.8: L = 0.332 m, ball diameter 7.2 cm, pivot at 1.457 m. Pixel rms is 3.6 px; the residual is
  mostly a slow drift of the swing plane.
- Depth_info residuals are within 5 cm. At frame 14 the model gives 1.393 m against the given 1.344 m.
- With g free the fit gives g = 9.41, which is close to 9.8 and so supports the metric scale.

**Acceleration at frame 14.**

| Reading / model | Value (m/s²) |
|---|---|
| Physical \|a\| (vector), g fixed | 6.07 |
| Physical \|a\| (vector), g free | 5.95 |
| Planar model \|a\| | 5.92 |
| Reference style on model frames, forward A[14] / centred A[13] | 5.94 / 5.38 |
| Depths rescaled so the swing matches the depth_info amplitude (×1.13–1.16) | 6.2–6.7 |
| Tangential reading, d\|v\|/dt | −5.4 to −5.6 (deceleration) |

The reference-style computation uses forward-difference velocity, 5-frame smoothing and a second difference.

**Answer.** Taking the vector magnitude of the second difference of the 3D centre gives about **6.1 m/s²**.
If the change of scalar speed is meant instead, the value would be about 5.5.

**Confidence.** Moderate. Routes based on the model agree within about ±10%. The route based on diameters
alone is too noisy to serve as an independent check.
