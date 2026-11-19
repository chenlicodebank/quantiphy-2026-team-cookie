# q_684: acceleration of the moving red general at t = 0.5 s

The file and the question both run at 24 fps, so t = 0.5 s is frame 12. The scene is 2D, viewed from straight above. The prior is a piece diameter of 0.097 m.

## Track (track_mine.py → mytrack.json)
- I tracked the piece on my own: I subtracted frame 44 (the piece is gone by then) in the column x 880–1040, thresholded, closed the mask and took its centroid. My y values match scene/tracks/red_general.csv to within about 0.5 px, and x stays at 959.1–959.3 px throughout.
- The video has duplicated frames, as the record says: the pairs (9,10), (11,12), (18,19), (20,21), (28,29) and (34,35) are identical. The first frame of each pair shows the next frame's position, so I dropped frames 9, 11, 18, 20, 28 and 34 from the fits. A raw one-frame difference at frame 12 would give a speed of 0, so it is not usable.

## Scale (profile.py, sam_check.py)
- Half-level edge profiles of the general give a horizontal diameter of 85.9–86.1 px (frames 12, 13, 24, 30). That direction is across the motion, so there is no blur. The vertical diameter is 85.2 px. My threshold mask gives 87 px.
- The SAM 3 mask ("chess piece", box-prompted) gives 89–94 px horizontally and 89–90 px vertically. That is more than 3 % larger than my measurement. On a zoomed overlay (frames/seg12_zoom.png) the SAM outline lies a few px outside the disc edge and bulges on the left, so SAM is too wide. I used the edge-profile value, D = 86.0 px.
- SAM's centroid matches mine within 0.3 px (for example frame 12: 229.8 vs 229.56).
- The scale is 0.097 / 86.0 = 1.128e-3 m/px.

## Acceleration (fit.py, local_acc.py)
- **Local quadratic fits centred on frame 12 (clean frames only):** half-widths 4–10 give 1.09–1.14 px/frame², about 1.11 on average.
- **Second route, global polynomials:** cubic and quartic fits over frames 2–30 and 2–39 give a(12) = 1.111–1.112 px/frame². The backward-difference convention on the fitted curve gives 1.115.
- The acceleration falls slightly through the clip (about 1.04 over frames 24–39). That is why a single quadratic over the whole clip gives a lower value, 1.08 px/frame² = 0.70 m/s². I used the local value at frame 12.
- Converting 1.11 px/frame² × 576 frame²/s² × 1.128e-3 m/px gives 0.72 m/s².

**Answer: 0.72 m/s².** The local fits span 0.71–0.74, and the whole-clip constant fit gives 0.70. Confidence: good, within about ±4 %.
