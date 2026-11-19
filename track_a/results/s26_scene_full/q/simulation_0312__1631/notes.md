# Q1631 — average speed of the star, start to end (m/s)

Prior: star height 0.2 m. depth_info: |camera→star| = 6.552 m at t=1 s (frame 24), 8.345 m at t=2 s (frame 48).
question_fps = 24 (file is 24.008 fps; frame indices used, t = frame/24). Answer = mean of per-frame 3D speeds,
frames 1..71 (= path length / (71/24 s)).

## Measurements
- `track.py`: re-segmented the star in every frame (background-difference silhouette near the red core); centroids
  agree with scene/tracks/star.csv to <0.05 px. Principal point assumed (540,540).
- `fit.py`, `fit2.py`, `fit3.py`, `fit4.py`: fitted a smooth 3D trajectory in camera coordinates to the 72 image
  centroids, constrained to reproduce both given distances exactly (they are reproduced to <1 mm).
  - Constant acceleration (quadratic): rms 0.33 px, avg speed 2.113 / 2.098 / 2.071 for f = 1550 / 1600 / 1700 px.
    Free f → 1709 (very flat minimum). Damped-gravity model gives the same (damping → 0).
  - Cubic: rms 0.13 px (residuals of the quadratic are systematic ~0.5 px), avg 2.042 / 2.027 / 2.001 for the same f;
    same with frames 10–71 only (2.029 at f=1600). Quartic: 2.11 (depth profile weakly constrained by the image).
- Focal length: from the 0.2 m height with the star's pixel height/main-axis length at the given-depth frames
  (47–48 px at Z≈6.43 m, 38–39 px at Z≈8.10 m) f ≈ 1510–1580 px; the star is somewhat tilted (foreshortened), so
  that is a lower bound; trajectory fit prefers ~1600–1700. Used f = 1600 px (HFOV ≈ 37°).
- Route 2 (`route2.py`): depth from apparent size (1/size) calibrated to the given depths, back-projected raw centroids:
  1.79–1.99 m/s, but the size-based depths do not reproduce the given depth ratio (6.60/8.28 instead of 6.552/8.345),
  because the tumbling star's apparent size is not ∝ 1/Z — so this route is biased low and given less weight.

## Answer
Mean of the quadratic (2.098) and cubic (2.027) fits at f = 1600 px: **≈ 2.06 m/s**.
Confidence: moderate; model/f spread about ±3% (2.00–2.11), size-based route lower (~1.9).
