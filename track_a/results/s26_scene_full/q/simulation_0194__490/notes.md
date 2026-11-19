# Q490: Callisto model's orbital diameter (m)

The scene is 2D, rendered at 30 fps (the file and the question agree), with a static camera. It shows one planet that does not move and one small moon (Callisto). Callisto moves on a circle around the planet's centre at a constant speed. No other moon is visible in the frame (I checked with a blob search on frames 0, 50 and 99).

## Method (`measure.py`, using `scene/tracks`)
- Planet centre: (958.3, 544.6) px. Callisto's distance from it: mean 412.77 px, range 412.5 to 413.2 px.
- Angular rate from a linear fit of the unwrapped angle: 0.0049267 rad/frame, which is 0.14780 rad/s.
- Pixel speed: 61.07 px/s from the mean of the per-frame steps, and 61.01 px/s from arc speed (ω·r).
- Scale: 0.627 m/s divided by 61.0 px/s.
- Diameter = 2r × scale = 8.476 m using the step speed, and 8.484 m using the arc speed.
- Scale-free check: diameter = 2v/ω = 2 × 0.627 / 0.14780 = 8.484 m. This does not depend on measuring the radius at all.

A free circle fit to the path gives R = 415 px. That is less reliable, because the path covers only a short arc (about 28°). The distance from the planet centre is constant to ±0.4 px, so I used that.

**Answer: 8.48 m.** Confidence is high (about ±1%).
