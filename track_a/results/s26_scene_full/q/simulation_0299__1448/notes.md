# q_1448 – speed of the forklift at 1.0 s

Prior: the forklift accelerates uniformly at 2 m/s^2. question_fps = file fps = 24, so t = 1.0 s is frame 24.
The answer is v = a × (time since the start of motion), using the benchmark's backward difference. What has to be
measured is the start time.

## Measurements
- `diff01.py`: frames 0 and 1 are almost identical (614 px differ by more than 10, against 50k+ for the later pairs),
  so the forklift is at rest there.
- `early.py`: phase correlation of the forklift region, frame to frame, for frames 0–24. The per-frame image step is
  0, 0.83, 1.23, 1.71, 2.18, 2.72, 3.37, ..., 11.40 px for frames 1..24.
  - The step grows linearly at about 0.484 px/frame.
  - A linear fit puts step = 0 at frame ≈ 0.47. A body accelerating from rest at frame f0 gives
    step(i) ∝ (i − 0.5 − f0), so f0 ≈ 0: the motion starts at t ≈ 0. Frames 2–6 match k(i−0.5) closely.
- `fit3d.py`: pinhole fit of the mask-centroid track (frames 15–71) to straight-line motion with a = 2 and the two
  given depths. It gives f ≈ 3100–3200 px and t0 ≈ −0.04 to −0.07 s, which also points to a start at t ≈ 0.
  The centroid is not the origin, so this is only a coarse check.

## Answer
The motion is uniform from rest at t = 0. The backward-difference speed at frame 24 is
2 × (24 − 0.5)/24 = **1.958 m/s**.
- The instantaneous value a·t would be 2.0 m/s (+2%).
- If the start were frame 1, the speed would be 1.917 m/s (−2%).
- All three readings are within about 2% of each other.

Confidence: high. The prior fixes the scale, and only the start offset matters.
