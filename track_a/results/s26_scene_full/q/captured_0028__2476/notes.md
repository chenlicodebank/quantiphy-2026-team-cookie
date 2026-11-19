# q_2476 – acceleration of ping pong ball at t = 1.0 s (cm/s^2)

File fps 24 = question_fps 24, so t = 1.0 s is frame 24. The ball is let go at about frame 21 and is in free fall
until it bounces in frame 26, so frame 24 is mid-fall.

## Method (measure.py, crops.py)
- Each frame (18-27): I thresholded the bright, low-saturation blob near the ball. For each frame I recorded the top
  edge, the bottom edge, the bbox width and the midpoint of the streak. I checked the crops visually (frames/fall.png).
- Scale: f = 0.5959 x 1280 = 763 px, and Z = 1.805 m at t = 1.0 (depth_info). The ball's width is 16-18 px through
  frames 18-27, and 763 x 0.04 / 17 = 1.80 m. This matches Z = 1.805 and shows the depth hardly changes during the
  fall. The given 1.557 m at t = 1.1 (the bounce frame) does not match the ball's apparent size, so I did not use it
  for the fall. 1 px = 0.237 cm.
- Pixel accelerations (px/frame^2; multiply by 24^2 x 0.237 cm):
  - top edge, quadratic fit over frames 21-25: 7.86 -> 1070 cm/s^2
  - top edge, frames 22-25 (second differences 9 and 8): about 8.5 -> about 1160
  - streak midpoint, fit over 21-25: 8.25 -> 1124
  - streak midpoint, centred second difference at frame 24: 9.5 -> 1295
  - bottom edge, second differences: 10 and 11 -> about 1400 (stretched by the lengthening blur)
- Gravity (981 cm/s^2) would be 7.2 px/frame^2. All the routes measure more than that, by 10-30 %. The likely
  causes are rolling-shutter stretching of a fast downward motion, plus some downward push from the hand at release.

## Answer
The reference convention is clicked centres, back-projected and smoothed over at least 5 frames. I followed it with
the 5-frame fits of the top edge and the midpoint (1070-1160) and answer about 1150 cm/s^2.
Confidence: moderate (the answer could be 15-20 % from the reference if the reference is plain gravity, 981).
