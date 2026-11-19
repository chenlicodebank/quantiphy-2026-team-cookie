# q 2875 – white ball velocity at 1.5 s (frame 36), captured_0054b

The file and the question both use 24 fps, so t = 1.5 s is frame 36. Camera: f = 0.5959 x 1280 = 762.8 px, c = (640, 360).

## Objects
- In the depth_info, "orange ball" = basketball, "green ball" = the yellow-green tennis ball, and "white ball" = the
  small off-white ball. At frame 24 the white ball is about 30-40 px across (blurred) at 1.235 m. That makes it about
  5.5-6 cm, which fits a small ball flying close to the camera.
- The white ball is thrown, flies ballistically, bounces at frame 38 and is seen until frame 47. Frame 36 is two frames
  before the bounce, while the ball is falling and moving away from the camera.

## Measurements (scripts in this folder)
- `measure.py`: my own mask per frame (difference from the background x a low-saturation colour rule). It gives the
  centre and the minor-axis diameter (4·σ_minor, which is not affected by blur). Masks were checked on
  frames/white_masks.png, and the centres agree with scene/tracks within about 1-2 px.
- One camera capture was skipped between frames 35 and 36: the step there is about 2x the normal one. A ballistic
  fit with the skip (frame >= 36 gets +1/24 s) has an RMS of 1.1-3.2 px; without the skip it is 6.5 px. The skip is
  confirmed.
- `ballistic.py`, `ballistic2.py`, `answer_calc.py`: 3D fit p(t) = p0 + v0·t + ½·g·t² with |g| = 9.81 and
  |p(frame 24)| = 1.235 m (the depth_info value), fitted to the pixel centres (plus a soft constraint from the size).
  - The gravity direction is either free or fixed from the vanishing point of the vertical wall/door edges
    (`vp.py`: VP at (476, 1515)).
  - Every variant gives a distance at frame 36 of 2.37-2.56 m and a distance at frame 38 of 2.76-2.93 m.
  - Independent size check: the fitted ball diameter is 5.5-6.0 cm. The basketball, scaled by its given 2.24 m at
    0.5 s, puts the floor bounce point at about 2.65-2.7 m.
- Physical (instantaneous) speed at frame 36 is 4.74-4.84 m/s, with a large depth component of about 4 m/s.

## Convention check on the prior (`prior_check.py`)
- The basketball's speed at frame 12 has a one-frame forward difference of only about 1.7 m/s, but the prior says
  2.21 m/s.
- The prior is reproduced only when the smoothing window includes the doubled 11→12 step:
  - 5-frame mean of the forward differences: 2.10-2.18;
  - (P14 - P10)/4: 2.18-2.26;
  - forward difference of 5-frame-smoothed positions: 2.09-2.15.
- Frame 36 has the same layout: the doubled step is 35→36, just before the asked frame.

## White ball at frame 36, by convention
| Convention | Speed (m/s) |
|---|---|
| Physical | 4.8 |
| Forward difference 36→37 | 5.0 |
| Forward difference of position-smoothed track | 5.1 |
| 5-frame mean of forward differences (34-38) | 5.5-5.6 |
| (P38 - P34)/4 | 5.7-5.8 |

**Answer: 5.6 m/s.** This is the reading that matches how the prior was evidently computed (smoothing that includes
the skipped capture). Confidence is moderate: the depth at frame 36 comes from the ballistic fit and the size, not
from a given value, and the convention leaves an uncertainty of about ±10 % (4.8 is the physical value if the reference
had no skip artefact).
