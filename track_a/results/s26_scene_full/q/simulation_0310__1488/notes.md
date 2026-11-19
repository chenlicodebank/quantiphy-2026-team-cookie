# q_1488 – speed of the forklift at t = 1.0 s (frame 24, question_fps = file fps = 24)

Answer: **2.06 m/s** (one-frame backward difference, frame 23 -> 24).

## Method
1. **KLT tracks** (`klt.py`, `vp.py`): about 190 rigid body points on the forklift, tracked through frames 0-71. They form straight
   image lines (max residual < 1 px) that meet at the motion vanishing point VP_d = (-2018, -799) ± (13, 6) px. The forks' edges
   (`forks.py`) point at the same VP, so the vehicle drives straight along its own axis, a pure translation.
2. **Camera** (`strip.py`): the rear roof edge (reflector strip) is perpendicular to the direction of travel. Its line at 7 frames
   (0…71) passes through one point, VP_p ≈ (5740, -800), which lies on the horizon row of VP_d, so the camera roll is 0. With the
   orthogonal-VP relation and the principal point at the centre, f = 3475–3553 px, mean ≈ 3515 px (HFOV about 40°), and the tilt is
   23.4° down. Check: the vertical vanishing point implied by the two pine trunks gives f ≈ 3610 and 3700 (rough, natural trunks).
3. **Motion profile** (`profile.py`): for a translating body, each point's camera depth ratio Z(t)/Z(24) = |x24-VP|/|x(t)-VP|.
   This gives the travelled distance s(t) up to scale. The normalised s(t) is an exact parabola from rest at frame ≈ 0.03
   (rms 5e-5), so the acceleration is uniform. The 23->24 step is 0.02718 of the 24->48 travel ds.
4. **Metric scale** ds = 3D travel from frame 24 to 48:
   - Height prior (`recon.py`, `height.py`): reconstruct the points up to scale (Z = dz/k). The roof/strip top is 0.784 ds above
     the ground. The ground is the rear-wheel hub minus the tyre radius; the tyre is 73 px, fitted from its ellipse in the image,
     with axis ratio 1.19 measured against 1.22 predicted. 2.47 m / 0.784 gives **ds = 3.149 m** (tyre radius 0.32 m, camera
     height 8.56 m).
   - depth_info (`origins2.py`): with the origin at the 3D bbox centre of the reconstructed vehicle, D24 gives ds = 3.131 and D48
     gives ds = 3.176. With the origin at the mean of the tracked points, ds = 3.196.
   - Sensitivity to f: at f = 3300 / 3700 the height route gives 3.085 / 3.208 and the depth route 3.30 / 3.12. The two routes
     cross near f ≈ 3600, at ds ≈ 3.16.
   - I used ds = 3.16 m.
5. Speed(24) = ds × 0.02718 × 24 = 0.652 × 3.16 = **2.06 m/s**. This is the same as a uniform acceleration a = ds/1.5 ≈ 2.1 m/s²
   from rest at t = 0, for which the backward difference gives 2.1 × 23.5/24 ≈ 2.06 m/s.

## Checks and caveats
- The depth ratio D48/D24 = 1.1371 is slightly larger than the ratio of any tracked point (≤ 1.131 at f = 3515). Using the ratio
  alone would give ds ≈ 3.6 (speed ≈ 2.35 m/s), but that is very sensitive to sub-percent depth errors. The absolute D24 and D48
  each agree with the height scale to within about 1.5%, so I trusted the absolute values rather than the ratio.
- scene/ record: the orange centroid is not a fixed body point. I used the KLT body points for the motion and the record's bbox
  only for search windows.
- Confidence: moderate to good. Uncertainty is about ±3% from the scale (ds 3.13–3.20 gives 2.04–2.09 m/s).
