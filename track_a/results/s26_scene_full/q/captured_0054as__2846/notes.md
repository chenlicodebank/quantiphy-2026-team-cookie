# q_2846: orange ball diameter (cm)

Lab video, 1280x720, 24 fps (the file rate and question_fps are the same). f = 0.5959*1280 = 762.8 px, principal point (640,360).
The orange ball is the scene/ record's `basketball`. At t=0.5 s (frame 12) it is free of the person, with d = 2.3557 m.
At t=1.0 s (frame 24) d = 1.81 m, but the bottom of the ball is cut off by the image border.

## Method
- Mask: |frame - clean background| > 60 (background = median of frames 0-5, or 40-48 for the left and bottom
  areas), then an opening and hole filling. At frame 12 this gives a bbox of 77 x 79 px, the same as the scene record.
- Model (`fit_sphere.py`, `traj.py`): the projected silhouette of a sphere (a cone of half-angle alpha around the centre ray),
  with a linear motion blur along the motion direction (fitted at about 5 px). It is fitted per frame (9-25) for the
  centre, alpha and blur. The overlay (frames/fit12.png) matches the mask edge.
  - Frame 12: angular diameter 2 f tan(alpha) = 66.8 px at theta = 26.8 deg off-axis.
  - Without blur, the tangential image extent is 74.8 px. The 77 px bbox includes blur and the oblique elongation.
- How to read depth_info: z-depth (as in the card's back-projection (x,y,1)*depth) or Euclidean distance.
  `traj_analyze.py` tests both:
  - z-depth: the smoothed size curve over frames 11-22, scaled at frame 12, predicts z = 1.816 m at frame 24
    (given: 1.81). The 5-frame smoothed speed at t=0.5 is 2.12-2.31 m/s (prior: 2.21). The centre height
    is constant, as expected for rolling (Y 0.761 -> 0.769 m).
  - Euclidean: predicts 1.763 m at frame 24 (2.6% off), with a speed of 1.89-2.07 m/s. This is a worse fit, so I used z-depth.
- D = 2R:
  - z-depth, frame 12: 23.09 cm (raw fit), 22.78 cm (smoothed size curve).
  - Frame 24 alone (cut-off ball): 21.9 cm (raw), 22.7 cm (smoothed).
  - The card formula, d x tangential extent / f = 2.3557 x 74.8 / 762.8, gives 23.1 cm.
- Other readings, for reference:
  - Euclidean reading: about 20.5 cm.
  - The naive scene bbox width of 77 px, which includes blur: 23.8 cm.
  - If the depth were to the front surface, the result would be about 24 cm.

## Answer
23.0 cm. Confidence: moderate-high. The main uncertainty is how depth_info should be read (about ±5%).
