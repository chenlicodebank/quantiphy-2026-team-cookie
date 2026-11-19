# Q1678 – length of the boat (m)

Prior: boat speed 4 m/s. depth_info: 90.1103 m at t=1 s and 90.4360 m at t=2 s. The question fps is 24, but the file is labelled 25 fps (75 frames).
I used 24 fps for every time conversion: t=1 s is frame 24 and t=2 s is frame 48, so the boat travels 4/24 m per frame.

## Measurement (measure.py → extents.csv)
- In every frame I took the boat's horizontal extent from the foreground (min RGB < 245) below y=330, which excludes the rock. The mast lies inside the hull's x-range. Frames 0–2 are clipped at the right edge, so I dropped them.
- Bbox-centre motion fits a straight line at −6.435 px/frame (residual std 0.84 px). The bottom edge moves −0.28 px/frame.
- Full horizontal extent, bow to stern including the rudder: 396.7 px at frame 24 and 393.8 px at frame 48. It shrinks slowly because the boat recedes from the camera. The record's hull-only value is about 390 px. I used the full extent for the bounding-box length.

## Route 1 – pinhole
I assumed the principal point is at the image centre. I back-projected the fitted centre at frames 24 and 48 using the given depths. Then I solved for the focal length that makes the 3D displacement over that 1 s equal 4 m. This gives f = 3494 px (horizontal FOV 15.6°).
Length = w_px × Z / f, which gives 10.21 m at frame 24 and 10.18 m at frame 48.

## Route 2 – ratio
Length = w_px / (px per frame) × (4/24 m per frame) = 395.2 / 6.435 × 0.1667, which gives 10.24 m. This route doesn't depend on the focal length. It also cancels any foreshortening, as long as the boat moves along its own axis.

## Answer
10.2 m. The two routes agree within 0.5 %. The main uncertainties are where the AABB ends (rudder and railings, about ±1.5 %) and the assumption that the boat moves straight along its axis. Confidence is good.
