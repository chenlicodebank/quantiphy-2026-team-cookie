# q 2623 — soccer ball displacement 0.5 s -> 0.6 s (cm)

Frames: question_fps = file fps = 24 -> t=0.5 is frame 12, t=0.6 is frame round(14.4) = 14.
Camera: f = 0.5959*1280 = 762.8 px, principal point (640, 360).

Pixel centres (scene track, checked on 4x crops frames/f12.png, f14.png): f12 (493.3, 391.9), f14 (523.7, 410.5);
pixel step 35.6 px. Ball is motion-blurred, so diameters use the minor axis.

Depth: given 2.758 m at f14 only. The f12 depth has to be inferred:
- Floor-plane route (main): the ball centres roll in a plane about 11 cm above the floor. I fitted that plane to
  the given anchors (soccer f14 2.758, soccer f38 3.052, basketball f14 2.270, and the second "1.6 s soccer" value 2.412,
  which is the basketball: its size gives 21.9 cm, matching f14) plus size-based depths of both balls over the
  clip (plane.py). Normal tilt 26 deg; camera 1.39 m above the centre plane; anchor residuals at most 3 cm.
  With the plane through the f14 anchor, f12 is at distance 2.863 m. Displacement f12->f14 = **16.6 cm**
  (16.4 cm with the free fit). Plane steps for frames 12-19 are steady at 7-9 cm/frame (about 2 m/s), which fits one
  steady roll.
- Size-ratio route (check): depth from the blurred minor-axis diameter gives 13.5 cm. Equal depth gives 12.6 cm;
  the area-equivalent diameter gives 24 cm. The blurred size is too noisy (it jumps 51 -> 54.5 px at f15), so this
  route is unreliable. Over frames 12-19 its trend also says the ball is approaching, which agrees with the plane.
- Basketball size check: 22.1 cm against the prior 23.2 (5% low, typical of the mask), and the soccer ball's size is consistent between f14 and f38.

Answer 16.5 cm. Confidence moderate (±15%): it depends on the inferred depth at f12.
