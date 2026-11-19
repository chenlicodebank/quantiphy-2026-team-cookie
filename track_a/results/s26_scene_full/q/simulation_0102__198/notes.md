# Q198 – boat length (m), simulation_0102 (2D)

Prior: shark acceleration = 1 m/s^2. fps = question_fps = 24, so no re-timing.

Method: a single metres-per-pixel scale from the shark's pixel acceleration, applied to the boat's pixel length.
- Shark acceleration: I fitted a quadratic to x(frame) over frames 2–59, after the motion starts at f2 and before the
  shark leaves the frame at f60.
  - My track (`measure.py`, background difference, mask > 60): nose −0.150, tail −0.150, centroid −0.150 px/frame^2.
    Over sub-windows (2–30 and 30–59) the values are 0.137–0.155.
  - The scene record's tracks give ref_x 0.150, nose 0.152 and tail 0.161 (2–60).
  - Adopted value: 0.1505 px/frame^2 = 86.7 px/s^2. Scale = 1/86.7 = 0.01154 m/px.
- Boat length (stern to bow, horizontal bbox on frame 0): 857 px from my integer-pixel mask (231–1087) and 854 px
  from the record's sub-pixel edges. I used 855 px.
- Boat length = 855 / 86.7 = 9.86 m. The range across the length estimates is 9.85–9.89 m. A ~10 m fishing boat
  is plausible.

Second route: the tail, nose and centroid tracks and the record's own tracks all agree on the acceleration to within
about 2% (the tail sub-window is noisier because the tail beats). Confidence: good, about ±3%.
