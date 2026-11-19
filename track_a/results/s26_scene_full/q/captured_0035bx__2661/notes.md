# Q2661: soccer ball displacement, 0.4 s to 0.9 s (cm)

Lab video, 24 fps (file and question_fps are the same). t=0.4 s → frame 10 (ball still at rest before the kick at frame 11),
t=0.9 s → frame 22. f = 0.5959·1280 = 762.8 px, principal point (640,360). depth_info is the Euclidean distance to the centre.

## Depths
- Frame 22: soccer 2.477 m (given).
- depth_info lists "soccer" twice at t=1.4 s (2.602 / 2.373). One of them must be the basketball. The sizes show 2.373 is the soccer ball:
  D_soccer from f22 is 2.477·58.5/763 = 19.0 cm, and from f34 it is 2.373·61/763 = 19.0 cm.
- Frame 10 has no given depth, so I estimated it two ways:
  1. **Apparent-size ratio.** I fitted an ellipse to radially sampled edge points. The ellipse was constrained to the
     projected-sphere shape (major axis radial, ratio 1/cosθ), and the shoe sector and image bottom were excluded.
     The minor axis is about f·D/dist. Frame 10: 69.2–69.7 px, rms 0.75 px. Frame 22: 57.4–59.2 px (constrained and
     unconstrained fits; blur adds some width). Z10 = 2.477·m22/m10 = 2.04–2.12, best about 2.08 m.
     - Check: the same fit on the basketball at f22 gives 64.8 px, against 63.7 px predicted from 23.2 cm at 2.7777 m (+1.7%).
       The scene record's bbox sizes (81 px at f10) included the kicking shoe and halo, so I didn't use them.
  2. **Plane of ball centres.** I fitted a plane to the 4 given 3D centres: soccer f22 and f34, plus basketball f22 and f34
     lowered by the 2.1 cm radius difference. Residuals were under 0.8 cm. Intersecting the f10 ray with this plane gives Z10 = 2.116 m.

## Positions and displacement
- Centres: f10 (437.4, 682.7) and f22 (615.2, 485.0) px.
- Each centre is back-projected as distance·unit ray.
- Route 1 gives 80.1–82.7 cm (best 81.3). Route 2 gives 80.1 cm.
- If the depth were read as z instead of Euclidean distance, the result would be 77.7 cm. I didn't use that reading.

**Answer: 80.8 cm.** Confidence is moderate-high, about ±3%. The main uncertainty is the depth at frame 10, which isn't given.
