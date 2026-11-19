# q_1005 – plane displacement from 0.5 s to 1.0 s

The scene is a 2D top-down render. The jet moves along -x at constant speed. The camera is static, as the record says.

## Measurements (check.py)
- The track in scene/tracks/jet.csv has steps of 34.2–34.6 px per frame from frame 2 onwards. A line fitted to frames 2–59 gives a slope of 34.398 px/frame, so the speed is uniform.
- I re-measured the shift independently by template matching (a jet crop from frame 12 or 13, with sub-pixel peak fitting):
  - frames 12→24: 413.07 px (the track gives 413.05)
  - frames 12→25: 447.80 px
  - frames 13→25: 413.04 px

## Scale and time base
- The prior is speed = 22.16 m/s. The speed is constant, so the scale is 22.16 / (34.398 px/frame × fps).
- The displacement is therefore steps × 22.16 / fps. The scale cancels out.
- **File fps of 24 (used):** frames 12→24 are 12 steps, so the displacement is 0.5 s × 22.16 = **11.08 m**. The scale is 0.02684 m/px, which gives a jet 15.1 m long with a 19.3 m wingspan. Both are plausible for a fighter.
- **Question_fps of 25:** this gives 10.64 m (frames 13→25) or 11.52 m (frames 12→25, 13 steps). Both are within 4% of 11.08 m.
- I chose the file rate. It gives exactly speed × 0.5 s, which is physically consistent with constant speed.

## Check
The two routes agree: the stored track and my own template matching give the same 413 px shift over 12 frames.

The displacement also equals the constant speed times the duration: 22.16 × 0.5 = 11.08 m.

**Confidence:** high.
