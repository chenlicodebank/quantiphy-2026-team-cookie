# q_1883: acceleration of the astronaut at t=0.5 s (frame 12, fps 24 = question_fps)

Method (m.py, m2.py):
- Scale: f is estimated as bbox height at frames 22-26 (~380 px) x 18.147 m / 2.2 m = about 3140 px.
  This is a rough estimate: the walking-pose bbox is not the rest height.
- Depth over time: depth(i) = 18.147 x size(24) / size(i), with size = mean of normalised bbox height and sqrt(mask area).
  Depth is about 19.5 m at frame 12 and nearly constant over frames 4-20.
- Position: back-projected pelvis or centroid from smoothed local fits. Speed is the one-frame backward difference x 24.
  Acceleration = (speed(12) - speed(11)) x 24.
- Speed at frame 12 is about 1.5-1.8 m/s. The image motion roughly doubles after frame 15, so the speed is already rising at frame 12.

Results: local-fit variants (windows 4-20, 6-18, 8-16, 2-22, 0-24; pelvis and centroid) give 0.9-3.3 m/s^2, median about 2.2.
Global high-degree polynomial fits were unstable (depth derivative noise) and are not used.
Raw per-frame differencing gives about 4.5 m/s^2, but is jittery.

Answer: about 2.2 m/s^2. Confidence is low-moderate, because the acceleration is a second difference of noisy tracks.
