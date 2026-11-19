# q_664: acceleration of the vacuum cleaner at t = 2 s

Question fps = file fps = 24, so t = 2 s is frame 48. The convention is a = (speed(48) - speed(47)) x fps, with
speed(i) = |p(i) - p(i-1)| x fps. That makes a = (step48 - step47) x fps^2 in px, converted with one m/px scale.
The scene is a 2D top-down view, so one scale applies.

## Scale (prior: diameter = 0.438 m)
- Record circle-fit diameter, mean over frames 40-56: 120.8 px. On a 3x zoomed, gridded crop of frame 48, the disc spans
  x 886-1007 and y 327-447, about 121 px. These agree.
- SAM 3 ("white round disc", frame 48, box prompt) gives a 144 x 134 px box and a centroid at (946.5, 391.9). The overlay
  shows that its mask includes the vacuum's shadow below and to the lower left. So SAM's extents (+19%) and centroid
  (+5 px in y) are wrong. The circle fit is correct: its centre is (946.65, 386.92), and the zoomed crop confirms it.
  ("robot vacuum" returned no instance.)
- m/px = 0.438 / 120.8 = 0.003626.

## Motion
- Track 1: the scene record's circle-fit centres.
- Tracks 2-4: my own masked template matching of the disc (track_tm.py). The vacuum does not rotate. Templates were taken
  at frames 44, 48 and 52, with subpixel peaks. All four tracks agree within about 0.15 px per frame.
- Steps (px/frame) near frame 48: f46 ~21.0, f47 ~21.6, f48 ~22.1, f49 ~22.7, f50 ~23.0, then the peak near f51-52.
  Raw step48 - step47 = 0.36-0.68 px/frame^2 (209-388 px/s^2), which is noisy.
- Route 1 (accel.py): polynomial fits to the speed curve over windows 40-56 to 44-52, then
  (s(48) - s(47)) x fps^2. Median 317 px/s^2, range 290-331.
- Route 2: polynomial fits to x(t) and y(t) (degree 3-4, windows 40-56 to 43-53), then backward-difference speeds of the
  fitted path. Median 323 px/s^2, range 307-335.
- Result: about 320 px/s^2 x 0.003626 = 1.16 m/s^2 (route 1 gives 1.148, route 2 gives 1.170).

## Answer: 1.16 m/s^2
Confidence: moderate-good. The scale is good to about 1%. The acceleration is changing near frame 48 (it falls from
about 1.3 to 0 m/s^2 between frames 45 and 51), so the one-frame value is uncertain by about ±10%.
