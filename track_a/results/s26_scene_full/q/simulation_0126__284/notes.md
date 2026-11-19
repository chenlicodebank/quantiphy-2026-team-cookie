# q_284: puck speed at t = 2.0 s

- 2D top-down air-hockey render at 24 fps (file rate and question_fps are both 24). t = 2.0 s is frame 48, which comes after the puck bounces off the bottom rail between frames 40 and 41.
- I re-measured the puck in `measure.py` with an HSV orange mask on frames 36-71.
  - Puck diameter: 64.4 px at frame 48. This is the equal-area diameter, and it is 64.0-64.5 px over frames 42-71. The saturation-profile subpixel width gives 64.6 px, and a circle drawn on the frame matches the edge (frames/puck48.png). The scene record gave 63.5 px from minAreaRect, which is about 1.5% low.
  - Scale: 0.074 / 64.4 = 1.149e-3 m/px.
- Motion after the bounce is straight up and uniform. A linear fit over frames 42-71 gives 9.344 px/frame. The single backward-difference step at frame 48 is 9.47 px, and the steps scatter ±0.15 px because of mask noise.
- Speed = 9.344 × 24 × 0.074 / 64.4 = 0.2577 m/s.
- Second route: the raw step at frame 48 gives 0.261 m/s, and the scene record's numbers (9.34 px/frame, 63.5 px) give 0.261 m/s. Both are within 1.5%.
- Answer: 0.258 m/s. Confidence high, about ±2%.
