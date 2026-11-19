# q_2881 – orange ball (basketball) diameter, cm

Method (lab card): f = 0.5959 x 1280 = 762.8 px. Diameter = depth x pixel diameter / f.
File fps = question fps = 24, so t = 0.5 s is frame 12 and t = 1.0 s is frame 24.

Pixel diameter at frame 12 (measure.py: HSV orange mask, then a circle fitted to the hull; overlay in frames/f12_fit.png):
- hull circle fit 77.4 px, equal-area diameter 75.9 px, bbox 72x78 (slight motion blur along the diagonal)
- scene record: 75.8 px
- the smooth trend over frames 13-20 extrapolates to about 76.4 px at frame 12
- adopted value: 76 px, giving 2.24 x 76 / 762.8 = 0.223 m, so **22.3 cm** (range 22.0-22.7 cm across the estimators)

Checks:
- Soccer ball at t = 2.0 s: about 52 px at 3.254 m gives 22.2 cm, a plausible size-5 ball, so f and the depths are consistent.
- Tennis-like yellow ball at frame 24: 38.9 px across the blur. At 1.235-1.331 m this gives 6.3-6.8 cm, which is plausible.
- The given orange depth at t = 1.0 s (1.81 m) is inconsistent. The ball shrinks from 76 px to 62 px between frames 12 and 24, so it is moving away. A constant size implies a depth of about 2.74-2.81 m, so 1.81 is probably a typo for 2.81. With 1.81 m the result would be 14.7 cm, which is implausible and contradicts t = 0.5. I did not use it.
- Prior velocity (2.21 m/s at 0.5 s): the image-plane speed (~24 px/frame at 2.24 m, about 1.7 m/s) and the depth rate from the shrinking size together give a speed of the same order, roughly 2-2.6 m/s.

Confidence: good (about ±3%).
