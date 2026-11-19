# q_1748 — average speed of the person (prior: height 1.75 m)

fps 24 = question_fps (no retiming). Static camera, steep oblique view from above (crops.py → crops.png, ascii.py mask dumps).
Person walks toward the camera (down the image).

Pixel motion (scene/tracks/person.csv, centroid ≈ pelvis): net f0→f71 = (7.9, 107.1) px over 71 frames
→ 1.51 px/frame along y (toward camera), 0.11 px/frame along x. Frames 0–1 static. Gait: bbox height minima at
frames 17, 34, 51, 68 → one step per 17 frames (0.71 s), ≈26 px of pelvis advance per step.

Scale: the camera looks down at θ ≈ 57–60°, so the person's height is foreshortened (×cosθ) and the walking direction
(along the ground toward the camera) is foreshortened by sinθ. A naive 2D scale (1.75 m / 46 px) would be wrong.
Estimates (from ascii mask dumps):
- image scale at the person m ≈ 0.028 m/px from shoulder width (≈17 px ↔ ~0.48 m), head width (~6 px ↔ 0.16 m),
  and a standing-leg model (legs-together leg ≈16 px = 0.85·cosθ/m);
- θ from the total legs-together extent (≈40 px = 1.75cosθ + head/toe depth terms) → ≈59°, and from front-leg vs
  legs-together leg projection ratio (≈1.5) → ≈57°.
Ground scale along y = m/sinθ ≈ 0.033 m/px; across x = 0.028 m/px.

Speed = sqrt((1.508·0.033)² + (0.111·0.028)²)·24 ≈ 1.20 m/s.
Check: step length 26 px·0.033 ≈ 0.86 m at 0.71 s/step → 1.21 m/s; plausible walking speed for a 1.75 m person.
(Naive planar 2D scale would give ≈1.4 m/s; ignoring the tilt is not physically right here.)

Confidence: moderate (θ and m uncertain ~±10%). Answer 1.2 m/s.
