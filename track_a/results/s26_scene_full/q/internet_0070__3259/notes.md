# q3259 – length of the speedboat (prior: v = 11 m/s at t = 1.00 s)

Time base: t = 1.00 s gives frame 30 at either 29.97 or 30 fps; I used 30 fps (question_fps) for px/frame -> px/s (the 0.1 % difference doesn't matter).

Method (internet convention, one scale from the prior):
- Pixel speed at f30 from the scene record's sub-pixel template tracks (`scene/tracks/boat.csv`), with the camera pan
  removed (background shift bg_dx; the camera pans right, adding about 0.45 px/frame). Light smoothing: a linear fit over f26-34.
  - canopy: 15.82 px/frame bg-compensated (15.41 raw); bow tip: 15.78 (15.37 raw). Forward differences at f30: 15.70 / 16.26 bg-compensated.
  - v = 15.82 x 30 = 474.6 px/s -> scale = 11 / 474.6 = 0.02318 m/px.
- Boat length at the same time (f30), bow tip to stern end (the flag edge; spray hides the transom): 218.7 px in the record,
  and I checked it by eye on a 4x zoom of f30 (flag edge at about x 182, bow tip at about x 399 -> about 217 px).
- Length = 218.7 x 0.02318 = 5.07 m.

Second route / spread: other reference points and difference schemes give 4.78-5.26 m (bow forward difference 4.93,
uncompensated canopy 5.20). A 5 m bowrider is realistic. Caveat: the boat's pixel length shrinks over the clip (228 px to 179 px, a yaw
change), so I measured the length at the prior's time. If the annotators used a later frame (about 200 px), the answer
would be about 4.6 m.

Answer: 5.07 m. Confidence: moderate (±5-8 %).
