# q 868: acceleration of the tennis ball at t = 1 s (frame 24)

Prior: ball diameter = 0.17 m. No depth_info. fps = question_fps = 24, so t = 1 s is frame 24.
The ball rolls down the straight ramp from frame 19 to frame 47, so frame 24 lies well inside the uniformly accelerating phase.

## Key finding: perspective, not a constant pixel acceleration
- A plain quadratic fit of the arc length (frames 19-47) gives 713 px/s², but the residual is 1.75 px rms and is systematic. The local pixel acceleration falls from about 870 px/s² (frames 20-28) to about 640 px/s² (frames 30-47).
- The ball's silhouette diameter shrinks from about 25.5 px (frames 20-25) to about 23.7 px (frames 40-47), a ratio of 0.93 (`diam2.py`, background difference against frame 5). The ramp strip narrows by the same ratio, 0.93, over the same x range (edge fits in scene/static_geom). So the ball moves away from the camera as it descends, by about 7%.
- Model (`fitproj.py`): a 1D projective map of a uniformly accelerated 3D line motion.
  sigma(t) = s1 + q/(1 + k q), with q = v(t-1) + a(t-1)²/2, where q is measured in local pixels at t = 1.
  - Fit: a_q = 920.8 ± 4.7 px/s², k = 5.23e-5 /px, residual 0.20 px rms.
  - The predicted depth ratio Z(f47)/Z(f24) = 1.070.
- Independent checks of k:
  - Diameter trend: 6.4e-5 to 7.3e-5.
  - Vanishing point of the two ramp edges: 1/|VP − ball| = 5.0e-5. The VP predicted by the fit, (14171, 13475), is close to the edge VP, (14792, 14089).
  - Fixing k = 5.0e-5 gives a_q = 911 px/s².

## Scale
- Ball diameter at t = 1, with the k-trend removed:
  - steepest-edge method: 25.0 px
  - half-level method: 25.4 px
  - D1 = 25.2 px is used. The HSV mask in scene/ gives 24.4 px, but it misses the dark limb.
- Line-direction factor λ = 1/sqrt(|kΔ + ê|² + (k f)²), where Δ is the ball's offset from the image centre. It depends only weakly on the focal length f:
  - f = 1000–4000 px gives λ = 1.033–1.011.
  - λ = 1.024 is used, for f ≈ 2667 px (the Blender default 50 mm lens on a 36 mm sensor).
  - The implied ramp descent is about 43.8°.
- a = a_q × 0.17/(D1 × λ) = 920.8 × 0.17/(25.2 × 1.024) = **6.07 m/s²**.

## Second route (`check.py`)
- The projective map was undone per frame, then backward-difference speeds and accelerations were computed per frame.
- Per-frame accelerations have mean 915 px/s² (median 906), roughly constant across the ramp. A linear fit of the per-frame speeds gives 920.8 px/s².
- Both agree with the model fit. In metres this is 6.0–6.1 m/s².

## Confidence
- Main uncertainties:
  - pixel diameter: about ±2%
  - unknown focal length: about ±2%, more only for a very narrow field of view
  - k: about ±1%
- Estimate: 6.07 m/s², about ±4%.
- Physical sanity check: g·sin 43.8° = 6.79 m/s² (frictionless) and 4.85 m/s² (rolling solid sphere). 6.07 m/s² lies between the two, which is plausible for a Bullet rigid body.
