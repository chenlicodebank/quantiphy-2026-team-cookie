# q2833 – soccer ball diameter (captured_0054a, lab, 24 fps = question_fps, 1280x720, f = 763 px)

Answer: **15.6 cm**

## Problem
depth_info gives no distance for the soccer ball (orange = basketball at t=0.5/1.0; "white"/"green" balls are the two
balls thrown by the standing person, ~3.05 m away). The soccer ball rests on the floor under the seated person's left
hand f0-23 (then rolls away, blurred). So its range was found from the floor plane, which comes from the basketball
(rolling on the same floor, with given ranges at f12 and f24).

## Measurements (scripts in this folder)
- `rayfit.py`: edge points along rays from the centre (max gradient; grey level for the soccer ball, R-B for the
  orange ball), then a fit of the sphere-projection ellipse with its orientation and axis ratio set by the pinhole geometry
  (major axis radial, major/minor = 1/cos(alpha)). Free parameters: centre and minor axis. True angular radius:
  tan(rho) = minor*cos(alpha)/(2f). `checks.py` confirms this formula on a simulated sphere (70.33 vs 70.35 px). The naive
  d*px/f would be ~20 % too large this far off-axis (alpha = 35 deg for the soccer ball). The wall seams are straight, so lens distortion is negligible.
- Soccer ball (`soccer_size.py`, frames 0-16, very stable): centre (158.8, 604.8), minor axis 53.66 px (range 53.4-54.1).
  Overlay frames/soc_fit_*.png: fits the left, bottom and right edges; the top is under the hand and is excluded.
- Basketball (`bball.py`, `bb24.py`): f12 minor 72.81 px at (344.7, 605.7). For blurred frames only edges normal to the
  motion were used. f24 centre (586.3, 683.2) (cut by the bottom edge). Rest f0-4: 61.5 px at (241.4, 575).
  Basketball D = 2*2.3557*sin(rho) = 20.06 cm. Check: the predicted f24 size from the given 1.81 m is 92.1 px; measured 90.2 px (blurred).
- Record scene/ soccer track (66 px) includes shadow; replaced by the fit above.

## Floor plane and soccer range (`geom.py`, `floorfit.py`)
Basketball centres = range x unit ray (given ranges at f12/f24; for other frames, range from its size with D_b).
These lie at height r_b above the floor. I scanned pitch with roll fixed to 0 or ±1 deg (the path is nearly a line, so roll
is not observable from it, and wall verticals show roll < 1 deg). The soccer range then solves d*(g.u + sin(rho)) = H.
| variant | pitch | soccer range | D |
|---|---|---|---|
| anchors f12+f24 only, roll 0 | 3.5 deg | 2.662 m | 15.28 cm |
| all frames, roll 0 | 0.0 deg | 2.744 m | 15.75 cm |
| rest+f12+f24, roll 0 | -0.2 deg | 2.746 m | 15.76 cm |
| rolling 10-24, roll 0 | 1.25 deg | 2.720 m | 15.61 cm |
| roll ±1 deg variants | | 2.64-2.77 m | 15.1-15.9 cm |
The soccer range barely depends on pitch, because the soccer ball sits next to the basketball's rest and f12 positions.

## Checks
- Prior: the basketball's 3D speed at t=0.5 from the size/depth track: (f14-f10)/4 frames gives 2.35 m/s and (f13-f11)/2 gives 2.04 m/s,
  consistent with 2.21 m/s, so the metric scale agrees with the prior.
- Ratio route: the soccer ball looks smaller than the basketball while sitting slightly closer; D_soccer/D_basketball ~0.78.
  The physical sizes are plausible: a mini (size-1 class, ~15 cm) soccer ball and a small youth basketball (~20 cm).
- If the naive no-cos(alpha) convention were used, the answer would be ~18.6 cm. I reject it because it is not the physical size.

Confidence: moderate-good; spread over variants ±3 %, plus edge/blur systematics ~±4 %.
