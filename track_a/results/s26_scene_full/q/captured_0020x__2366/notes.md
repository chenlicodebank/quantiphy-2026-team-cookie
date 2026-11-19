# q_2366: height of the yellow toy (cm)

The yellow toy is the "carrot" in depth_info: a pale-yellow body with a dark olive top, thrown by the far person.
scene/ calls it `yellow_fruit`. The file and the question are both 24 fps, so t = 0.60 s is frame 14, which is also
the toy's first free-flight frame. I took "height" to mean the toy's long axis, from the tip to the top of the leaves.
This is the only reading that makes sense for a carrot-like toy.

## Method
- f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
- Mask: the non-green pixels, i.e. the SAM2 composite, with G - max(R, B) < 128. I removed hand pixels by colour
  (R - G > 38 and R > 140) and kept the connected component at the track centroid (f14.py, size.py). The masks were
  drawn and checked in frames/k*.png and frames/m*.png.
- I took Feret extents over 0-179 deg. Motion blur is a Minkowski sum, so I subtracted L |cos(angle - motion)|, with
  L = exposure fraction x image speed. The fraction is about 0.44 of a frame, measured from the white ball:
  extent along the motion minus extent across it, divided by speed.
- Depth across frames (fit3d.py): a joint ballistic fit of the ball and the toy, |g| = 9.8 m/s^2 (the prior), with
  one gravity direction for both. The given depths at f14 are used: ball ("jar") 1.9735 m, toy 2.63 m. Reprojection
  RMS is 1.26 px and the camera tilts about 59 deg down. That tilt fits the strong perspective on the near person.
  The ball's apparent diameter scales as 1/depth in this solution (about 9 cm, CV about 5%). A shallow-tilt
  solution also exists, but it fits worse (discrim.py, profile.py).

## Key measurements (long axis)
| frame | px (blur-corrected 0.44 / 0.30 / raw) | depth m | cm |
|---|---|---|---|
| f14 (stated time, given depth) | 50.5 / 51.4 / 54.0 | 2.630 | 17.4 / 17.7 / 18.6 |
| f15 | 54.9 / 56.8 / 61.4 | 2.48 (fit) | 17.9 / 18.5 / 20.0 |
| f16 | 54.3 / 56.4 / 61.4 | 2.35 (fit) | 16.7 / 17.4 / 18.9 |
| f17 | 58.3 / 60.1 / 64.1 | 2.22 (fit) | 17.0 / 17.5 / 18.7 |

## Second route
- Frames f15-17 use depths from the gravity fit, which is a route independent of the f14 depth. They give 16.7-20 cm,
  which agrees with f14.
- In f0 the far person holds the toy at her hip (about 3.2 m away, partly hidden by the hand): about 39 px, so at
  least about 16 cm.
- Frames f20-23 show an elongated side view, but the motion there is along the long axis, so blur is largest:
  - blur-corrected: 13 cm;
  - raw: 16-19 cm.

  The two disagree, and I gave these frames little weight.

## Answer
18 cm. Confidence is moderate, about ±10%. The main uncertainties are the motion-blur correction and possible
foreshortening, since the toy tumbles.
