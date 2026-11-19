# q_626 — width of the wooden bench (m)

Prior: black cat speed = 0.94 m/s. No depth_info. fps = question_fps = 24, so no re-timing.
Scene: a top-down 2D render with a static camera. I used one m/px scale for the floor plane.

## Scale (measure.py)
- Black cat mask: max(BGR) < 60, largest component, frames 0–49.
- Linear fits of x against frame number, in px/frame:

  | point | slope |
  |---|---|
  | front edge | 10.99 |
  | body back edge | 10.95 |
  | body centroid | 10.97 |
  | full centroid | 10.94 |

- The first and second halves of the clip agree within about 1%, so the speed is constant.
- Pixel speed: 10.97 × 24 = 263.3 px/s, which gives 0.94 / 263.3 = 0.003570 m/px.

## Bench (bench_profile.py and measure.py)
- The bench is the orange slatted bench at the top left. It spans x 294–583 (290 px) and y about 173–288.
- Width is the shorter horizontal extent, front to back, which is the y extent in the image.
- Half-maximum saturation edges in clean columns (no sun patch) give 113.7–114.2 px. Frames 0, 24 and 49 agree.
- The colour-mask column counts give 116 px.
- I used 115 ± 1 px.

## Answer
- Width = 115 × 0.003570 = 0.41 m. The range 114–116.5 px gives 0.407–0.416 m.
- Check: bench length = 290 px = 1.04 m, and cat body = 148 px = 0.53 m. Both are plausible.

## Caveat
The seat top sits higher than the floor where the cat walks. With an unknown perspective camera it could look a few
percent larger. The 2D one-scale convention ignores this.

Confidence: fairly high, within about 5%.
