# q1337 — width of the turning yellow car (taxi), simulation_0066

The file rate and question_fps are both 24, so t = 0.58 s is frame 14.

## Camera (focal length)
- `lines.py`: Hough lines on scene/bg.png.
  - Road-A curbs (3 lines) meet at VP_A = (621, 77).
  - Road-B curbs (5 lines, both near and far) meet at VP_B = (3128, 77).
  - Lamp-post and traffic-pole verticals meet at VP_V = (1066, 2105).
- Focal length from three independent checks:
  - VP_A ⟂ VP_B with the principal point at the image centre: f = 852.
  - Horizon plus the vertical VP: f = 851.
  - Orthocentre of the three VPs: principal point (1066, 530), f = 844.
- Used f = 852 px with the principal point at (1080, 540). The camera tilts 28.5° down with no roll.
- A prior check was not possible. The prior (white van, a = 4 m/s²) only gives the van displacement between t = 0.58 and 1.58. That displacement depends on when the van started (~f7) and on its centroid-vs-origin offset, so it is too loose to calibrate f. The vanishing-point geometry was used instead.

## Main route: the given taxi depth at t = 0.58 s (f14)
- At f14 the taxi faces the camera almost head-on: the front is symmetric, and only ~7 px of its left flank shows, so yaw is about 2°.
- `mirror14.py` and `prof14.py` give the half-max silhouette edges.
  - Mirror-to-mirror span: left mirror x ≈ 824 (rows 398–402) to right mirror x ≈ 923 (rows 392–396), about 99 px.
  - Body front corners (rows 412–436): x 826 to 921, about 95 px. The flank and tyre add pixels out to 928.
- Origin ray at the car's image centre (876, 418): O = 19.6514 · r gives camera Z = 18.92 m.
- The mirrors sit about 1 m ahead of the origin, toward the camera, and about 0.3 m higher. The forward direction has F_z = −0.852 and up has U_z = −0.477, so mirror Z ≈ 17.8–17.9 m (17.6 m if the root is at ground level).
- W (mirrors) = 99 × 17.6–17.9 / 852 = **2.04–2.08 m**.
- Body without mirrors, front corners at Z ≈ 16.6–17.0: 95 px gives about 1.86–1.90 m. The body's maximum width over the front wheels is slightly larger, about 1.95.

## Second route: ground plane plus camera height (independent of the taxi depth)
- `height.py`: at f38 the pedestrian's pelvis depth (21.35 m) and feet pixel give camera height H = 7.13 m (person about 2.0 m tall, so the scene is slightly larger than real scale).
- At f14 the mirror ray meets the plane at mirror height h_m = 1.0–1.2 m at z = (H − h_m)/0.330 ≈ 18.0–18.6.
- That gives W = 99 px × z / 852 ≈ 2.07–2.12 m.
- `route2.py` repeats this crude-band span (threshold-25 outer edge, about +1.5 px per side) over f4–f18. The span is narrowest when the car is most frontal (f12–14): 2.10–2.18 m for 99–102 px, or about 2.08 at the half-max 99 px.

## Answer
Width = world AABB extent across the car, including the mirrors (they are part of the model's bounding box): **2.08 m**.
- Body-only reading, if mirrors were excluded: about 1.9–1.95 m.
- Confidence: moderate. The main uncertainties are where the origin sits relative to the mirrors (±2%) and whether the mirrors count (about 7%).
