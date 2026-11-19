# q_1572: speed of the magnifying glass at t = 0.25 s

The question rate (24 fps) is the same as the file rate. t = 0.25 s is frame 6, so speed = |p(6) - p(5)| x 24.

## Method
- The magnifying glass falls freely in frames 0-11 and hits the desk between frames 11 and 12. The prior is a = 9.8 m/s^2 before 0.5 s.
- `fit.py` fits a 3D constant-acceleration model (|a| = 9.8, with a free direction) to the tracked pixel path, frames 0-11. Its free parameters are the focal length f, the direction of gravity in camera coordinates and the 3D initial velocity v0. The start point is the frame-0 pixel back-projected at the given depth of 4.2401 m. The principal point is taken at the image centre.
- I ran the fit on four reference points from the track: bbox centre, lens centre, mask centroid and bbox top.
  - All fits give f of about 2600-2740 px (HFOV about 43 deg). The RMS residual is 0.25-0.33 px, except about 1 px for the mask centroid.
  - The velocity component along gravity at t = 0 is between -0.04 and +0.01 m/s, so the glass is released from rest at frame 0. The pixel steps (6, 16.5, 28.5 px...) have a first/second ratio of about 3, which matches this.
  - The fitted speeds at frame 6 are 2.278, 2.271, 2.254 and 2.260 m/s.
- Route 2 (analytic, release from rest at t = 0): v = g x 5.5/24 = 2.246 m/s. This is the backward difference over frames 5 to 6.
- Check: the model depth at frame 11 is about 4.47-4.54 m, close to the given 4.41 m at 0.5 s, when the glass is lying on the desk. The fall height of about 1.1 m is plausible for a drop onto a desk.

## Answer
2.25 m/s (the routes give 2.246-2.278). The horizontal drift is negligible. Confidence: high (about 2%).
