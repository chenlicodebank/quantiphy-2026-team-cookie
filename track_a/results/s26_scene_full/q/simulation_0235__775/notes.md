# q775 — basketball acceleration at t = 1.5 s

- 2D render, 24 fps (file and question rates agree). t = 1.5 s is frame 36, in the rise after the bounce at frame 24.
- Scale: the ball's diameter is 106.1 px by circle fit and 108 px by bbox (which includes antialiased edge pixels). I used 106.5 px, so the scale is 0.282 / 106.5 = 0.002648 m/px.
- The ball's x position is constant, so the motion is purely vertical. Position is the circle-fit centre (scene/tracks/ball.csv).
- Rise phase: a quadratic fit gives a = 711 px/s² over frames 26–50 (rms 0.22 px), 709 over 30–42, 712 over 37–50, 713 in a ±6-frame window around frame 36, and 709 from a cubic fit evaluated at 1.5 s. The per-frame second differences average about 1.24 px/frame², which is about 715 px/s².
- My own bbox-top tracking (measure.py) agrees: 717 px/s².
- Result: 711 × 0.002648 = 1.88 m/s². The speed is decreasing because the ball is rising and decelerating; the magnitude is reported.
- Caveat: the fall phase has a larger magnitude (770 px/s², 2.04 m/s²). The question is about the rise, so the rise value is used.
- Confidence: moderate to high, about ±3%, plus some uncertainty about whether the reference used the fall value.
