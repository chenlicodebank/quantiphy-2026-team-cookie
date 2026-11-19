# Q1341 — average speed of the bicycle, f0–f71 (m/s)

File fps is 24, the same as question_fps. 72 frames. Static camera, 3D render.

## Method
- I used the cyclist and van pixel tracks from scene/tracks. The cyclist track was read by hand every 4 frames (±3 px). I spot-checked it on gridded crops at f0, f6, f12 and f18 and it looked consistent.
- Pinhole model with the principal point at the image centre. 3D positions at f14 (t=0.58) and f38 (t=1.58) come from depth_info:
  P = d · unit ray.
- The bike moves in a straight line (projection residual < 9 px over the whole clip). For each frame I took the position s along the 3D line
  A→B whose projection best matches the pixel point. The resulting position vs time is linear, with fitted acceleration ≈ 0.0 m/s², so the speed is
  constant. Average speed = path length of the quadratic-smoothed positions / (71/24 s), which equals the mean per-frame speed.
- Focal length from the prior (white van, a = 4 m/s²): I tracked the van the same way (line between its two given depths) and fitted a quadratic
  to position vs time over f8–71. a = 4 gives f ≈ 1390 (mask centroid as the reference point) to 1790 (bottom point); a mix of the two gives 1480–1580.
  Over f8–60 the fit gives f ≈ 1175–1420. The van's velocity profile is close to linear and starts at about f3–f7.
- Bike speed at these f values: 4.70 (f 1790) to 4.79 (f 1390) for the f8–71 van fits, and 4.85–4.95 for the f8–60 van fits.
  Most of the speed is fixed by the given depths: the radial change alone is 4.41 m in 1 s.

## Checks
- The pedestrian's walking speed at f≈1400 comes out at ≈ 0.97 m/s, which is plausible.
- At f≈1400 the pedestrian is ≈1.3–1.4 m tall and the van is about 0.7 × the size of a real Chevy Express. This fits a scene that is not at real-world
  scale. A real-size van would imply f≈830 (bike ≈ 5.5). That contradicts the prior: the van's acceleration would come out at ≈ 5 m/s².
  I trusted the prior.
- The ground-plane check (horizon y≈88) gives motion that is almost horizontal for all of the f values.

## Answer
4.82 m/s. The plausible range is about 4.7–5.0. Confidence: moderate-high, about ±4%.
