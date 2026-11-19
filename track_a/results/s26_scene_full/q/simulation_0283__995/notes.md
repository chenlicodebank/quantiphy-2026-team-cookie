# Q995: speed of the dragon at t = 1.0 s (prior: dragon length = 0.75 m)

The video is 24 fps, and question_fps is also 24, so t = 1.0 s is frame 24. The camera is static. This is a 2D scene: the dragon's size shows no trend that would mean a change in depth. I used one metres-per-pixel scale.

## Scale
- Frames 21-24 give a clean side view, with the wings folded up and nowhere beyond the nose or tail.
- In those frames the mask's horizontal extent, from snout to tail tip, is 528, 518, 520 and 517 px (scene record, checked on zoomed crops `frames/f23.png`, `frames/f24.png` and `frames/s20.png`).
- In frame 24 the straight snout-to-tail-tip distance is about 515 px.
- I take L = 520 px, so the scale is 0.75 / 520 = 1.442e-3 m/px.

## Speed
The silhouette centroid in the scene record is unusable here. The wingbeat moves it by about 60-70 px per frame near frame 24, while the body moves only about 36 px per frame. So I tracked rigid body points instead, by NCC template matching (`tmatch.py`).
- **Frame 23 to 24, forward (frame-24 templates):**
  - head: (-35.9, +2.1)
  - torso: (-33.2, +9.4)
  - leg: (-35.0, -4.4)
  - tail tip: (-36.0, -8.8)
- **Frame 23 to 24, reverse (frame-23 templates):**
  - head: 35.7
  - torso: 36.2
  - leg: 35.0
  - tail tip: 37.0 px
- **Mean step:** about 35.8 px per frame.

## Checks
- The frame 24 to 25 steps are similar: about 35-36 px.
- The average horizontal pixel speed over the whole flight, from frame 2 to frame 49, is 34.8 px per frame.

## Result
Speed = 35.8 × 24 × 1.442e-3 = **1.24 m/s**.

## Confidence
Moderate. The main uncertainty is what "length" means: the in-flight nose-to-tail span, or a rest-pose bounding box with a straight tail. If the reference used a longer length, for example 570-600 px, the answer would be about 1.07-1.13 m/s.
