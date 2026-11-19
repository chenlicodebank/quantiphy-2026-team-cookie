# Q2489 – acceleration of the ping pong ball at 1.3 s (cm/s²)

The file and question_fps are both 24, so t = 1.3 s is frame 31 (31.2). That is the apex of the first rebound arc. The arc runs from the bounce at f26 to the bounce at f36, with the apex near f31–32.

## Method
- `measure.py`: I re-tracked the ball myself. The background is the per-pixel median, the mask is |diff| > 40 and brightness > 70, and the position is the mask centroid. The positions match scene/tracks/ball.csv to within 1 px, an offset from the pixel-centre convention. I checked the overlays at f29 and f31.
- `accel.py`: the lab camera has f = 0.5959 × 1280 = 762.8 px and principal point (640, 360). I back-projected the centroids with ((u−cx)/f, (v−cy)/f, 1)·Z.
- I tried three depth models:
  - Z constant at 1.4115 m.
  - Z linear through the given depths at t = 1.1 s (f26) and t = 1.3 s (f31).
  - Z from the ball's pixel width, anchored at 1.4115 m at f31.
- I fitted a quadratic to the free-flight arc (f27–35 and sub-windows) and also took the raw second difference at f31.

## Results (|a|, cm/s²)
| Z model | fit f27–35 | fit f28–34 | fit f28–33 | 2nd diff f31 |
|---|---|---|---|---|
| const | 795 | 777 | 784 | 784 |
| linear | 822 | 807 | 837 | 815 |
| diameter | 808 | 791 | 809 | 798 |

- The pixel acceleration is 7.46 px/frame², almost entirely vertical.
- The routes agree at about 780–840 cm/s². This is lower than g (981). One likely cause is that the measured depth gives a smaller metres-per-pixel scale; the ball's pixel width implies a depth of about 1.33–1.39 m, which is slightly closer than the given 1.4115 m.
- Following the reference method (measured centres, depth_info scale), the answer is the measurement, not g.

**Answer: 810 cm/s².** Confidence is moderate: the measurement spread is about ±4%, and there is a risk that the reference instead used g ≈ 981.
