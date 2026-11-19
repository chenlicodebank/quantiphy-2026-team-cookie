# q_764 – speed of the basketball at t = 0.5 s

- 2D simulation, static camera, fps = question_fps = 24, so t = 0.5 s is frame 12.
- I re-measured from scratch in `measure.py`: HSV mask, then a least-squares circle fit to the contour for frames 0-23. The overlay `frames/f12_overlay.png` shows that the fit follows the ball edge.
- Scale: the diameter is 74.8 px from the circle fit and 75.8 px from the mask area. 75 px is between them and matches the record. That gives 0.282 / 75 = 0.003760 m/px.
- Backward difference: y12 − y11 = 806.77 − 795.97 = 10.80 px/frame. x does not change. Speed = 10.80 × 24 × 0.00376 = 0.975 m/s.
- Second route: a parabola fit to the descent (frames 0-22) gives 10.86 px/frame, or 0.980 m/s. Using the other diameter estimates gives 0.965-0.982 m/s.
- The fitted acceleration is about 2.05 m/s² in the prior's scale, so the scene is not at real-world scale. That is expected, because the prior sets the scale.
- Answer: **0.975 m/s**. I'm confident it is within about 2 %.
