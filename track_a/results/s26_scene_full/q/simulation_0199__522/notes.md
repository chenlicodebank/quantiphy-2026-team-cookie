# Q522: droplet speed at t = 0.1 s

- 2D render at 60 fps (the file and the question agree, so there is no re-timing). t = 0.1 s is frame 6. Speed = |p6 - p5| x fps.
- Scale comes from the prior, a = 9.7 m/s^2. The pixel acceleration is the slope of the per-frame step lengths against frame number:
  about 31.5 px/frame^2 = 113,300 px/s^2, so the scale is 9.7 / 113,300 = 8.56e-5 m/px.
- Track: scene/tracks/droplet.csv (mask centroid, with frame 13 as the background). I checked it: the steps are
  17.1, 48.3, 81.0, 111.5, 145.2, **176.0** (5 to 6), 207, … px, which are close to linear.
  My own quick re-segmentation (measure.py) is noisier (its mask width jumps between 29 and 53 px) but gives the same pixel acceleration (30.5–31.4) and v6 = 0.90–0.93 m/s.
- v6 = 176.0 x 60 x 8.56e-5 = 0.904 m/s from the raw backward difference. A linear fit of the steps gives 0.899. The bbox centre gives 0.896–0.905.
  Changing the fit window (frames 1–10, 2–8, 3–8) keeps the answer between 0.896 and 0.910.
- The answer is scale-free in effect: v = a x step6 / (A x fps).
- Answer: **0.90 m/s**. Confidence is high (±2%).
