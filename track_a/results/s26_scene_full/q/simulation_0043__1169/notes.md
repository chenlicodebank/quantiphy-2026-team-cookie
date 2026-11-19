# Q1169 — boat speed at t = 1.0 s (frame 24 at question_fps 24 = file fps)

Prior: boat length 10 m. Depths: 173.7093 m at t=1, 174.5515 m at t=2 (boat recedes slowly).

## Method (measure.py)
- I checked the scene/ track (body-mask centroid, mast excluded) on the frame-24 crop, and it covers the boat.
  The motion is a straight line at constant speed from frame 2 on.
- Pixel velocity at frame 24, from a linear fit of the centroid over frames 12–36: (−3.567, −1.064) px/frame,
  so 3.722 px/frame. Fits over frames 18–30 and 2–71 give 3.731 and 3.695.
- Boat pixel extent along the motion direction (the boat heads along its own axis), measured on the mask at
  frames 22–26: 214.4 px. The track's main-axis length is 215.8 px.
- Route 1 (ratio along the same 3D direction, so the foreshortening cancels): 3.722 / 214.4 × 10 m × 24 = 4.17 m/s.
- Route 2 (pinhole with the depths): I back-projected the centroids at frames 24 and 48 using the given depths,
  with the principal point at the image centre. I solved for the focal length that makes the boat 10 m long along
  the 3D motion line: f ≈ 3769 px (HFOV ≈ 16°). The 3D displacement over 1 s is 4.168 m and the local speed at
  frame 24 is 4.176 m/s. This reproduces the 0.84 m/s radial (depth) change.
- The two routes agree to within 0.3%.

## Uncertainty
- If the true 10 m horizontal extent projects a few px shorter, because the stern-bottom corner adds to the
  mask, the speed would be about 1–2% higher.
- Frames 0–1 are identical, which does not affect t = 1 s.

Answer: 4.17 m/s. Confidence high (±3%).
