# Q927 speed of spacecraft at 0.5 s
2D top-down render; the spacecraft (car-like craft) moves straight left along y=718, uniformly accelerating from rest at ~frame 0.
Scale from prior a=4 m/s^2 at 1.0 s.
- scene/ track (template NCC): quadratic fit frames 2-60 gives a=517.8 px/s^2 (rms residual 0.09 px); median per-frame accel 515.5; local fit around f24: 517.
- My own re-track (rear-template NCC from frame 0): quad fit 519.9 px/s^2, local 528.
- Scale = 4/518 = 0.00772 m/px.
- Speed at 0.5 s = frame 12 backward step (11->12): scene 251.3 px/s -> 1.94 m/s; mine 246.8 px/s -> 1.90 m/s.
- Second route: ideal uniform acceleration from rest at t=0: v_back(12)=a*23/48 = 1.917 m/s; quadratic-fit vertex ~frame 0.06.
Answer 1.92 m/s. fps=question_fps=24. Confidence high (~3%).
