# q_2764 — velocity of the white ball at 1.4 s (cm/s)

- "White ball" = the white oblong toy, the only moving object (scene/tracks/white_toy.csv). File fps = question fps = 24,
  so t = 1.4 s means frame round(33.6) = 34.
- Frame 34 is right after the hidden first bounce (frame ~33, behind the tape roll and card tent). Frames 32, 34 and 35 are partly occluded.
  I checked crops of frames 30-38 (crops.py → frames/) and corrected their centres by eye: 32 (572,421), 33 ≈ (622,465) (impact, guessed),
  34 (660,440), 35 (694,400). The others come from the track.
- Camera: f = 0.5959·1280 = 763 px, principal point (640,360). Depth taken as linear in time through the given values
  (frame 36: 0.7045 m, frame 48: 0.627 m) and extrapolated back to frames 30-35 (≈0.73 m). The point is back-projected along the
  unit ray × Euclidean distance (vel.py).
- Per-frame forward 3D speeds (cm/s) for frames 30-38: 138, 146, 152, 103, 118, 163, 70, 90, 109. These are noisy: the 35→36 step is
  61 px but 36→37 is only 32 px.
- Estimates around frame 34:
  - mean of forward speeds over frames 32-36: 121
  - central difference (36-32)/4: 109
  - post-bounce (37-34)/3: 111
  - (36-34)/2: 139
  - physics check: post-bounce apex at frame ~36.3, so vy ≈ g·2.3/24 ≈ 0.94 m/s; with vx ≈ 0.7-1.0 the speed is ≈ 1.2-1.3 m/s.
- Answer: 120 cm/s. Confidence is moderate (±15 %), because the bounce falls inside the smoothing window and frame 34 is partly occluded.
