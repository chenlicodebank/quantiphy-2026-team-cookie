# q2955 — pizza cutter velocity at 0.2 s (cm/s); prior: money width = 7.5 cm

File: 24 fps, 48 frames; question_fps = 30. 11 exact duplicate frames (2,6,11,15,...,44); 37 unique frames.

## Scale (money.py)
Top Monopoly 500 note, frame 0/5/10, colour-saturation column profiles at x=890/900: note spans y≈196.5→266
=> short side ≈ 69.5 px (C1: 69, C2: 72.4, scene record: 64 by eye). Width = short side (7.5 cm is a
banknote short side; length then ≈ 16 cm, realistic). Scale = 7.5/69.5 = 0.1079 cm/px.

## Where the candidates part ways: the time base
- C1 (55): unique frames treated as consecutive 30 fps frames; 16.8 px per unique step x 30.
- C2 (35): real time preserved in the 24 fps file (unique rate 18.5/s): ~340 px/s.
- Per the stated convention (t -> frame round(t x question_fps), times by question_fps, frame column of the
  record), t = 0.2 s -> frame 6, velocity = forward difference x 30.

## Motion (look.py, scene/tracks/pizza_cutter.csv guard front point, stabilised to background)
Frame 6 is a duplicate of 5; forward step f6->f7 = 15.2 px (stab), 14.7 px (raw).
=> 15.2 x 30 = 456 px/s x 0.1079 = 49.2 cm/s (raw: 47.6).
Checks: unique-step average around t (f3-f10) 17.1 px -> 55 cm/s if unique frames are the 30 fps frames (C1's
reading); file-frame average f3-f10 14.5 px/frame -> 47 cm/s; real-time reading (C2) -> ~34 cm/s.

## Decision
I follow the question_fps frame convention (file frame 6, forward difference x 30) and get ~49 cm/s. This sits
between C1 and C2 and is closer to C1. C2's real-time reading conflicts with the stated rule that times use
question_fps. Confidence: moderate. The main uncertainty is the time base (the range of readings is 34-55).
Answer: 49 cm/s.
