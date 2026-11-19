# q_1082: speed of the human at t = 1.0 s (frame 33 at question_fps 33.0; the file runs at 33.0033 fps, which makes no practical difference)

## Scale
- Prior: h = 1.87 m. Given camera distances: D(0) = 12.26 m and D(1 s, frame 33) = 10.97 m.
- Focal length from f = sqrt((D·H/h)^2 - r^2), where r is the pelvis offset from the image centre: 895 px at frame 0 and 899 px at frame 33. I used f ≈ 897 px. The two estimates agree, so the height prior and both depths are consistent.
- Depth along the axis from the given distances: Z0 = 12.176 m and Z33 = 10.879 m. That puts the mean speed over 0–1 s at 1.296 m/s, because the lateral and vertical motion is negligible (lateral vX ≈ 0.02 m/s).

## Speed near t = 1 s (scripts: measure.py, check2.py, check3.py, check4.py)
Three depth cues from the scene track, each scaled to the given depths:
- 1/H (apparent height)
- 1/(feet_bottom − horizon)
- 1/(horizon − head_top)

Results:
- **One-step boxcar (17 frames, cancels the gait cycle):**
  - 1/H: dZ/dt at frame 33 = 1.48 m/s.
  - Feet cue: 1.57–1.61 m/s.
  - Difference over frames 25→41: 1.57–1.64 m/s.
- **Foot-strike step lengths (feet cue):**
  - Steps of 0.65, 0.77, 0.75, 0.65 and 0.57 m.
  - The step from frame 24 to 41, which contains frame 33, gives 1.49–1.53 m/s.
  - The early step (frames 7→24) gives about 1.3 m/s.
- **Polynomial fits of Z(t):** dZ/dt at 1 s = 1.38–1.7 m/s.

The cues agree that he speeds up: about 1.2–1.3 m/s early, about 1.5 m/s around 1 s, then slower later. This fits the 0–1 s mean of 1.30 m/s fixed by the given depths. The whole-clip mean is about 1.35 m/s.

## Answer
1.5 m/s. Confidence is moderate, about ±10 %. The main uncertainties are the gait oscillation of the pelvis within a step and noise in the cues.
