# Q147: distance between the big bird (eagle) and the small bird (crow) at 0.3 s

- Time: fps = question_fps = 24, so t = 0.3 s is frame round(7.2) = 7.
- Treated as a 2D scene: both birds fly horizontally in one plane, side-on, and there are no perspective cues. One m/px scale is used for both birds.
- My script `measure.py` re-segments the frames by background difference (threshold 15, 3x3 opening). Its results match scene/tracks exactly.

## Positions at frame 7
- Eagle: it is cut by the left edge at frame 7, but its tail end (bbox x1) is still clean: 817, 817, 688, 560, 432, 304, 176, 48 for frames 0-7, a steady 128 px/frame.
  - On unclipped frames the body centre is 74.5 px left of the tail end (frame 0: 742.5 vs 817). So the eagle centre at frame 7 is x = 48 - 74.5 = -26.5 px (just off-screen), with y ≈ 588.
- Crow: its beak end x1 goes 1198 -> 1903 over frames 1-10, which is 78.33 px/frame. The tail end x0 gives the same rate. The centre at frame 7 is x = 1624, y ≈ 593.
- Separation: dx = 1650.5 px and dy ≈ 5 px, so 1650.5 px.

## Scale
- The crow speed of 11 m/s corresponds to 78.33 px/frame x 24 = 1880 px/s, so the scale is 0.005851 m/px.
- The distance is 1650.5 x 0.005851 = 9.66 m.

## Second-route check
- Extrapolating the eagle's body_cx track instead (105 at frame 6, minus 128) gives -23. That puts the separation at 1647.5 px, or 9.64 m.
- Taking the crow speed as the mean of the per-frame centroid steps (78.4) gives 9.65 m.
- Sanity check: the eagle speed comes out at 128 x 24 x 0.00585 ≈ 18 m/s, which is plausible.

Confidence: high. The remaining uncertainty is where each bird's origin sits relative to its pixel extent (about ±3 px, under 0.5%).
