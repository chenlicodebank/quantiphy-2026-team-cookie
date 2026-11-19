# Q2194 – ball velocity at t = 0.6 s (captured_0010)

Question: "What is the ball's velocity at 0.6s in m/s?" Prior: g = 9.8 m/s². The depth_info gives the camera-to-ball distance at
frames 7, 14, 22, 29, 36 and 43. question_fps = file fps = 24, so t = 0.6 s is frame round(14.4) = 14.
Camera: f = 0.5959 x 1280 = 762.75 px, c = (640, 360).

## Scene
A ball hangs on a string held in a hand. The pivot pixel is about (638, 226), checked on frame 14. The ball swings as a
pendulum, mostly towards and away from the camera. At frame 14 it is about 3 frames before the near turning point (f17),
so it is slowing down quickly. The scene/ ball track (centroids, ±0.5 px) was checked on crops and is correct.

## Method
- Apparent size gives too noisy a depth: blur at mid-swing inflates the mask, and frame-to-frame depth jitter turns into
  fake speed (0.2–1.1 m/s at f14). I used it only as a sanity check (`vel.py`).
- Main route (`pendfit.py`): a 3D spherical pendulum, integrated under g = 9.8 (prior), with damping and a free gravity tilt.
  The pivot sits on the measured string-top ray at a fitted distance. The model is fitted to the ball's image centroids,
  the given depths and the pivot pixel. Positions are back-projected the lab way, so the model's 3D centre reproduces
  both the image track and the given depths.
  - All frames: pixel RMS 2.4 px. Depths at the given frames are 1.717 / 1.385 / 1.435 / 1.742 / 1.713 / 1.384, against
    the given 1.706 / 1.344 / 1.4605 / 1.784 / 1.717 / 1.350 (the given depths scatter ±3 cm around any smooth path).
    Fitted L = 0.33 m, swing amplitude about 38°.
  - Frames 0–30 only (avoids the later hand drift): pixel RMS 0.9 px.
  - Variants (g free → g_eff 9.88, which agrees with the prior; tighter depth weights) change the result by less than 3%.
- Speed at frame 14 from the fitted trajectory:
  | variant | instantaneous | forward diff P15−P14 | mean of fwd diffs f12–16 | fwd diff of 5-frame-smoothed positions |
  |---|---|---|---|---|
  | all frames | 0.944 | 0.821 | 0.788 | 0.780 |
  | f0–30 | 0.918 | 0.794 | 0.762 | 0.755 |
  | f0–30, tight depth | 0.915 | 0.787 | 0.755 | 0.749 |
- The lab reference uses forward differences of 3D centres smoothed over at least 5 frames, which gives about 0.76–0.82.
  The instantaneous speed is about 0.92–0.94; it is higher because the ball slows by about 0.25 m/s per frame here.

## Second route
Using only the given depths, the mean depth rate from f7 to f14 is (1.706 − 1.344)/7 frames = 1.24 m/s. That fits the
model's speeds, which fall from about 1.4 m/s at f10 to about 0.9 m/s at f14. At f14 the ball's image motion adds only
about 0.19 m/s sideways. A sinusoid fitted to the f7/f14 depths with the observed period gives a depth rate of about
0.86 m/s at f14, or about 0.88 m/s once the sideways motion is added.

## Answer
0.80 m/s, the forward-difference/smoothed convention. Confidence: moderate, ±10%. The main uncertainties are the
reference's smoothing choice (0.76 smoothed up to 0.93 instantaneous) and the noise in the given depths.
