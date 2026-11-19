# q_1523 - acceleration of the yellow car at t = 0.5 s (frame 12 at 24 fps)

Answer: **10.35 m/s^2**

## Data
- Prior: tyre diameter 0.764 m. depth_info: frame 0, camera to the right-front tyre (hub) = 14.244 m.
- question_fps = file fps = 24. t = 0.5 s -> frame 12. Convention: a = (speed(12) - speed(11)) x 24 = (s12 - 2 s11 + s10) x 576.

## Measurements (scripts in this folder)
- `rims.py`: segments the white rim of the front-right wheel (image left, frames 0-32) and the rear-right wheel
  (frames 20-37), and fits an ellipse to each (centre u, v and the vertical extent).
- `edges.py`: sub-pixel top and bottom rim edges, taken as half-level crossings on a vertical profile through the
  hub. Also measures the tyre bottom. Tyre/rim radius ratio is about 1.51 in bright frames (12-16, and a visual
  check of frame 30). The dark frames 0-9 read about 1.62 because the floor under the car is in shadow there.
- Hubs sit at v ≈ 829-830, which is the horizon (y 829 from the ceiling-tube vanishing point). So the hubs are at
  camera height, the camera pitch is atan(289/f) and the hubs move in the camera's horizontal plane.
- `traj.py`: 3D hub positions from rim height (depth) and u (lateral). The front-hub and rear-hub tracks lie on
  **one straight line**: perpendicular residuals are a few cm and both lines have the same offset (4.10 / 4.11 m).
  The rear wheel passes the front wheel's earlier positions. So the car translates along a straight line with no
  yaw, the origin moves exactly like a hub, and the change in apparent yaw is only viewing angle. The line runs
  about 92° to the ceiling tubes (it is the parking-lane direction).
- Route 1 (rim-height depth): positions are noisy (about ±4 cm), and the dark early frames read the rim about
  2.5 % too small.
- Route 2 (`sfromu.py`, `calib.py`): the line is fitted from bright frames (≥12). The position along it comes from
  the precise hub image x by intersecting each ray with the line. Calibration:
  - K (rim depth scale) = 0.764 f / (ratio cos²φ).
  - f is solved so that the frame-0 front-right hub lies 14.244 m from the camera. This gives f ≈ 2279 px
    (HFOV ≈ 46°).
  - The implied frame-0 rim height is 88.2 px. The measured value is 86.0 px, which confirms the dark-frame bias.
- Motion: speed rises from 0 at frame 0 to a peak of about 10.1 m/s near frame 28, then falls. This is Blender's
  default Bézier ease (smoothstep), s = s0 + D(3τ² - 2τ³). Fit: i0 = -0.07, T = 57.4 frames, D = 16.08 m. Fit RMS is
  5 mm over 50 points (front frames 0-32 plus rear frames 20-37).

## Results for a(12)
| method | a(12) m/s^2 |
|---|---|
| smoothstep fit, ratio 1.51 (f 2279) | 10.38 |
| cubic polynomial over frames 6-18, same positions | 10.32 |
| ratio 1.45 / 1.57 (f 2170 / 2386) | 10.51 / 10.26 |
| line from all frames (`fit.py`, u-route) | 10.33-10.40; degree-3/4 polynomials 10.45 / 10.20 |
| rim-depth route (noisy, dark-frame bias) | 9.1-9.7 |

- Sensitivity: the result scales roughly with the frame-0 distance anchor (±5 % f gives ±3 %).
- Second-route check: the independent rim-depth route agrees within about 7 %, and its bias is explained.
- Confidence: about ±4 %.
