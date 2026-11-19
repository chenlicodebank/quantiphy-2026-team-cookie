Tracked the white paper-airplane/dart across the chalkboard (frames 16-32, background-median subtraction, weighted and binary centroids agreeing <1 px). Local quadratic fits of x(t),y(t) centred on frame 24 (t=1 s) give ax=-805, ay=+2216 px/s^2, |a|=2357 px/s^2 (quartic and Savitzky-Golay second-derivative routes: 2395 and 2370). Scale from the prior: chalkboard outer length 1370 px = 5 m -> 3.650 mm/px, so |a| = 2380 x 0.003650 = 8.7 m/s^2.

Final message:
**Answer: 8.7 m/s²**

Method summary:
- **Object**: the white paper-airplane/dart crossing the chalkboard (the scene record mislabels it "chalk"; the overlay confirmed the shape).
- **Motion**: background-median subtraction + centroid (weighted and binary, three thresholds, all agreeing <1 px) over frames 16–32, where the object is over the dark green board.
- **Acceleration at t=1 s (frame 24)**: local quadratic fits of x(t), y(t) over a 9-frame window centred on frame 24 → ax = −805, ay = +2216 px/s², |a| = 2357 px/s²; quartic fit (2395) and Savitzky–Golay second derivative (2370) confirm → adopted 2380 px/s².
- **Scale**: chalkboard outer length 1370 px = 5 m → 3.650 mm/px (green surface only would give 3.768 mm/px, a 3% difference).
- **Result**: 2380 × 0.003650 ≈ **8.7 m/s²**.

Caveat recorded in notes.md: the method card's "change of scalar speed" reading would give ≈2.9 m/s² at the apex; I report the vector acceleration magnitude, since reference accelerations for uniformly accelerated objects are constants, which only holds for the vector.
