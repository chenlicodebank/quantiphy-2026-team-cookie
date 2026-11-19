# q1057 – average speed of bird, 0.5–1.0 s (m/s)

File fps 22.892, question_fps 24 used for time: t=0.5 → frame 12, t=1.0 → frame 24. Average speed = mean of
per-frame speeds at frames 13..24 × 24.

Track: scene/tracks/bird.csv (mask centroid and body centroid), checked on crops (frames/crops.png, len_*.png):
mask covers the whole bird, no occlusion in frames 0–38.

Scale (3D pinhole, principal point at image centre): depth linear in frame between 34.584 m (f0) and 33.999 m (f24).
Focal from bird length 1.19 m = beak-to-tail in wings-level frames (wings point toward the camera, so the image
length is the body length; bird flies ~perpendicular to the view ray, foreshortening ≈ 1):
bbox widths f1 152, f2 172, f19 157, f36 168, f44 170 px → f ≈ 4530–5120, median ≈ 4560 px (read-off beak–tail
lengths from overlays give ~4470). Uncertainty in f ≈ ±5 %.

Results (measure.py, f = 4560): mean per-frame 3D speed f13–24: centroid raw 4.09, smoothed(3) 4.05,
smoothed(9) 3.98; body centroid raw 4.14, smoothed(3) 4.08, smoothed(9) 3.99. Second route: net displacement
f12→f24 / 0.5 s = 3.95–3.99 m/s. The bird is accelerating (0–1 s average ≈ 3.2 m/s).
Answer 4.03 m/s (between the smooth-path and wobble-including values). Confidence: moderate (±7 %), dominated by focal.
