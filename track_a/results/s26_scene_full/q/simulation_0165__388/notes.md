# q388 – bike length (m)

2D video, 24 fps (file fps = question_fps). Prior: bike speed 5.52 m/s. The bike moves parallel to the image at
one depth (constant pixel size and y), so a single m/px scale applies.

- Speed (pixels): straight-line fits to the hub positions over the 44 clean frames (scene/tracks/cyclist.csv):
  rear hub 21.015 px/frame, front hub 21.023 px/frame -> 504.45 px/s. Scale = 5.52 / 504.45 = 0.010943 m/px.
- Bike length (pixels): rear tyre edge to front tyre edge, from dark tyre pixels at hub height (measure.py).
  Frames 44, 50, 56 and 60 all give 161 px. Frames 64-72 gave 210 px because a dark background pole fell inside
  the search window, so I dropped them. The zoomed view of frame 60 (frames/f60.png) shows the same thing by eye:
  x 1136 to 1297.
- Check: wheelbase 95.5 px + tyre diameter about 66 px = 161.5 px, which matches. The box around bike and rider
  is 163 px (1.78 m), so the rider barely extends beyond the wheels.
- Length = 161 x 0.010943 = 1.762 m, a realistic size for a bicycle.

Confidence: high (about ±2%).
