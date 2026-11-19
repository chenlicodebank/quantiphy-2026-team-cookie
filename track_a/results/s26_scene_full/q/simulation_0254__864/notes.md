# Q864 — speed of the tennis ball at t = 1 s (simulation_0254)

- fps = question_fps = 24, so t = 1 s is frame 24. Speed = |p24 − p23| × 24 × (m/px).
- 2D scene with a single ball rolling down the incline; I used one scale from the prior: diameter 0.17 m.
- **Positions** (`measure.py`, which re-tracks with an HSV mask and agrees with scene/tracks/ball.csv to within 0.1 px):
  - p23 = (432.64, 120.26)
  - p24 = (460.38, 147.57)
  - step = 38.95 px/frame
  - The steps before and after (36.2, 37.3, 38.9, 40.5, 42.1) increase smoothly, so frame 24 is not an outlier.
- **Second route for speed** (`speed.py`): a quadratic arclength fit over frames 19-47 gives a step of 39.5 px, 1.5% higher. Acceleration is not quite constant over the whole ramp (fit rms 1.7 px), so I kept the local raw step.
- **Ball diameter in pixels:**
  - The saturation mask (sat > 110) gives an equivalent diameter of 24.4 px at f24 and about 23.5-23.7 on the floor.
  - Half-max saturation profiles in 12 directions give a median of 22.6 px. This underestimates, because the dark side is less saturated.
  - Half-max colour-distance profiles give a median of 24.6 px. This is inflated by the contact shadow in some directions; directions free of shadow give about 23-25 px.
  - Adopted D = 23.8 px (uncertainty about ±3%), giving 0.00714 m/px.
- **Answer:** 38.95 × 24 × 0.17 / 23.8 = **6.68 m/s**. Over D = 23-24.5 px the answer ranges from 6.49 to 6.91 m/s.
- **Confidence:** moderate-high. The diameter in pixels is the main source of uncertainty (about ±4%).
