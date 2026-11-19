Scale from the prior: tire diameter 0.764 m and the given 14.244 m distance to the right-front tire at t=0 fix the pinhole scale (focal length ~1.5-2 kpx, horizon/principal v near 826 from the corridor vanishing point and the size-vs-height consistency of the wheel). I tracked the bright wheel-face blob of the right-front tire frame by frame (centroid u,v and vertical extent h, h proportional to 1/Z) and reconstructed 3D positions p = Z*((u-cx)/f,(v-cy)/f,1) with Z = f*K/h, K calibrated by the t=0 anchor. Speed = |p(i)-p(i-1)|*24 fps. The reliable window (frames 13-24, where the blob is large and clean) gives 10-12.5 m/s; the earlier window (frames 0-13, small blob, threshold-biased) gives ~7-8 m/s, so the car is accelerating through the shot and the speed at t=0.5 s (frame 12) sits near the lower end. Second route: an independent least-squares fit of a straight-line constant/accelerated motion model to the same blob track plus the t=0 anchor gave 7.5-8.5 m/s at frame 12, and a fit to the SAM car-bbox track gave 7.5-7.7 m/s. I take 9.0 m/s (32 km/h, consistent with the garage's 30 km/h sign). Main uncertainty: the wheel-face blob is a lit region rather than the full tire, so the tire/blob size ratio (0.75-1.0) and the exact principal point are only partly constrained, giving roughly +/-25% (about 7-12 m/s).

Final message:
I've submitted the answer. Summary of the work:

**Method**
- Read `scene/notes.md` and `scene/scene.json`: the only moving object is a yellow sports car driving left→right and toward the camera in a parking garage; the camera is static.
- Established the camera geometry: vertical pillar edges are exactly vertical (no roll/pitch), and the corridor vanishing point from the ceiling light strips plus the size-vs-image-height consistency of the wheel both put the horizon/principal row near v≈826.
- Used the prior (tire diameter 0.764 m) and the given 14.244 m distance to the right-front tire at t=0 as the absolute anchor, giving f·K ≈ 950–1050 px·m.
- Tracked the bright wheel-face blob of the right-front tire frame by frame (centroid u, v and vertical extent h ∝ 1/Z) and reconstructed 3D positions p = Z·((u−cx)/f, (v−cy)/f, 1), then took one-frame backward differences × 24 fps.

**Checks**
- Second route: independent least-squares fits of a straight-line motion model (constant and accelerated) to the wheel-blob track and, separately, to the SAM car-bbox track, both anchored at t=0 — they agree at 7.5–8.5 m/s at frame 12.
- The reliable later window (frames 13–24) gives 10–12.5 m/s, the earlier window ~7–8 m/s, i.e. the car is accelerating through the shot, so the value at t = 0.5 s sits near the lower end.

**Answer**: 9 m/s (≈32 km/h), with roughly ±25 % uncertainty dominated by the tire/blob size ratio and the exact principal point.
