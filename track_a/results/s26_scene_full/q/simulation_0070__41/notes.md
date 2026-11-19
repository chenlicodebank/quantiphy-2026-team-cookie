# Q41 – speed of the yellow car at t = 2.5 s

- 2D orthographic top-down render, 24 fps (file and question rate agree). t = 2.5 s -> frame 60.
- The "yellow car" is the only car in the clip: the peach/yellow sedan, which turns right into the horizontal road.
  At frame 60 it is almost straight (axis about 1 deg).
- Scale: car length 5.44 m. Pixel length is 219 px: record PCA 218-220, and my own paint-mask bbox x-extent is
  219.3 px over frames 66-71 while the car is horizontal. So 0.02484 m/px.
- Pixel speed: record centroid steps are 6.74 px at f60 and 6.77 mean over f56-64; the whole-clip mean is
  6.83 ± 0.18 (motion is near-constant). Second route (measure.py, bbox-centre of the paint mask):
  6.875 px/frame mean over f56-64. I used 6.82 px/frame.
- Speed = 6.82 / 219 x 5.44 x 24 = 4.07 m/s. The routes range from 4.00 (single-frame step) to 4.09 m/s.
- Confidence: high (about ±2%).
