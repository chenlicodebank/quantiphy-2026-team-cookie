# q_2118 — length of the deck chair (m); prior: swimmer height = 1.8 m

The video is a 2D internet clip: a top-down drone shot with a static camera (drift under 1 %). Following the annotators' convention, I used one planar scale taken from the prior. Timing does not matter here because this is a size question; everything was measured on frame 0.

## Swimmer (prior object), frame 0
At frame 0 the body is flat at the surface with the arms stretched forward.
- Toe tips are at x ≈ 579–581. This comes from the HSV profiles along rows 690 and 712 (`feet.py`).
- The top of the head (hair edge) is at x ≈ 783. This comes from grey-level rows 690–706 (`head.py`).
- Feet to top of head = **≈ 203 px**. The scene record gives 205 px, so I used 204 px.
- Scale = 1.8 / 204 = 0.00882 m/px.

## Deck chair (teal lounger), frame 0
I segmented the teal cushion mask (`measure.py`):
- Top-left lounger: y 128–371, length 244 px. The record has 246 px.
- Top-right lounger: y 136–379, length 244 px. The record has 246 px.
- The bottom loungers are partly hidden in shadow; the record estimates their length at ~240 px.
- I used 245 px.

## Answer
245 × 0.00882 = **2.16 m**

## Checks
- The two top loungers agree with each other, and my measurements agree with the scene record within 2 px.
- 2.16 m is plausible for a sun lounger, which is usually about 1.9–2.1 m long.
- Alternative reading: if the swimmer's "height" were taken as toes to fingertips (256 px), the answer would be 1.72 m. I rejected this because height means head to feet.

Confidence: moderate. The main uncertainty is which swimmer extent the annotators used as "height".
