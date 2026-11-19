# q3039: acceleration of the swimming woman, 0 s to 5.20 s

**Answer: 0.012 m/s²** (low confidence, because the quantity is ill-conditioned)

## Setup
- The video is an overhead drone shot. The camera is nearly static, with drift of about 10–17 px; I subtracted it using `cam_dx_smooth` from scene/.
- Time base: I used 24 fps (question_fps). The file's 22.52 fps looks like a re-timed clip. At either rate the speed is about 0.38–0.41 m/s and the stroke cycle is about 2 s, so physics cannot decide between them. At 24 fps, 5.20 s is frame 125; at 22.52 fps it is frame 117.
- Scale: one factor, prior height / pixel head-to-toe length. The stretched glide frames f122–124 measure 702–716 px, so I used 715 px. The factor is 1.63/715 = 0.00228 m/px.

## Measurement
- The swimmer's average speed is constant to within the noise: about 7.3 px/frame, i.e. about 0.4 m/s, with a surge inside each stroke. The cycle-averaged acceleration is therefore about 0. The answer comes from the difference between the instantaneous body velocities at t = 0 and t = 5.2 s, divided by 5.2 s. This telescopes the mean of the per-frame second differences, which is the annotators' convention.
- Reference point: the hip, i.e. the centre of the swimsuit bottom. I tracked it with short-range template matching from hand-picked seeds:
  - f0 at (1230, 940), tracked over f0–40
  - f110 at (2080, 975), tracked over f95–140
- Scripts are `hiptrack2.py` and `accel.py`. Overlays in `frames/hip_start.png` and `frames/hip_end.png` confirm that the box stays on the hips.
- Hip velocity:
  - at f0: 3.9 px/frame (single forward difference), 4.6–5.0 px/frame (fits over ±2–5 frames)
  - at f125: 5.5–5.8 px/frame
- Acceleration at 24 fps: 0.0076–0.0185 m/s², depending on the smoothing window. With ±2-frame fits it is 0.0123 m/s². The single-frame forward difference gives 0.0167 m/s².
- Second route, 22.52 fps (end frame 117): 0.0015–0.026 m/s², with ±2-frame fits giving 0.0123 m/s². This is consistent in sign and size.

## Caveats
- The head (hair centroid) is NOT a good body reference here. It lunges relative to the hips: about 10 px/frame at f0 against 5 px/frame at f125, which would give about −0.055 m/s².
- The visible-mask centroid in scene/ gives a positive sign like the hips (about 5 → 6.6 px/frame).
- The true answer is a small difference between two noisy velocities, so the uncertainty is large (roughly ±50%).
- For reference only: assuming she started from rest, 2d/t² would give about 0.15 m/s². This is not consistent with the video, where she is already moving at frame 0.
