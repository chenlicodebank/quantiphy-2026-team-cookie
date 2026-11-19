# q_1153 — height of the person (simulation_0037)

Prior: person walks at 1.3 m/s. depth_info: 122.8569 m (t=1 s), 122.8588 m (t=2 s), so the distance changes by only 2 mm in 1 s.
The file and question both run at 24 fps.

## Geometry
- The camera is static (per scene record). One person walks left to right, about 1.70 px/frame in x and +0.12 px/frame in y.
- The walk is close to parallel to the image plane:
  - The given distance is nearly constant. Either the origin stays put, or the walk is perpendicular to the line of sight. The person is only a few degrees off the optical axis, because a ~1.8 m person is 59 px tall at 123 m, which gives f ≈ 4000 px.
  - The apparent height drifts by at most about 3 px with no consistent sign: the feet move down while the height shrinks slightly. That is gait and mask noise, not a real depth change. A depth change big enough to matter would also make the speed inconsistent.
- So one metres-per-pixel scale at the person's depth comes from the prior speed.

## Measurements (measure.py, analyze.py, my_track.csv)
- Mask: difference from the temporal median over a crop. The wet-sand reflection is cut at the lowest row that has dark (jeans/shoe) pixels. 4 of 72 frames where the reflection leaked in were dropped (68 clean frames).
- Pixel speed: linear fit of the upper-body centroid x gives 1.703 px/frame. Adding the vertical drift of 0.123 px/frame gives 40.98 px/s. Scale = 1.3 / 40.98 = 0.03172 m/px.
- Height from head top to sole, over the clean frames:
  - median 59.0 px, mean 59.06 px, 75th percentile 60 px
  - with a sub-pixel half-max head top: median 58.4 px

## Result
- Height ≈ 59 px × 0.03172 m/px = 1.87 m.
- Range: 1.85 m (sub-pixel top) to 1.90 m (75th-percentile, near-full-stance height).
- Answer: 1.87 m.

## Check
- The scene record measured independently (median 57 px, 1.712 px/frame), which gives 57 / 41.1 × 1.3 = 1.80 m. Its threshold mask clips the pale head slightly.
- Both routes give an adult between 1.80 and 1.90 m, which is plausible.
- Confidence: moderate, about ±4%. The main uncertainty is the blurry head and shoe edges (±1–2 px out of 59 px).
