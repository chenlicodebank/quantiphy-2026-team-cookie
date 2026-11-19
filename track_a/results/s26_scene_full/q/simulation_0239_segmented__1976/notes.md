# q_1976 — length of the white horse (m)

Prior: speed of the brown horse = 0.874 m/s. 2D clip, 24 fps (file fps = question_fps, no retiming issue).
The camera looks straight down and does not move; both horses walk right on the same ground plane, so one metres-per-pixel scale is used.
White horse = the cream animal (lower, row ~865). Brown horse = the upper animal (row ~776).

## Scale (m2.py)
- Brown horse pixel speed: the nose (bbox x1) is very steady at 63.6 px/s over every window (0-20, 0-40, 8-48, 28-48, ...).
  The centroid averaged over whole gait cycles (period ~20 frames) gives 63.1-64.4 px/s. I used **63.6 px/s**.
  Frame 49 is a reset artifact, so it is excluded.
- Scale = 0.874 / 63.6 = 0.01374 m/px.

## White horse length (m3.py, my own segmentation with overlays checked in frames/ov*.png)
- Horizontal mask extent over all 50 frames: median 176 px (threshold 235) / 178.5 px (threshold 245). Range 164-194 px with the gait.
  The scene record gives a bbox_w median of 174.5. I used **177 px**.
- Length = 177 x 0.01374 = **2.43 m** (the range over the gait is 2.25-2.67 m).

## Checks
- The brown horse's length works out to 148 px x 0.01374 = 2.03 m, and the white horse is 2.43 m. Both are plausible horse sizes.
- Cross-check of the speed from the centroid: the mean per-frame speed is 61.5 px/s. With that, the length would be 2.52 m (+3.5%).
  The nose and phase-matched values are preferred because they are less noisy.
- Confidence: moderate-high. The main uncertainty is how the reference treats a length that changes with the gait (±5%).
