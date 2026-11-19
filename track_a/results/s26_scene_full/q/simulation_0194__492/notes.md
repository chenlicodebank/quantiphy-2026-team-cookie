# Q492: diameter of the Jupiter model

This is a 2D scene with a static camera, rendered at 30 fps (the file's fps matches question_fps). The frame shows one planet, Jupiter, which stays still at (958.3, 544.6). One small moon orbits it, and it is the only moon in view. A blob search outside the planet disk at frames 0, 50 and 99 found nothing else. So this moon is the outermost one, Callisto, the object of the prior.

## Measurements (measure.py)
- Callisto moves on a circle of radius 412.7 px around the planet centre, at a steady angular rate of 0.004927 rad/frame.
  - Speed from arc length: 2.0336 px/frame, or 61.01 px/s.
  - Second route: the mean per-frame step is 2.0355 px/frame, which agrees to 0.1%. It is slightly higher because of centroid noise.
- Scale: 0.627 / 61.01 = 0.010277 m/px.
- Jupiter's diameter:
  - The circle fit in the record gives 167.5 px (range 167.3-167.9).
  - My own threshold profiles give 168-169 px horizontally and 166 px vertically.
  - I use 167.5 px.
- Diameter = 167.5 × 0.010277 = **1.721 m**. Using the profile range instead gives 1.706-1.737 m.

## Confidence
High. The motion is uniform and the planet's rim is sharp. The estimated error is about 1%.
