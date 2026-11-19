# Q44: speed of the yellow car at t = 2.5 s (m/s)

The prior is that the yellow car's length is 5.44 m. There is no depth_info. This is a 2D top-down render. question_fps and the file's fps are both 24, so t = 2.5 s is frame 60.
There is only one car (a peach/yellow sedan), and it is the object of both the question and the prior. At frames 55–71 it drives right (+x) along the horizontal road with a heading under 4°, at a steady speed.

## Measurements
- `measure.py`: background-difference mask. The mask included a soft halo or shadow (width 105 px), so I rejected it.
- `measure2.py`: colour mask (R−B > 25, limited to the road rows, holes filled). The overlay `frames/own_mask60_color.png` fits the body tightly.
  - Length (PCA extent): 220.6 px at frame 60; the median over frames 55–71 is 220.1 px.
  - Centroid step from frame 59 to 60: 6.77 px.
  - Mean step over frames 55–65: 6.80 px/frame.
  - Linear fit over frames 55–71: 6.81 px/frame.
- SAM 3 "yellow car" segment, frames 59 and 60. The overlay looks clean.
  - Length: 218.4 and 219.5 px.
  - Centroid step from frame 59 to 60: 6.9 px.
- scene/ record: length 222.5 px; step 6.67 px at frame 60, about 6.8 px on average.
- The length readings (219.5 SAM, 220.6 mine, 222.5 record) agree within 1.4%, and the steps (6.77, 6.9, 6.67, fit 6.81) agree within 2%. Nothing differs by more than 3%. I use L = 220.5 px and step = 6.80 px/frame (fit, consistent with the raw backward difference).

## Result
- Scale: 5.44 / 220.5 = 0.02467 m/px.
- v = 6.80 px/frame × 24 × 0.02467 = **4.03 m/s**.

Second route: the raw single-frame backward difference (6.77 px) gives 4.01 m/s. Using SAM's own length and step gives 6.9 × 24 × 5.44 / 219.5 = 4.10 m/s. The speed is roughly constant over the whole clip (about 6.8 px/frame), so it does not depend on the frame window.

Confidence: high, within about 2%.
