# q_2955 — velocity of the pizza cutter at 0.2 s (cm/s); prior: money width = 7.5 cm

## Scale (money.py, money2.py)
- Top Monopoly 500 note (frame 0/5): horizontal long side 874→1022-1025 px ≈ 150 px; short side (left edge,
  x≈880-890, colour/luminance profile) y≈196→266 ≈ 69-70 px (scene record said 64; my profile gives ~69).
- "Width" of a banknote = its short side, and 7.5 cm is a typical banknote short side (a 7.5 cm long side is
  not a banknote size). Scale = 7.5 / 69 = 0.1087 cm/px. (If the long side were meant: 0.050 cm/px, answer ~25 cm/s.)

## Time base
- File 24 fps, question_fps 30. The file has 11 exact duplicate frames (2,6,11,...,44) and the cutter's step
  across a duplicate is the SAME as a normal one-frame step (~15-19 px), i.e. the duplicates are inserted padding
  and the 37 unique frames are uniformly spaced original frames. Treated the unique frames as consecutive frames
  of the 30 fps original (the annotator's frame-by-frame forward difference on the original gives one unique step x 30).
  t = 0.2 s -> unique index 6 (file frame 8).

## Motion (vel.py, vel2.py)
- Cutter track from scene/tracks/pizza_cutter.csv (black guard front point and blob centroid), verified on zoomed
  crops of frames 3 and 7 (front point sits on the guard's upper-left end). Camera drift small (~1 px/frame).
- Local linear fits over unique indices 2-10 / 3-9 / 4-8: 16.3-17.1 px/frame (front, raw and stabilised),
  17.0-17.9 (centroid; slightly biased by the growing visible blob). Single forward diff idx 6->7 = 19.7 px (noisy).
- Adopted 16.8 px/frame x 30 = 505 px/s -> 505 x 0.1087 = 54.9 cm/s.

## Check
- Second reference point (centroid) gives 55-58 cm/s; front point raw vs stabilised 53-56 cm/s. Consistent.

## Confidence
- Moderate-low. Main risks: which money dimension the prior refers to (factor 2.2) and the time base
  (if real time were preserved at ~18.5 unique fps the answer would be ~33 cm/s).

Answer: 55.0 cm/s
