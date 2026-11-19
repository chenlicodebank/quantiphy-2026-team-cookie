# q_2743 – diameter of the white cup's rim (cm)

File fps = question fps = 24. The cup is static and the camera is static (scene/camera_shift.json).

## Scale
Lab method card: f = 0.5959 x 1280 = 762.8 px, principal point (640,360).
depth_info gives `distance_white_cup_camera = 8420m`, which is clearly a typo. I read it as **0.842 m**, which fits
the scene: the cup stands behind the card (0.69 m) and in front of the poker tower and tape region (0.91 to 0.97 m).

## Measurement (measure_cup.py, subpix.py)
- I averaged frames 0-22 (the ball is far left in these frames) and found the cup's left and right edges per row,
  to sub-pixel precision, at the half-level between the background and the cup body.
- The rim is seen almost edge-on (the camera is near the height of the cup top), so the rim's horizontal extent is
  its diameter. Rows 380-393, just below the silver rim band, give 739.2 -> 813.5, a width of **74.2 px**
  (spread 73.8-74.5). Lower rows narrow because the cup tapers (73.5 at y=399, about 50 px at the bottom).
- Diameter = 0.842 x 74.2 / 762.8 = **0.0819 m = 8.19 cm**.

## Check (card.py and a gridded crop)
Credit card lying flat at 0.69 m. It is a parallelogram in the image: the front edge is about 99 px and the back
edge about 92 px, mean about 95.5 px. The expected value is 762.8 x 0.0856 / 0.69 = 94.6 px. They agree to about
1 %, which confirms f and the depth convention.

If the off-axis cos² correction is applied (the cup is about 10° off-axis), the result would be about 7.9 cm. I
answer with the plain method-card value instead.

Confidence: good (about ±3 %). The main risk is how the depth typo is read.
