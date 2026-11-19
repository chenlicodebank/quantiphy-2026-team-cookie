# Q1883: acceleration of the astronaut at t = 0.5 s (m/s^2)

Time base: the file and the question are both 24 fps, so t = 0.5 s is frame 12 and acc = (speed12 - speed11) x 24.

## Where the candidates part ways
All the candidates use about the same focal length (f ≈ 3134 px from bbox_h = 380 px at f24, H = 2.2 m and Z = 18.147 m).
They differ in the **depth model and the fit window**:
- C1, C2 and C6 (0.25, 0.35 and 0.57) take depth from a rigid part (the backpack). That depth is almost constant over
  f0-14, and they fit only inside the first motion segment (f0-14).
- C3 and C4 (2.2 and 6.5) take depth from the per-frame bbox_h, which is pose-dependent, and/or fit windows that run
  across the abrupt kink at f14→15, where the image speed jumps from about 11 to 20-30 px/frame. A fit across that
  kink pulls the later speed-up back into f12, which is why they get large positive values.
- C5 (1.1) averages the centroid and head-top tracks, which are noisy and pose-affected.

## My measurement
- `track_ecc.py`: affine ECC registration of a rigid backpack and helmet patch (f12 region x705-790, y668-830), tracked
  from f12 out to f0-16, with cc 0.95-1.0. The image steps over f1-14 are smooth:
  - dx is about 10 → 10.9 px/frame;
  - dy is 7.3 → 1.6 px/frame;
  - the image speed falls from 12.7 to a plateau of 10.9-11.0 px/frame over f10-14.
  The kink at f15 lies outside every window I used.
- Depth: the patch scale (det of the affine map) is about 1.00 over f6-14. C1's backpack height is constant (168 px)
  over f0-22. Both say the depth is roughly constant near f12: Z ≈ 18.4 m from the backpack, or 20.1 m from bbox_h.
- `accel.py`: back-projection with f = 3134 px. I tried Z = 18.4 or 20.1 m, with depth trends of ±0.01 m/frame.
  - Speed at f12 is about 1.54-1.69 m/s, a plausible walking pace.
  - The raw one-frame acc12 is -0.27 to -0.31 m/s^2.
  - Quadratic and cubic fits over windows f1/3/5/7 to f14 give -0.20 to -0.32 m/s^2.

## Second route
The image-plane speed alone gives the same result: it changes from 11.00 to 10.92 px/frame at f11→12. At 0.0059 m/px
this is about -0.27 m/s^2. It agrees with the 3D fits. C6 argues the focal length should be about 5 pct higher,
because the walking pose is shorter than rest height; that would lower the value by about 5 pct.

## Answer
The scalar speed is slightly decreasing, at a ≈ -0.27 ± 0.05 m/s^2. I report the magnitude, **0.28 m/s^2**. This
agrees with C1 and C2. I reject C3 and C4, whose fits cross the f14/15 kink and use pose-driven bbox depth.
Confidence: low-moderate. The true value is near zero, so the relative error can be large. The camera cannot be checked
(the background has been removed), so I assumed it is fixed.
