# Q1376 – height of the white car (white Chevrolet cargo van = "van" in scene/), prior length = 6 m

File fps = question fps = 24, so there is no time-base issue. Static camera, 3D Blender scene.

## Camera
- Vertical vanishing point from 5 clean vertical poles (poles.py): about (1084, 4619) px. The camera is pitched down about 24-25 deg.
- Focal length (focal.py): the vehicles and cyclist move on level ground, so the 3D displacement between t=0.58 s (frame 14)
  and t=1.58 s (frame 38), back-projected with the given depths, must be perpendicular to the vertical. This gives f ≈ 1890-1950 px
  from the van, the cyclist and the pedestrian; the taxi gives no solution (its motion is almost parallel to the image).
- Kerb-line vanishing points (kerbs.py) are noisy and give about 1650-1770 px.
- The van-model depth ratio D38/D14 (given 0.886) lies between the values at f=1750 (0.871) and f=1900 (0.894), so f ≈ 1850.

## Van height (fit2.py / fit2b.py / fit2d.py)
- Masks: background subtraction with GrabCut (mask3.py, mask38.py), taking the convex hull together with hand-picked
  tyre-contact and bumper-bottom points (the soft shadow made the lower outline unreliable).
- Model: a van-shaped prism (rear box, sloped windscreen, hood; body bottom at clearance c) plus tyre contact points on the ground.
  - Fitted jointly on frames 14, 60 and 71: shared shape, separate pose (ground x, y, yaw) per frame.
  - Cost = silhouette IoU plus tyre keypoint error.
  - Scale is set by L = 6 m (the prior).
- Results (height H at L = 6):
  - f=1900: H=2.375, W=1.87 (IoU 0.89/0.87/0.95)
  - f=1750: H=2.384, W=1.92 (IoU 0.94/0.85/0.93, best cost)
  - f=2100: H=2.333 (worse fit)
  - W fixed at 1.80 / 2.05 (f=1750): H = 2.389 / 2.370, with almost the same cost. H does not trade off against W.
- Depth check (fit3.py): with this shape, the model's ground-centre distances (32.9 m at frame 14, 28.8 m at frame 38, f=1750) are
  about 5% above the given 31.28 m / 27.72 m. A front-axle origin would match both depths (scale 1.00-1.02).
  - Either the van's origin is not at its centre, or the depth-implied length is about 5.7 m.
  - This affects only the absolute scale, not H/L. The answer uses H/L × 6 from the prior.
- Rough second route: the rear vertical edge at frame 38 spans about 133 px from roof to the ground point below it.
  With depth about 30 m, f ≈ 1800 and the camera pitch, this gives H ≈ 2.4 m, which agrees.

Answer: H ≈ 2.38 m. For comparison, a real Chevy Express (2.08 m tall, 5.69 m long) scaled to 6 m long would be 2.19 m.
The fitted ratio H/L = 0.40 is a little higher than that. Confidence: moderate (about ±6%).
