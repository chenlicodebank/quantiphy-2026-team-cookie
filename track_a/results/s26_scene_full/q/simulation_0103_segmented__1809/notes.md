# Q1809 – length of the boat (m)

2D side-view scene, 24 fps (file fps = question fps). Prior: shark acceleration = 1 m/s^2. It sets one m/px scale.

## Shark pixel acceleration (fit.py)
Quadratic fits x(t) to the scene/tracks/shark.csv positions over frames 1/2/5 to 53:
- bbox centre -85.6 px/s^2, mask centroid -85.8, nose -86.1, tail -85.1 (rms 0.4-1.3 px).
- Sub-windows give 2-30: 84-87; 25-53: 78-85 (noisier).
Adopted value: 85.7 px/s^2, so the scale is 1/85.7 m/px = 0.01167 m/px.

## Boat length (boatlen.py, my own segmentation)
Horizontal extent from stern to bow tip of the hull rows (y 250-660), taken at frames 25, 35, 45 and 53: 859, 858, 856, 858 px,
giving about 857 px (the scene record says 853-857). The boat is not clipped after frame 20.

## Answer
857 / 85.7 = 10.0 m.
Check: the frame-53 hull-only value of 856 px from scene/ and the centroid acceleration of 85.8 give 9.98 m. The plausible
acceleration range of 84-87 px/s^2 gives 9.85-10.2 m.
Confidence: high.
