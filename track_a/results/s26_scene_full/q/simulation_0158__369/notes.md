# q_369 — acceleration of the shark at 1 s (m/s^2)

Prior: turtle acceleration = 2.639 m/s^2. No depth_info. 2D scene, static camera, 24 fps (file fps = question_fps; no re-timing).
Both animals swim right-to-left in a plane facing the camera (y constant), starting from rest and speeding up steadily.
One metres-per-pixel scale for both, so a_shark = 2.639 x (shark px accel / turtle px accel).

## Measurements (scripts in this folder)
- `steps.py`: frame-to-frame displacement by matching a patch from frame i in frame i+1 (high-pass, contrast-normalised
  grey, sub-pixel peak). Shark patch = rigid head + mid-body (snout .. snout+650 px, rows 60-230). The tail is left out
  because it flexes. Turtle patch = carapace (rows 495-560, ±130 px around the record's centre).
- `accel.py`: a straight-line fit of step vs time gives the acceleration in px/frame^2.
  - Shark: 2.540 (frames 5-40, rms 0.19 px), 2.538 (14-34), 2.535 (18-30). Steps rise linearly from about 1 px at frame 0,
    so the acceleration is uniform. After frame 40 only the flexing tail is visible, so those frames are unreliable and were not used.
  - Turtle: 0.926 (0-47), 0.930 (5-40), 0.922 (14-34), 0.900 (30-47, cleanest). Speed starts at about 0, so the acceleration is uniform.
- Ratio: 2.73-2.75 (wide windows) and 2.86 (narrow window 18-30, noisier turtle) give 7.21-7.27 m/s^2 (7.55 for the narrow window).
- Correcting the record: the record's shark ref_x and the tail-tip and rear patches give lower values late in the clip
  (1.9-2.2) because the tail flexes. The rigid head and body give 2.54, and the record's head-template fits (2.50-2.53) agree with that.

## Second route
The scene record's ref_x quadratic fits (shark 2.50-2.53, turtle 0.95-0.96, frames 5-40) give a ratio of 2.61-2.64, or 6.9-7.0 m/s^2.
Speed divided by time from rest gives shark 99.5/39.5 = 2.52 and turtle 42.8/46.5 = 0.92, a ratio of 2.74, or 7.2.
Scale check: 2.639 / (0.926 x 576) = 0.00495 m/px, so the shark is 911 px = 4.5 m long and the turtle about 1.6 m. Both are plausible.

Answer: 7.25 m/s^2 (estimated uncertainty about ±4 %; most of it comes from the turtle's pixel acceleration, 0.90-0.95).
