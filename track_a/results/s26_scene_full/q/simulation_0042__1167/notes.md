# Q1167 – eagle wingspan (m)

File fps = question fps = 24. Static near-top-down camera, 1080x1080.

## Scale (solve_f.py)
- Bird centroid track (scene/tracks/bird.csv, frames 2-66) is a straight line in the image; a linear fit
  removes the flap wobble (rms residual 7.7 px). Pixel speed is 16.89 px/frame.
- The fitted positions at frames 24 (t=1) and 48 (t=2) are back-projected with the given depths (179.2691 and
  177.1009 m), with the principal point at the image centre. I solved for the focal length f that makes the 3D
  displacement equal 11.84 m (speed prior x 1 s). Result: f = 6202 px (HFOV about 10 deg), so 0.0289 m/px at
  179.3 m. The radial part of the motion (2.17 m/s) comes from the depths; the lateral part is 11.64 m/s.

## Wingspan in pixels (span.py, crops.py)
- I measured the Feret diameter of the silhouette with a half-contrast threshold (rerun with fractions
  0.2-0.7) for frames 2-66. The flap cycle peaks at frames 5 (55.6 px), 31 (56.7 px) and 54 (63.0 px).
- Frame 54 holds 62-63.8 px at every threshold. The zoomed crop confirms the long, fully extended wings.
- Frames 59-65 sit at about 54 px over very dark water, where contrast is low.

## Answer
- Fully spread = the largest span, at frame 54. Depth at frame 54 is extrapolated linearly to 176.56 m.
- 63.0 x 176.56 / 6202 = **1.79 m**.
- Under the other reading, the mean of the three peaks (58.4 px) gives about 1.67 m. The frame 5 and 31 peaks
  give 1.60-1.62 m. Spans from depth/perspective differ by only about 1 % across the clip, so the gap between
  peaks comes from the wing pose, not distance.

## Check / confidence
- The scale depends on the speed prior plus the depths. Pixel speed is nearly constant (fitted change about
  0.9 px/frame over 64 frames, about 5 %), so the scale is uncertain by about ±3-5 %.
- The main uncertainty is which flap peak counts as "fully spread" (1.6-1.8 m). Confidence: moderate.
