# q_283 – speed of the puck at 0.5 s (m/s)

2D top-down air-hockey render. The file and question_fps are both 24, so t = 0.5 s is frame 12. The camera is static.

## Scale (prior: puck diameter = 0.074 m)
- Own HSV mask (measure.py): bbox 63-64 px, area-equivalent diameter 62.8 px (the anti-aliased rim is partly cut off).
- Subpixel 50%-crossing profiles through the centre (diam_profile.py): 64.2-64.3 px horizontally and vertically on frames 10 and 12.
  (On frame 14 the horizontal profile hits a table marking, so I discarded it.)
- SAM 3 "orange puck" (k=2) on frames 11 and 12: horiz 64 px, vert 64 px (on frame 11, vert is 66 px with a looser outline).
- Zoomed frame (frames/zoom12.png): x ≈ 506-570 and y ≈ 957-1021, so ≈64 px.
- Diameter used: 64.0 px, so the scale is 0.074/64.0 = 1.156e-3 m/px. The sources differ by <1.5% (63.5 in the scene record, 64.2 by profile).

## Motion
- Puck centroid (own mask), frame 11 → 12: y 964.67 → 989.00, step 24.33 px. SAM centroids 964.0 → 988.4, step 24.4 px (agrees to 0.3%).
- The puck moves at constant velocity over frames 2-40: mean step 24.43 px/frame, std 0.46 (single-step jitter comes from mask noise). The scene record gives 24.41.
- Step used: 24.41 px/frame, which is 585.8 px/s.

## Answer
speed = 585.8 × 1.156e-3 = **0.677 m/s**.
Second route: the single backward difference at frame 12 (24.33 px) gives 0.675 m/s. With the record's 63.5 px diameter it would be 0.683 m/s.
Confidence: high (±1.5%). The mallet contact at frames 5-6 is not near t = 0.5 s and does not change the puck's speed.
