# q_676: acceleration of the vacuum cleaner at t = 0.5 s

Question fps = file fps = 24, so t = 0.5 s is frame 12. Prior: the vacuum is 0.438 m across. 2D top-down video, and the robot moves on the floor, so one m/px scale comes from the robot's own diameter.

## Scale (diam.py)
- I measured the diameter at stationary frame 75, where there is no motion blur. I took the half-max edge crossings along 12 profiles through the circle centre and got **120.25 px** (range 119.0–120.8). In my threshold masks the vertical bbox is 119–121 px. The scene record's circle fit gives 117.8 px (a stricter mask).
- At frame 12 the same profiles give 122 px on average, with up to 124.5 px along the motion direction. That is motion blur (about 12 px/frame), so I did not use frame 12 for size.
- SAM 3 ("white disc", box prompt) gives 126 x 124 px at f75 (equivalent diameter 124.3) and 134 x 138 px at f12. Both are more than 3 pct larger than my measurement. On the zoomed frame (frames/f75z.png) the bright disc spans about 120 px. The SAM outline (frames/seg_02_f12.jpg) runs around the soft grey shadow/halo and has a bump at the bottom, so it is too big. **My 120.2 px is the correct size.** The SAM centroids agree with my circle centres to within 0.4 px: (650.3, 499.9) vs (650.1, 500.2) at f75, and (1599.7, 408.7) vs (1599.5, 408.3) at f12.
- Scale = 0.438 / 120.2 = 0.003644 m/px.

## Motion (measure.py, accel.py)
- Tracking: I made my own masks with |frame − bg(f79)| at thresholds 20, 35 and 50, fitted a robust circle to each, and compared the result with the scene record track (circle centre).
- The per-frame speed rises by about 1.0–1.1 px/frame each frame over frames 3–15, so the acceleration is nearly constant there. It then tapers off and the speed peaks at frame 25.
- Acceleration at frame 12 = speed(12) − speed(11):
  - Raw values: 0.88 (record), 0.98, 1.05 and 1.01 px/frame² (my three tracks). These are noisy.
  - Polynomial fits of x(i) and y(i) over windows from 8–16 to 3–22, with the same backward-difference convention applied to the fitted positions: 1.01–1.09.
  - Linear slope of speed over frames 8–16: 1.03–1.08.
- Second route: the mean slope over frames 3–15 on the thr35 track is (15.22 − 2.69) / 12 = 1.044.
- Adopted value: 1.045 px/frame².

## Answer
a = 1.045 px/frame² × 24² × 0.003644 m/px = **2.19 m/s²**.
- Spread: 2.12–2.29 across the fit choices.
- If the scale came from the 117.8 px circle-fit diameter, the answer would be 2 pct higher.
- Confidence: moderate-high, about ±5 pct.
