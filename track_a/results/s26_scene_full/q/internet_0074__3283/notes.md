# q_3283: distance between the two players at t = 0 s

Overhead drone view of a pickleball court (planar, 2D). Frame 0 is the same at either rate (23.976 file fps or 30 question fps).

Scale: court width (sideline to sideline) at frame 0 = 902 px centre-to-centre, 911 px outer edges (from scene record,
consistent with the frame-0 image). I used ~906 px for 6.1 m, so 6.733 mm/px.

Player positions at frame 0:
- From scene mask centroids: far (956.9, 236.5), near (658.0, 2352.7) -> 2137 px. The near player's centroid is pulled up
  by the raised tossing arm.
- From zoomed crops (torso/head centre by eye): far ~(955, 235), near ~(670, 2375) -> 2159 px.
- Mean ~2148 px.

Distance = 2148 px x 6.1/906 = 14.46 m (range 14.3-14.6 m over the different width readings and point choices).
Sanity check: the players stand just behind opposite baselines (13.4 m apart), with an x offset, so ~14.4 m makes sense.

Answer: 14.45 m. Confidence: moderate-high, about ±2%.

Note: one shell call that chained commands was refused, so the crops were made with the helper tool using absolute paths. No separate
measurement script was written; the crops are in frames/.
