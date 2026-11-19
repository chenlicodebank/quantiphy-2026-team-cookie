# Q2750 – velocity (speed) of the white ball at t = 1.5 s, cm/s

Clip: captured lab video, 1280x720, file fps 24 = question_fps 24, so t = 1.5 s is frame 36. f = 0.5959*1280 = 762.8 px, principal point (640, 360).
The credit-card prior is not needed: depth_info gives the ball distance at 1.5 s (0.7045 m) and 2.0 s (0.6270 m, frame 48).

## Track check
I used scene/tracks/ball.csv centroids and checked them on crops of frames 32–40 (frames/seq.png); they are correct to a few px.
Frame 36 sits in flight 2, near its apex, between bounces at frames 33/34 and 41. measure.py re-measured the masks and checked
the container timestamps, which are perfectly regular (512/12288 s per frame).
**Anomaly:** the x step from frame 35 to 36 is 60.5 px, while the other steps are 31–36 px/frame. The y steps (-40, -39, +1, +20, +39)
also break the gravity pattern (~18.5 px/frame² at this depth), so the camera almost certainly dropped one frame between 35 and 36.
The reference annotators index frames as they come, so their smoothed velocity includes this jump.

## Depth for the frames in the window (fit3d.py)
P36 = (0.104, -0.002, 0.697) m and P48 = (0.360, 0.079, 0.507) m are back-projected from the given distances.
I assumed a level camera, so X and Z (horizontal) are linear in time between bounces. Fitting X/Z to the observed u values (frames 34–48)
works only with the dropped frame included: residuals are ≤6 px, and the velocity is nearly constant across the bounce
(seg A Vx 0.64, Vz -0.39 m/s; seg B 0.42, -0.37 m/s). Without the drop the fit is poor (residuals up to 22 px, and Vz jumps from +0.04 to -0.68).
I also ran two alternative depth models: distance linear in time, and constant Z.

## Speed at frame 36 under different conventions (conventions.py, cm/s; drop model / lin-D / const-Z)
- 5-frame moving average of the forward differences (vector), = (P39-P34)/5: **92.4** / 85.5 / 86.4
- (P38-P34)/4: 103.4 / 95.4 / 95.1
- linear fit to positions 34..38: 106.5 / 98.2 / 97.9
- mean of the scalar per-frame speeds 34..38: 114.1 / 108.5 / 109.1
- forward window (P40-P36)/4: 89.1 / 88.6 / 93.3
- Physical speed in real time at the apex (horizontal 0.745 m/s, vertical ~0): ~75 cm/s. The reference cannot see the dropped frame,
  so it would not get this value.

## Answer
The convention as written (forward difference, smoothed over 5 frames) gives about 92 cm/s; the other window choices give 86–114.
Answer **95 cm/s**, a central value. Confidence: moderate (±10–15 %). The main uncertainties are the reference's smoothing window,
which interacts with the dropped-frame jump, and its per-frame depths.
