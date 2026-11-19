# q_2202: acceleration of the ball at 0.6 s (lab clip captured_0010s)

The question fps and the file fps are both 24, so t = 0.6 s is frame 14. That is 3 frames before the near turning point of the swing (f17).

## Object and record
The ball is a red pendulum bob on a string with its pivot near pixel (637, 229). It swings mostly along the line of sight, with depth running from about 1.37 to 1.86 m.
I checked scene/tracks/ball.csv against the depth_info. With the equivalent diameter from the mask, depth × diameter is 47.5–54 px·m at the 6 given times (scatter about ±7 %, which is depth-sensor and mask noise).

## Method
1. Direct route (recon.py, empirical.py): I back-projected each centroid with f = 0.5959·1280 = 763 px and the per-frame depth d = K/diam, with K = 51.3 px·m taken as the median over the depth_info frames. Second differences of these 3D centres are far too noisy, because diameter noise of ±1 px is about ±5 cm in depth. The |a| at f14 came out between 3.4 and 15 m/s² depending on the smoothing, so I did not use this route for the answer.
2. Main route (pendfit_core.py, pendfit_var.py): I fitted a physical spherical-pendulum model with g = 9.8 (the prior) and light damping.
   - Free parameters: pivot pixel and depth, gravity direction (camera tilt), L, initial state, ball diameter and a mask-bias term.
   - Data: u, v and the diameter for every frame, plus the 6 depth_info distances.
   - Result: L ≈ 0.33 m, with a period of about 1.23 s that matches the track. The amplitude is about 45°: |a| at the turning point is about 7.0, which equals g·sinθ0.
   - The image residuals are about 2–3 px. The fitted depths are within about 5 % of depth_info.
   - Model acceleration (vector, tangential plus centripetal) at f14: 6.11 m/s², with speed 0.94 m/s. The second difference of the model positions at f14 gives 6.05.

## Checks (variants of the fit)
| Variant | \|a\| at f14 (m/s²) |
|---|---|
| Mask bias fixed to 0 | 6.14 |
| Depth weight 2 % | 6.06 |
| Depth weight 10 % | 6.24 |
| No damping | 6.08 |
| Frames 5–30 only | 6.09 |
| Frames 8–22 only | 6.42 |

The range is 5.9–6.4, so the answer is 6.1 m/s².

Alternative reading: the rate of change of scalar speed (tangential only) would be about 4.4 m/s². I did not use it because the lab convention is the second difference of the 3D centres, which is the vector magnitude.

Confidence: moderate. The reference was made from noisy per-frame depths, so its value may scatter around the physical value.
