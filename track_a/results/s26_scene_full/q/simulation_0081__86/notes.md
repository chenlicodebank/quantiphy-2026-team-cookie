# Q86: distance between the walking person and the bike at t = 0.5 s

- **Frame:** t = 0.5 s → frame 12. fps and question_fps are both 24, so no re-timing.
- **View:** the camera looks straight down at the floor (a top view). The distance is measured in the ground plane.

## Bike
- I checked the bike's cyan bounding box from the record on frame 12: x 1047–1427 (length 380 px), y centre 643.5.
- The origin is taken as the bounding-box centre: (1237, 643.5).
- Scale: 1.7 m / 380 px = 0.004474 m/px.

## Pedestrian pelvis
- The pelvis can't be seen from above. I used the centroid of the shirt (torso) as a stand-in, measured by `torso.py`.
- Mask: bluish pale pixels; the overlay is in `frames/shirt12.png`.
- At frame 12 the centroid is (230.1, 443.8). It moves smoothly, about 12.4 px per frame.
- The head covers the back of the shirt, which pulls the centroid slightly forward, so I took the torso centre as about (228, 444).
- The head track in the record (x = 210.6) is not used. The head sits higher than the pelvis, so perspective pushes it about 15–20 px outward from the image centre.

## Results
- **Route 1, plain 2D with one scale:** 1028.5 px × 0.004474 = **4.60 m**.
- **Route 2, overhead pinhole camera with parallax** (`dist.py`):
  - Camera height comes from the record's rider-head parallax (0.040 px per px): about 24–28 m, focal length about 5200–6000 px.
  - The bike's ends are placed at their real heights, about 0.35 m (wheel) and 0.8 m (rack).
  - Result: 4.56–4.60 m, depending on the height assumed for the torso point (1.0–1.3 m). It barely depends on the camera height.

## Answer and confidence
- **Answer:** 4.58 m (in the ground plane).
- **Uncertainty:** about ±2%, mostly from where the pelvis is placed (±10 px ≈ ±0.045 m).
- **If 3D distance were meant:** with the pelvis about 1 m above the bike's origin, a full 3D distance would be about 2% larger.
