# q_1915: length of the truck (m)

The file and the question both run at 120 fps. This is a 2D side view with a static camera, so a single metres-per-pixel scale comes from the prior (the box falls at 9.8 m/s²).

**Scale.** `fit.py` fits a quadratic to the box centre_y from scene/tracks/box.csv, frames 0-58 (before the impact at f60).
- a = 1965 px/s² (centre) and 1963 px/s² (face bottom edge), with residual rms 0.6 px. v0 ≈ 0, so the box starts from rest.
- The fits for frames 5-58 and 10-55 give 1962-1967 px/s².
- The shorter windows (28-58: 1860; 0-40: 2017) are noisier and average out to about the same value.
- Using a = 1963 px/s², the scale is 9.8 / 1963 = 0.004992 m/px.

**Truck.** `truck.py` uses a non-white mask, and the truck is static. Its extent is x 124-1840, which is 1717 px, from the rear tail-lift bracket to the side mirror. The same extent appears at f0, f40 and f199. Around f90 a dark tail-lift flap swings out to x≈20; that is a transient animation and is ignored.
- Length = 1717 × 0.004992 = **8.57 m**.
- Without the mirror (bumper at x≈1812): about 1689 px, or 8.43 m.

**Check.** The box's front face is 410 px, about 2.05 m (a large crate). The wheel radius of about 89 px gives a 0.89 m wheel diameter, which is realistic for a truck wheel. A length of 8.6 m is plausible for a box-body catering truck.

Confidence: moderate-high, with an error of about 3% (from the acceleration fit and from whether the mirror counts).
