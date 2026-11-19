# q_2899: velocity of the white ball at 1.5 s (frame 36)

The file rate and question_fps are both 24, so frame = round(t x 24): t = 1.5 s is frame 36. Camera f = 0.5959 x 1280 = 763 px, principal point (640, 360).
The ball called "yellow_ball" in scene/ is the depth_info's "green ball" (a yellow-green tennis-type ball). The "white_ball" track
is the off-white ball, checked on montage crops (frames/m1.png, m2.png).

## Key facts
- f35->f36 has a dropped recording frame: every object moves about 2x its usual step. The white ball bounces between f37 and f38
  (its lowest image point is at f38).
- The white ball's depth is given only at f24 (1.235 m). Its apparent width at f20-26 is inflated by motion blur and by overlap
  with the green ball (about 48 px), so a plain diameter ratio from f24 is biased.
- Depth path, from `ballistic.py` (fit A): a 3D parabola fitted to the image track f20-37 with the distance at f24 fixed at 1.235 m,
  free gravity vector, and the dropped frame accounted for (RMS 2 px). Distance at f36 = 2.03 m, f37 = 2.14 m.
  Check: apparent width x fitted distance stays constant over f27-36 (47 +/- 2 px*m, which implies a 6.2 cm ball). This
  confirms the relative depth path independently. Fit A gives |g| = 7.35 m/s^2, and the green ball's fit gives 7.7. A fit
  with |g| = 9.81 forced would put the depths about 30% further away. I kept the depth_info scale, as the rules require.
- Positions: the track centre ray x the distance. Forward differences of the speed: f34->35 2.75, f35->36 6.26 (spans the
  dropped frame), f36->37 3.59 m/s. The analytic speed of fit A at f36 is 3.44 m/s.

## Convention check against the prior
For the basketball, with depth 2.24 m at f12 scaled by 1/diameter (`prior_check.py`): the forward difference at f12 is
1.89 m/s, while the 5-frame centred mean of the forward speeds (f10..f14) is 2.26 m/s. The prior is 2.21 m/s. So the
reference seems to smooth over a centred window, and that window includes the oversized step at f11->12.
For f36 the same centred mean (f34..f38) is 3.50-4.07 m/s, depending on the assumed depth just after the bounce, which is
poorly known (`variants.py`). |P38-P34|/4 gives 3.45-4.04 m/s.

## Answer
The physical speed at f36 is about 3.5-3.6 m/s, and the smoothing convention that reproduces the prior gives about 3.5-4.0 m/s.
Answer: **3.65 m/s**. Confidence: moderate, roughly +/-10%. The main uncertainties are the depth scale (one given depth only)
and how the reference's smoothing handles the dropped frame and the bounce.
