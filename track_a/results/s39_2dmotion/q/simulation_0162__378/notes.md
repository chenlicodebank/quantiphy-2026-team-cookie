# q378: acceleration of the ball at t = 1 s (m/s^2)

The prior is a ball diameter of 0.21 m. This is a 2D simulation, so a single m/px scale comes from the ball's diameter.
question_fps is 24 and the file fps is 24, so t = 1 s is frame 24. The camera is static, as the scene record says.
Acceleration at frame 24 = (speed(24) - speed(23)) x fps, which is about x''(23) of the origin track.

## Track
- `measure.py`: my own background-difference tracker (median of left/right edge midpoints in the rows above the shadow).
  Its cx matches scene/tracks/ball.csv within about 0.5 px over frames 18-60, and the SAM centroids at frames 24, 36, 48 and 60
  agree within about 1 px (`samfit.py`).
- The residuals from any smooth fit show a sinusoid of about ±1.1 px whose period in *travelled distance* is about 249-255 px. That equals
  pi x D, so it is a texture bias that follows the ball's rolling rotation. It is not real motion. Because of it, plain local quadratics
  in a window around frame 24 scatter from 0.34 to 0.49 px/frame^2 (`accel.py`, `models.py`).
- `models2.py` fits a smooth motion model plus a bias that is periodic in x (1-2 harmonics, period free):
  - exp model (v -> v_max with tau ≈ 30 frames), frames 19-92: rms 0.15 px, a(24) = 0.468 px/frame^2
  - poly5 and poly6 over the same frames: 0.470 and 0.463. Over frames 13-92: exp 0.476, poly 0.485-0.488. Over frames 19-60: 0.456-0.474.
  - **Adopted: 0.47 ± 0.01 px/frame^2 = 270.7 px/s^2.**

## Scale: ball diameter in px
| Source | Diameter (px) |
|---|---|
| scene circle fit, frames 40-80 | 80.2-81.8; its headline value is 81.5 |
| SAM masks, frames 36/48/60: area-equivalent | 80.6 / 80.2 / 79.4 |
| SAM masks, frames 36/48/60: contour circle fit (+1 px for the pixel-centre offset) | 80.7 / 80.3 / 79.6 |
| SAM boxes | 79.8-81.5 |
| own sub-pixel top edge (607.5) with cy 647.4 | about 79.8 |
| rolling period pi x D, from the bias fit | P = 248-255, so D ≈ 79-81 |

- At frame 24 the SAM box (84.7 x 79.4) and the scene fit (83.9) are widened horizontally by motion blur and the shadow, so I did not
  use them. The vertical extent there (79.4) agrees with the other estimates.
- My first threshold-40 vertical extent (83-84) includes the antialiased rim and shadow, so it is too large.
- Adopted D = 80.6 px (±1). The scene's 81.5 is 1.1 % larger, within the 3 % tolerance.
- Scale = 0.21 / 80.6 = 2.605e-3 m/px.

## Answer
a = 270.7 px/s^2 x 2.605e-3 m/px = **0.705 m/s^2**

## Second route
- The scale from the rolling period alone (D = P/pi ≈ 79.4 px) gives 0.716 m/s^2.
- The model-fit spread of a(24), 0.456-0.488 px/frame^2, gives 0.68-0.73 m/s^2.

Confidence: good, about ±4 %.
