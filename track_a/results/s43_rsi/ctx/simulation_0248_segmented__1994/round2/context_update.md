# Round 2 addendum — q1994 (rabbit length)

## Established (re-measured with own code: measure2.py, feet.py, overlay.py)
- Pixel values reproduce round 1:
  - Left horse: 77.37 px/s (centroid) and 77.02 px/s (torso band).
  - Middle horse: 142.50 and 142.55 px/s.
  - Horse lengths are 192 and 229 px; heights are 165 and 178 px.
  - Rabbit bbox median is 46 px (frame 0: 45). Frames reading 53 px include a touching horse hoof.
- Round 1's fault proof is reproduced. Putting the prior on the middle horse gives 0.00614 m/px, which makes the horses 1.18 and 1.41 m long and 1.0–1.1 m tall (about 45 pct below real size). The left-horse scale, 0.01132 m/px, gives real-size horses.
- My own value is 45.5 px × 0.01132 = 0.515 m, which agrees with round 1 (0.51) and C3 (0.516).

## Ruled out
- Gait timing as an independent scale. Both horses' hooves stay planted (no foot slip), with stride periods of about 0.9 s (left) and 0.71 s (middle). Dynamic similarity favours opposite readings for the two horses, because the playback rate is matched to each horse's speed. It is not decisive.

## Decision this round
Switch confirmed: 0.515 (follows C3). Confidence is medium.

## Open
The colour word "brown" by itself fits the middle horse slightly better. If the scene is a deliberately scaled-down one, 0.283 would be right. No in-clip absolute reference exists to settle this.
