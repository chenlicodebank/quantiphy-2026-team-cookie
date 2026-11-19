# q_1917: diameter of the truck's tire (m)

The scene is 2D, 120 fps (the file rate matches question_fps). The prior is that the box falls at 9.8 m/s² before 0.6 s.

## Scale (fit.py)
- I fitted a quadratic to the box centre y (scene/tracks/box.csv) over frames 0-58/59, before the impact at f60. The result is a = 1955-1965 px/s², with v0 ≈ 0 (released from rest) and rms 0.6 px.
- The bottom edge of the face gives the same value, about 1960 px/s².
- Scale = 9.8 / 1960 = 0.00500 m/px.

## Tire (wheel2.py, frame 120)
I fitted a circle to the tire/white-background boundary below the arches: the left and right edges plus the bottom profile.
- **Front wheel:** centre (1580, 978.5), r = 85.2 px, rms 0.5 px. The top edge of the tire against the fender is at y≈893, which agrees: (1063 − 893)/2 ≈ 85.
- **Rear wheel:** r = 82.1 px. Its right edge is partly mixed with the mud flap and other parts, so this value is less reliable.
- scene/ gave r ≈ 88-90 from a rougher fit.
- I adopted a diameter of about 168 px (± 4).

## Answer
Diameter = 168 × 0.0050 = **0.84 m**.

**Checks:**
- The truck's overall length of 1717 px becomes 8.6 m. That is plausible for a lift/catering truck.
- A tire of 0.84 m is plausible for a truck.

**Caveat:** the box sits on the roof centreline, slightly farther from the camera than the wheels. With perspective the true tire size would be a little smaller. I used the single 2D scale, as the 2D convention says. Confidence is moderate to good (about ±5%).
