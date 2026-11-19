# Q2054: average moving speed of the player in white (m/s)

**Scale.** The prior is "court width = 4.88 m". 4.88 m (16 ft) is the width of the lane (key), so I used the key. I measured the key's width in code (`measure.py`) as the distance between the centres of the two lane lines, on 16 rows of frame 0: **1077.0 px** (spread ±0.5 px). That gives 4.88/1077 = **0.004531 m/px**. As a check, the outer sidelines are 3334.5 px apart, which is 15.1 m at this scale. That matches a FIBA court width of 15 m, so the scale is consistent.

**Track.** I used scene/tracks/player_white.csv, the centroid of a clean mask (±5 px), over all 107 frames, 0-106. The drone barely moves: the image drifts by at most about 20 px.
- Path length from per-frame steps: 1465 px uncompensated, 1479 px camera-compensated.
- Smoothed path (5-frame average): 1442 px.
- Net displacement: 1449 px. The path is nearly straight.

**Time base.** The file runs at 20.43 fps; the question states 25 fps. I used **25 fps**:
- the reference answers follow the original footage;
- the dribble cycle of the player in black (hand release to release takes about 14-20 frames) is 0.56-0.8 s at 25 fps, which is typical, but 0.7-1.0 s at 20.43 fps, which is slow;
- the white player's shuffle-step cadence (about 7.75 frames per step) is 3.2 steps/s at 25 fps and 2.6 steps/s at 20.43 fps. Both are plausible, so this does not decide it.

Elapsed time = 106 frames / 25 = 4.24 s.

**Result.** Average speed = mean of the per-frame speeds = path / time:
- uncompensated path: 1.566 m/s;
- compensated path: 1.581 m/s;
- smoothed path: 1.541 m/s.

**Second route.** Net displacement / time gives 1.549 m/s, which agrees within 2%.

**Answer: 1.56 m/s.** At 20.43 fps it would be about 1.28 m/s.

**Confidence.** The scale and the path are solid, to about 2%. The main risk is the choice of frame rate.
