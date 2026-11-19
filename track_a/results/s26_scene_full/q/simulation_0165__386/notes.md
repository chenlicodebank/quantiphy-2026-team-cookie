# q386 – bike wheel diameter (m)

Prior: bike speed 5.52 m/s. 2D video (cyclist rides parallel to image plane at one depth, constant y and size),
fps = question_fps = 24, so one metres-per-pixel scale from the prior speed.

## Speed in pixels
Scene record line fits: rear hub 21.015 px/frame, front hub 21.023 px/frame. Re-measured with my own circle fits
of the dark tyre rings (wheel.py, frames 40-75): rear 21.005, front 21.051 px/frame. Use 21.02 px/frame
= 504.5 px/s (uniform motion, no acceleration). Scale = 5.52 / 504.5 = 0.01094 m/px.

## Wheel size in pixels
- wheel.py: circle fit to dark tyre pixels; tyre centreline radius 31.5 px (median over 22 clean frames, both wheels).
- profile.py: median radial intensity profile (upper half + sides, avoiding ground shadow) over frames 42-63, both
  wheels: tyre dark band between r = 29.3 and 33.0 px (half-max edges) -> outer diameter 66.0 px
  (agrees with scene record ~66 px and grid reading on zoomed frame 60: x 1136-1200, y 674-739 ≈ 64-65 px).

## Answer
Outer tyre diameter = 66.0 px x 0.01094 m/px = 0.722 m. (Tyre centreline diameter 63 px would give 0.69 m;
the bounding-box convention uses the outer extent, so 0.722.)
Check: wheelbase 95.5 px -> 1.04 m, bike+rider height 163 px -> 1.78 m: plausible proportions.
Confidence: good (~3 %), dominated by edge definition of the tyre.
