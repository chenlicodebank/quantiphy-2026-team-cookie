# q1380 – thickness of the red blood cell (simulation_0110)

File fps = question_fps = 24, so frame = round(t*24). The depths are given at t=1 s (frame 24) and t=2 s (frame 48) for the left cell.

## Focal length (f_est.py)
The prior speed is 4.7833 m/s, and the motion is constant-velocity: the depth grows linearly and the per-frame steps are smooth.
I back-projected the left-cell centroid at frames 24 and 48 using the given Euclidean distances (17.9557 m and 22.7150 m).
Then I solved for the f at which |P48 − P24| = 4.7833 m:
- **f ≈ 2641 px** using the mask centroid
- 2640 px using the bbox centre

That is an HFOV of about 40°. Caveat: the motion is almost radial (Δd = 4.759 m), so f depends mostly on the ~63 px lateral image shift. A 1 px error there gives about 1.6% in f.

Check: the diameter D = bbox_w·Z/f stays at 1.666 ± 0.01 m over all frames 2–71. Z comes from the given depths, interpolated linearly in time, so the scale is self-consistent.

## Thickness (band.py, draw.py, thick.py)
- The cells are biconcave discs viewed obliquely, at about 20–22° to the disc plane, so the image height (h/w ≈ 0.54) mixes tilt and thickness.
- In a rounded-rim (torus) model, the visible near-rim band has image height ≈ T whatever the tilt. This band runs from the bright rim crest line (the steepest drop of the G channel) down to the bottom silhouette (half-max of redness).
- The upper part (silhouette top to crest), which is (D−T)·sinα, gives α ≈ 22°.
- I measured the band per column over the central 60% of the width, every 3rd frame from 2 to 71. I converted it with the depth of the near rim, Z − R·cosα (about 0.57 m nearer than the origin).

Results:

| Cell | Median band | 90th-percentile band |
|---|---|---|
| Left | 0.423 ± 0.003 m | 0.447 m |
| Right (same Z, equal apparent size) | 0.399 m | 0.419 m |

- The rim is irregular and wavy, so the band varies between columns; overlay checked in frames/draw24.png.
- The crest edge sits slightly below the true crest: the torus model gives a visible band ≈ r(1+cosα) ≈ 0.96·T.
- Answer: **T ≈ 0.435 m**. T/D ≈ 0.26, which is plausible for a red blood cell (real ratio ≈ 0.26–0.32).

## Alternative reading
If "thickness" meant the world vertical extent of a disc tilted toward a level camera, the answer would be about 0.88 m (full silhouette height × Z/f). I rejected this reading: the disc's thickness is its intrinsic short dimension, and with a downward-looking camera and a flat-lying cell, that is also the AABB height.

## Confidence
Moderate. The spread between the cells and the percentile choice is about ±5%, and f carries about ±2%.
