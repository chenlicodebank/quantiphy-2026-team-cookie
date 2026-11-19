# q_2631 – basketball velocity at t=0.6 s (cm/s)

- t=0.6 s at 24 fps (question_fps = file fps) -> frame 14. The basketball is free and rolling (clear of the foot from frame 12, collision at frame 19), so frames 12–18 are a clean window.
- Camera: f = 0.5959*1280 = 762.8 px, principal point (640,360).
- Track: scene/tracks/basketball.csv circle centres. I re-measured them independently (refit.py: orange HSV mask + enclosing circle) and the centres agree within about 1 px. The crop of frame 14 confirms the fit.
- Depth: depth_info gives Z = 2.27 m at frame 14. The depth at the other frames is Z_i = 2.27 * d14/d_i, using a linear fit of the circle diameter over frames 12–18. The diameter shrinks by about 1.05 px per frame (74.1 px at frame 14), so the ball is moving away from the camera at about 0.77 m/s. The mask-area diameter shows the same slope (77.6 -> 70.9 px over frames 12–18).
- The 3D centres are back-projected from these depths, and the speed is the forward difference times 24 (vel.py):
  - per-frame forward-difference speeds over frames 12–17: 139, 140, 144, 139, 143, 147 cm/s;
  - 5-frame smoothed window 12–17: 141.1; window 13–18: 142.6; window 12–18: 142.0; the single forward difference at frame 14 is 144.2.
- Second route: with the depth held constant (lateral motion only) the speed is 130–135 cm/s. This is too low because it ignores the clear shrinking of the ball's image (the ball is moving away). For comparison, depth from the ball's size alone (f*0.232/74.1) gives 2.39 m, 5% more than the given 2.27 m. I anchored the depth to the given value.
- Note: the jump at frames 11->12 (a dropped capture frame, per the record) is kept out of the window.
- Answer: about 142 cm/s. Confidence: moderate-high (±5%). The main uncertainty is how much of the motion is along the depth axis.
