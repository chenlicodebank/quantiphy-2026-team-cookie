# q3286: distance from the ball to the nearest player at 2.00 s

**Where the earlier answers differ:** the time base. C1 (2.85 m) used file frame 48. It assumed the file was a
30 fps source with every 5th frame dropped, so that source frame 60 maps to file frame 48. C2 (1.53 m) used frame
round(2.00 x question_fps 30) = 60. The task rules say to time every clip by question_fps
("time t means frame round(t x question_fps)"), and to do so even when the file's rate differs (the file runs at
23.976 fps). So I use **frame 60**, and I reject C1 on this step. Their scales agree (about 6.67-6.70 mm/px).

Frame 60 (look.py on the scene tracks, checked on frames/f60.png):
- Ball at (1045.8, 790.4) px, just after the far player's contact at frames 58/59.
- Nearest player: the far player. Mask centroid (1017.6, 581.3) px, which includes the arm and paddle. Reading the
  crop, the body centre (shirt/torso to hips) is about (997-1005, 565-575) and the hips are about (985, 600).
- Pixel distance: body-centre reading 220-225 px; mask centroid 211 px; C2's SAM body centre 230 px;
  hips 200 px. I use about 221 px.

Scale: court width 6.1 m. At frame 60 the sidelines are at x = 339.9 and 1250.5 (line centres), 910.5 px apart, so
6.70 mm/px. Using the outer edges (~919 px) gives 6.64 mm/px; I take 6.67 mm/px. As a check, the court length of
2011 px against 13.41 m gives 6.67 mm/px, which agrees.

**Answer: 221 px x 0.00667 m/px ≈ 1.48 m.** The body-centre readings span 1.41-1.53 m. I agree with C2's frame and
scale; my reference point is slightly different.

If frame 48 were the intended frame (C1's dropped-frame reading), the answer would be about 2.85 m. I did not use
it because it contradicts the question_fps rule.

Confidence: moderate. The main uncertainty is the player reference point (±5%). The frame convention is decided
by the rule above.
