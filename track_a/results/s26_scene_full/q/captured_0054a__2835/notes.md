# Q2835 – white ball diameter (cm)

Video is a lab capture at 24 fps (file fps = question fps = 24), 1280x720, focal length f = 0.5959*1280 = 763 px.

## Which ball is the "white ball"
depth_info at t=1.0 s (frame 24) gives white 3.0735 m and green 3.0390 m. Those are the two small balls the standing
person throws (in flight at frame 24, near the back wall). Green = the yellow-green tennis ball. White = the pale
white/pinkish-grey ball (scene/ tracks/pale_ball.csv). The soccer ball is at the seated person, closer to the camera (66 px;
at 3.07 m it would come out at 27 cm, which is not plausible), so it is not the ball asked about.

## Measurement (frames 23-29, where the ball is in free flight against the plain grey wall)
Background = median of frames 0-12 and 44-48. Colour-distance image |frame - bg|. The ball has a bright top and a
dark shaded bottom, with low contrast at the terminator. The scene/ track mask only covered the bright top (bbox h ≈ 10 px), so it is too small and I did not use it.
Motion blur is small (the parallel and perpendicular extents are nearly equal), so the exposure is short.
- profile.py / perp.py: half-max widths of profiles through the refined centre. Vertical extent: f24 17.9, f25 16.6, f26 17.2,
  f27 16.9, f28 17.7 px (mean 17.3).
- rays.py: half-level edge points on 72 radial rays, then a circle fit: f24 18.1, f25 17.3, f26 17.9, f27 18.2 px.
- circfit.py: threshold masks. thr20 gives 17.3-18.5 px (lower thresholds pick up the compression halo).
Best estimate is about 17.6 px (±0.6) at frame 24. Size = 3.0735 * 17.6 / 763 = **7.09 cm**.

## Check
With the same methods the tennis ball (green, 3.039 m) measures 16.0 px (profiles) to 17.2-17.8 px (rays) at f24-26, which gives
6.4-7.1 cm. A real tennis ball is 6.7 cm, so the pipeline is consistent to about ±5%. The pale ball's size is steady over f24-27, so the
depth is about constant around t=1.0 s.
Answer 7.1 cm (range 6.95-7.3). Confidence moderate to good, about ±5%.
