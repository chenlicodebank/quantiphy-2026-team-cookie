# Q344: speed of the train at t = 0.5 s (m/s)

Prior: side window width (not the door windows) = 1.8 m. The video is 2D, 24 fps, and question_fps is also 24, so t = 0.5 s is frame 12.
Speed = (near-layer shift from frame 11 to frame 12, in px) x (1.8 m / side-window width in px) x 24.
The windows are openings in the train's near wall, so they lie in the same layer as the near-layer shifts in scene/.
The far-side graffiti seen through the windows moves at about 0.72x that rate and is not used. Using one layer for both
the scale and the shift removes the perspective ambiguity.

## Side-window width (px)
- `rowedges.py`: for each row y 500-700, I found the subpixel edge from the dark body to the bright interior and took the
  median width per row (threshold 30):
  f6 345.6, f8 345.3, f9 349.6, f12 351.0, f14 351.6, f17 353.4. Mean 349.4.
  (`winedges.py` measures at the top and bottom strips, where the rounded corners trim the width, so it gives about 332-340. Not used.)
- SAM 3 "train window" masks (`samrun.py`, plus f12), horizontal extent: f6 355, f8 348, f9 353, f12 354, f14 354, f17 356.
  Mean about 353.
  SAM is about 1-1.5 pct wider than my edges because it includes the light rim/glow at the frame (seen in the zoomed f12 crop,
  `frames/f12z.png`). That is under 3 pct. Adopted W = 352 px (between the two methods; f12 itself gives 351.0 from my edges and 354 from SAM).

## Shift at frame 12 (px/frame, near layer)
- `shift12.py`: window C left edge, same rows 640-715. At f11 it is at x 1840.9-1843.2, partly clipped by the arch
  above row 600. At f12 it is at x 1467.9-1468.7. d12 = 373.1 / 374.5 (thresholds 25 / 30).
- scene/ NCC record: d12 = 371.6 measured. The line fit d(i) = 334.10 + 3.199 i gives 372.5.
- Check of the record against my edges: d13 = 376.0-377.3 (fit 375.7), d14 = 378.4-378.6 (record 379.7, fit 378.9).
  SAM window right edges give f12 1821.8, f13 1446.8 and f14 1066.8, so d13 = 375 and d14 = 380. These agree.
- Adopted d12 = 373 px (±1.5).

## Result
speed = 373 / 352 x 1.8 x 24 = 45.8 m/s.
- Range over the method choices: (W 349.4, d 372.5) -> 46.1, and (W 354, d 374.5) -> 45.7.
- Second route: the record's line fit with the SAM width gives 372.5/354 x 1.8 x 24 = 45.5. With my edge width it gives 46.1.
- The train accelerates steadily (about 3.2 px/frame²), so this speed is specific to frame 12.

Confidence: high. The estimate should be within about 2 pct, with the remaining doubt being whether the window
edge sits at the glass or at the frame rim (about 1 pct).
