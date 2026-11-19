# q_286: shortest distance between the puck and the right handle (m)

- 2D top-down air-hockey render, 24 fps (fps = question_fps). The "handle on the right" is the red mallet at the lower right, which never moves. The record's centre for it is (713.3, 1434.3). On a 3x zoomed crop of frame 30, its disk spans x ≈ 662-767 and y ≈ 1380-1487, so the centre is ≈ (714, 1433), which confirms the record. (My own HSV mask merged with the red face-off circle lines, so I didn't use it.)
- The puck moves vertically at x = 537.8 (my measurement matches the record). It passes the mallet's y level on the way down (frame 30) and again on the way up (frames 65-66).
- The minimum centre-to-centre (origin) distance over all frames is 175.6 px (frame 65: 175.6, frame 30: 175.7). This is essentially the horizontal gap 713.3 - 537.8 = 175.5 px.
- Scale: the puck diameter of 0.074 m equals its 64 px horizontal mask width (measured over 5 frames; the record says 63-64 px). That gives 0.001156 m/px.
- Distance = 175.6 × 0.074 / 64 = 0.203 m. Using 63.5 px instead gives 0.205 m.
- Second-route check: the record's tracks (min over frames = 175.6 px) and my own centres plus the visual crop agree within about 1 px.
- Edge-to-edge distance would be much smaller (≈ 175.6 − 32 − 57 ≈ 87 px ≈ 0.10 m). I used the origin-to-origin convention.
- Confidence: good (±2%) for the centre-to-centre reading.
