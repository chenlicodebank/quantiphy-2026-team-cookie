# Q57: speed of the turing yellow car at 2.5 s (m/s)

Prior: the white car (the white van) is 6 m long. 2D top-down render, file fps = question fps = 24, so t = 2.5 s is frame 60.
The "turing yellow car" is the record's `tan_car`, the yellow/peach sedan. At f60 it is driving right along the horizontal road at about (1298, 633).

## Scale (white van length)
- At rest at f0 (near the bottom of the image), the van shows a grey front bumper above the white body because of perspective.
  Measurements at f0: SAM 244 px, white body 236 px (record thr25, mine thr25 237), bumper outer edge at y≈800 to the rear at 1047, so about 246 px.
- I used f44, where the van's centre row (y≈640) matches the yellow car's row (633), so the perspective is the same:
  - SAM 236.1 px.
  - My background-difference mask (`van44.py`, bg = f0): thr25 gives 234 px, the white body alone is 232 px, and the dark bumper rim at y≈519-521
    to the rear at 758 gives about 239 px. The zoomed frame (frames/van44.png) shows a thin bumper above the body, which SAM partly cuts off.
  - I took 238 px (bumper to bumper) as the length. mpp = 6/238 = 0.02521 m/px.
- SAM 244 at f0 vs body 236 is a 3.4 pct difference. Zoomed crops (frames/vantop.png, vanrear.png) show it is the bumper,
  which SAM includes, plus extra visible front face from perspective near the image edge. So I did not use f0.

## Car motion (`measure.py`, `speed.py`)
- My centres come from an HSV yellow mask with a min-area-rect centre (`yellow_centres.json`). The SAM centre at f60 (1298.3, 632.8) matches mine (1298.4, 632.9).
- The speed is near-constant: per-frame steps of 6.0-7.2 px, with quantisation jitter. The step at f60 is 6.92 (mine), 7.45 (record) and 4.88 (SAM, jitter).
- Robust local speed:
  - Linear fit over f52-68: 6.79 (mine), 6.76 (record), 6.88 (SAM) px/frame.
  - Mean of the per-frame steps over f55-65: 6.74 / 6.76 / 6.96.
- I took 6.80 px/frame × 24 × 0.02521 = 4.11 m/s.

## Second-route check
Three independent centre tracks give 4.09-4.16 m/s. The scale uncertainty from the van length (236-241 px) is about ±1.5 pct.
Using the f0 SAM length (244) would give 4.01. Confidence: good, about ±3 pct.
