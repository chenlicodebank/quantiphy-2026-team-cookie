# q_3036: swimming woman's average speed from 0 to 2.07 s

**Answer: 0.41 m/s**

## Scale
- Prior: the woman's height is 1.63 m. I measured her head-top-to-toe length on zoomed glide frames with a grid (crops.py → frames/c*.png):
  - f22: about 750 px (this includes the grey face-blur patch)
  - f29: about 730 px (to the blur front) or about 690 px (to the hair edge)
  - The record's f123 check gives about 730 px.
- I used L = 720 px, so the scale is 1.63/720 = 2.26 mm/px. Following the internet convention, this single scale applies everywhere.

## Motion
- The camera is a drone looking straight down with only slow drift. I used the camera-compensated tracks from scene/tracks/swimmer.csv and spot-checked them on frames 0, 47 and 50. On those frames the head front is at x ≈ 1506, 1902 and 1940.
- Displacement rate from 0 to 2.07 s (speed.py, cycles.py):
  - Body centroid / trunk: 7.3–7.5 px/frame. This matches the whole-clip mean of 7.3 px/frame, and the window is about one breaststroke cycle.
  - Head: 8.2 px/frame. The head runs ahead within the stroke phase in this particular window.
- Time base: the file is 22.52 fps but question_fps is 24. Under either rate the stroke cycle (2.1 s or 1.96 s) and the speed are plausible, so physics can't tell them apart. The end frame is 47 at 22.52 fps or 50 at 24 fps.

| reference point | 22.52 fps | 24 fps |
|---|---|---|
| trunk / centroid | 0.377 m/s | 0.402 m/s |
| head | 0.418 m/s | 0.445 m/s |

- I answered 0.41 m/s, in the middle of these four values. It is within about 9% of every reading.

## Second route
- The whole-clip mean (7.3 px/frame × 22.52 to 24 fps × 2.26 mm/px) gives 0.37–0.40 m/s. This agrees with the trunk values.

## Confidence
- Moderate. The main uncertainties are the reference point (head vs. body), the time base and the pixel length of the prior (±4%).
