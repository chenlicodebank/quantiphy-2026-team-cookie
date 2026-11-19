# q_1806: distance shark-boat at t = 0.5 s (frame 12), 2D clip, 24 fps (file fps = question fps)

## Scale from the prior (shark acceleration = 1 m/s^2)
fit.py: quadratic fits to the shark's x track (scene/tracks/shark.csv; frames 1-58, while it is fully in frame).
- bbox centre: -86.2 px/s^2 (frames 1-58), -88.8 (1-30), -84.3 (30-58)
- nose bbox_x0: -86.7 (1-58), -86.5 (1-30), -84.8 (30-58)
- mask centroid: -86.0 (1-58)
=> 86.2 px/s^2 = 1 m/s^2, so the scale is 0.01160 m/px. Sanity check: the shark is 280 px = 3.25 m and the boat is 858 px = 9.96 m. Both are plausible.

## Positions at frame 12
- shark: bbox centre (723, 904)
- boat x: bbox centre 855 (hull x 426-1284)
- boat y: **ambiguous**. The mast is cut off by the top of the image in every frame, so the full AABB centre
  cannot be measured. Candidates and the distances they give:
  - visible-bbox centre y = 322 (a lower bound on the height of the full-AABB centre): 597 px = 6.93 m
  - hull centre / waterline y ~ 500-540 (the waterline stripe is at image-centre height, which suggests a
    camera at the water level and a boat origin at the waterline): 406-425 px = 4.7-4.9 m
  - keel bottom y = 643: 292 px = 3.39 m
- Chosen: y ~ 510, so dx = 132 and dy = 394. That gives 415.5 px = **4.82 m**. This is the hull-centre/waterline
  reading, and it also hedges between the two extreme readings.

## Checks
- The acceleration is consistent across windows and reference points (84-89 px/s^2, within ±3%).
- The horizontal separation is small (1.53 m), so the vertical origin of the boat dominates the uncertainty.

Confidence: low-moderate. The scale is good to about 3%, but the boat's vertical origin is unknown (the answer
could range from 3.4 to 6.9 m).
