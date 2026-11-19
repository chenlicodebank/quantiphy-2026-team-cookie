# Q120: distance between the car and the bike at t = 1.0 s (frame 24)

The video is 2D and top-down at 24 fps; question_fps is also 24, so no re-timing is needed. Prior: the car's acceleration is 4.03 m/s².

## Method (`measure.py`)
- Each frame is compared with the empty frame 71, and only the object bands are kept in memory. The car's front (left) bumper edge stays sharp, so it is tracked over frames 0–56. The bicycle position is the centre of its bounding box.
- I fitted x = xa − ½·a·(f − f0)² with f0 free (the car starts moving at about frame 0.7):
  - a = 0.5448 px/frame², which is 313.8 px/s².
  - Residual RMS is 1.4 px.
  - Quadratic fits over sub-windows give a = 0.53–0.555, a spread of about ±2%.
- Scale = 4.03 / 313.8 = **0.01284 m/px**.
- Sanity checks on the scale:
  - Car length 438 px → 5.62 m. A real Cybertruck is 5.68 m, about 1% away.
  - Bicycle 129 px → 1.66 m, which is plausible.
  - Cyclist speed 16.04 px/frame → 4.94 m/s, which is plausible.

## Frame 24
- Car origin = front x 722.5 + 218.5 (half the length) = 941.0, with y = 651.75.
- Bike centre x = 1317.5, with y = 477.25.
- dx = 376.5 px and dy = 174.5 px, giving 415.0 px → **5.33 m**.

## Second route and alternatives
- Taking the scale from the real Cybertruck length (5.68 m / 438 px) gives 5.38 m.
- Using the rider's body (a proxy for the pelvis, about 11 px behind the bike centre) gives 5.20 m.
- I answer with the bike's centre: **5.33 m**.

Confidence: good, about ±3%. Most of the uncertainty comes from the acceleration fit and from where exactly each object's origin sits.
