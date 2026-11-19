# q_117 – length of the bike (m)

Prior: the car's acceleration is 4.03 m/s². The video is 2D and top-down (static camera looking straight down), 24 fps. question_fps is also 24, so the time base is unambiguous.

## Scale from the prior (fit.py, fit2.py, fit3.py, track.py, track2.py)
- I tracked the car with sub-pixel template matching against frame 0 (track.py). Blur is symmetric, so this gives the car's centre.
  - Quadratic fit, frames 2–48: a = 0.536 px/frame² (rms 0.36 px).
  - Frames 2–20: a = 0.534 px/frame².
  - Frames 5–45: a = 0.534 px/frame².
  - Second differences are flat at about −0.535 over frames 3–48.
- Bounding-box and mask-centroid fits over frames 2–30 give 0.524–0.537 px/frame².
- After frame 48, some tracks show a higher apparent acceleration (0.6–0.7). The rear-edge steps over frames 57–68 fall back to about 0.5. I treated this late part as less reliable, because of motion blur and the car leaving the frame.
- There is no lens distortion: the cyclist moves at a constant 16.22 px/frame across the whole right half (cyc.py).
- I used a = 0.537 px/frame², which is 0.537 × 24² = 309.3 px/s².
- Scale = 4.03 / 309.3 = 0.01303 m/px.

## Bike length (bike.py)
- Frame 0 is static and sharp. I took the difference from the empty frame 71 and read the column-max profile along the bike axis.
- The tyre ends are at x = 884.4 and 1012.0 at half contrast (threshold 50 of a plateau of about 110–128), so the length is 127.6 px.
  - At threshold 30 it is 129.1 px, as in the scene record.
  - At threshold 70 it is 126.7 px.
- Length = 127.6 × 0.01303 = **1.66 m**. The range across thresholds is 1.65–1.68 m.

## Check by a second route
- The car is 437–438 px long, which gives 0.01303 × 437.5 = 5.70 m. A real Cybertruck is 5.68 m long, so the scale from the prior is consistent with the model being at real size.
- Using the bike-to-car pixel ratio, 127.6 / 437.5 × 5.68 m, gives 1.66 m.

## Uncertainty
- If the late-frame acceleration (overall mean of about 0.555) were the true value, the answer would be 1.61 m, about 3% lower.

Confidence: good, within about 4%.
