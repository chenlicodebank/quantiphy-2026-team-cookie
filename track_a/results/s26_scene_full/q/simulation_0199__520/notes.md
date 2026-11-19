# q520: droplet speed at t=0.2 s
- 2D render, 60 fps (file and question agree). t=0.2 s is frame 12, but the drop leaves the frame after frame 10, so the speed is extrapolated from the constant-acceleration fall.
- measure.py re-tracks the drop at full resolution (difference from frame 13, threshold 25). The centroids match scene/tracks/droplet.csv to within about 1 px.
- A quadratic fit of the centroid y over frames 2-10 gives a_px = 112744 px/s^2. Scale = 9.7 / a_px = 8.60e-5 m/px.
- The fit puts the release at t0 = -0.002 s, i.e. effectively at frame 0. The extrapolated step from frame 11 to 12, including the small leftward drift, is 363.3 px, so speed = 363.3 x 60 x scale = 1.875 m/s.
- Check: fitting the top edge instead gives 1.864 m/s. Analytically, g(11.5/60) = 1.859 m/s with release at t=0. (The bottom-edge fit, 1.945 m/s, is thrown off by pedestal-edge noise at frame 4 and is not used.)
- Answer 1.87 m/s. Confidence high (about +-1.5%).
