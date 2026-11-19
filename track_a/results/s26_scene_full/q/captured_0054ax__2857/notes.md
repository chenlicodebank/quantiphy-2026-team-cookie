# q_2857 – white ball diameter (cm)

File fps = question fps = 24; t=1.0 s -> frame 24.

## Identification
At t=1.0 (f24) the depth_info gives white ball 3.0735 m and green ball 3.039 m, which matches the
two small balls the standing person (far, centre) throws. The soccer ball sits at the nearer crouching
person, and the basketball is the orange ball (1.81 m at t=1.0). The "white" ball is the pale
grey/whitish small ball (scene/ calls it `pink_ball`), at (569,271) in f24. The "green" ball is the
yellow tennis-type ball (`yellow_ball`).

## Method (lab method card)
f = 0.5959 x 1280 = 762.8 px. Size = Z x pixel diameter / f, with Z = 3.0735 m.
Pixel diameter comes from a soft alpha mask (background is pure green; alpha from G - max(R,B)), in
measure.py and measure2.py:
- f24: across-motion (minor-axis, second-moment) diameter 17.4 px -> 7.03 cm; area-equivalent
  19.3 px -> 7.78 cm (inflated by motion blur).
- f25 (nearly round, least blur): 18.1-18.4 px -> 7.3-7.4 cm. The ball is moving slightly toward the
  camera, so the depth there is a bit below 3.07 m.
- f26-29: 19.0-19.5 px. The apparent size grows as the ball flies toward the nearer crouching person,
  and no depth is given for those frames.
Adopted: about 18.0 px at 3.0735 m -> **7.2 cm**.

## Second route / sanity check
The green (yellow) ball, measured the same way at its given depth of 3.039 m (f25-28, minor axis
18.0-18.5 px), gives 7.2-7.4 cm. A real tennis ball is 6.7 cm, so the method reads at most about 5-8 %
high here; part of that is because those frames come after t=1.0. The two small balls have nearly the
same pixel size, so a white ball of about 7 cm is consistent.

Confidence: moderate, about ±5-8 %. The ball is only about 18 px across, so a 1 px error is about 5 %.
