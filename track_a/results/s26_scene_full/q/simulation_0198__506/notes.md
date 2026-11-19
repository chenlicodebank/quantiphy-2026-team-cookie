# Q506: horizontal length of the droplet (m)

2D Blender video, 2560x2560, 60 fps (the file fps and question_fps agree). The camera is static. Prior: the droplet's acceleration is 9.7 m/s^2.

## Method (measure.py)
- I made a background-difference mask against frame 13, where the drop is gone. It is the largest component, with holes filled. I tried thresholds 10, 18 and 30.
  Threshold 10 gives the fullest mask. I drew the contour on frame 3 (frames/f3_mask.png) and it hugs the teardrop.
- Pixel acceleration comes from a quadratic fit of the centroid y against time:
  - frames 0-6 (uniform render steps): a = 114,055 px/s^2, residual 0.28 px.
  - frames 1-6: 114,003 px/s^2.
  - all frames 0-10 with the scene record's render-index mapping (frame 7 is a duplicate and render step 8 is missing): 114,151 px/s^2.
  - The horizontal part, about 1,200 px/s^2, changes the magnitude by less than 0.01%.
- Scale: 9.7 / 114,055 = 8.505e-5 m/px.
- Horizontal extent (bbox width) in frames 0-9: 59-61 px at threshold 10 and 57-59 px at threshold 18. The scene record gives a median of 59.
  I used 59.5 px. Frame 10 is on a dark background and reads low, so I left it out.

## Answer
59.5 px x 8.505e-5 m/px = 5.06e-3 m.

## Check
Independent fits (frames 0-6, frames 1-6, and the remapped frames 0-10) give accelerations within 0.15% of each other. The scene record's step of 31.6 px/frame^2, which is 113,760 px/s^2, is within 0.3%.
The width uncertainty (±1 px, about 2%) dominates.

Confidence: high, about ±3%.
