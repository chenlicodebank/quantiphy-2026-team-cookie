# Q1392 – length of the bike (m)

Prior: bike speed 5.52 m/s. Depths: 28.219 m at t=0 (frame 0) and 25.554 m at t=0.5 s (frame 12). File fps = question fps = 24.
3D video with a static camera; the bike rides toward the camera and to the left (it is seen obliquely, at about 30-40° to the line of sight).

## Focal length (fit_f2.py, sens.py)
- Depth track: camera-axis depth Z ∝ 1/(cyclist bbox height) from scene/tracks/cyclist.csv (I spot-checked h = 177 px at frame 0 and 419 px at frame 79 on zoomed frames), anchored to the 28.219 m at frame 0. I converted between camera-axis depth Z and Euclidean distance using the ray-length factor, which matters because the bike starts 876 px off-axis.
- 3D path = back-projected smoothed bbox centre. I chose f so that the mean per-frame speed is 5.52 m/s: **f ≈ 2594 px**. The per-frame speed then stays flat (5.44-5.61 m/s), and the depth at frame 12 comes out at 25.505 m (given: 25.554).
- Variant: add a 4.5 px offset to the heights so that d12 is reproduced exactly. This gives **f ≈ 2504 px**, again with flat speeds (5.48-5.56).
- Independent check: using only frames 0-12 (the two given depths, a 2.76 m chord) gives f ≈ 2511. This route is very sensitive to error, but it agrees.

## Length (length2.py)
- Heading = 3D velocity direction (made horizontal) from the reconstruction: about (-0.555, 0, -0.832) in camera coordinates.
- I read the hub centres and tyre vertical diameters by hand on zoomed frames 79 and 68. Solving s·rF − t·rR = w·heading, with the hub mid-depth set to the reconstructed bike depth, gives the wheelbase and both hub depths. Wheel diameter = vertical pixel diameter × Z / f.
- Bike length = wheelbase + wheel diameter (front tyre to rear tyre along the heading).
- Checks:
  - The ellipse minor/major ratio predicted from the heading (0.63-0.65 at frame 79, 0.53-0.55 at frame 68) matches the measured tyre ellipses (≈0.58-0.65 and ≈0.51-0.53).
  - The hub-depth ratio from the solve (1.07) matches the ratio of wheel pixel diameters (1.09).

| f (px) | frame | wheelbase (m) | wheel diameter (m) | length (m) |
|---|---|---|---|---|
| 2594 | 79 | 0.963 | 0.69 | 1.655 |
| 2594 | 68 | 1.002 | 0.68 | 1.686 |
| 2504 | 79 | 0.977 | 0.725 | 1.702 |
| 2504 | 68 | 1.013 | 0.71 | 1.727 |

**Answer: 1.69 m** (range 1.65-1.73).

Caveat: the yellow parcel on the front rack reaches about 20 px beyond the front tyre in the image at frame 79. If it counts as part of the bike's bounding box, the length could be a few cm longer. I have not included it.

Confidence: moderate, about ±5-8%. The main uncertainty is f, which depends on the accuracy of the depth-from-height track.
