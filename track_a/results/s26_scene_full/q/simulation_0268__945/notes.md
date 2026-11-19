# q_945 — length of the spacecraft (m)

Prior: acceleration at 1.0 s = 4 m/s^2. 2D video, top-down view, 24 fps (file fps = question fps). Camera is static.

## Pixel acceleration (fit.py)
I fitted a quadratic to scene/tracks/vehicle.csv, frames 3-58. The motion is uniformly accelerated from rest at frame ~0
(residual rms 0.16 px).
- x_ref (silhouette bbox centre): a = 697 px/s^2. The one-frame-difference convention at frame 24 gives the same 697.
- x_body_texture (top surface, nearer the camera): 721 px/s^2.
- rear fin edge: 679 px/s^2.
I used x_ref (697 px/s^2) because it is based on the silhouette, the same as the length measurement.
Scale: 4 / 697 = 0.00574 m/px.

## Pixel length
At frame 36 the vehicle is centred in the image. On a zoomed crop the nose tip is at x = 777 and the rear fin tips at
x = 1813-1814 (this matches the record's rear_x_fins = 1813). That makes the length 1036 px. The record's nose at
frame 36 (806) was wrong: the white nose blends into the cloud. The record gives 1022-1031 at frames 24-30 and 1042 at
frame 38. I used 1035 px.

## Answer
L = 1035 × 4 / 697 = 5.94 m.

## Second route
Using the top-surface texture acceleration (721 px/s^2) gives 5.74 m. Using the record's median length of 1020 px gives
5.85 m. All routes fall within 3.5% of each other. Confidence: moderate-high, with about 4% uncertainty from the
perspective/parallax choice.
