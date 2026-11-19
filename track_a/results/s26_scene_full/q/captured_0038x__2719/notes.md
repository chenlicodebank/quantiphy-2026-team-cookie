# q2719 – height of the pink bottle (cm)

The file and the question both run at 24 fps. t = 1.4 s → frame 34. The camera is static and the bottle does not move.
I used a median of frames 0, 5, 10, 34, 40 and 48.

## Method (lab method card)
f = 0.5959 × 1280 = 762.8 px. Depth to the pink bottle = 0.9998 m (depth_info, t = 1.4 s).
- Top edge (measure2.py, sub-pixel half-max per column): about 329.5 px at the centre columns (328.5–329.5).
  It falls to about 331.5 at the sides because the lid corner is rounded.
- Bottom edge: only the left part is visible; the standing card hides the centre. The strongest
  bright→shadow gradient runs from 475.5 at x = 642 to 477.5 at x = 656. That is the bottom ellipse
  (semi-minor axis about 3 px). Extrapolated to the front centre it is about 478; the ellipse centre is about 475.3.
- Pixel height: silhouette 148–148.5 px (scene record: 148). Axis (bottom ellipse centre to top) about 146 px.
- Height = 0.9998 × px / 762.8: 19.47 cm from the silhouette, 19.11 cm from the axis. A pinhole calculation
  with a camera tilt of about 3° (taken from the thickness of the cup-rim ellipse) gives 19.27 cm, and with no
  tilt 19.18 cm. The answer is 19.3 cm.

## Check (second route)
I checked the scale with the prior object, the dark-navy credit card at 0.6867 m. Its visible long side is about
94–96 px along x, which gives 8.46–8.64 cm against the true 8.56 cm (within about 1 %). So f = 763 and the given
depths are consistent.

## Confidence
High: the error is about ±2 % and comes mostly from where the hidden bottom edge lies.
