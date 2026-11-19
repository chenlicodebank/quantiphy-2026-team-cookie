# q_679: speed of the vacuum cleaner at t = 2 s (m/s)

The video is a 2D top-down render at 24 fps. question_fps is also 24, so t = 2 s is frame 48.
Prior: vacuum diameter = 0.438 m. The vacuum is the white disc. It is the only object that moves.

## Method (measure.py, output in measure_out.json)
- For frames 44–52 and 79 the script thresholds the disc at the mid level between disc and floor, keeps the
  largest component, fits a robust circle to its contour (centre = origin), and finds sub-pixel half-level edge
  crossings through the centre, both horizontally and vertically.
- Diameter in px: the circle fit gives 119.2 (median). The horizontal edge crossings give 120.3, the vertical ones about 120.0,
  and the bbox is 120. The scene record uses a stricter threshold (gray > 185) and gets 117.8, which cuts off the softer rim.
  The SAM 3 mask ("white disc", frame 48) is 120 px horizontally and 127 px vertically. Its bottom edge runs into
  the soft shadow below the disc (seen in the overlay seg_01_f48.jpg and the zoomed frames/f48.png), so I did
  not use the vertical value. The SAM horizontal value (120) agrees with my edge measurement. I used D ≈ 119.2–120.3 px,
  so the scale is 0.438/119.7 ≈ 3.66e-3 m/px.
- Speed (backward difference) at frame 48: |p48 − p47| = 22.19 px/frame. The scene record gives 22.16, which matches.
  This gives 22.19 × 24 × 0.438 / 119.2 = 1.957 m/s with the circle-fit diameter, or 1.940 m/s with the edge diameter.

## Second route
- A central difference over frames 47–49 gives 22.37 px/frame, i.e. 1.956–1.973 m/s. The motion is smooth
  (it accelerates by about 0.4 px/frame per frame here), so the backward difference is the convention I followed.
- Using the scene-record diameter of 117.8 would give 1.98 m/s. So all routes fall between 1.94 and 1.98.

Answer: 1.95 m/s. Confidence is high: the routes agree within about 2%.
