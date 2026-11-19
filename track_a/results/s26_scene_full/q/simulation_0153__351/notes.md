# Q351 — speed of the blue car at t = 1.5 s (m/s)

Prior: the blue car's tyre diameter is 0.369 m. No depth_info is given. fps = question_fps = 24, so t = 1.5 s is frame 36.
Speed at frame 36 is the backward difference p36 − p35.

## Scale (tyre diameter in pixels)
- `wheel2.py`: for each wheel in frames 31–41, I scanned rays out from the hub over the side sectors (top and bottom
  left out because of the wheel arch and the ground contact). On each ray I found the sub-pixel dark→bright outer edge
  of the tyre, then fitted a circle with a robust fit.
- Rear tyre (close to the image centre, so very little perspective): D = 108.0–110.1 px, median about 108.6 px.
  At frame 36: D = 108.9 px.
- Front tyre: 108–115 px. Its outline merges with the front bumper edge, so it is less reliable. At frame 36 it
  gives 108.2 px.
- `wheel.py` raw row profiles at frame 36: rear 820.5→930 (109.5 px), front 1151.5→1262 (110.5 px).
- I used D = 108.8 px, which gives a scale of 0.369 / 108.8 = 3.392e-3 m/px. The tyre and the side-panel tracking
  point are on the same near side of the car, so they share this scale. The car moves parallel to the image plane:
  the ground line stays constant and the size changes by about 1 %.

## Pixel speed at frame 36
- Panel template (scene/tracks/cart.csv, smooth): increments for frames 34, 35, 36 and 37 are 49.2, 48.6, 48.1 and
  47.3 px/frame, so p36 − p35 = 48.06 px.
- Rear-wheel circle centre (second route, independent): 875.4 − 827.6 = 47.8 px/frame.
- I used 48.0 px/frame, which is 1152 px/s.

## Result
Speed = 1152 × 3.392e-3 = 3.91 m/s. The rear-wheel route gives 3.89 m/s. Answer: **3.9 m/s**.
Confidence: about ±3 %. The main uncertainty is the tyre's pixel diameter (108–110.5 px).
