# Q124: length of the bike (m). Prior: car acceleration = 4.03 m/s^2. 2D top-down render, 24 fps (file and question rates match).

## Scale from the car's acceleration
- `steps_car.py` template-matches the car frame to frame (subpixel) and gives its pixel speed per frame:
  1.06, 1.81, 2.52 ... 25.8 at f37 ... 38.7 at f53.
- Speed is very linear over f3-37: the slope is 0.707 px/frame² (0.7067 for f3-20, 0.7039 for f20-37).
  - After f38 the slope rises to about 0.76, and it reaches about 1.0 in f50-53. The front and rear edges show the same thing (`measure.py`).
  - Fit over all frames: 0.720. Quadratic fits on the front edge: 0.705 to 0.763 depending on the window.
- I used a = 0.707 px/frame² = 407 px/s². Scale = 4.03 / 407 = 0.00990 m/px.
- Sanity check: the car is about 570-577 px long → 5.65-5.7 m, which matches a Cybertruck (5.68 m). With the late slope of 0.8, it would be only 5.0 m.

## Bike pixel length
- Wheel tip to wheel tip (`steps_bike.py`, `measure.py`): 174 px near the left edge, falling to 169-170 px near the image centre.
  - The fall comes from height parallax in a perspective view; the size is truest near the centre. I used 169.5 px.
- The bike's speed is a constant 21.48 px/frame (±0.5%) across x = 100-1050. That means the scale does not change with x.

## Result
- 169.5 px × 0.00990 = 1.68 m.
- Perspective correction: the tracked car features sit at about 1.1 m height, the bike's wheel tips at about 0.35 m, and the camera is estimated at about 30-40 m from the car's length shrinkage. This adds about 1-2%.
- **Answer: 1.69 m.**

## Second-route check
- Using the full-clip acceleration of 0.720 gives 1.65 m.
- Bike speed comes out at 5.1 m/s and the car at 5.7 m, both plausible.

## Confidence
Moderate, about ±4%. The main uncertainty is that the car's pixel acceleration is not constant late in the clip.
