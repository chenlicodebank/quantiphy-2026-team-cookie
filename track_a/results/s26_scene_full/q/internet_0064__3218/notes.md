# q_3218 – ball displacement 3.50 s → 3.70 s

- fps = question_fps = 30, so the frames are 105 and 111. Both are in free flight 1 (release at 81, bounce at 114).
- Scale from the prior (g = 9.8 m/s²): I fitted a quadratic to the ball's cy (scene/tracks/ball.csv, fit.py).
  - Flight 1, frames 82–112: ay = 3537 px/s² (3543 with camera drift removed).
  - Flight 2, frames 117–142: ay = 3536 px/s² (3562 with drift removed).
  - Both flights agree, so I used ay = 3540 px/s², which gives 9.8/3540 = 0.002768 m/px.
  - Caveat: inside flight 1 the early part gives 3640 and the late part 3410. The ball's apparent size also shrinks from 85 to 80 px, so there is a slight perspective/depth effect. Following the single-scale convention, I used the fit over the whole flight.
- Positions (raw pixels):
  - Frame 105: (1109.8, 448.0). Frame 111: (1273.6, 785.6).
  - The displacement is (163.8, 337.6), which is 375.2 px. With drift removed it is 377.1 px (0.5 % more).
- Answer: 375.2 × 0.002768 = **1.039 m**.
- Second route: a scale from the ball's size (about 85 px for a basketball of about 0.24 m) gives 0.00282 m/px and 1.06 m, within 2 %. The size implied by the gravity scale is 85 × 0.002768 = 0.235 m, which is plausible for a basketball.
- Confidence: good (within about 5 %).
