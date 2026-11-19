# Q1591 – width of the table (desk), simulation_0209

Answer: **1.06 m**. This is the desk top's short horizontal extent, front to back. The long side is about 2.4 m.

File fps = question fps = 24, so frame = round(t*24).

## Camera (pinhole, principal point at the image centre (1062, 540))
- `lsd.py` and `vps.py`: straight-line segments from frame 0, grouped into three orthogonal vanishing points.
  - Vertical: about 20 pedestal/leg edges, VP (1062, 11679).
  - Long axis: the desk's front and back top edges.
  - Short axis: the right silhouette edge and the left lip edges.
  - The three VP pairs give f = 2658, 2627 and 2626 px. The orthocentre (1088, 536) sits next to the image centre.
  - Roll is 0.0°. Tilt is 13.4° whether taken from the vertical VP or from the horizon at f ≈ 2640.
- `fit.py`: free-fall route. I put the typewriter's origin at bbox-centre pixels (frames 2-9) on a vertical world line
  starting at the frame-0 point at depth 4.32 m, and fitted s(t) = s0 + v0 t + ½ a t² with a fixed at 9.8 m/s².
  - At 13.4° tilt this gives f ≈ 2550 px. Different frame windows give 2470-2560.
  - The bottom edge of the box accelerates faster than its centre and the top edge slower, so this route is uncertain
    by ±4%.
  - With the VP camera, the fitted acceleration is 9.44 instead of 9.8 (4% off).
- I used **f ≈ 2600 px (range 2550-2640) and tilt 13.4° (range 13.1-13.7°)**.
- Landing-depth route: matching depth 4.501 m at t = 0.5 s (frame 12) to a point on the fall line would need a 15.6°
  tilt. I rejected it because the vertical VP, the horizon and the 90° far corner all reject it. At frame 12 the
  typewriter is rocking, so its origin is a few cm behind the fall line; the VP camera predicts 4.46 m.
- Plausibility check: the typewriter's resting origin comes out about 7 cm above the desk top, which fits a centred
  origin.

## Desk top plane and width (`silh.py`, `width.py`, `combo.py`)
- Desk plane: the horizontal plane through the revolver origin, at 4.704 m along its pixel ray (1448, 625).
- Desk silhouette against the wall, edges fitted with rms 0.4 px:
  - back edge y = -0.1424x + 751.8
  - right edge y = 0.303x + 39.9
  - far corner B = (1598.5, 524.4)
  - front-right corner on the right-edge line at x = 1998
- Width = 3D distance B to FR on the plane:
  - f 2640, tilt 13.4°: 1.046 m (corner angle at B 89.5°)
  - f 2550, tilt 13.4°: 1.078 m
  - f 2600, tilt 13.2-13.4°: 1.06-1.07 m
  - If the revolver origin is 1-2 cm above the leather, width rises by +0.6 to +1.6%.
- Second-route check: with the chosen camera, the 4th corner predicted as L + (FR - B) projects to (693, 890). The
  front-left corner seen in the image is at about (698, 885). The rectangle closes, so the tilt and scale are
  consistent.

## Confidence
Moderate, about ±5%. Width changes by about 0.05 m per degree of tilt and by about 1.2% per 1% in f. The two f routes
(VPs 2640, fall 2550) differ by 3.5%.
