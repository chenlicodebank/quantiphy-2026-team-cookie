# Q869: tennis ball acceleration at t = 1.5 s (frame 36). Answer: 6.05 m/s^2

Time base: the file and the question are both 24 fps, so t = 1.5 s is frame 36. At that frame the ball
is mid-way down the straight ramp (it is on the ramp for frames 19-47).
Scale prior: ball diameter = 0.17 m.

## Tracking (`measure.py` -> `mytrack.csv`)
- The ball centre is the HSV colour-mask centroid. It agrees with scene/tracks/ball.csv to about 0.1 px.
- A second track uses the difference from the background (frame 0). It includes the shadow, so it is used only as a check.

## Key finding: perspective (the scene is 3D, not a flat 2D plane)
- The per-frame pixel acceleration falls steadily along the ramp, from about 1.4 to about 1.0 px/frame^2.
- Three independent cues show that the ball recedes from the camera by about 7% in depth over the ramp:
  - The ball's pixel diameter shrinks from 25.2 to 23.65 px (frames 20 to 47), a depth ratio of 1.067 (`diam.py`, saturation 0.3-level).
  - The dark ramp-top strip narrows by 7% from x = 300 to x = 1300, a ratio of 1.074 (from the scene record's edge lines).
  - The projective fit described below.
- Projective fit (`projfit.py`, `projfit2.py`):
  - The image position along the path is modelled as P0 + s/(1 + C s), with s = v0 t + a t^2/2. This is constant world acceleration seen in perspective.
  - It fits to 0.21 px rms. A plain quadratic (no perspective) leaves 1.75 px rms.
  - Best fit: C = 5.3-5.4e-5 per px, which implies a depth ratio of 1.07-1.08 over the path. This matches the diameter and strip cues.
  - a36 = 1.50 px/frame^2 in frame-36-local pixels. Across fit windows 19-47, 22-47, 19-44 and 24-46 it ranges 1.490-1.505.
- So the ball accelerates uniformly. The apparent slowing is perspective, because image steps along a receding line scale as 1/Z^2.

## Pixel diameter at frame 36
| Method | D36 (px) |
|---|---|
| Luma edge radii (`radial2.py`), opposite-angle pairs, frames 22-47 rescaled to f36 with the depth model; contact/shadow side excluded | ~24.5 |
| Saturation 0.3-level equivalent diameter, linear-trend value at f36 | 24.3 |
| Colour-mask equivalent diameter | 23.9 |
| Visual read on a 16x crop | ~24.0-24.3 |

Adopted: D36 = 24.4 px, so the scale is 0.17 / 24.4 = 0.00697 m/px near frame 36.

## Result
- a = 1.50 px/frame^2 x 576 x 0.00697 m/px = 6.02 m/s^2.
- Path-obliquity factor:
  - The path's depth component is cot(phi) = f x C, which is about 0.1-0.2 for typical focal lengths.
  - So the path is slightly foreshortened, and 1/sin(phi) is about 1.005-1.02.
- Final answer: about **6.05 m/s^2**.

## Second route (`route2.py`)
- The depth ratio is taken from the measured diameter trend alone (not from the fitted C).
- Each step is rescaled by (Z/Z36)^2, and a line is then fitted to the per-frame speeds:
  - saturation-diameter trend: 1.45 px/frame^2
  - luma-diameter trend: 1.55 px/frame^2
- These bracket the projective fit's 1.50. Converted with the same scale, they give 5.8-6.2 m/s^2.
- Without the perspective correction, a single-scale 2D reading would give about 4.8-4.9 m/s^2. I reject that: a constant-acceleration model then does not fit the track, and three cues show the receding depth.

## Confidence
- The pixel acceleration is good to about ±3% and the diameter to about ±2%. The obliquity factor adds about 1%.
- Expected error is about 4-5%.
