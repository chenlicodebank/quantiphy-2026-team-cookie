# Q1802: average speed of the boat (m/s)

2D side-view clip, 24 fps (file and question rates are the same), with a static camera. Prior: the shark's acceleration is 1 m/s².

## Scale from the prior (shark pixel acceleration)
I fitted a quadratic to the shark's x over frames 1–58, while the shark is fully in frame (`fit.py`, using the scene tracks):
- template_dx: 85.2 px/s² (rms 0.27 px, the cleanest)
- bbox nose x0: 86.7, bbox centre: 86.2, ref_x over frames 1–72: 86.4, tail x1: 85.8 px/s²
- I take 85.8 ± 0.6 px/s². With a = 1 m/s², the scale is 1 m = 85.8 px.

## Boat speed
Rigid template track of the boat. Its speed is constant (quadratic-fit acceleration about 0).
- Linear fit over frames 2–72: 429.1 px/s. The mean of the per-frame speeds over frames 2–72 is 429.3 px/s.
- 429.2 / 85.8 = 5.00 m/s.
- Second route: the bbox-centre differences over frames 2–47 average about 17.9 px/frame, which is 430 px/s and gives the same value.
- If the at-rest step from frame 0 to frame 1 is counted in the mean, the result is 423.4 px/s, which gives 4.93 m/s. Both frames show the same image, so this looks like a duplicated start frame, and I answer with the moving-speed value of 5.0.

Confidence: high (about 2%).
