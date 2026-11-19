# q_2200: ball velocity at 0.6 s (m/s)

The file and question_fps are both 24, so t = 0.6 s is frame 14. That is 3 frames before the near turning point (f17), so the ball is slowing down quickly.
Prior: g = 9.8 m/s². depth_info gives distances at frames 7, 14, 22, 29, 36 and 43.

## Method
- The track in scene/tracks/ball.csv (red-mask centroid and equivalent diameter) was checked on a zoomed frame 14, and the mask is good.
  The pivot is the string top at about (638.5, 228) px, from string.csv for frames 9–28 and 38–48.
- Depth from ball size alone (`measure.py`, d = k/diam) is too noisy for frame-to-frame differences
  (the diameter jitters by about 1 px). It gave anywhere from 0.65 to 1.4 m/s depending on the smoothing, so I did not use it directly.
- `pendfit.py` fits a 3D damped pendulum (exact elliptic-function solution, g = 9.8) projected through the pinhole camera
  (f = 763 px, cx/cy = 640/360) to the u, v and diameter of every frame. The free parameters are L, amplitude, turning time, damping, pivot depth,
  world-up direction, swing azimuth and ball diameter. With the pivot fixed at (638.5, 228) and frames 3–32 (one period around f14),
  the rms residuals are 1.0 / 1.1 / 0.9 px. The fit gives L = 0.331 m, amplitude 46°, camera pitched about 25° down and ball D = 0.070 m.
- Scale route 1 (g through the period): the model depths at the depth_info frames are 1.79, 1.47, 1.52, 1.82, 1.79 and 1.47 m,
  against the given 1.71, 1.34, 1.46, 1.78, 1.72 and 1.35 m. The two routes agree to within 5 % (factor 0.948).
- Scale route 2 (depth_info) multiplies the model by 0.948.

## Speed at frame 14 (`conventions.py`)
| convention | g scale | depth_info scale |
|---|---|---|
| instantaneous | 0.926 | 0.878 |
| forward diff f14→15 | 0.805 | 0.763 |
| 5-frame moving average, then forward diff | 0.765 | 0.725 |
| 5-frame MA, central | 0.868 | 0.823 |

Back-projecting the measured u, v with the model depth gives the same numbers as the model positions to within 0.01.
The paper uses a forward difference smoothed over at least 5 frames, which favours about 0.73–0.80. The instantaneous value is about 0.88–0.93.
**Answer: 0.78 m/s.** This is a compromise between the reference convention and the instantaneous value.

## Confidence
Medium. The geometry is solid: the two scales agree to within 5 % and the fit residuals are about 1 px. The main uncertainty is the
smoothing convention, because the speed changes quickly near the turning point and the candidate values span 0.73–0.93.
The fit also has a full-video variant with larger residuals (3 px in u), which shows a small amount of damping.
