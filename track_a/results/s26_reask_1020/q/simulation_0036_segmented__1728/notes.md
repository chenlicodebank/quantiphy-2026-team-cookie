# Q1728: average speed of the boat (m/s)

The prior says the boat is 10 m long. depth_info gives the boat at 133.957 m (t=1) and 131.256 m (t=2), and the person at about 139.10 m.
question_fps is 24, the same as the file's rate. The scene/ tracks (boat mask centroid, red-hull extent) were checked on frames 0, 24 and 71, and they are right.

## Method (geom.py, profile.py, measure.py)
- Pixel motion: from frame 2 on, a linear fit of the boat centroid gives -3.07 px/frame in x and +0.05 px/frame in y. Frames 0→1 barely move (0.18 px), so motion starts at frame 1.
- The two given depths put the boat at 3D points (pinhole camera, principal point at 539.5): ray direction × the given Euclidean distance at frames 24 and 48.
  This gives the velocity as a function of the focal length f.
- How f was fixed (two routes that agree):
  1. Apparent hull length. I assumed the boat moves along its own long axis, which is plausible because the bow points the way it moves. I projected a 10 m segment
     along the 3D velocity direction and compared it with the measured red-hull x-extent (173→195 px).
     They match at f ≈ 3270–3300 px. The predicted growth of the extent over the clip (+13.0%) matches the measured growth (+12.2%) at every f,
     which supports the along-axis assumption. That puts the boat at about 43° to the image plane.
  2. Person height. The person is 40 px tall at 139.1 m. With f = 3270 they are 1.70 m tall, an adult (the f-only route).
- Result: with f = 3270 the velocity is (-2.95, -0.10, -2.73) m/s and the speed is **4.02 m/s**.
  With f = 3346 the speed is 3.97 m/s; this f follows from the identity v = L × (pixel speed) / (pixel length), which does not depend on f.
- The speed is constant: the per-10-frame pixel speeds rise from 3.0 to 3.2 px/frame only because the boat gets closer (depth falls 6%).
- Mean of the per-frame speeds: including the start-up frames (0→1 almost zero, 1→2 partial) would give about 3.96 m/s. The steady speed is 4.02 m/s.

## Answer
4.0 m/s. Confidence: good (±4%). The main uncertainty is f, but the hull-extent route and the human-height check agree.
