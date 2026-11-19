# q_1852: rocket acceleration at t = 1 s (frame 24)

The prior is the rocket length, 2.9 m. The video is a 2D side view with a static camera, 24 fps. question_fps is also 24, so there is no re-timing.
t = 1 s is frame 24. By the benchmark convention, a(24) = [s(24) - 2 s(23) + s(22)] x fps².

## Measurements (my own scripts)
- **nose.py:** Each frame is background-subtracted against frame 28, which shows the truck alone. The image is resampled into a strip along the launch axis from the scene record (direction 39.0° above horizontal), at 0.25 px steps. From this I build a soft-mask width profile.
  - Nose tip: the sub-pixel position where the width falls to 3, 5, 8 or 11 px. It is clean on the white background in frames 9-20.
  - Frame 21's nose is an outlier (+6 to +9 px; a stray dot at the tip), so I dropped it. Frame 8's nose (-266) was read from frames/early.png and matches the scene record.
- **tailfeat.py:** Tail end, from the width crossing 4-14 px.
  - The bluish nozzle-glow blob makes the tail longer in frames 21-23 (frame 21 gives L = 231 instead of 220), so I dropped those frames.
  - Clean tail frames: 15-20, 24 and 25.
- **Rocket length:** L = nose(thr5) - tail(thr4) = 218.8-223.3 px over frames 15-20; the joint fits give 220.5. The scene record has 221.9. I used L = 222 px measured along the rocket axis, which gives 2.9/222 = 0.01306 m/px.

## Motion model (resid.py, model.py, unc.py, smooth.py)
- **Constant acceleration is rejected.** A quadratic joint fit (nose and tail with a fitted length offset) gives about 2.07 px/f². Its residuals are systematic, and the F-test for a cubic is 12-55 for every threshold and subset. This holds even with nose frames 8-20 plus tail frames 15-20 only (no late frames), where the cubic gives a(23) = 1.32.
- **Ease-in/out keyframe.** A Blender Bezier ease (smoothstep), fitted freely, puts the start of the motion at frame -1.0 to +1.4, which is the first frame of the clip. This independently supports a keyframed ease-in from rest at frame 0.
  - With the start fixed at frame 0, the fits give a duration T = 74-80 frames.
  - a_def(24) = 1.46, 1.48, 1.46, 1.51, 1.48, 1.58, 1.61, 1.52 px/f² across the variants.
  - Free cubic fits give a(23) = 1.33-1.61.
- **Chosen value:** a = 1.48 px/f² (spread about ±0.1).

## Answer
a = 1.48 px/f² x 576 f²/s² x 0.01306 m/px ≈ **11.2 m/s²**.

## Second-route check
The free cubic polynomial and the smoothstep with its start fixed at frame 0 agree (1.3-1.6 px/f²). The early-only and late-only subsets both show the acceleration falling over time.

## Confidence
Moderate, about ±10%.
- If the reference assumed constant acceleration, the answer would be about 15.6 m/s².
- If the length meant a world-axis-aligned bounding-box extent instead of the length along the rocket's axis, the scale would change by about 20%.
