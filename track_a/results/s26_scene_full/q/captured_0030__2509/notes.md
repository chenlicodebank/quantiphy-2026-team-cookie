# q_2509 — red ball velocity at t=0.4 s (frame 10), cm/s

File fps = question_fps = 24, so t=0.4 s is frame 10. I took the depth anchors at frames 5, 10, 14 and 19 (t = 0.2, 0.4, 0.6, 0.8 s). The "0.8715s" in depth_info is read as metres.

## Method (vel.py)
- Ball centres (cx, cy) come from scene/tracks/ball.csv. I checked frames 9–13 on zoomed crops (frames/f9_13.png, crops.py) and the centroids sit on the ball. The 11→12 jump (51 px, against 15 and 31 px either side) shows up in the video itself, not as a tracking error.
- Lab intrinsics: f = 0.5959·1280 = 762.8 px, principal point (640, 360).
- I interpolated the depth (Euclidean camera–ball distance) between the four depth_info anchors (linear or cubic spline), converted it to z, and back-projected each centre to 3D.
- I then took the velocity at frame 10 with smoothing over at least 5 frames, two ways:
  - Quadratic fit to the 3D positions, window ±2 to ±4 frames: 146–148 (linear depth) and 153–163 (spline depth).
  - Mean of the 5-frame forward differences over frames 8–12: 165 (linear) and 176 (spline). This window includes the 11→12 jump, which pushes it up.
- Most of the speed comes from the change in depth. depth_info alone gives about 1.3–1.4 m/s radially (0.2945 m over frames 5–10, 0.206 m over frames 10–14). The image-plane motion adds about 0.4–0.6 m/s across that.
- Check: depth worked out from the ball's apparent size (7 cm prior) is noisy per frame (±10–15%). It roughly agrees with depth_info (0.76/1.05/1.40/1.44 m against 0.87/1.17/1.37/1.32 m), so I didn't use it for the speed.

## Answer
About 155 cm/s, a value in the middle of the 147–165 cm/s range from the methods above. Confidence is moderate (±10%): the main uncertainty is how the depth changes between the anchors.
