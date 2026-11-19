# q_292: length of the red car (m)

The scene is a 2D top-down street at 24 fps (the file and question_fps are the same). The camera does not move.
The prior is: bike speed = 24 m/s.

## Scale
- Cyclist step: the scene record gives a mean of 31.64 px/frame. My own NCC matches over 20-frame spans (10→30, 20→40,
  30→50) give 31.80, 31.85 and 31.80 px/frame. I used 31.7 px/frame = 761 px/s.
- Scale = 24 / 761 = 0.03155 m/px.

## Red car (parked, lower left, nose pointing left)
- I read pixel profiles along rows y = 730–790 on frame 45 (`profile.py`, `measure.py`):
  - The nose edge is at x≈14–16.
  - The red body ends at x≈241. A dark red rear bumper and tail lights run on to x≈254–255, and the road starts after
    that (clearest at y=730, where the road is not in shadow).
- That gives a length of 241 px (±3). The scene record's box gives 244 px (13–257), which slightly includes the shadow.
- Length = 241 × 0.03155 = **7.60 m** (7.7 m with 244 px; 7.5 m with the 31.64 px/frame step).

## Plausibility
24 m/s is not a realistic bike speed, and the scene is scaled up consistently by about 1.6×: the bike is 2.7 m long,
the blue car 7.4 m and the road 17 m. Because the prior itself is unrealistic, I kept the prior's scale and did not
rescale to a real car size. (A real-size reading, with the bike at about 1.8 m, would give a car of about 5 m.)

Confidence: moderate-high, given the prior-scale convention.
