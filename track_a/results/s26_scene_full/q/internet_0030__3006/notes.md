# q_3006 — boat speed between 0.5 s and 1.37 s (prior: speedboat length = 3.2 m)

Method (internet convention: one scale from the prior, planar, pixel tracking):
- Tracks from scene/tracks/boat.csv (bow tip and orange stern marker template tracks). I checked them on 4x zooms of frames 0
  and 29: bow ≈ 607 / 1016 px and stern ≈ 400–405 / 822 px, which matches the CSV to within a few px.
- Camera pans right at about 0.75 px/frame, so I used the background-stabilised x (`*_stab`). The reference point is the
  bow–stern midpoint (the boat's centre).
- Time base: question_fps = 30. Frames round(0.5·30)=15 to round(1.37·30)=41 (the last frame). Mean forward-difference
  speed = 14.67 px/frame (bow 14.49, stern 14.85; raw unstabilised 13.93).
- Scale: the bow-to-stern pixel length falls from 208 px (frame 0) to 190 px (frame 41). The canopy length stays at
  67 px, so this drop is not a zoom. I used the clip mean of 197.8 px (frame 20 = 197.5) → 0.01618 m/px.
- Speed = 14.67 × 30 × 3.2 / 197.8 = 7.12 m/s.

Checks / sensitivity:
- At the file rate of 29.15 fps (frames 15–40): 6.93 m/s.
- Length choice: frame 0 (208 px) gives 6.77 m/s; the mean over the question window (194.5 px) gives 7.24 m/s.
- Bow-only gives 7.03 m/s and stern-only 7.21 m/s.
- All of these fall within ±5% of 7.1.

Answer: 7.1 m/s. Confidence: moderate-high. The main uncertainty is which frame the annotators used to measure the
length (±5%).
