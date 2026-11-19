# q1165 – boat speed at t=1.0 s (frame 24, question_fps 24 = file fps)

Method (measure.py): tracks from scene/ (bird = eagle centroid, boat = hull centroid, cx_ref/cy_ref), checked on
frame 24 (eagle at ~(368,461), boat hull centred ~(385,955)). Pinhole camera, principal point at image centre,
depths linearly interpolated between the given t=1 and t=2 values; points back-projected as unit ray x depth.
Focal length fitted so the eagle's mean 3D per-frame speed = 11.84 m/s: f = 6232-6296 px depending on window
(frame 24 only, 22-26, 20-28, 12-36, 24-48, 3-66) -> f ≈ 6245 px (HFOV ≈ 9.9 deg). With this f the eagle's
per-frame speed stays 11.3-12.5 m/s through the clip, i.e. constant speed, which fits the prior.

Boat: per-frame speeds 3.6-4.5 m/s (centroid jitter ±0.5 px), no trend -> constant speed.
v(frame 24) = 3.97-4.01; mean of frames 22-26 = 4.10-4.14; frames 20-28 = 4.02-4.06; frames 3-62 ≈ 4.06.
Second route: chord frame 2 -> 60 = 340 px / 58 frames = 140.7 px/s -> lateral 4.0 m/s at 177.5 m, plus a radial
part from the depth change (0.79 m/s) -> ≈ 4.08 m/s. Agrees.

Answer: 4.05 m/s. Confidence: good (±4 %); the main uncertainty is that the boat's origin may differ from the hull
centroid, which does not matter for a translating boat.
