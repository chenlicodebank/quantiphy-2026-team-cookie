# q 3146 – length of the brown chairs (m)

The "brown chairs" are the four wooden benches under the pergola. Length is the long horizontal extent, measured from the outer edge of one armrest to the outer edge of the other.
The prior is the rider's average speed, 4.9 m/s. Time base: 30 fps (the file and the question give the same rate).

## Scale (internet convention: one planar scale from the prior)
`measure.py` computes the mean per-frame displacement of the rider's reference points from scene/tracks/rider_scooter.csv:
- Camera-stabilised (measured against the background): cx 16.56, front axle 16.59, rear axle 16.50, torso 16.63 px/frame.
- Raw image coordinates: 16.23, 16.27, 16.20 and 16.29 px/frame. The camera drifts by about 0.34 px/frame, about 2 %.
- I used the stabilised value, 16.56 px/frame = 496.8 px/s. Scale = 4.9 / 496.8 = 0.009863 m/px.

## Bench pixel length (frame 0)
- `measure.py` uses a wood-colour HSV mask in rows 1015–1050. It gives 272 px for bench 2 (1516–1787) and 278 px for bench 4 (2188–2465). At frame 40 bench 2 measures 273 px.
- On benches 1 and 3 the left armrest is in deep shadow, so the mask misses it. Reading them manually from a zoomed crop gives about 283 px and about 270 px, which agrees with the scene record.
- I used the mean of the four benches: about 276 px.

## Result
276 × 0.009863 = **2.72 m**, answered as 2.73.
Second route: with raw (unstabilised) speed the scale is 4.9/486.8 m/px, which gives 2.78 m. Using only the two clean benches (275 px) gives 2.71 m. Spread is about ±2 %.
Sanity check: the prior's scale is large compared with the real world (the scooter comes out at about 1.8 m and the rider at about 2.8 m tall). That suggests the prior speed is generous. The question asks for the planar single-scale convention anyway, so I kept it.
The benches stand slightly behind the path, so with a perspective correction they would come out a few percent shorter. Per the convention I did not apply one.
Confidence: medium-high, provided the reference uses the same convention.
