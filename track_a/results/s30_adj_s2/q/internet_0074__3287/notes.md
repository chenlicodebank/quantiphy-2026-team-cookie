# q3287: ball velocity at 3.00 s (internet_0074, overhead pickleball court)

## Where the candidates part ways: the time base
- C1 (8.0 m/s) treats the file as a 30 fps source with every 5th frame dropped and maps t = 3.00 s to real time,
  which is file frame 72. At that frame the ball is in the far player's return, at about 40 px per frame.
- C2 (3.7 m/s) uses frame = round(t x question_fps) = round(3.00 x 30) = file frame 90. At that frame the ball is
  rising after bounce 2 (frame 82), before the near player hits it (93/94), at about 18 px per frame.
- The rule says to use question_fps for every time and frame conversion, even when the file fps differs, and to use
  the frame index. So t = 3.00 s is **file frame 90**, and I agree with C2's time base. (File fps is 23.976; the
  question fps is 30.)

## Scale
At frame 90, the sidelines at rows 1100, 1440 and 1800 are 914.0, 916.5 and 917.0 px apart centre to centre
(about 924 px over the outer edges). Using 916 px = 6.1 m gives 150.2 px/m. This agrees with scene/ (914.6 px) and
with C2 (916.5 px).

## Ball (measure.py: colour-mask centroid; scene/tracks/ball.csv as a cross-check)
Displacement per step. Steps into frames 88 and 92 come after a dropped frame and span 2 source frames.
- 89 to 90: 19.4 px (scene track: 18.8)
- 90 to 91: 16.8 px (scene track: 18.0)
- 91 to 92: 32.7 px, so 16.3 px per frame (scene track: 16.25)

The ball is slowing down. The forward difference at frame 90 is about 17.4 px per frame (mean of the two tracks).
The central or local mean is about 17.6 to 17.8 px per frame.

v = 17.6 x 30 / 150.2 = 3.5 to 3.6 m/s. The spread between the backward and forward differences gives 3.5 to 3.8.

## Answer
3.6 m/s. This is close to C2 (3.7); I estimate the forward step slightly smaller. Confidence: moderate. The answer
mainly depends on choosing file frame 90 as the time base. If the reference used real time instead (file frame 72),
the answer would be about 8 m/s (C1).
