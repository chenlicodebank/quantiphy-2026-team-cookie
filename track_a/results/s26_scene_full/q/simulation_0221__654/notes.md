# Q654: diameter of the vase (m)

Prior: the vacuum's diameter is 0.438 m. There is no depth_info. fps is 24, the same as question_fps, so there is no re-timing issue (the question is about size, so time does not matter).

## Scene
A top-down 2D render. The vase is the white and blue round vase on the left end of the dark console, centred at about (753.7, 236.5) px. It does not move. I checked it on frames 0 and 72.

## Measurements (scripts are in this folder)
- `measure.py` and `vasedir.py` make a white, low-saturation mask of the vase. Its extents are about 74 px for thresholds 125-140: radial 74.2-74.7 px and tangential 73.1-74.0 px. `rays.py` gives a mid-edge circle fit of 72.5 px. **Apparent vase diameter: 74 px.**
- `vacwh.py` measures the vacuum mask on 7 frames. Its extent perpendicular to the image-centre direction (tangential) is a steady 119-121 px. Its extent along that direction (radial) grows with distance from the image centre, by about 4 px at r = 650 px. This is the side wall seen in perspective. **Vacuum diameter: 120 px** (the scene record gives 120.4-120.9 at the vase's radial distance).
- Simple single 2D scale: 0.438 / 120 = 3.65 mm/px, so the vase is 74 x 3.65 mm = **0.270 m**.

## Perspective correction (main uncertainty)
- The vase's dark opening is at (749.3, 227.7) px. That is about 8.4 px further from the image centre than the centre of the vase's outline, which is clear evidence of perspective. The vase's widest part sits about 0.6 m above the floor (on the console), so it looks magnified.
- The vacuum's radial side-wall growth gives h/H of about 0.006. Taking a vacuum height of about 0.095 m, the camera is about 15 m up.
- Vase magnification is about 1/(1 - 0.6/15) = 1.04. The vacuum's own magnification is about 1.006.
- Corrected: 0.438 x (74 / 1.04) / (120 / 1.006) = **0.261 m**.
- A lower camera (about 9 m, if the opening-to-widest-part height is only 0.2 m) would give about 0.25 m.

## Answer
**0.262 m.** This sits between the uncorrected 0.270 m and the perspective-corrected 0.25-0.261 m, leaning towards the correction.

Confidence: moderate, about ±5%. The pixel measurements are solid to about 1%. Most of the uncertainty comes from the perspective correction.
