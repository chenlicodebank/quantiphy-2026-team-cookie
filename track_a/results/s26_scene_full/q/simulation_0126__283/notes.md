# q_283: speed of the puck at 0.5 s (simulation_0126, 2D top-down air hockey)

- Time base: 24 fps (the file and the question agree). t = 0.5 s → frame 12.
- Puck motion (measure.py, my own HSV mask re-tracking): the puck moves straight down at a constant rate over frames 2-40. Step 11→12 = 24.40 px, and the mean step over frames 2-40 is 24.41 px/frame (the scene record agrees). Frames 5-6 are disturbed by the mallet contact (26.5/22.3), but their sum is normal. Frame 12 is far from that contact and from the bounce at frame ≈40.5.
- Scale (diam.py): I measured the puck's diameter at subpixel precision with a fractional-coverage "orangeness" (R−B) area and with the radius where the radial profile reaches half its level, on frames 0/10/12/14/20/28. Both give 64.6-65.3 px, mean ≈64.8 px. The thresholded mask gives 63.8 px, which is too small because the darker anti-aliased rim is cut off. So the scale is 0.074/64.8 = 1.142e-3 m/px.
- Speed = 24.41 px/frame × 24 × 1.142e-3 = **0.669 m/s**.
- Second route: the single-frame step 24.40 px gives 0.669 m/s. With the mask diameter (63.8 px) it would be 0.680 m/s. The uncertainty is about ±1.5 % and comes mainly from where the edge of the diameter is taken.
- Confidence: high.
