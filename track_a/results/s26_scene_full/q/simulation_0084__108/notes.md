# Q108: speed of the black and white car at 1.0 s

- 2D top-down render, 24 fps (file fps = question_fps, so no re-timing). t = 1.0 s is frame 24.
- Re-measured both cars myself (`measure.py`, same mask as the scene record, x extents over core body rows). The results agree with scene/tracks to within 1 px.
- Dark (black/white) car: cx = 518.5 at frame 23 and 532.5 at frame 24, so the step is 14 px. The step is constant at 13.5/14 px from frame 2 to the end (mean 969/70 = 13.84 px/frame), and the 14 vs 13.5 difference is rounding noise. Speed = 13.84 x 24 = 332.2 px/s.
- Scale from the yellow car length (5.67 m). Its apparent length shrinks toward the image centre (278 px → 268 px), because the car's height inflates its outline off-centre under perspective. The car's pixel speed stays constant across x, which shows the motion-plane scale is uniform. So I took the near-centre length, about 267–268 px (frame 71: 268 px), giving 0.02119 m/px.
- Speed = 332.2 x 5.67 / 268 = 7.03 m/s.
- Check: if I use the mid-clip yellow length (272 px), the speed is 6.92 m/s. If I use the frame-24 step of 14 px, it is 7.11 m/s. Every variant falls within ±1.5% of 7.03.
- Confidence: high (about ±3%).
