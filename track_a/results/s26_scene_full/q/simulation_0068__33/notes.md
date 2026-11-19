# q33 – speed of the yellow car at 2.5 s (m/s)

Prior: acceleration of the white car = 4 m/s^2. 2D top-down scene, 24 fps (file fps = question_fps), t = 2.5 s -> frame 60.
Checked frame 60: white car = van (N-bound, x≈831), yellow car = tan sedan (turned east, now heading east).

## Scale (from the van's pixel acceleration), fit.py
Quadratic fits of van centre y (colour-mask centre ccy) vs frame:
- frames 3-71: 0.2797 px/frame^2; 10-71: 0.2791; 20-71: 0.2775; 3-40: 0.2814; 40-71: 0.2732
- front edge (cbbox_y0): 0.278-0.283; rear edge (cbbox_y1): 0.268-0.283
Adopted a = 0.279 px/frame^2 = 160.7 px/s^2 -> scale = 4 / 160.7 = 0.02489 m/px
(sanity check: van 234 px = 5.8 m, sedan 219 px = 5.45 m; both plausible).

## Sedan speed
Per-frame steps of the sedan centre are near constant all clip (mean 6.85 px/frame over frames 2-71; mean 6.80 over 55-65;
8-frame chord 56-64 = 6.82 px/frame; the single step into frame 60 is 6.15, which is noise of about ±0.5 px).
Used 6.83 px/frame -> 164 px/s -> 164 x 0.02489 = 4.08 m/s.

## Second check
The diff-mask centre (cx, cy) gives sedan 6.78-6.93 px/frame and van acc 0.285 px/frame^2 -> 3.97-4.10 m/s.
Range across methods: 3.97-4.12 m/s. Answer: 4.08 m/s. Confidence: good (about ±3%). The main uncertainty is the van acceleration fit.
