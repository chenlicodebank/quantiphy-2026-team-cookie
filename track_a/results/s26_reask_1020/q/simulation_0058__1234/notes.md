# Q1234 – width of the lane (simulation_0058)

The question names no particular lane, so the answer is the curb-to-curb width of the main road, the one that recedes from the camera and that the taxi drives down. File fps is 24, the same as question_fps.

## Method (3D pinhole model)
- Principal point is taken as the image centre. Pitch and yaw come from the main-road vanishing point (1253, 422.5), roll is 0 (the horizon row is level). See `cam.py`.
- **Focal length** (`van_f.py`): the prior says the white van accelerates at 4 m/s². Its rear edge fits a quadratic in frames 2–71 (rms 1.8 px), so it starts from rest at about frame 0.3–1.
  - That gives a 3D displacement of 4.17–4.29 m between frames 14 and 38.
  - The van's distances at those frames are 31.07 m and 29.92 m. Back-projecting its box centre at those distances, the gap between the two points matches that displacement when f = 2300–2410 px. I used f ≈ 2380.
  - Check from the pixel acceleration: 0.532 px/frame² = 306 px/s². At about 30.5 m that is 4 m/s² when f ≈ 2330. This agrees.
- **Camera height** comes from each given distance applied to that object's ground-contact row: pedestrian 2.64–2.70 m, cyclist 2.59–2.61 m, van and taxi 2.69–2.88 m. The van and taxi values are biased high because their rows are the near-side wheels, not the point under the centre. I used h ≈ 2.63 m, from the pedestrian and cyclist.
- **Curbs** (`curbs.py`): I fitted the road edge at the foot of the curb on the near side (frame 71, saturation edge, residuals about 1 px):
  - left: x = -2.5076·y + 2335.2
  - right: x = 1.7010·y + 532.0

  Both lines meet near the vanishing point. The far-side curb lines are in scene/_vp.json.
- **Width** (`width.py`): each curb line is intersected with the ground plane, and the lateral offsets perpendicular to the road direction are subtracted.
  - Near side (12–17 m from the camera): 11.08 m at h = 2.671 m, so 10.9 m at h = 2.63 m.
  - Far side (about 65 m): 10.88 m at h = 2.671 m, so 10.7 m at h = 2.63 m.

## Checks
- Scale plausibility at f = 2380:
  - van length about 5.7 m
  - taxi length about 5.2 m
  - pedestrian about 1.88 m
  - cyclist with bike about 1.6 m
- Second route, the parked Mercedes: it is 270 px wide (with mirrors) against 1673 px of road at its row. With a car width of 1.8–1.95 m that gives a road of about 11–12 m, which agrees roughly.

## Answer
10.9 m (main road, curb to curb). Confidence is moderate: most of the uncertainty comes from the camera height, about ±3 %.
