# Q3035: average speed of the top (giver) hand, 1.4 s to 2.2 s

## Scale
- Prior: the bill's width (short edge) is 66.3 mm.
- The short edge measures 610.9 px at frame 0 (corners read by eye, recorded in scene/), 611.3 px at frame 35 and
  607.4 px at frame 44.
- I checked the corners on a frame-44 overlay (frames/bill44_LB.png): the L corner sits within a few px of the true
  corner, and B is under the thumb, so it is extrapolated.
- I used 610 px, which gives 0.1087 mm/px. Single planar scale, as in the annotator convention.

## Time base
- The file runs at 24.0625 fps; question_fps is 25. The clip is 69 frames long.
- At 25 fps, t = 2.2 s is frame 55, the last frame where the top hand is visible: it leaves through the top-right
  corner. That coincidence suggests the question was written on 25 fps footage.
- The withdrawal speed cannot tell the two rates apart physically.
- I used 25 fps: t = 1.4 s is frame 35 and t = 2.2 s is frame 55.

## Measurement (measure_hand.py, speed.py)
- Skin mask: LAB a* > 131.5. The top hand is the component touching the top border.
- Reference point: the fingertip, taken as the mean of the 0.5% of mask pixels furthest along the direction opposite
  to the retreat, (-0.627, 0.779). I checked it on overlays (frames/tip_*.png).
- A second reference point, the lowest skin pixels, gives the same results.
- The hand is still until about frame 38. From there it moves up and to the right, accelerating to about 270 px per
  frame, and leaves the frame after frame 55.

| Frames (fps) | Straight-line displacement | Path length | Speed from displacement | Speed from path length |
|---|---|---|---|---|
| 35→55 (25) | 2012 px | 2150 px | 0.273 m/s | 0.292 m/s |
| 35→54 (25) | 1745 px | 1881 px | 0.250 m/s | 0.269 m/s |
| 34→53 (24.06) | 1482 px | 1617 px | 0.204 m/s | 0.223 m/s |

- The path length includes some finger jitter during the hand-over (frames 35-45).

## Answer
- About 0.28 m/s: between the displacement and path-length values for frames 35→55.
- If the file rate (24.06 fps) were the right time base, the answer would be about 0.21 m/s.
- Confidence: moderate. The main uncertainty is the time base and frame window, because the hand accelerates
  strongly at the end of the interval.
