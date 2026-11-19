# Q2021 — average speed of the red car (red pickup, lane 4)

**Answer: 29.1 m/s**

## Setup
- The camera is static and looks almost straight down (see scene/notes.md; I checked frame 10 by eye). The motion is planar, so one scale is used.
- **Scale:** the prior is lane width = 3.66 m.
  - The red car's lane lies between the dash rows at y≈989 and y≈1310.
  - I paired up dashes at the same x and measured centre-to-centre: 319.3, 317.4 and 325.6 px, mean **320.8 px**.
  - That gives 0.01141 m/px.
  - Using the mean over all lanes (318 px) instead would give 29.4 m/s.
- **Motion:** I used the template track `scene/tracks/red_pickup.csv` (`cx_full`, `cy_full`) on frames 0–29, where the car is fully in view.
  - The mean per-frame 2D step is **106.3 px/frame**, including the slow downward lane-change drift of about 4.7 px/frame.
  - Steps vary smoothly between 104 and 109 px.
  - Frames 30–33, where the car is cut by the image edge, were left out.

## Time base
- The file runs at 19.61 fps, but the question states 24 fps. A rate of 19.61 fps is unusual, which suggests the clip was re-timed.
- At 24 fps the car does 29.1 m/s (65 mph). That is a typical cruising speed on a wide US freeway (12 ft = 3.66 m lanes).
- At 19.61 fps it would do 23.8 m/s (53 mph).
- The car is 532 px long, which is 6.07 m. That fits a crew-cab pickup, so the scale holds.
- I used the question's 24 fps.

## Second route
- I tracked the centroid of the red-hue pixels independently, frame by frame from the video. Its net displacement over frames 0–31 is 107.2 px/frame, which gives 29.4 m/s at 24 fps.
- This agrees with the first route to within 1%.

## Confidence
- The pixel measurements are solid (about ±1%).
- The main uncertainty is the fps choice: if the reference used 19.61 fps, the answer would be 23.8 m/s.
