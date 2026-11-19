# q_665 — length of the wooden bench (m)

Prior: robot vacuum diameter = 0.438 m. No depth_info. fps = question_fps = 24, so no re-timing issue.
The camera looks straight down at the room, so I treat the scene as 2D with one scale taken from the vacuum.

## Measurements (frame 77, static scene)
- Vacuum diameter: robust circle fit from scene/tracks = 117.8 px (median over frames; range 117.3–118.3; bbox 119).
  This value is consistent across the whole path.
- Bench (orange slatted bench, top-left) in `measure_bench.py`, which thresholds on orange colour (r−b):
  - mask bbox x 294–583 → 289 px
  - half-max edges of the mean column profile 295.0–581.6 → 286.6 px
  - I used 288 ± 1.5 px. The bench width is 116 px, so the long axis is x.
- Uncorrected 2D scale: 0.438 / 117.8 = 3.718e-3 m/px → bench length = 1.071 m.

## Perspective check
The bench top sits higher than the vacuum's rim, so it is closer to the camera and looks slightly larger. I found
these cues in zoomed crops (`zoom.py`, frames/z_*.png):
- No side face of the bench shows at its right end, which faces the image centre.
- Small dark pieces under the bench, probably legs or rails, stick out only about 3 px past the slat ends.
- Both cues mean the camera is high compared with the bench height, so the magnification is small, roughly 1–4 %.
- On the other hand, the walls are visible up to at least 0.23 × the camera height. That limits how high the camera
  can be if the walls have a normal height.

I applied a correction of about 2 %: 1.071 / 1.02 ≈ 1.05 m.

## Second route
Comparing the bench's half-max length with the vacuum's bbox diameter gives 0.438 × 286.6 / 119 = 1.055 m. That
agrees with 1.05–1.07.

## Answer
1.05 m. I'm fairly confident it is within ±4 %. The main uncertainty is the perspective correction (0–4 %).
