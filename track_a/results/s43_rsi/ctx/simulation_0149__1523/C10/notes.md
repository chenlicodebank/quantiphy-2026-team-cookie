3D reconstruction of the yellow car: depth from the car's silhouette height (Z = C/h) anchored at the given t=0 tire distance 14.244 m (car centre ~13.55 m), lateral from the bbox-centre column with f ~1.35 kpx obtained from the 0.764 m tire's pixel size at frame 27; global robust fits of X(t),Z(t) over five frame windows give a speed of 9.3-9.6 m/s at t=0.5 s and a change of scalar speed of -4.3 m/s^2 (windows: -4.29,-4.00,-3.56,-4.62,-5.24). Second route (3-point Z(t) fit + lateral speed) gives |a| ~3-3.5 m/s^2, same order. The car is braking as it passes the camera.

Final message:
I measured the car's 3D trajectory and its acceleration at t = 0.5 s.

**Method**
- Confirmed the scene geometry: static camera, car driving left→right and toward the camera, showing its right flank, so the visible front wheel is the named "right front tire" (depth 14.244 m at t=0).
- Anchored the metric scale on the given tire depth (car centre ≈ 13.55 m at t=0) and on the 0.764 m tire diameter, which gave f ≈ 1.35 kpx (consistent with the car's derived body height of ~1.37 m).
- Reconstructed Z(t) from the car's silhouette height and X(t) from its image column, then fitted X(t), Z(t) with constant-acceleration models over five independent frame windows.

**Result**
- Speed at t = 0.5 s: 9.3–9.6 m/s (very stable across windows).
- Acceleration at t = 0.5 s: −4.3 m/s² (windows: −4.29, −4.00, −3.56, −4.62, −5.24); the car is braking as it passes the camera. A second, independent 3-point route gives |a| ≈ 3–3.5 m/s², the same order.

**Answer: 4.3 m/s²** (notes.md written with the full method, checks and confidence).
