# Q1441 – diameter of the truck's tyre (m) – answer 0.758 m

The file and the question both run at 30 fps, so there is no time-base issue (t = 0.5 s is frame 15, t = 1 s is frame 30).

## Method (3D pinhole, level camera)
- Camera: static and level. The horizon is at y ≈ 540–545 from the record's vanishing points, so I used cy = 542 (and
  tried 539 and 545). cx = 960.
- `geom.py`: I took the front-hub track from scene/tracks/truck.csv (frames 3–46). The hub stays at a constant height,
  so for a trial focal length f each hub pixel back-projects to a 3D point up to scale (hub height H below the camera).
  These points lie on a straight line. I fitted the path coordinate s(t) with a quadratic. The prior
  a = 10.757 m/s² gives the metric scale, H = 0.5·a / (quadratic coefficient). The fit is clean: the truck is at rest
  at t ≈ 0.002 s, v0 ≈ 0, and the rms residual is 3 mm.
- Focal length: the truck origin was placed on the ray of the record's body-centre proxy at frame 40 (also tried
  frames 35 and 30). It moves rigidly with the hub. I then solved for (f, distance along that ray) so that
  |O(15)| = 22.532 and |O(30)| = 19.525 hold exactly. Result: f ≈ 2650–2790 px and H_hub ≈ 1.89–1.92 m.
  H depends only weakly on f.
- Tyre pixel size (`wheel.py` makes contrast-enhanced crops, `edges2.py` takes sub-pixel half-max edges on vertical
  profiles through the hub column):

  | frame | top | bottom | diameter (px) | rim centre y | 2·(bottom − centre) |
  |---|---|---|---|---|---|
  | 20 | 767.5 | 879.7 | 112.2 | 822.7 | 114.0 |
  | 30 | 789.4 | 913.3 | 123.9 | 851.0 | 124.7 |
  | 36 | 811.0 | 944.4 | 133.3 | 877.4 | 134.0 |
  | 40 | 831.1 | 972.7 | 141.6 | 900.8 | 143.8 |

  Frame 45 was rejected because of motion blur (it gives about 2 % less). The diameter in metres is
  D = Z·Δv/f = H·Δv/(v_hub − cy). The ratio Δv/(v_hub − cy) ≈ 0.400 and is stable across frames.
- `final.py`: D = 0.753 (top–bottom edges) / 0.761 (2 × the hub-to-bottom radius) with cy = 542 and the frame-40
  reference. Over all variants (cy 539–545, proxy frame 30/35/40) D ranges from 0.746 to 0.784 m.

## Second-route check
- Diameter from both tyre edges vs 2 × the radius from the rim-ring centre: these agree within 1 %.
- Four frames at different depths give the same normalised ratio within ±1 %.
- Three different origin-proxy frames for the f solve give f from 2650 to 2790 px, which changes D by only 1.6 %.

## Confidence
Answer 0.758 m. The estimated uncertainty is about ±3 %. The main sources are the horizon row (cy) and the true origin
position used in the f solve.
