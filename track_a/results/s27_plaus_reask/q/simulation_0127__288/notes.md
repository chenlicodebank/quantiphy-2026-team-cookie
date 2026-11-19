# q_288: width of the blue car (m)

Prior: the bike's speed is 24 m/s. depth_info: none. Both the file and the question run at 24 fps.
The video is a 2D top-down render with a static camera, so I used one metres-per-pixel scale from the bike's pixel speed.

## Scale
- The cyclist moves at a constant speed to the left. The record gives 31.62 px/frame (ref_x from frame 10 to 50).
- My own NCC template matching (`cyc_speed.py`) over windows of 10, 20 and 40 frames gives 31.66 to 31.87 px/frame.
- I used 31.7 px/frame, which is 760.8 px/s, so the scale is 24 / 760.8 = **0.03155 m/px** (about ±0.4%).

## Car width (pixel extent across the motion, along y)
- **Top edge** (`topedge.py`): I took the background difference against a median of the car-free frames 42–56.
  The top edge is flat at y≈276.5 along the whole car in frames 20, 22 and 24. There is no mirror bump.
- **Bottom edge** (`colprof.py`, `rowprof.py`): I read it in the rear-end columns, where the shadow (which falls
  lower right) does not touch the edge. It is at y≈360–361 in frames 20 and 24. The row-mean luminance step is
  at y 361–364.
- **Width ≈ 84 px (±2).** The scene record said 80 px (277–357), which reads the bottom edge a few px too high.
- **Width = 84 × 0.03155 = 2.65 m.** With the record's 80 px it would be 2.52 m.

## Plausibility
The prior (24 m/s for a bike) is unrealistic, and the scene is scaled about 1.55× uniformly:
- bike length 85 px → 2.7 m
- car length 240 px → 7.6 m
- car width → 2.65 m

All three are about 1.5–1.6× real size, so they agree with each other. Under the stated rule (a prior that is not
realistic allows a scaled scene), I kept the prior's scale.

Confidence: moderate-high. The scale is good to about 1%; the pixel width to about ±3%.
