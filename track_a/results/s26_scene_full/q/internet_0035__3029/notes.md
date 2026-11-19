# Q3029 — average speed of the toilet paper core, 0 s to 0.83 s (cm/s)

## Time base
The file is 22.297 fps and the question states 30 fps. I used **30 fps**. At 30 fps, 0.83 s is frame round(24.9) = 25, which is
exactly where the tube clears the holder arm's end-plate (frames 24–25). That is the natural end of the "slide along the arm"
phase. At 22.3 fps the end would be frame 19, which is an unremarkable point in the middle of the slide.

## Scale
- The prior is "core size = 100 mm". I took this as the tube's length along its axis.
- In frame 0, the left end is at x ≈ 1718–1720 and the open right end at ≈ 2271–2275, both visible between the fingers. That
  gives **555 px**. I checked the record's value on a gridded crop (view.py → frames/f0.png).
- Scale = 100 mm / 555 px = 0.1802 mm/px. Sanity check: the 260 px diameter gives 4.7 cm, which is realistic for a core.

## Motion (camera is static: grout moves < 1.2 px)
- Reference point: the tube's free left end.
  - Frame 0: x = 1720.
  - Frame 25: x = 2352. I confirmed this on frames/f25.png, where the left end is at ≈ 2345–2355 and blurred.
- Displacement is Δx = 632 px. The centre moves Δy ≈ −48 px, mostly from rotation and the noisy top edge, giving a 2D
  displacement of 634 px. The path is nearly straight, so the net displacement is about the same as the mean of the per-frame
  speeds.
- 632–634 px × 0.1802 mm/px = 113.9–114.2 mm, over 25/30 = 0.833 s, gives **13.66–13.70 cm/s**.

## Second route
The visible-mask centroid moves 1966.2 → 2595.5 (629 px), giving 13.6 cm/s. This agrees with the main route.

## Alternative
If the 22.3 fps time base were used instead (frames 0 → 19, 376 px), the answer would be ≈ 8.1 cm/s. I rejected it for the
reason given above.

## Answer
13.7 cm/s. Confidence is moderate to good; the main risk is the time base.
