# Q489 — orbital diameter of Callisto (m)

Prior: Callisto speed = 0.627 m/s. 2D scene (pole-on Jupiter, moons on circular orbits in the image plane), file fps = question fps = 30.

Method (measure.py, measure2.py):
- Callisto track from scene/tracks/callisto.csv (checked: re-measured centroids at frames 33/66/99 agree within 0.2 px;
  at frame 0 my quick crop was pulled by the "Callisto" text label, the track is on the moon as the zoomed frame shows).
- Orbit centre fixed at the common centre of all moon orbits (958.45, 542.72); the free circle fit on Callisto's 28° arc alone
  isn't well constrained (gives R=408), so I didn't use it.
- R = 414.14 ± 0.20 px (drawn orbit line 414.47 px). Angular speed 8.434 deg/s, giving a model speed of 60.96 px/s; the mean of the per-frame speeds is 61.09 px/s.
- Scale = 0.627 / 60.96 = 0.010285 m/px, so the diameter is 2 × 414.14 × 0.010285 = **8.52 m**.

Second route: D = 2v/ω = 2 × 0.627 / 0.14720 rad/s = 8.519 m (no pixel radius needed). Using the mean raw speed gives 8.50 m;
using the orbit-line centre gives 8.55 m. Spread is under 0.6 %.

Confidence: high (about ±1 %).
