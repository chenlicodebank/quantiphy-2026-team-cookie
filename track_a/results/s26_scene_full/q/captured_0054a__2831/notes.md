# q2831 – orange ball (basketball) displacement 0.5 s → 1.0 s

File fps = question fps = 24, so the frames are 12 and 24.

Method (lab card): f = 0.5959·1280 = 762.8 px, principal point (640, 360). Each centre is back-projected along its pixel ray, scaled
so its Euclidean range equals the given depth (2.3557 m at f12, 1.8100 m at f24). Displacement = |P24 − P12|.

The script is `measure.py`. It uses an HSV orange mask plus a circle fit to the contour (at f24 the ball is cut by the bottom edge, so the fit
ignores border points). The masks were drawn and checked (frames/mask12.png, mask24.png).
- f12: centre (343.7, 603.3), fitted diameter 73 px; scene record (344.0, 605.7)
- f24: centre (585.2, 678.4), fitted diameter 88 px; scene record (585.8, 680.5)
- P12 = (−0.818, 0.671, 2.105) m and P24 = (−0.120, 0.696, 1.667) m, which gives a displacement of **0.824 m**. The record centres and the bbox centre
  give 0.824 and 0.826, so the result does not depend on how the centre is chosen.

Checks:
- Prior check: with depth interpolated linearly, the backward-difference speed at f12 is 2.41 m/s; the prior is 2.21. The f11→f12 pixel step
  is about twice the neighbouring steps, which looks like an irregular frame interval. The neighbouring per-frame speeds are 1.5–1.75 m/s.
- The path length f12→f24, summed from per-frame speeds, is about 0.82 m, the same as the displacement because the motion is nearly straight.

Confidence: good, about ±3%. The main uncertainty is the depth values themselves.
