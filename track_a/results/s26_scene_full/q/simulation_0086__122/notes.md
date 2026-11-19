# Q122: speed of the car at 1.5 s (prior: car acceleration = 4.03 m/s^2)

The video is a 2D top-down render at 24 fps. question_fps is also 24, so there is no re-timing. t = 1.5 s is frame 36.

## Method
- I tracked the car's front bumper edge to sub-pixel precision in `measure_front.py`. The script takes the difference from the empty frame 71 and finds where the column-summed difference profile crosses half its level, for frames 0–56. The front edge stays sharp, while the rear is smeared by motion blur.
- The car is at rest in frames 0–1. From there the per-frame step grows linearly, which means constant acceleration.
- The scale comes from the prior. Speed in m/s = step_px(36) / a_px × 4.03 / 24. Here a_px is in px/frame² and step_px is the backward difference at frame 36.

## Measurements
- Quadratic fits of position:
  - Over the windows 4–55, 10–50, 20–52 and 26–46, a_px = 0.546–0.557 px/frame².
  - The fitted step at frame 36 is 18.89–18.97 px.
  - This gives v = 5.71–5.83 m/s.
- Second route, linear fits of the per-frame steps in `check_steps.py`:
  - a_px = 0.551–0.565, with the zero-speed point near frame 1.3–2.2.
  - This gives v = 5.67–5.82 m/s.
- Physical model: the car accelerates from rest starting at frame 1. The backward difference at frame 36 is then a × (35.5 − 1) / 24 = 4.03 × 34.5 / 24 = 5.79 m/s.

## Answer
5.79 m/s. Confidence is high, about ±2%.

For comparison, the naive a × t = 6.05 m/s would ignore the 1-frame rest at the start and the backward-difference convention.
