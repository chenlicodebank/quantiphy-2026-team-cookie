# q_1949 — acceleration of the red general chess piece at t = 1.5 s

## Object identification
The only moving object is the cream piece sliding down the wooden ramp. The scene record calls it a "block", but it is
the Chinese chess piece (a disc seen nearly edge-on, so it looks like a capsule). Its long image axis is the disc
diameter, and that axis lies along the motion direction (mask axis −26° to −28°, path −26.0°). The prior's object and
the asked object are the same piece. File fps = question_fps = 24, so t = 1.5 s is frame 36.

## Scale (prior: diameter = 0.097 m)
- Background-difference masks (diff_mask.py; each frame minus a frame where the piece is elsewhere): long axis
  80.6 px (frame 20), 81.1 px (frame 30), 81.2 px (frame 36). The scene record gives a median of 81.3 px (range
  79.6–83.6 px over frames 0–36). Measured by hand on the 4× zoom at frame 36: about 79–80 px.
- SAM 3 (box-prompted "beige object"): 86.9 px (frame 20) and 88.5 px (frame 36), 7–9 % larger. On the 6× zoomed
  overlays (frames/diff_36.png, frames/cmp_20.png), the SAM outline takes in the dark trough rim above the piece and a
  gap at its left end, so SAM is too long. I used my own measurement and the record's (they agree): **81.0 px**.
- Scale = 0.097 / 81.0 = 1.198e-3 m/px.

## Motion
- Track: scene/tracks/block.csv, `s_along_path` (template-matched centre projected on the straight path; ±1 px).
  I checked the track against my own diff-mask centroids at frames 20, 30 and 36: they agree within 1–3 px.
- The clip has duplicated frames (6, 13, 25, 28, 35, 38) and a double step just before each one. A raw one-frame
  difference would be 0 or 2× at these frames, so I used the record's true render-index mapping and dropped the
  duplicates. With that mapping the per-frame steps grow smoothly (2.7 … 38 px), which is uniform acceleration.
- Quadratic fits of s against true time (fit_windows.py):
  - frames 3–36: 582 px/s²; 3–39: 578; 6–36: 580; 12–36: 575; 20–36: 568; 24–36: 555.
  - Late windows that include the partly hidden frames 37–39 fall to 520–530.
  - The slope of the per-frame speed is 575 px/s².
- Adopted acceleration: 572 px/s², giving 572 × 1.198e-3 = **0.685 m/s²**.

## Second route
A three-point divided difference at frames 20, 30 and 36 gives 556 px/s² from the record track and 610 px/s² from my
own diff-mask centroids. That is consistent with the fits, but noisier. The spread of 0.665–0.70 m/s² comes mainly from
the choice of fit window.

## Confidence
Moderate to high: about ±4 % from the fit window and about ±2 % from the diameter in pixels. One assumption: the
reference uses the constant sliding acceleration rather than a raw difference across a duplicated frame.
