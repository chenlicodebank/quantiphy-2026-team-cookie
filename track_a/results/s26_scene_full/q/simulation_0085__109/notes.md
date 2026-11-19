# Q109: speed of the bike at 1.0 s (frame 24)

The video is 2D and seen from the top, with a static camera and no perspective change. The video fps and question_fps are both 24.
I took one metres-per-pixel scale from the prior (car acceleration = 4.03 m/s^2).

## Car pixel acceleration
- `track_tm.py`: template-matched the car from frame 50 (with sub-pixel parabola refinement), frames 0-71.
  - The car starts from rest at about frame 1.5.
  - Its speed grows almost linearly through frames 8-47, by about 0.91-0.95 px/frame^2.
  - From about frame 48 to 56 it rises a little faster, then it levels off at about 62 px/frame after frame 64.
- Quadratic fits to position over different frame windows:
  - frames 3-63: 0.954 px/frame^2
  - frames 3-30: 0.948
  - frames 10-55: 0.921
  - frames 3-71: 0.977
- Integer front-edge track from scene/ (`fit.py`):
  - frames 3-63: 0.939
  - frames 10-60: 0.938
- Average from rest to the speed plateau: 62 px/frame over about 64.5 frames = 0.96.
- Adopted value: a = 0.935 px/frame^2 = 538.6 px/s^2. Uncertainty is about ±4%.
- Scale = 4.03 / 538.6 = 0.007483 m/px.
- Sanity check: the car is 727 px long, which gives 5.44 m (a Cybertruck is about 5.7 m), and the bike is 208 px, which gives 1.56 m.

## Bike speed
- The bike moves at a constant speed. A linear fit to the bbox centre over frames 4-67 gives 26.67 px/frame, and a fit to the front edge over frames 2-67 gives 26.63 px/frame.
- The per-frame steps alternate between 26 and 27 px only because the edges are whole pixels.
- v = 26.65 × 24 × 0.007483 = 4.79 m/s.

## Second route
- Using only the cleanest stretch of the car's motion (frames 8-47, 0.91-0.95 px/f^2) gives 4.71-4.92 m/s.
- Using the integer-edge fit (0.939) gives 4.76 m/s.

Answer: 4.78 m/s. Confidence is moderate. The main uncertainty is that the car's acceleration is not perfectly uniform, worth about ±4%.
