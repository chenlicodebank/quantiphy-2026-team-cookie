# q_3033: speed of the bottom hand, 0 s to 1.4 s

## Scale
- Prior: the bill is 66.3 mm wide, which is its short edge.
- I checked the frame-0 corners on a zoomed crop (frames/b0.png): L ≈ (412,2028) and B ≈ (822,2478), which gives a
  short edge of 611 px. This matches the scene record.
- Scale = 66.3 / 610.9 = 0.1085 mm/px. I used this one scale throughout (2D, top-down view).

## Motion
- The bottom (receiver) hand enters from the bottom-left corner. At t = 0 only a sliver of fingertip is in view,
  with its leading edge at about (10, 3925).
- It reaches the bill by about frame 25 and then stays still, holding the bill, through frame 35.
- Reference point: the hand's leading fingertip. At the end it sits at about (1298, 1766), the mean of frames 30-35
  in the tip track.
- Displacement = 2514 px = 0.273 m. Speed = 0.273 / 1.4 s = **0.195 m/s**.
- Time base: the hand is at rest from about frame 25, so the end position is the same whether 1.4 s is taken as
  frame 34 (file rate, 24.06 fps) or frame 35 (question rate, 25 fps). The choice of rate does not change the answer.

## Checks
- Path length of the smoothed tip track: 2517 px, giving 0.195 m/s. The motion is nearly straight.
- Starting instead from the frame-1 tip extrapolated back one frame: 2538 px, giving 0.197 m/s.
- I rejected the skin-mask centroid. It is biased by the frame-border truncation and gives 0.10 m/s.

## Confidence
Moderate. The hand is non-rigid and barely visible at t = 0, so the start point is uncertain by about 100 px (about
4%). The answer also assumes "speed" means average speed over the whole 0-1.4 s window. The hand actually finishes
its reach in about 1 s, so it is faster than 0.195 m/s while moving.
