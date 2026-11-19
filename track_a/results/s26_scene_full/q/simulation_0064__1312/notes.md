# Q1312 — width of the turning yellow car (taxi), simulation_0064

The file fps and question_fps are both 24. It is a 3D Blender scene with a static camera.

## Focal length
- **Vertical vanishing point:** I fitted lines in code to the 4 signal poles (`poles.py`, `poles2.py`). Slopes: near-left +0.0905, near-right −0.1178, far-left +0.0392 and far-right −0.0738. They meet at (1050–1065, 7540–7800).
- **Horizon:** y ≈ −121, from the street-curb vanishing point in scene.json (possible range −103 to −187).
- **Result:** with the principal point at the image centre, f² = (540 − y_h)(y_v − 540), so f ≈ 2150–2190 px. If the horizon is at −160, f ≈ 2220.
- **Van kinematics check (`vanfit.py`):** the prior a = 4 m/s² from rest, plus the two van depths, needs a start time of 0.04–0.06 s if f ≈ 2150. That fits the record, where motion starts between frames 1 and 2. The check is weak, because the result is very sensitive to the start time.
- **Sanity check:** with f = 2150 the pedestrian (103 px tall at about 38.3 m) is about 1.71 m tall.

## Taxi depth at frame 0, where it faces the camera
- I took the taxi origin at t = 0.58 s (frame 14) as the given distance 35.53 m along the ray through its bbox centre.
- I placed the frame-0 origin on the same horizontal plane, along the frame-0 ray (`taxigeo.py`, `solve.py`). That gives d0 ≈ 37.6 m and camera depth Zc ≈ 37.2 m.
- The front face is about L/2 nearer to the camera. L ≈ 5.36 m comes from the side view at frame 71 (bbox 395 px, minus the visible rear face), which puts the front face at Zc ≈ 34.7 m.

## Pixel width
- At frame 0 (`edges.py`) the left body edge is at x ≈ 881 and the right front corner (headlight and bumper end) at x ≈ 993, so the front face is about 112 px wide.
- The full body silhouette reaches x ≈ 998, because a sliver of the right side is visible. That fits a car heading along the street.
- The image columns come in duplicated pairs, so each edge is only good to about ±2 px.

## Result
W = 112 × 34.67 / 2150 ≈ 1.81 m (1.79 m at f = 2170; 1.87 m if the face is 116 px). **Answer: 1.80 m** (body width; the task's convention measures a car's width wheel to wheel).

If the bounding box includes the mirrors (bbox x 880–1006, 126 px), the width would be about 2.03 m. I used the body width.

## Caveats
- The plane method predicts 33.8 m for the depth at 1.58 s against the given 33.0 m. The taxi is side-on and partly occluded then, so the bbox centre is a poor stand-in for its origin.
- I used frames 0 and 14, where the car faces forward, and did not rely on frame 38.

## Confidence
Moderate, about ±5%. The main sources are f (±3%), the front-face pixels (±2%) and the front-face depth (±2%).
