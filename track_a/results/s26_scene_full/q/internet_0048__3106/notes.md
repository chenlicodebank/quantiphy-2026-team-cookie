# Q3106: ball displacement from 1.20 s to 1.80 s (frames 36 to 54 at 30 fps)

fps = question_fps = 30, and with that rate the scale comes out at a plausible value (below).

## Method (script: fit.py)
- Ball centre track from scene/tracks/ball.csv. Frames 36–60 are clean free flight: after release (35) and before the bounce (61).
  I checked frames 36 and 54 by eye on 2x zoomed crops: the centres sit at about (195, 472) and (1365, 476), which agree with the
  track's (193.3, 471.1) and (1364.8, 475.9).
- Scale from the prior g = 9.8 m/s²: I fitted a parabola to y(t) over the free-flight frames. The pixel acceleration is
  3709–3787 px/s² depending on the window (36–60: 3729; residual RMS 0.3–0.6 px). The mean of the second differences is 3772.
  This gives a scale of 0.00263 m/px (range 0.00259–0.00265).
- Pixel displacement from frame 36 to 54 is sqrt(1171.5² + 4.8²) = 1171.5 px in raw coordinates (1175.5 px camera-compensated).
- Displacement = 1171.5 × 0.002628 = **3.08 m**.

## Checks
- Other fit windows give 3.03–3.12 m. Camera-compensated coordinates give 3.09–3.12 m.
- Sanity check: the ball is 94 px across, which at this scale is 0.247 m, close to a real basketball (0.24 m).
- Horizontal velocity of about 1938 px/s is 5.1 m/s, which is plausible for a throw.

Confidence: high, about ±2 %.
