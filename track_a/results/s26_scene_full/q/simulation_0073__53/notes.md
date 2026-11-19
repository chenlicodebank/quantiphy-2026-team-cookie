# Q53: side length of the square earthen platform (m)

The video is a 2D top-down scene at 24 fps (question_fps is also 24, so no re-timing). The prior is that the bicycle's speed is 5.33 m/s.

## Scale from the bicycle
- The cyclist moves straight up at a constant speed from frame 1 to frame 71.
- A linear fit to the centroid track (scene/tracks/cyclist.csv) gives 8.916 px/frame.
- A second, independent route used template matching of the cyclist (frame-10 template, frames 10 to 71, sub-pixel peaks) and gave 8.943 px/frame.
- I used 8.93 px/frame, which is 214.3 px/s, so the scale is 5.33 / 214.3 = **0.02487 m/px**.

## Platform size (squares.py, profile.py)
- The "earthen platforms" are the three identical brown squares on the sidewalks (TL, BL, BR). The dark slab at the top is a different object.
- The squares are slightly raised. A thin lighter rim (the platform's side face) appears only on the sides facing the image centre: right and top for BL, right and bottom for TL, and top for BR. That fits a perspective view of a low box with height ≈ 1% of the camera distance, so the magnification effect is about 1%.
- Gradient-peak edges (the top face) give these widths:
  - TL: 78.0 x 77.5 px
  - BL: 77.7 x 77.7 px
  - BR: 77.8 x 77.1 px
  - Mean: 77.6 px.
- The scene record's 80–83 px bboxes include the side-face rim and the blur halo, so they overstate the size.
- The ground footprint (top face shrunk by about 1%) is about 76.8 px. I used **77.3 px** as the side.
- The BL profile read by hand agrees: the top face spans x 369.6 to about 447 (77.4 px), and the rim's outer edge is at x ≈ 453.4.

## Answer
77.3 px × 0.02487 m/px = **1.92 m**. Plausible values run from 1.90 m (footprint) to 1.93 m (top face).

Confidence: moderate to high. The main uncertainty is the edge definition (±1.5 px, about 2%) and whether the reference counts the rim (80 px would give 1.99 m).
