Tracked the car's near front wheel/rim (SAM + rim blob) over frames 8-31. Camera calibrated from the scene: horizon v=828-830 (light-strip VP and bollard-line VP agree) and camera height = wheel-centre height 0.382 m. Rim apparent height gives 1/h = 0.013316-0.0062566 t, lateral (u-960)/h = -13.512+10.974 t. Scale fixed by the prior+anchor: near front tire depth at t=0 = 14.244 m minus the ~1.0 m near/far track-width offset = 13.2 m, giving K=f*D_rim=990 and f=1924 px from the car's 1.23 m height. At frame 12: dZ/dt=-6.19 m/s, dX/dt=5.65 m/s -> 8.4 m/s. Second route: straight-line path t=0 to frame 31 gives 8.0 m/s average, and the background-subtracted car-height depth rate gives ~8.0 m/s. Answer 8.2 m/s (=30 km/h, matching the '30' sign in the scene).

Final message:
**Answer: 8.2 m/s** (question 1522 — speed of the yellow car at t = 0.5 s).

Method summary:
- **Camera calibration from the scene itself**: the horizon row (v ≈ 828–830) came from two independent vanishing-point fits (ceiling light strips → (4048, 828); bollard top/bottom lines → (3877, 828)). The wheel/rim centre row stays constant at ~830 while the car's apparent size doubles, which forces the camera height to equal the wheel-centre height (0.382 m = tire radius).
- **Tracked the near front wheel** with SAM and its silver rim by colour, giving a clean depth signal: 1/h = 0.013316 − 0.0062566·t and (u−960)/h = −13.512 + 10.974·t.
- **Scale** from the prior (0.764 m tire) + depth anchor (14.244 m to the *far* right front tire at t=0, corrected by the ~1.0 m track-width offset), giving K = f·D_rim = 990 and f ≈ 1924 px (checked against the car's 1.23 m height).
- At frame 12: dZ/dt = −6.19 m/s, dX/dt = 5.65 m/s → 8.4 m/s.
- **Second route**: straight-line path from t=0 to frame 31 gives 8.0 m/s average; the background-subtracted car-height depth rate gives ~8.0 m/s. Final 8.2 m/s, which is 30 km/h — matching the "30" speed-limit sign in the scene.
