# Q2007: speed of the mug at t = 0.2 s

- 2D segmentation video, 24 fps (file and question_fps agree). t = 0.2 s → frame round(4.8) = 5.
  Speed is the backward difference between frames 4 and 5.
- I re-segmented the frames myself in `measure.py` (non-white threshold 40, largest component). My positions
  match scene/tracks/mug.csv.
- Scale comes from the prior (g = 9.8 m/s² before 1 s). I fitted a quadratic to the mask-centroid y over frames
  0–18 (free fall, before the impact at f19). That gives a = 8.843 px/frame², so the scale is
  9.8 / (8.843 × 576) = 1.924 mm/px. The fitted release time is −0.10 frame, so the mug falls from rest at t ≈ 0.
- Speed at frame 5:
  - raw centroid step 40.55 px × 24 × 1.924 mm/px = **1.872 m/s**
  - from the fitted curve: 1.876 m/s
- Check: the free-fall model with release at −0.1 frame gives v = 9.8 × (4.5 + 0.1) / 24 = 1.88 m/s.
- The top and bottom edges give 1.78–1.94 m/s. Both are affected by the mug's slight tilt (its apparent height
  changes), so I use the centroid instead.
- Scale caveat: at this scale the mug comes out about 0.21 m wide (with handle) and 0.19–0.21 m tall. That is
  large for a mug, so the mug model is probably oversized. The speed comes straight from the gravity prior
  (v ≈ g·t), so the mug's size does not affect it.
- Answer: 1.875 m/s. Confidence is high (within about 3%).
