# q_2362 — velocity of the yellow toy at t = 0.60 s (cm/s)

Answer: **290 cm/s** (≈ 2.9 m/s).

## Setup
- Lab video, 24 fps (file fps = question_fps = 24), 1280x720, f = 0.5959*1280 = 763 px, c = (640,360).
- t = 0.60 s -> frame round(14.4) = 14 = the release frame of the yellow toy (a yellow carrot toy with green
  top; thrown by the far person to the near person, free flight 14-26, hand contact from ~24-26).
- The yellow toy is the "carrot" in depth_info: distance 2.63 m at t = 0.60 (the white object = jar, 1.9735 m).
- Prior g = 9.8 m/s^2 is used as the flight's acceleration.
- scene/ track for yellow_toy checked on zoomed crops (frames/toy_tiles.png): centroids are on the toy;
  frames 24-26 are contaminated by the catching hands (track jumps by ~20 px from a ballistic path), 18 is
  occluded by the white object -> both excluded from fits.

## Method
Only one depth is given, so the depth rate (radial velocity) must come from physics:
1. Camera pose from the two standing people (cam.py): feet pixels on the floor, pelvis ~0.9 m above the
   feet, given distances 1.58 m and 3.237 m -> camera height ~1.89 m, pitch 39.6° down (38.5-41.8° for pelvis
   0.8-1.1 m), no roll. So gravity direction in camera coordinates is known.
2. Ballistic 3D fit (world3.py / sens.py): P(t) = P14 + V (t-t14) + ½ g t², P14 = 2.63 m along the
   frame-14 pixel ray (small free pixel offset), g = 9.8 m/s² along the camera-frame down vector, V free.
   Fitted to the toy's image centroids frames 14-23 (minus 18): rms 1.3 px (very good).
   |V0| = 2.95 m/s; forward diff 14->15 = 2.83 m/s; 5-frame centred smoothing (forward diffs 12-16) = 2.86 m/s.
3. Sanity of the 3D solution: release point 0.97 m above floor, 0.9 m in front of the far person; extrapolated
   catch point (frame 26) 0.6 m in front of the near person at 2.16 m distance; the white jar's fitted release
   (1.97 m given) is likewise 0.62 m in front of the near person -> consistent geometry.

## Sensitivity / second route
- Pitch 36 / 39.6 / 42 / 46°: |V| at frame 14 = 2.70-2.82 / 2.83-2.95 / 2.92-3.05 / 3.08-3.22 m/s. The toy fit
  and the jar's fit both slightly prefer a higher pitch (rms falls), and the people's body-axis vanishing
  point suggests ~44-46° -> centre taken slightly above 39.6°, ~2.9 m/s.
- Roll ±4°: ±5%. Frame subsets (14-20 … 15-23): 2.6-3.0 m/s.
- Free-gravity-direction fits (fit.py, fit3.py) are degenerate (depth along the line of sight is weakly
  constrained by the image track alone), which is why the camera pose from the people was used.
- Lateral (image-plane) part alone: 23.8 px/frame at 2.63 m = 1.97 m/s (lower bound); the remaining part is
  the toy approaching the camera (radial ≈ -2 m/s).
Confidence: moderate (±10-15%), dominated by the camera pitch / roll uncertainty.
