# Q683: speed of the moving red general at t = 0.5 s (m/s)

The file fps and question_fps are both 24, so t = 0.5 s is frame 12. The speed is the backward difference p(12) − p(11).

## Track (measure.py → own_track.json)
- I made my own mask from the difference to frame 44, where the piece has left the column. The mask centroid x stays at 959.1–959.2 px, so the motion is purely along +y. My track matches the scene record to within about 0.1 px.
- Frames (11,12) are the same image. Frame 11 already shows frame 12's position (229.3 px), so frame 11's true position is missing. A raw difference would give 0.
- The motion is uniformly accelerated. Quadratic fits over clean frames only (duplicate first-frames 9, 11, 18, 20, 28, 34 left out) give:
  - frames 8–16: a = 1.118 px/frame², p(11) = 217.00, p(12) = 229.31 → **v = 12.31 px/frame** (rms 0.04 px)
  - frames 5–20: 12.29 px/frame
  - frames 2–39: 12.32 px/frame
- Second route, using clean frames only: (p13 − p8)/5 = 11.19 px/frame at frame 10.5. Adding one frame of acceleration (≈1.11) gives 12.30 px/frame at 11.5, the same as above.
- The speed is 12.31 × 24 = 295.4 px/s.

## Scale (profile.py)
- The prior gives the piece diameter as 0.097 m. I measured the moving general's own diameter at frame 12.
  - Half-maximum edge crossings along 6 directions give 85.1–85.8 px (mean 85.5).
  - The mask bounding box gives 87 px (pixel count, inclusive).
  - I used **86 px**, so the scale is 0.001128 m/px.
- SAM 3 check:
  - A loose box prompt gave a 110×125 px mask that spilled onto the board, so I rejected it.
  - A tight box prompt gave 94×93 px (equivalent diameter about 92 px), about 8 % larger than my measurement.
  - frames/mask_cmp_f12.png compares them on a 4× zoom. The SAM outline (green) sits 3–4 px outside the visible rim and takes in the dark shadow halo. An 87 px circle (red) follows the real edge.
  - So my edge measurement is the right one, not SAM's. The SAM centroid agrees with mine to within about 1 px (229.97 vs 229.25 at frame 12; 289.73 vs 289.67 at frame 16).

## Answer
v = 295.4 px/s × 0.097/86 = **0.333 m/s**. It ranges from 0.329 m/s (87 px diameter) to 0.335 m/s (85.5 px).
Confidence: high, about ±2 %.
