# Q399 – speed of the police car at 1 s (m/s)

Prior: bike speed = 5.52 m/s. 2D top-down render, static camera, 24 fps (file fps = question fps). Both the car and
the cyclist move along +x in the same lane, with the road plane parallel to the image, so one m/px scale applies.

Scale from the prior: cyclist pixel speed. The bike moves at a constant mean speed; the rider point oscillates
13-15.8 px/frame because of pedalling.
- Record track (pelvis chain): linear fit 14.415 px/f, mean per-frame 14.44, net (f0→f79) 14.42.
- My own check (check_cyc.py), long-baseline template matching of the whole rider and the front crate:
  14.37-14.69 px/f, typically ≈14.45 (0→79: 14.46 / 14.45).
- Used 14.44 px/f → 5.52 / (14.44·24) = 0.01593 m/px.

Police car: constant speed. Record track 18.046 px/f, per-frame scatter ±0.15, so speed at frame 24 equals the
constant. My rear-template check gives 18.14-18.17 px/f; part of this is the perspective difference between features
at different heights (~0.5%). Used 18.08 px/f.

Speed = 5.52 × 18.08 / 14.44 = 6.91 m/s (range 6.88-6.95 across routes).
Confidence: high (about ±1%).
