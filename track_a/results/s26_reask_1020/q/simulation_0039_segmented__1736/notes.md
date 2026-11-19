# q1736: height of the person (m). Answer: 1.67 m

File is 25 fps with duplicate frames 1, 26, 51 (a 24 fps render resampled to 25 fps); question_fps = 24.
Render frame k = video frame ceil(25k/24), so t=1 s -> video frame 25 and t=2 s -> video frame 50.

## Scale and camera (geom.py)
- Prior: boat speed 4 m/s. Boat origin = scene/ track ref point (rigid template shift), video frames 25 and 50,
  depths 177.2077 / 177.9993 m. Solved f so that |P2 - P1| = 4 m over that 1 s: **f = 9070 px** (HFOV 9.7 deg).
  The result is insensitive to the absolute boat reference point (+-30 px changes f by 0.02%).
- The camera has no roll: the mast and the person's body show up vertical in the image. The boat's velocity is
  horizontal, so the camera pitch is atan(-v_y/v_z) = **54.4 deg below the horizon**. The ray to the person is
  depressed beta = 53.3-53.8 deg.
- Check: the person's image speed is ~52 px/s, about 1.05 m/s perpendicular to the ray. Walking toward the camera on
  the ground, that gives a ground speed of 1.05/sin(beta) = 1.31 m/s, a normal walking speed. Its given distance
  barely changes (+0.09 m/s), so the character's origin is ~static, as described in the instructions.

## Person extent (person.py, prof.py)
- Mask = darkness (255 - min channel) > 30, the largest component, measured per frame. The vertical image extent
  oscillates with the stride between 54 and 72 px. The minima (mid-stance, feet together) are 57 / 54 / 55 px
  at frames 36 / 54 / 71. Using thresholds of 15 or 60 changes these by about 1 px. Used L = 55.5 px.
- Body distance ~182.5 m (the origin is at 183 m; the body walks toward the camera), so L = 1.117 m
  perpendicular to the ray.
- Model: L = H cos(beta) + head-silhouette excess (~0.036 m; for an ellipsoid head the top of the silhouette lies
  above the crown's projection) + toe-forward offset (~0.12 m) x sin(beta).
  So H = (1.117 - 0.036 - 0.097) / 0.593 = 1.66 m. Rounded up slightly to 1.67 m because walking posture is a
  little shorter than standing height.
- Sensitivity: toe offset 0.08-0.16 m gives 1.60-1.72 m; pitch +-1 deg gives about +-0.03 m.

## Confidence
Moderate (about +-5%). The scale is solid: f comes from the prior, and the walking-speed check gives 1.31 m/s.
The main uncertainty is the foreshortening model for a person seen from about 54 deg above the horizon.
