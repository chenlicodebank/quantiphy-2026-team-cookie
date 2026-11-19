# Q192: speed of the boat at 1.0 s (m/s)

This is a 2D scene: side-on view, both objects move horizontally to the left. fps = question_fps = 24, so 1.0 s is frame 24.

## Scale from the prior (shark acceleration = 1 m/s²)
I fitted a quadratic to the shark's x(t) from scene/tracks/shark.csv (fit.py):
- Centroid, frames 2-72: a = -85.9 px/s² (rms 0.35 px). Frames 2-36 give -85.5 and frames 36-72 give -86.8.
- bbox centre: -86.7. Tail tip: -86.4. Nose: -87.0 (noisier).
- I use a = 86 px/s². The scale is 1/86 m/px = 0.01163 m/px.

## Boat speed
- bow_x moves at a constant -17/-18 px per frame. The step at frame 24 is 18 px, and frames 2-72 are fitted linearly at 428.9 px/s (a quadratic fit gives a ≈ 0, so the speed is constant).
- Speed = 428.9 / 86 = 4.99 m/s.

## Check
- Fits over separate windows (frames 10-40 and 2-72) give a boat slope of 428.9 px/s.
- The shark reference points (centroid, tail, bbox) agree to within about 1% on the acceleration.
- The answer is about 5.0 m/s. Confidence is high (about ±2%).
