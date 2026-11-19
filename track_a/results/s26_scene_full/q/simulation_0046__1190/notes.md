# q_1190: average speed of the moving bicycle, 1.0 s to 2.0 s

Question fps 33 = file fps 33. t=1 s -> f33, t=2 s -> f66. Average speed = mean of per-frame speeds f34..f66 = path length f33->f66 / 1 s.

## Scale (3D, pinhole)
- The prior is wheel diameter 0.65 m. I took the **vertical** outer tire diameter, which yaw does not shorten. Script `vert_diam.py`: a column profile through the ring centre from `ellipse_fit.py`, with the half-level crossing at the outer edge of the dark tire, top and bottom.
  - Front wheel: about 95.2 px at f36-45 and 91.4 px at f60-70. That is about 96.4 px at f33 (extrapolated) and 91.2 px at f66.
  - Rear wheel (nearer the camera): about 97.1 px at f33 and 92.7 px at f66.
  - Before f34 the front wheel overlaps the walker, so the f33 values are extrapolated from linear trends.
- The ellipse outer-edge fit (`outer_fit.py`) picked up clutter and gave values that were too large (rear about 98 px). When I checked by eye on zoomed crops, the rear wheel at f66 is about 90-93 px, so I discarded that fit.
- Focal length: f = D_px * Z / 0.65, with Z = depth_info / sqrt(1 + r^2/f^2) and the principal point at the image centre.
  - At t=1 s: f = 1838. At t=2 s: f = 1825, using the mean of the two wheels.
  - The two depths are reproduced to within 0.7%. The measured size ratio is 1.052 against an expected Z ratio of 1.044.
- Position: the bike reference is the hub midpoint (scene/tracks/cyclist.csv, template-tracked, about ±0.5 px), back-projected with the given distance (12.6215 m at f33, 13.2055 m at f66).

## Result
- Displacement f33->f66 is 4.95-4.99 m and ΔZ = 0.545 m. The path length, with depth interpolated linearly, is 4.98-5.02 m. Tracking jitter inflates the path slightly; the motion is straight.
- Variants:
  - front wheel only: 4.97-5.06
  - rear wheel only: 4.94-4.98
- **Answer: 4.98 m/s.**
- Second route: calibrating at t=1 alone gives 4.95/4.98 (disp/path), and at t=2 alone gives 4.99/5.02. These agree within about 1%.
- Confidence: about ±3%. The main uncertainty is the 1-2 px wheel-edge definition (1 px is about 1.1%).
