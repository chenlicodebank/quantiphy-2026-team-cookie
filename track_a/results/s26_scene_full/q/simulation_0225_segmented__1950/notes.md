# q_1950 — length of the black cat (incl. tail)

The prior is the black cat's speed, 1.041 m/s. The video is 2D-style: the cat walks left to right, parallel to the image
plane, and its pixel size stays constant. Both fps values are 24.

## Scale (from the speed prior)
- Record centroid track (scene/tracks/cat.csv): linear-fit slope 5.403 px/frame in x and -0.05 px/frame in y.
  The bbox left and right edges both give 5.42 px/frame.
- My own dark-fur centroid (measure.py, my own segmentation): 5.372 px/frame.
- Using 5.40 px/frame × 24 = 129.7 px/s gives 1.041 / 129.7 = 0.00803 m/px.

## Cat length
- Length is the horizontal bbox extent along the walking direction. The tail is raised, so it adds little.
  The zoomed frame 15 shows the tail at x≈603 and the head at x≈705, so the bbox is about 103 px.
- Record median over 50 frames: 107 px (range 103–123; the larger values come from leg or tail pose).
  My own mask gives a median of 109 px. It sometimes includes lounger legs the cat passes, so I prefer the record's
  cleaner value.
- 107 px × 0.00803 m/px = **0.86 m**.
  - With my mask's median: 0.88 m.
  - With the minimum width: 0.83 m.
  - With the dark-centroid speed: 0.864 m.

## Check
Two independent speed routes (record centroid and bbox edges vs. my dark-fur centroid) agree within 0.6%.
The length is in the same horizontal image direction as the motion, so any perspective effect cancels.
Confidence: moderate–good (about ±5%); the main uncertainty is which pose the reference bbox used.
