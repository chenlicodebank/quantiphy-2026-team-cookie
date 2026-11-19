# Q2089: distance between the two players at the beginning (frame 0)

The drone looks straight down at the court, so one planar scale from the prior is enough (the annotators' convention).

**Scale.** I measured the singles sidelines (white-line peaks) in code at frame 0, in 25 columns from x = 900 to 3400 (`measure.py`).
- Singles width: median 925.7 px, mean 924.7 px, std 2.3 px. This matches the scene record's 924.7 px.
- Scale = 8.23 / 925.7 = 0.008891 m/px.

**Player positions at frame 0** (scene tracks, checked on zoomed crops in frames/p_rec.png and frames/p_srv.png):
- Receiver (left baseline): mask centroid (788.5, 642.2) and core (774.3, 639.5). The body centre seen in the crop is about (778, 645); the racket sticks out to the right.
- Server (right baseline): mask centroid (3650.0, 1185.1) and core (3655.6, 1187.1). The torso centre seen in the crop is about (3650, 1195).

**Distance:**
| Points used | px | m |
|---|---|---|
| Mask centroids | 2912.5 | 25.90 |
| Core centroids | 2932.9 | 26.08 |
| Visual body centres | ≈2924 | ≈26.0 |

**Answer: 26.0 m.** As a sanity check, the players stand about one court length apart (23.77 m) and are offset diagonally, so 26 m is plausible.

The time base doesn't matter here because only frame 0 is used. Confidence is high, about ±2 %, which is the uncertainty in each player's reference point.
