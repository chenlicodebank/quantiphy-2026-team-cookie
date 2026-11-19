Ball tracked sub-pixel (HSV mask, verified with SAM 3 masks); lane-plane homography gives u affine in distance along the lane. Quadratic fit of u(t) over pre-impact frames 8-36 gives u''=-0.076 u/s^2 (rms ~1 px). Metric scale k=4.17 m per lane unit from the exact depth prior (9.391 m at t=0.5 s, k=4.07) and the 0.21 m ball diameter (k=4.27). Acceleration = k*|u''| = 0.32 m/s^2; an independent global fit (straight-line trajectory + all image positions + SAM diameters + depth constraint) gives 0.17 m/s^2, so answer 0.30 m/s^2.

Final message:
I measured the ball's motion and answered.

**Method summary:**
- Tracked the blue ball with a sub-pixel HSV mask (verified against SAM 3 masks and half-max edge scans for the silhouette diameter).
- The lane-plane homography makes the lane coordinate `u` affine in true distance along the lane; `u` depends only on image x, so the sub-pixel centroid gives a very clean `u(t)`.
- A quadratic fit over the pre-impact frames (8–36, pins are first hit at frame 40) gives `u'' = -0.076 u/s²` with ~1 px residuals, stable across fit windows.
- Metric scale `k` from the exact depth prior (9.391 m at t=0.5 s → 4.07 m/unit) and from the 0.21 m ball diameter (4.27 m/unit), adopted 4.17 m/unit.
- **Acceleration = 0.30 m/s²** (deceleration), with a second independent global fit (straight-line trajectory + all image positions + SAM diameters + depth constraint) giving 0.17 m/s², bracketing the answer.
