# q_2656 — basketball velocity at t = 1.3 s (cm/s)

File fps = question_fps = 24, so t = 1.3 s → frame 31.

## depth_info
The t = 1.4 s lines both say "soccer_ball"; one is the basketball. The basketball's pixel diameter (frame 22: 61.2 px median;
frame 34: 65.1 px) times the given depth is constant (85.00 vs 85.03 for 2.7777 m and 2.6020 m), so the basketball is
at 2.6020 m at 1.4 s. The soccer ball, which comes back toward the camera after the collision, is at 2.3730 m.
(Ruler size 23.2 cm with f = 763 gives depths about 4 % larger, 2.89 and 2.71 m. This is a consistent apparent-size bias, and the given depths are used.)

## Method (measure.py)
- Centres come from the scene/ basketball track (RANSAC circle fit). I checked them against my own orange-HSV mask centroid
  and minimum enclosing circle for frames 18-42. They agree within about 1 px; frames 28-35 are unoccluded (fit inlier fraction 0.96-0.995).
- Depth for each frame is linearly interpolated between 2.7777 m (frame 22) and 2.6020 m (frame 34). The other option is depth ∝ 1/radius
  scaled to those anchors.
- Back-projection uses f = 763, principal point (640, 360), and P = d · r/|r|.
- Velocity is the magnitude of the 3D centre displacement per frame × 24, smoothed over windows of 5 or more frames around frame 31.

## Results (cm/s)
- Linear depth with track centres: window 29-33 = 109.9, window 28-34 = 110.3, window 27-35 = 109.4. Raw per-frame speeds are 105-113.
- Second route, linear depth with my own mask centroid: 109.9 / 110.4. With enclosing-circle centres: 108.5 / 110.3.
- Depth from pixel size: 110.2 (window 29-33), but noisier (106-121 depending on window).
- Frames 35→36 contain a dropped source frame. I excluded it from every window.

Answer: **110 cm/s**. Confidence is good, about ±5 %; the main uncertainty is the depth rate (z-component about 35 cm/s).
