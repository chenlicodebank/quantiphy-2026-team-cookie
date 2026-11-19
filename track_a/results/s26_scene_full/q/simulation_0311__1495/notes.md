# Q1495 – car length (front to back), simulation_0311

Question: length of the car in m. Prior: car height = 1.15 m. Depths to the car origin: 17.8278 m at t=1 s (frame 24) and
23.1989 m at t=2 s (frame 48). question_fps = file fps = 24.

The car is a red Ferrari LaFerrari model driving away from a static, downward-tilted camera. The camera looks down at only
about 20-25°, so the car's length is strongly foreshortened and the nose is hidden behind the hood and front fenders in every frame.
That means the front-to-back extent can't be read straight off the silhouette.

## Calibration (scripts: poles.py, fsolve.py, joint.py, recon4.py, final_calib.py)
- Principal point at the image centre. Vertical vanishing point from the pole edges (poles.py): x ≈ 1280, y ≈ 12150
  (near pole and far-left pole edges, sd 0.4 px).
- f from the given depths: the car origin must have the same height at frames 24 and 48. This depends very little on where
  the origin sits in the image (f changes by less than 1% for origin shifts of 0-80 px). With VY = 12150 this gives f ≈ 3520-3680.
- Rigid-body check: I reconstructed the car pose (with yaw fitted) in both frames from the left wheel-rim centres
  (48: (923.5,753.5), (1104.5,888.5); 24: (1366,1101), (1635,1309.5)) and the taillights (48: (1180,864), (1409.5,817);
  24: (1744,1287)). The wheelbase is the same in both frames when VY = 11650 (4% from the pole estimate). That gives
  **f ≈ 3570 px (horizontal FOV ≈ 39.5°)**, camera ≈ 7.7-8.1 m above the origin.
- A separate orthogonality test on the frame-48 hub line and taillight line gave f ≈ 4200 ± 400. This test is weak, because a
  1° error in reading a line moves f by about 300 px.

## Measured dimensions (self-consistent calibration, almost independent of the origin choice)
- Wheelbase 2.64 m. Taillight spacing 1.60 m. Rear hub to rearmost point (diffuser) 1.08 m.
- Rear hub to the visible front hood edge: 3.31 m. This is not the nose, which is hidden.
- These match a real-size LaFerrari: wheelbase 2.650, length 4.702, rear overhang ≈ 1.08, so front overhang ≈ 0.97.
- Measured length estimate: 2.64 + 1.08 + ~0.97 (front overhang, assumed) ≈ 4.69 m. The uncertainty is about ±4% from the calibration.

## Prior-based route
The model is a LaFerrari (real length/height = 4.702/1.116). Scaling by the prior height gives 4.70 × 1.15/1.116 = 4.84 m.
The measured wheelbase suggests the model is close to real size (length ≈ 4.70). Its 1.15 m height is 3% taller than the real car.

## Answer
Both routes give 4.69-4.84 m, so I answer **4.75 m**. Confidence: moderate (about ±4%). The front overhang can't be seen and
relies on the model's proportions. If the car's yaw is not aligned with the world axes, the world-AABB length could be slightly
larger.
