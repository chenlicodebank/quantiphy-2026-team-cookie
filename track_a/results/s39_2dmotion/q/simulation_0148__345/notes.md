# q_345: acceleration of the train at t = 0.5 s (frame 12 at question_fps 24, which is also the file's rate)

Prior: the side windows (not the door windows) are 1.8 m wide. depth_info: none. This is a 2D video, so I used one
metres-per-pixel scale. The scale and the motion are both taken from the near side wall of the train: the window
frames and the body. This matters because the train is close to the camera and its far side moves 0.72 times as fast
in pixels. Because both come from the same layer, the layer choice cancels out.

## Pixel acceleration (accel.py, measure.py)
- measure.py: for each pair of consecutive frames, a normalised correlation of the x-gradient column profile over the
  window band. It gives shifts for frames 7-18 of 355.75, 359.75, 363.75, 366.25, 368.25, 371.5, 376.5, 379.0, 383.25,
  386.25, 387.75 and 391.0 px/frame. These match scene/ to within about 1 px.
- The shifts lie on a straight line: slope 3.215 px/frame² (rms 0.78 px), so the acceleration is steady. Frames 9-15
  alone give 3.295. The raw value d12 - d11 is 3.25.
- Second route: the edges of the same window in two frames give d7+d8 = 713.5 px and d16+d17 = 772.5 px, so a slope of
  3.27 px/frame². I used a pixel acceleration of about 3.23 px/frame², which is about 1860 px/s².

## Window width in pixels (winwidth3.py, outside-in half-level edge scan at y 580-690)
- Window A (frames 6 and 8, the same window): 346.2 and 345.9 px.
- Window B (frame 12, the window visible at t = 0.5 s): 352.3 px.
- Window C (frames 15 and 17): 353.2 and 353.5 px.
- The width depends on which window it is, not on where it sits in the image: frames 8 and 17 are at nearly the same x
  but give different widths. The mean over the three windows is about 350.6 px. I used 350 px, with an uncertainty of
  about 1%.
- SAM 3 masks (maskrows.py): frame 6 gives a median width of 352.5 px and frame 12 gives 359.5 px. Both are about 6-7 px
  (2%) wider than my edge scan, so the gap is under 3%. On the zoomed frames (frames/f6.png, f12.png) the SAM outline
  sits on the thin dark rim just outside the glass, while the half-level edge is the glass boundary. Using SAM's width
  would lower the answer by about 2%, to 9.35.

## Answer
a = 3.23 × 24² × 1.8 / 350 ≈ 9.57 m/s². Depending on which window and fit I use, the range is 9.43-9.63
(9.80 at the extremes: the 3.27 slope with window A). The two routes agree to within 2%.
Answer: 9.55 m/s². Confidence: good, about ±3%.
