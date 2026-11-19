# q1278: height of the walking pedestrian (simulation_0061)

The file rate and question_fps are both 24 fps, so t=0.58 s is f14 and t=1.58 s is f38.

## Focal length (from the prior: white van acceleration = 4 m/s^2), `focal.py`
- The white van's 3D origin at f14 and f38 is its bbox centre back-projected with the given depths (45.5234 m and 43.9499 m), with the principal point at (1080, 540).
- I assume the van moves in a straight line through those two points. For every frame, the van position along that line is where the frame's pixel ray comes closest to the line.
- I fitted a quadratic in time to that position and solved for the f that gives a = 4 m/s^2.
- Result: f ≈ 2170 px using the centre over f2–71. Other frame windows and the rear or front edge give 2020–2200 px.
- The fitted start time is about -0.04 s, matching the record's note that the van starts from rest near f1. The speed rises steadily from 0.6 to 11.8 m/s.
- The horizontal field of view is then about 53°.

## Sanity checks of f (second route)
- Taxi side-view length, 286 px at about 40.1 m, gives 5.3 m. A real Crown Victoria taxi is about 5.38 m.
- Van length, about 296 px at about 44 m, gives 6.0 m, which is a normal full-size van.
- Bike length, wheel to wheel, 86 px at 41.9 m, gives 1.66 m.
- The pedestrian's walking speed comes out at about 1.2 m/s, which is plausible.

## Pedestrian height
- Pixel height comes from the segmentation bbox in scene/tracks/pedestrian.csv. I checked it by eye at f38: head top about 545, feet about 676, so about 131 px.
- Depth over time is interpolated linearly between 33.4337 m (f14) and 32.4161 m (f38). I converted it to forward depth Z = D·f/|(u-cx, v-cy, f)|, a factor of about 0.968 because he is at x≈500.
- Height per frame = h_px·Z/f, which ranges over 1.82–1.91 m. Mean 1.868 m, 90th percentile 1.89 m. At f14 it is 1.85 m and at f38 1.87 m.
- Answer: **1.87 m**.

## Confidence
The main uncertainty is f, about ±4%. Gait changes the bbox height by about ±1.5%. The answer is probably within about 5%.
