# q_3287: ball velocity at 3.00 s (internet_0074, overhead drone view of a pickleball court)

## Time base
The file runs at 23.976 fps but was made from a 30 fps source by dropping every 5th frame: every 4th step is about
twice as long as the others. question_fps is 30. So file frame k = original frame k + floor(k/4), and real time is kept.
t = 3.00 s is original frame 90, which is file frame 72 (72 + 18 = 90; 3.0 x 23.976 = 71.9 gives the same frame).
The step from file frame 72 to 73 is a normal one-original-frame step (1/30 s).

## Scale (one factor from the prior)
Court width 6.1 m. Sidelines at frame 72 (white pixels in rows 1100, 1440 and 1800):
- Measured centre to centre: 339.5 to 1253 = 913.5 px, giving 0.006678 m/px.
- Measured over the outer edges: 335 to 1257 = 922 px, giving 0.006616 m/px.

## Ball (measure.py: centroid of the yellow-green colour mask; matches scene/tracks/ball.csv to within 1 px)
Distance moved per original frame:
- 70 to 71: 43.1 px
- 71 to 72: 82.5 px over 2 original frames, so 41.3 px per frame
- 72 to 73: 40.07 px
- 73 to 74: 39.2 px
- 74 to 75: 37.7 px

The ball is in flight after the far player's return and before the bounce at file frame 82. The camera is close to
static (slow zoom of about 1.6% over the whole clip, which is negligible here).

Forward difference at frame 90: 40.07 px x 30 = 1202 px/s, which is
- 8.03 m/s with the centre-to-centre scale, and
- 7.95 m/s with the outer-edge scale.

## Check
Averaging the neighbouring steps (41.3, 40.1 and 39.2 px per frame, mean about 40.2) gives 8.0 m/s, the same answer.
Real-world sanity check: a drive return of about 8 m/s is plausible for pickleball.

## Answer and confidence
Answer: 8.0 m/s. Confidence is good, about ±3%. The main uncertainty is which edges the annotators measured the court
width between, and the fact that the ball is above the ground (no perspective correction, following the convention).
