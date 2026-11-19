# q_680 — acceleration of the vacuum cleaner at t = 2 s

The question asks for the acceleration at t = 2 s. The prior is a diameter of 0.438 m. The video is a 2D overhead render at 24 fps, and question_fps is also 24, so t = 2 s is frame 48.
a = (speed(48) − speed(47)) × fps, where each speed is a backward difference of the disc centre.

## Scale (prior object = the vacuum itself)
- `measure.py`: I cast 360 rays from the centre and found where each one crosses the rim at sub-pixel precision, at the
  half-way point between the disc's brightness and the floor's. A circle fit to those points gives a radius of
  59.88–60.04 px over frames 36–58, so the diameter is **120.0 px**.
- `profile.py`: the median radial profile at frame 48 falls from 197 at r = 58.5 to 110 at r = 62. The half-max point
  is at r ≈ 60.0. Just outside the rim (r ≈ 61.5–63) there is a dark contact-shadow ring.
- The scene record's threshold mask gives 117.8 px. The threshold of 185 cuts inside the soft edge, so it is about 2% small.
- SAM 3 ("white disc", frame 48, k4) gives 125 px (equivalent diameter 124.6). That is 4% larger than 120. On the zoomed
  overlay (`frames/rim48.png`: red = rim fit, green = r 62.5) SAM's outline reaches the dark shadow ring, beyond the
  disc's edge. **I use the half-max rim at 120 px.**
- Scale = 0.438 / 120 = 0.003650 m/px.

## Motion
- My rim-fit centres (`my_track.json`) match the scene record within about 0.15 px and the SAM track centres within
  0.2–0.6 px (`samcheck.py`), so all three are tracking the same object.
- Rim-fit speeds in px/frame: 46: 20.951, 47: 21.694, 48: 22.176, 49: 22.599, 50: 22.871.
- Per-frame differences in speed (px/frame²): 45: 0.88, 46: 0.86, 47: 0.74, 48: 0.48, 49: 0.42, 50: 0.27. The robot
  is still speeding up but less each frame; the speed peaks at frame 51.
- Estimates of the acceleration at frame 48 (`accel.py`):
  - Raw backward difference: 0.482 px/f² from the rim fit, 0.531 from the mask fit, 0.458 from the scene record and
    0.57 from SAM.
  - Smoothed: a quadratic fit to the speeds over frames 42–54 gives a slope of 0.503 at frame 47.5; a cubic fit gives
    0.570. A cubic fit to the 2D path gives 0.535.
- Adopted value: 0.52 px/f² (spread 0.48–0.57). 0.52 × 24² × 0.003650 = **1.09 m/s²**. The estimates above span about
  1.01–1.21 m/s².

## Confidence
The scale is good to about ±2%. If the scale came from the threshold mask's 117.8 px instead, the answer would be
1.11 m/s². The bigger uncertainty is the acceleration itself, because a single-frame difference of speeds is noisy;
the estimates span roughly ±8%. My best estimate is 1.09 m/s².
