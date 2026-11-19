# Q863: speed of the tennis ball at t = 0.5 s (frame 12)

The file's fps and question_fps are both 24, so frame 12 is t = 0.5 s. Prior: ball diameter = 0.17 m. No depth_info.

## The difficulty
The ball is **not visible** at frame 12. It enters at the top edge at frame 18, which is cut off; it is fully visible
from frame 19. The speed at frame 12 has to be extrapolated from the ramp motion (frames 19-47).

## Measurements (scripts in this folder)
- `measure.py`, `diam.py`, `diam2.py`: ball pixel diameter.
  - Scene HSV-mask equivalent diameter is 23.3-24.8 px.
  - Saturation full width at half maximum is about 22 px.
  - Radial half-max of the difference from the empty frame 5 gives about 24-24.6 px.
  - Equivalent diameter shrinks along the ramp, from about 24.8 px (f19) to 23.1 px (f47). This suggests mild perspective: the ball moves slightly away from the camera.
  - Values used: 23.5 px as the overall value, and about 24.7 px near the top of the ramp.
- `speed.py`, `model.py`: path coordinate along the fitted ramp line from the scene centroids (±0.5 px). I checked these against my own difference-mask centroids.
  - The per-frame pixel step does **not** grow at a constant rate. The step growth falls from about 1.55 px/f² (f20-27) to about 1.0 px/f² (f40-47).
  - A constant-acceleration (quadratic) fit leaves a 1.75 px rms residual, which is poor.
  - A damped model, s = c0 + c1·i + c2·e^(−k·i), fits with 0.22 px rms (k = 0.0185 per frame). Its zero-speed point is at frame ≈ 1.6-1.9, which fits a ball released from rest when the simulation starts. This is a good sign that the model is right.
- Backward-difference step at frame 12 (|p12 − p11|):

| Model | Step at f12 (px/frame) |
|---|---|
| Damped model | 19.2 |
| Cubic fit (independent check) | 19.9 |
| Damped model, perspective-corrected (steps in units of the local ball diameter) | 18.1 at 23.5 px/diameter |
| Quadratic fit (rejected because of its poor fit) | 25.0 |

## Converting to m/s
v = step × 24 × 0.17 / D_px.

| Case | Speed (m/s) |
|---|---|
| D = 23.5 px, damped model | 3.34 |
| D = 23.5 px, cubic fit | 3.45 |
| Perspective-corrected | 3.14 |
| Local diameter about 24.7-25.3 px | 3.10-3.19 |

**Answer: 3.2 m/s.**

## Confidence
Moderate. The main uncertainties are:
- The 8-frame extrapolation, about ±5%. The damped and cubic fits agree within 3%.
- The pixel scale, about ±5%.
