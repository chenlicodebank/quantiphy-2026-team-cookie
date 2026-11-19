# q_1885: acceleration of the astronaut at t = 1 s

**Time base:** the file and the question both run at 24 fps, so t = 1 s is frame 24.

**Scale:** the bbox height at f24 is 380 px, the astronaut is 2.2 m tall (prior) and 18.147 m from the camera (depth_info), so
f ≈ 380·18.147/2.2 ≈ 3134 px (HFOV ≈ 40°). I also tried f = 3299 (taking 380 px as 95% of the standing height). The
speed changes by only about 3%.

**3D track:** depth Z(i) = 18.147 · h_s(24)/h_s(i), where h_s is the Savitzky-Golay smoothed bbox height (the f18 outlier
is interpolated). Positions are back-projected along the ray through the mask centroid or the scene pelvis estimate.
- Speeds: about 2 m/s at f0–f10, rising to about 6.2 m/s at f20–f28, falling to about 2.2 m/s from f35 on. At t = 1 s the
  astronaut is at the top of this speed bump and just starting to slow down.
- Acceleration (convention: the change of one-frame backward speed between frames 23 and 24, ×fps):
  - Savitzky-Golay smoothing of the positions (windows 7–11, several depth smoothings): -0.6 to -11 m/s². This route
    is very noisy.
  - Polynomial fits (degree 1–4, windows from f10–38 down to f18–30) to the raw per-frame 3D speed, evaluated at
    f24 − f23: -0.3 to -3.1 m/s², median about -1.8 (scripts `fit.py`, `accel.py`).
- The answer is the magnitude: 1.8 m/s².

**Second-route check:** I tried a depth cue that does not depend on leg pose, the helmet visor size (`visor2.py`).
The segmentation is unreliable in many frames. Over f19–29 it suggests a smaller depth change than the bbox height
does. That would lower the speed and the size of the acceleration.

**Caveats:** the camera cannot be checked (the background is white). There is a strong vertical image motion, a rise
of about 1 m between f16 and f35, which is not consistent with flat ground. The root motion is probably keyframed or
mocap with per-frame jitter.

**Confidence:** low. The sign shows deceleration (about -1.8 m/s²); the size is uncertain by a factor of about 2.
