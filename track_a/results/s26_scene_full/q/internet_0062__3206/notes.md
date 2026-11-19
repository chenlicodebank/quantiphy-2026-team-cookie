# q 3206 – velocity of the wallet at 2.60 s

- 2D internet clip, 30 fps (file fps = question_fps; the free fall gives a constant acceleration, so the rate is consistent).
  Footage is rotated: gravity points along image +x. Camera static during the fall (<0.5 px).
- The wallet (black pouch) is released at frame 66 and falls freely until frame 80; it hits the baseboard at frame 81.
  t = 2.60 s → frame 78 (inside the free fall).
- measure.py: my own dark-pixel mask (V < 70, largest component, wall area x < 1437), centroid per frame 64-80.
  It agrees with scene/tracks/pouch.csv to < 0.3 px for frames 68-80.
- Scale from the prior (g = 9.8 m/s²): quadratic fit of centroid x vs frame gives a = 11.70 / 11.79 / 11.85 px/frame²
  (fits from frame 67 / 69 / 71 to 80); second differences ~11.0-12.5. Using 11.79 px/frame² = 10611 px/s²,
  scale = 9.8 / 10611 = 0.000924 m/px.
- Velocity, forward difference as the annotators did: cx(79) - cx(78) = 146.5 px/frame = 4395 px/s → 4.06 m/s
  (4.04-4.09 across the three scale fits).
- Check: the quadratic fit's derivative at frame 78.5 (the midpoint of that forward step) gives 4.05 m/s, which matches.
  The instantaneous fitted velocity at exactly frame 78 is 3.89 m/s, and the backward difference is 3.72 m/s.
  These are lower because the answer follows the forward-difference convention.
- Answer: 4.05 m/s. Confidence: good. The main uncertainty is the convention (forward difference vs instantaneous, about 4%).
