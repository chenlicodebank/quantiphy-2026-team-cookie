# q_1831 — speed of the right (last) ball at t = 2 s

The file and the question both run at 30 fps, so t = 2 s is frame 60. The scene is a 2D Newton's cradle and the asked ball is ball_right, the ejected ball. At frame 54 it is at its apex. At frame 60 it is swinging back down to the left.

## Measurements (measure.py, speed.py)
- measure.py thresholds each frame (any channel < 235), takes the rightmost ball component and fits a least-squares circle to its densified convex hull. The centres match scene/tracks/ball_right.csv to within 0.01 px.
- Raw backward difference at frame 60: |p60 - p59| = 6.79 px/frame.
- speed.py fits a circle to the swing path (pivot (1308.7, 240.3), R 552.5 px, rms 0.18 px). It then fits polynomials to the angle over windows of ±5 to ±13 frames and takes the backward difference of the fitted positions: 6.76–6.92 px/frame. Cubic fits to x and y directly give 6.88–6.92 px/frame. **Adopted: 6.85 px/frame.**
- Scale: diameter = 2 m. The pixel diameter is 164–165 px near the image centre: the middle ball's fit is 163.8 px, the right ball at rest is 164–165 px (eqd and width). At x ≈ 1643 the ball looks elongated by perspective: width 169 px, eqd 167.4 px, height 164 px. The in-plane scale f/Z matches the near-centre diameter, so I use 164.5 px, which gives 0.01216 m/px.
- Speed = 6.85 × 30 × 2 / 164.5 = **2.50 m/s**.

## SAM 3 check (phrase "grey ball", frames 59 and 60)
- The overlay shows the right ball outlined cleanly (k0).
- SAM centroids are (1648.7, 676.5) at frame 59 and (1643.0, 680.5) at frame 60, a step of 6.96 px/frame. That is within 2 % of my 6.85.
- SAM extents at frame 60 are 167 px horizontally, 163 px vertically and 166.4 px across the minor axis. My mask gives width 169, height 164 and eqd 167.4. These agree to within 3 %.

## Second route and sensitivity
- Using the local equivalent diameter (167.4 px) instead of 164.5 px gives 2.46 m/s. Using the raw difference with SAM centroids gives 2.54 m/s.
- The spread is about ±2 %. Confidence: high.
