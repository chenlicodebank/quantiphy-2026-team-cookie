# q 2690 – width of the tape (cm)

File rate is 24 fps, and question_fps is also 24, so frame = t × 24.

## What I measured
The "tape" is the flat translucent tape roll lying on the table between the glass jar and the cards, at x ≈ 521–592 and
y ≈ 430–474. Its outline is round, so the length and width (the two horizontal extents) are both its outer diameter.
The image width of a vertical cylinder's silhouette is that diameter. (If "width" instead meant the height of the tape
band, which is vertical when the roll lies flat, it would not be a horizontal extent, so I did not use that reading.)

`edges.py` averages the colour channels and rows y = 436–448, where the roll is seen against the flat green background.
It then finds where the brightness crosses half-way between the background and the roll on each side, to sub-pixel
precision:
- frames 0, 12, 24 and 40 give L ≈ 521.2 and R ≈ 591.6–591.9, so the width is 70.40, 70.42, 70.43 and 70.80 px
  (mean 70.5 px). The camera is static, so the value is stable across frames.
- `measure.py` (a threshold mask for each row) gives 65–68 px for the strict-threshold interior, which matches the
  same edges.

## Scale (lab method card)
f = 0.5959 × 1280 = 762.8 px. depth_info at t = 1.0 s puts the tape 1.038 m from the camera.
width = 1.038 × 70.5 / 762.8 = 0.0960 m, which is **9.6 cm**.
Correcting for the off-axis ray would give 9.49 cm. The reference convention does not use that correction, so I kept
9.6.

## Check
At frame 24 (t = 1.0 s, apex 2, little blur) the ball's diameter across its motion is about 25–27 px. At 1.055 m,
that gives 3.5–3.8 cm against the 4 cm prior (28.9 px expected). The ball's blurred edges make this check noisy, but it
agrees with the scale within about 5–10 %. A tape roll about 9.6 cm across is a plausible real size.

Confidence: good. The tape edges are clean against green, with about ±1 px, which is about 1.5 %.
