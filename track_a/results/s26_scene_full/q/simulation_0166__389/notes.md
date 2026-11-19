# Q389 – diameter of the bike's wheel (m); prior: bike speed 5.52 m/s

2D convention: the cyclist moves left to right, parallel to the image plane; the camera is static. fps = question_fps = 24, so no re-timing.

## Scale from the prior
- Cyclist ref_x track (scene/tracks/cyclist.csv): a linear fit gives 21.030 px/frame for f30–75 and 21.025 px/frame over the whole clip.
- Independent check from the wheel positions in my own row profiles (wheel.py): the rear wheel centre is at x ≈ 748 at f40 and x ≈ 1064 at f55, which is 316 px / 15 frames = 21.07 px/frame. Hub row tyre minima give 21.0 px/frame.
- 21.03 px/frame × 24 = 504.7 px/s, so the scale is 5.52 / 504.7 = 0.010937 m/px.

## Wheel pixel diameter (wheel.py: intensity profiles through the hub row y≈706 and the hub column, frames 40/45/50/55)
- Tyre centre-line minima are 63 px apart both horizontally and vertically, for both wheels and in every frame checked.
- The outer tyre edges at half-maximum (horizontal, which avoids the road shadow at the bottom) are 67.2 px (rear, f45) and 67.0 px (front, f45). The vertical outer extent is about 68 px, but the bottom edge is blurred by the contact shadow.
- I took the outer diameter as ≈ 66.5 px (allowing for compression blur), which agrees with the scene record's ≈ 66 px.

## Answer
- 66.5 px × 0.010937 = 0.727 m (outer tyre diameter, which is the bounding-box extent of the wheel).
- The tyre centre-line reading (63 px) would give 0.689 m. Both are plausible for a real 700c / 28" wheel.
- Confidence: about ±4 %.
