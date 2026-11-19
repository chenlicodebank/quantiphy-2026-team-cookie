# q528: speed of droplet at t=0.2 s (frame 12, 60 fps; file fps = question fps)
- 2D scene; scale from prior a = 9.7 m/s^2.
- I re-measured the drop's top tip myself (diff against frame 13, |diff|>8, in columns 1120-1230) for frames 0-11, and I also used the record's centre track.
- I fitted a quadratic to frames 2-11 (and to 3-11). Pixel acceleration = 28.8-28.9 px/frame^2, residuals under 2 px, rest point at frame -0.07.
- Scale = 9.7 / (28.87*3600) m/px. Frame 12 is below the image, so the step from frame 11 to 12 comes from the fit: 334.1 px/frame.
- v = 334.1*60*scale = 1.871 m/s. All fits (top or centre, start at frame 2 or 3) give 1.869-1.875.
- Check: an ideal free fall from rest at frame 0 gives a backward-difference speed of 9.7*11.5/60 = 1.859 m/s, which agrees.
- Answer 1.87 m/s. Confidence high (within about 2 pct).
