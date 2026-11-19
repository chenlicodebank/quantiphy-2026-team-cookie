# q_263: speed of the left first ball (ball1) at 1.0 s

- 2D Newton's cradle render. The two frame rates differ by only 0.03% (30.0075 in the file, 30.0 with the question), so the choice doesn't matter. t = 1.0 s is frame 30, after ball1 hits the row between frames 27 and 28.
- Scale: the prior gives a ball diameter of 2 m. The record measures 163 px, and the frame-30 difference mask of ball1 agrees (cols 554–717, about 163 px). That gives 2/163 = 0.01227 m/px.
- After the impact, ball1 drifts left slowly at an almost constant rate, with y constant at 783.
  - Record track (rim fit): 29→30 = 1.03 px. Neighbouring steps: 0.89, 0.82, 0.93. The 28→34 mean is 0.90 px/frame and the 29→39 mean is 0.87.
  - Route 2 (`measure2.py`): phase correlation of background-subtracted crops with ball2 excluded gives 29→30 = 0.85 px. Over frames 28–39 it totals 9.0 px against 9.55 px for the track, so it is probably biased slightly low.
  - Route 3: the sub-pixel left-edge step for 29→30 is 0.92 px.
- Adopted step: 0.93 px/frame × 30.0075 fps = 27.9 px/s × 0.01227 m/px ≈ 0.343 m/s. Answer: 0.345 m/s.
- Confidence: moderate. Because the step is only about 1 px, the plausible range is 0.31–0.38 m/s.
