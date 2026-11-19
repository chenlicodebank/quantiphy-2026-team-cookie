# q_2851: velocity of the green ball at 1.5 s (m/s)

File fps = question_fps = 24, so t = 1.5 s is frame 36.

## Identification
- Green ball = the yellow-green tennis ball (`scene/tracks/tennis_ball_yellow.csv`). White ball = the light-grey small ball, and
  orange = the basketball (both checked on frame 24 crops).
- At frame 24 (t = 1.0) the green ball is still in the standing person's hand at (599,290), depth 3.039 m. It is released at
  frame 25, flies, and bounces at frame 37 (its lowest point). Frame 36 is the last frame before the bounce, with heavy motion blur.

## Measurements
- Centroids from the scene track. I checked them with my own colour mask (`measure.py`), and they agree within about 1 px.
- Pixel steps per frame: 33→34 45 px, 34→35 53 px, 35→36 135 px, 36→37 53 px. One capture frame is missing between 35
  and 36.
- 3D ballistic fit (`fit3d.py`): a pinhole model with f = 763 and c = (640,360), |g| = 9.81, and camera pitch as a free
  parameter, fitted to the (u,v) points of frames 25–36. The depth constraint is |p(24)| = 3.039 m.
  - Without a dropped frame the fit is poor (rms 7.5 px). With one frame dropped between 35 and 36 the rms is 0.43 px and
    the pitch is 11°.
  - The fit's predicted ball diameters (17.8→24 px) match the measured widths in the scene record.
  - Fitted without the depth constraint, gravity alone sets the scale and gives |p(24)| = 3.35 m against the given 3.04 m.
    The two agree to about 10 %.
- The fitted velocity at frame 36 is (-1.19, 4.44, -2.00) m/s, so |v| = 5.0 m/s. This is the true speed just before the
  bounce.

## Second route (reference-style forward differences, `refstyle.py`)
- I back-projected the centres using the fitted depths, then extrapolated the depth linearly after the bounce.
  - The single forward difference 36→37 gives 3.3 m/s. It is low because the bounce happens inside that step.
  - The 5-frame mean of the forward differences over 34–38 gives 4.85 m/s.
  - The central difference 35→37 gives 6.3 m/s.
- Depth from the ball's measured size is too noisy here (the diameter is only 17–30 px and blurred) and gives a scatter of
  3–11 m/s.
- I checked the prior's convention on the basketball around frame 12 and get about 1.8–1.9 m/s, against the given 2.21.
  The reference is probably noisier or higher than my estimate, but I did not rescale.

## Answer
5.0 m/s. Confidence is moderate. The physical speed is well constrained, but how the reference smooths across the
bounce and the dropped frame is uncertain.
