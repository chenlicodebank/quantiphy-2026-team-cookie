# Q686 – acceleration of the moving red general at t = 1 s

The file and the question both run at 24 fps, so t = 1 s is frame 24. The scene is 2D (the board is seen from above).
The prior gives the piece diameter as 0.097 m. The asked object and the prior's object are the same moving red
general (帥).

## Scale (diam.py)
- I measured the horizontal diameter, across the motion so that vertical motion blur does not affect it. I used
  half-max edge crossings searched outward from x = 959 on the rows through the disc centre.
- Results: 86.0–86.3 px on frames 0, 1, 14, 16, 22, 24–27, 30 and 32. The mean on the isolated frames is **86.17 px**.
- The scene record's mask bounding box gives 86–87 px, which agrees.
- Scale: 0.097 / 86.17 = 1.1257e-3 m/px.

## SAM 3 check (sam_check.py, crop_overlay.py → frames/cmp_f24.png)
- With a text-only prompt ("chess piece", "wooden disc"), SAM found no instance on the general. With the box prompt
  "game piece" it gave masks with horiz 93–94 px, which is 8 % more than my 86.2 px.
- On the zoomed overlay of frame 24, the SAM outline bulges outside the disc into the dark shadow and halo. My
  86.2 px circle follows the cream disc edge. **My edge measurement is the correct one.**
- The SAM mask centroid sits a constant ~2.8 px lower than my centre (from the shadow). A constant offset does not
  change the acceleration.

## Motion (measure.py → track.json; fit.py, fit2.py)
- I tracked the vertical centre of the disc frame by frame as the midpoint of the half-max top and bottom edges. The
  piece moves only along +y.
- The video has duplicated frames: (9,10), (11,12), (18,19), (20,21), (28,29) and (34,35) are identical. I excluded
  the first frame of each pair because its own position is missing. Frames 22–27, around t = 1 s, are all clean.
- Quadratic fits to the clean frames give the acceleration in px/frame²:

  | Frames | Acceleration | rms |
  |---|---|---|
  | 14–26 | 1.077 | — |
  | 16–33 | 1.066 | 0.05 px |
  | 19–30 | 1.063 | — |
  | 22–27 | 1.066 | — |
  | 22–33 | 1.065 | — |

- A cubic fit over frames 5–33 gives 1.063 at frame 24, so the acceleration is uniform.
- Raw second differences at frames 22–26 are 0.91, 1.32, 0.73, 1.32 and 0.97, mean 1.05. These are noisy (±0.3 px)
  but centred on the same value.
- I take a = 1.066 px/frame² = 1.066 × 576 = 614 px/s².
- Fits on the scene record's mask_centroid_y give 1.067–1.074 px/f², which agrees. Its integer `cy` gives
  1.07–1.11 (rounding noise).

## Answer
a = 614 px/s² × 1.1257e-3 m/px = **0.691 m/s²**.

Second route: the scene record's centroid track with its 86.5 px diameter gives 618.8 × 0.097 / 86.5 = 0.694 m/s².

Confidence: high, about ±2 %. The one-frame backward-difference convention matches the constant acceleration because
the motion is uniformly accelerated.
