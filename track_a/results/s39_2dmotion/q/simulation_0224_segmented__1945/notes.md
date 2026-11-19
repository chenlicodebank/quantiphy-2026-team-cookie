# q_1945 — acceleration of the red general chess piece at t = 0.5 s

Prior: diameter of a Chinese chess piece = 0.097 m. 2D video, 24 fps (file fps = question_fps = 24), t = 0.5 s -> frame 12.

## Object
The scene record calls the only moving object a "cream block". It is the chess piece: a disc lying flat in the
trough of the ramp, seen obliquely (bright top face over a shaded side), sliding down-left with uniform
acceleration (frames 3–39). Same object for the question and the prior. Track: scene/tracks/block.csv (checked on
zoomed frames; centre follows the piece).

## Scale (diameter in pixels)
The disc's diameter is the long axis of its image, which lies along the ramp. I rotated each frame so the path runs
horizontally, computed |frame − frame 44| (piece gone) and took the end positions from gradient peaks on the widest
rows (len3.py). The result was 79.7 px (frames 0–32: 79.3–80.1). A visual read on frames/rot_f12.png gave ends at
x≈60 and ≈139, so about 79 px.
- The record's PCA length of the silhouette is 81.3 px, 2% more, because the diagonal of the oblique silhouette
  (top + side) is longer.
- SAM 3 ("chess piece", frame 12) gave length 96.6 px (box 1111–1208 × 533–600). That is 21% too large. The zoomed
  overlay (frames/size_f12.png, red outline) shows the SAM mask is loose and includes grey trough below and beside
  the piece, so it is wrong here. SAM's centroid (1160, 566) is also shifted toward the trough compared with the
  track (1163, 561).
- My first mask (diff to frame 44, size.py) gave 89.5 px because it picked up rim pixels. The cream-colour mask
  (diam.py) gave 75 px because it covers only the bright upper half. I checked both visually and rejected them.

Scale = 0.097 / 79.7 = 1.2171e-3 m/px.

## Acceleration in pixels
The video has duplicate frames (6, 13, 25, 28, 35, 38, 41) and double steps. I used the record's true-render-index
mapping for times.
- Route 1 (fit.py): quadratic fit of s_along_path vs time. Frames 3–39 give 577.5 px/s² (rms 0.68 px), 3–25 give
  587.2, 7–20 give 584.8, 14–39 give 567.2. A fit on the raw frame index (no remapping) gives 583.9.
- Route 2 (fit2.py): linear fit of per-step speeds vs time gives 576.8 (all), 588.9 (≤1 s), 568.5 (0.25–0.8 s).
- The raw single difference at frame 12 (speed(12) − speed(11)) is 530 px/s², but one difference like that is
  dominated by noise. The motion is uniformly accelerated, so I used the fitted constant.

I took a = 580 px/s² (spread ±2%).

## Answer
a = 580 × 1.2171e-3 = **0.706 m/s²**. Range from the fits and scale: 0.69–0.72.
Confidence: fairly good (about ±3%). The main uncertainty is the pixel diameter (79.7 vs the record's 81.3).
