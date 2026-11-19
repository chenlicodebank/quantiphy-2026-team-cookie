# Q3038: speed of the swimming woman from 0 to 5.20 s (m/s)

The prior is the woman's height, 1.63 m. The video is a top-down drone shot of a pool with a near-static camera. I used the internet convention: one scale from the prior.

## Scale
- I measured head top to toes in a stretched glide frame (f123, zoomed crop with grid, `crops.py`): toes at x≈1720 and top of head at x≈2445–2450, so about 730 px.
- The scene record gives 690–730 px for glide frames. I used L ≈ 715 px (range 700–730), so the scale is 1.63/715 ≈ 0.00228 m/px.

## Time base
- The file runs at 22.52 fps and the question at 24 fps. Both give a plausible breaststroke (stroke cycle of 47 frames is 2.1 s or 1.96 s), so physics does not decide between them.
- The odd 22.52 fps looks like a re-timed cut of 24 fps footage, so I used 24 fps. That puts 5.20 s at frame 125.

## Motion
- I used the camera-compensated tracks from scene/tracks/swimmer.csv (camera drift is about 1.5% of the travel). The f0 and f123 crops confirm the head positions.

| reference point | displacement f0 → f125 | speed (net) | speed (linear fit of x(t)) |
|---|---|---|---|
| head | 997 px | 0.43–0.45 m/s | 0.41–0.43 m/s |
| trunk | 912 px | 0.39–0.41 m/s | 0.40–0.42 m/s |
| visible centroid | 919 px | 0.39–0.41 m/s | 0.40–0.42 m/s |

- Each speed range covers L = 730 to 700 px.
- Path-length sums are inflated by stroke jitter and mask noise, so I did not use them.

## Answer
- **0.42 m/s**: about 960 px over 5.2 s, at 0.00228 m/px.
- Second-route check: the linear-fit slopes agree with the net-displacement speeds to within about 4%.
- If the file's 22.52 fps were used instead (end frame 117), the result would be about 0.38–0.41 m/s.
- Confidence: moderate. The main uncertainty is the prior's pixel length (±4%) and the reference point (±5%).
