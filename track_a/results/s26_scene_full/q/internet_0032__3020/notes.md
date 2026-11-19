# q3020: acceleration of the boat, from 2-4.5 s to 4.5-7 s

## Method
- The camera is static (scene record shift < 0.2 px). The boat moves right to left, side-on, and gets slowly closer.
- I checked the scene track (`scene/tracks/boat.csv`) against a zoomed frame at t=2 s (frame 60): bow ≈ 672, stern ≈ 897, which matches the track (673 / 896).
- Time base: question_fps = 30 vs file 29.85. The difference is negligible (frames 60/135/210 vs 60/134/209), so I used 30.
- Pixel velocities: v1 = mean velocity over 2-4.5 s and v2 = mean over 4.5-7 s. Then a = (v2 - v1)/2.5 s. Script: `measure.py`.
  - Hull centre, endpoint positions (±0-6 frame averaging): |v| goes 45.0 → 48.2 px/s, a ≈ 1.25-1.51 px/s² (depending on fps and averaging).
  - Linear fit in each window: hull centre 1.42-1.44, bow 1.32-1.34, stern 1.52-1.53 px/s².
  - Quadratic fit over 2-7 s: 1.37-1.59 px/s².
  - Adopted value: 1.40 px/s². The speed magnitude increases, and part of that increase is perspective (the boat approaches), but the annotation convention is in pixels.
- Scale: hull length bow to stern. It is 236 px median over 2-7 s (225 at 2 s, 236 at 4.5 s, 246 at 7 s). I used 235.5 px → 3.5/235.5 = 0.01486 m/px.
- a ≈ 1.40 × 0.01486 ≈ 0.0208 m/s². **Answer: 0.021 m/s²**, speeding up.

## Second route
- I re-segmented the hull band independently (`reseg.csv`). The stern-tip fits give 1.64-1.67 px/s² and the mid fit 1.49-1.50. The bow tip is noisy in this segmentation (thin bow), so the endpoint differences there are unreliable.
- Overall the routes span about 1.3-1.6 px/s², which is 0.019-0.024 m/s².

## Confidence
Low to moderate. This is a small difference of two velocities, so it is sensitive to px noise (about ±15%). A length taken from a different frame (212-249 px) changes the scale by up to ±8%.
