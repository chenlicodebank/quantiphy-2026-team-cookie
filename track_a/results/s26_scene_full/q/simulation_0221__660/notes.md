# q_660: acceleration of the vacuum cleaner at t = 0.5 s

- The video is a 2D top-down render at 24 fps. question_fps is also 24, so t = 0.5 s is frame 12.
- Scale comes from the prior: vacuum diameter 0.438 m = 122.8 px (circle-fit diameter near frames 10-14 in scene/tracks). That gives 0.003567 m/px.
- Per-frame speeds (step lengths, in px/frame) around frame 12, in two ways:
  1. The scene record's circle-fit centres.
  2. An independent template-matching track (`measure.py`, template taken from frame 12, sub-pixel peak).
  Both give steps rising linearly at about 1.0 px/frame per frame through frames 4-20 (for example 11.28 -> 12.29/12.46 -> 13.26/13.10).
- The raw one-frame difference at frame 12 is noisy: 1.00 (template) or 1.18 (circle fit). Local linear and quadratic fits over windows 6-18, 8-16 and 4-20 give a slope between 0.99 and 1.05. Adopted value: 1.01 px/frame^2.
- a = 1.01 x 24^2 x 0.003567 ≈ 2.08 m/s^2.
- Confidence: good (about ±4%). The two tracks agree, and the speed is changing smoothly at this point.
