# q_664: acceleration of the vacuum cleaner at t = 2 s

**Question:** what is the acceleration at t = 2 s? **Prior:** the vacuum diameter is 0.438 m. There is no depth_info.

**Video:** a 2D top-down Blender render with a static camera. The fps and question_fps are both 24, so t = 2 s is frame 48.
The convention is acc = (speed(48) - speed(47)) x fps, where speed is the one-frame backward difference of the centre.

## Tracking (two independent routes plus the scene record)
- The scene record (`scene/tracks/robot_vacuum.csv`) fits a circle to the outer rim of the disc.
- `track_mine.py` subtracts the background (frame 0, when the vacuum is far right) and masks bright, low-saturation pixels,
  which excludes the vacuum's shadow. It then gives (a) a least-squares circle fit to the contour and (b) the mask centroid.
  Overlay: `frames/ov48.png`. At frame 48 the vacuum crosses the sun/shadow boundary, and the fit is still clean.
- All three tracks agree to within about 0.3 px. Raw single differences at frame 48 are 0.38 to 0.46 px/frame^2, but the
  noise on a second difference is about ±0.17 px/frame^2.
  The neighbouring raw values are 0.95 (f46), 0.69 (f47), 0.43 (f48), 0.55 (f49) and 0.42 (f50).

## Smooth model (`segfit.py`, `segfit2.py`)
- Frame 39 is a keyframe-like kink: the speed minimum, where the speed derivative jumps. The segment from 39 to 69 is
  one smooth curve. y(f) is a cubic (rms 0.07 px). x(f) needs degree 5, which gives an rms of 0.05-0.10 px. That is the
  noise level, so the model is adequate.
- Fits of degree 5 and 6 over the windows 39-69, 40-68, 41-66, 41-62 and 42-58, on all three tracks, give a speed at
  frame 48 of 22.19-22.24 px/frame. They give acc48 = speed(48) - speed(47) = 0.561-0.593 px/frame^2, median about 0.578.
  Local cubic and quartic fits over 43-53 and 44-52 (`acc_fit.py`) give 0.54-0.59, which agrees.

## Scale
- `diam.py` uses radial gradient edges. The diameter is 120.0-121.0 px at frame 48, and the record gives 120.6. The disc
  is near the image centre here, so perspective has little effect. I used 120.5 px.
  Scale = 0.438 / 120.5 = 0.003635 m/px.

## Answer
acc = 0.578 px/frame^2 x 24^2 x 0.003635 m/px = **1.21 m/s^2** (the speed is increasing towards a peak at about frame 50).
The range across methods is 1.17-1.24. Using the raw single difference without smoothing would give about 0.91, but that
value lies within the noise and is not used.
Confidence: moderate-high, about ±5%.
