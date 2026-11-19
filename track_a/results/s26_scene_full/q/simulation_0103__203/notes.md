# q203: boat speed at 1.0 s (frame 24)
2D render, static camera, fps 24 (= question_fps). Scale comes from the prior: shark acceleration = 1 m/s^2.
- Shark acceleration in px: I fit a quadratic to x(frame) for frames 1-53. Centroid track (scene record): 0.1516 px/frame^2. Nose-edge track: 0.1507. My own template match of the rigid head and front body: 0.1508 (residual 0.1 px). I used 0.151 px/frame^2, which is 86.98 px/s^2, so the scale is 1 m per 86.98 px.
- Boat: the bow template track gives a constant step of 17.95 px/frame (17.97 at frame 23->24, 17.94 mean over frames 10-40, 17.89 from a quadratic fit). That is 430.8 px/s.
- Speed = 430.8 / 86.98 = 4.95 m/s.
- Check: the boat is 858 px long, which is 9.9 m at this scale, and the shark is 3.0 m. Both are plausible.
- Caveat: the boat and the shark could be at different depths. I assumed a single scale, as the 2D convention says.
Confidence: good, about 2 pct measurement uncertainty.
