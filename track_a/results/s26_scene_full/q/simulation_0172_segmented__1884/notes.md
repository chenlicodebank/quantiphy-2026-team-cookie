# Q1884: astronaut speed at t = 1 s (m/s)

Prior: the astronaut is 2.2 m tall. Depth: 18.147 m from the camera to the astronaut at t = 1 s. The video is 24 fps
and the question uses 24 fps, so t = 1 s is frame 24. Speed is the backward difference from f23 to f24, times 24.

## Measurements
- **Image motion** (scene track and measure.py, centroid and pelvis): the figure moves steadily at about
  du = +30.4 px/frame and dv = -12.3 px/frame over f20-f28. The origin is at about (1080, 768) px at f24.
- **Depth change:** bbox height is biased by the gait (crouched with feet together at f16, upright with legs spread
  at f32), so I did not use it directly. I estimated the upper body's scale change with SIFT plus a RANSAC similarity
  fit (scale_sift.py, scale_sift2.py). Around f24 the log-scale rate is 0.0050-0.0066 per frame, stable across crop
  fractions of 0.25-0.6 and frame gaps of 1-4; I used 0.0057. That makes the depth fall by about 0.104 m per frame.
- **Focal length:** I normalised bbox height by the SIFT depth (hnorm.py). At f24's depth the astronaut measures
  361-394 px over the walk; at f24 itself it is 380 px. Rest height is about the maximum, roughly 395 px, which gives
  f ≈ 395 × 18.13 / 2.2 ≈ 3255 px (horizontal FOV about 39°). I converted the 18.147 m range to a z-depth of 18.132 m.
- **Back-projection** with Z23 = 18.236 m and Z24 = 18.132 m gives dP = (0.173, -0.073, -0.104) m per frame. That
  is 0.214 m per frame, or **5.14 m/s**.

## Checks
- If 380 px (the f24 pose height) stands for 2.2 m, f = 3131 px and the speed is 5.30 m/s.
- Using the single-frame SIFT scale for f23→f24 (0.0064) gives 5.32 m/s.
- Taking depth from bbox height instead (pose-biased) gives 6.4 m/s; from mask area, about 9.8 m/s. I rejected both
  because the gait changes them strongly.
- Elsewhere in the clip (f0-12, f34-60) the 3D speed is about 2 m/s. The fast stretch from f15 to f30 shows up
  directly as the image speed tripling, so it is real motion and not an artefact of the depth estimate.

The answer is 5.2 m/s. Confidence is moderate: the depth-rate cue is the main uncertainty (about ±10%).
