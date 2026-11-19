# q_1992 — length of the white horse (prior: brown horse speed 0.874 m/s)

2D side view, static camera, 24 fps (file fps = question_fps), so no re-timing. The scene has two horses and a hamster.
I checked thresholds down to 254 and found no hidden white horse against the white background (probe.py).

Identity (main uncertainty): neither horse is white. One is a chestnut/red-brown horse on the left (mean RGB 67,28,24).
The other is a desaturated grey-brown/taupe horse in the middle (68,50,44). I took the chestnut as the "brown horse"
(prior) and the paler grey-brown one as the "white horse":
- With this assignment the scale gives realistic horses: the grey horse is 2.57 m long and about 2.0 m to the top of
  its head, and its walking speed is 1.59 m/s.
- The other assignment gives horses about 1.1 m tall.

Measurements (measure.py, using scene/tracks after checking them):
- Red/brown horse torso, frames 0–48 (frame 49 is a loop reset): 3.250 px/frame = 78.0 px/s. The centroid gives 3.197 px/frame.
- Scale: 0.874 / 78.0 = 0.01121 m/px.
- Grey ("white") horse bbox length: median 229 px at threshold 235 (range 223–241 over the gait); 234 px at threshold 254.
  I used 230 px.
- Length = 230 × 0.01121 = 2.58 m.

Check: the centroid-based speed gives a scale of 0.01139 m/px and a length of 2.62 m. The gait range gives 2.50–2.70 m.

Confidence: the measurement is good to about ±4 %. The colour-name assignment is the main risk: if it is reversed, the
answer would be about 1.2 m (the red horse's length on the grey horse's speed scale).
