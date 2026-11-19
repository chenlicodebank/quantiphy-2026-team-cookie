# q_1055 – maximum height of the cart from the ground (m)

The file runs at 22.892 fps and the question at 24 fps. Times are converted with 24 fps (t = 1 s is frame 24); I used frame numbers, not the record's seconds.
The cart does not move, so its maximum height is the top of its bounding box above the ground.

## Focal length (from the prior: bird length 1.19 m, depth_info for the bird)
- Bird depth: a straight line between the two given values, 34.584 m at t=0 and 33.999 m at t=1 s.
- Bird pixel length: the bounding-box width (tip to tail) from scene/tracks/bird.csv. I checked the boxes on zoomed crops (frames 1, 19, 36). They include the tail and the grey head.
- Wings-level frames (bbox_h < 80) give a median f = 4503 px. The median over all clear frames 0–38 gives f = 4488 px. Spread is about ±5 %.
- The bird flies almost parallel to the image plane: its direction from the two 3D points is (0.99, 0.09, -0.10). So shortening of its length by the viewing angle is under 1 %.
- I used f ≈ 4500 px (focal.py, geom.py).

## Cart
- Pixel extent at frame 0, read on 5x zoomed crops (cartcrop.py): the top is the raised rear corner of the bed at (1864, 1010). The bottom is the near wheel touching the ground at y = 1267. That gives 257 px.
- Depth: I took the cart origin to be near the image centre of the cart's bounding box (1592, 1140). With distance 30.374 m, the depth along the camera axis is Z ≈ 30.06 m.
- Height = 257 × 30.06 / 4500 = **1.72 m**.
- Effect of the rear corner being a little farther away: for a level camera, height = h_cam + (v_horizon − v_top)·Z_top/f. A depth error of about 0.5 m changes the result by less than 0.01 m.

## Checks
- Focal length from wings-level frames vs all clear frames: 1.716 vs 1.721 m.
- Sanity check: the wheel diameter comes out at 210 px → 1.40 m, which is plausible for a large cart wheel.
- Main uncertainty: the bird's rest-pose length in pixels (the bounding-box width ranges 152–172 px), about ±5 %.
- Confidence: moderate to good.
