# q 1856 — speed of the blue car at t = 1.5 s

- question_fps = file fps = 24, so t = 1.5 s is frame 36. Speed = |p(36) - p(35)| x 24 (one-frame backward difference).
- 2D side-view scene with a static camera and one object (the light-blue cart). There is a single px->m scale from the prior: tyre diameter = 0.369 m.

## Tyre pixel diameter (measure_tire.py, SAM 3)
- My own measurement (dark-pixel extent through the front hub, frames 30–40): horizontal 108–113 px (111 at frame 36), vertical 109–111 px.
  - The rear-tyre dark extent (133 px) includes the dark wheel arch, so I rejected it.
- SAM 3 "tire" masks:
  - frame 35: boxes 108.8 x 108.9 and 109.8 x 110.6;
  - frame 36: 110.0 x 109.0 and 110.6 x 107.7.
  - The overlay (frames/seg_00_f36.jpg) outlines both tyres cleanly.
- Scene record: about 112 px (113 horizontal / 111 vertical, frame 30).
- All of these agree within 3 %. Median D = 110.0 px, giving a scale of 0.003355 m/px.

## Displacement from frame 35 to 36
- Template tracks (scene/tracks/cart.csv): front hub 47.54, rear hub 47.96, white sill marker 48.08 px.
- Second route, SAM 3 tyre-mask centroids: front 1160.8 -> 1208.7 = 47.9 and rear 827.1 -> 875.0 = 47.9 px.
- The SAM whole-car centroid (+54 px) is not usable, because the mask area changes by 5 % between the two frames.
- Mean of the tracks and SAM tyre centroids: 47.88 px/frame, which is 1149 px/s. Motion is horizontal only.

## Result
v = 47.88 x 24 x 0.003355 = 3.85 m/s.
Sensitivity: D = 112 px gives 3.79 m/s. Confidence: good, about ±3 %, limited mainly by the tyre pixel diameter.
