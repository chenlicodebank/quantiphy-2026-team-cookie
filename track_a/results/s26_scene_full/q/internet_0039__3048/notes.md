# q_3048: swimmer's speed from 0 to 2.33 s (m/s)

**Answer: 0.76 m/s**

## Setup
- The view is overhead, the scene is 2D and the camera is static (the record's background-shift check confirmed this). The swimmer swims toward −y.
- **Scale:** the prior is height = 1.68 m. I measured the pixel height from cap top to feet. The record's `head_to_feet` has a median of 1040.7 px (range 985–1082 over the stroke). I checked frame 20 by eye: cap top ≈ 1665 and feet ≈ 2665, so ≈ 1000 px with the legs splayed. Scale = 1.68 / 1040.7 = 1.614 mm/px. As a sanity check, the lane is 1364 px wide, which gives 2.2 m, a plausible lane width.
- **Time base:** the file runs at 18.54 fps and the question at 25 fps. The file contains duplicate frames from a rate conversion. I used **25 fps**:
  - At 25 fps one stroke cycle (56 frames) takes 2.24 s and the speed is about 0.76 m/s. Both are typical for a relaxed front crawl.
  - At 18.54 fps the cycle would take 3.0 s and the speed would be 0.57 m/s, which is very slow.
  - So 2.33 s means frame 58.

## Measurement (`measure.py`, using the scene tracks)
| Reference point, method | 25 fps (frames 0–58) | 18.54 fps (frames 0–43) |
|---|---|---|
| Head (cap), net displacement / time | **0.761** | 0.566 |
| Head, path length | 0.785 | 0.580 |
| Head, linear fit | 0.762 | 0.576 |
| Hip (trunks), net displacement | 0.740 | 0.528 |
| Hip, linear fit | 0.729 | 0.540 |

For the head, net displacement over time equals the mean of the forward-difference speeds (the motion is monotonic). The head is the smoothest point. The hip estimate is a second, independent route and agrees within 3%.

## Confidence
Moderate. The main risk is the time base: at 18.54 fps the answer would be 0.57. The height in pixels is uncertain by about ±4%.
