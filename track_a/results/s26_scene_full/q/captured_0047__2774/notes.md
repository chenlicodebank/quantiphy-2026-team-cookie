# q_2774: yoga ball diameter (cm)

Lab video: 1280x720 at 24 fps (file fps = question_fps = 24). f = 0.5959*1280 = 762.8 px, principal point (640,360).
Scale comes from depth_info: at t=1.0 s (frame 24) the yoga ball is 2.4985 m from the camera (to its centre).

## Measurement (measure4.py)
- Ball edge points come from radial intensity profiles (gradient peak), taken every 4 deg. The floor-shadow sector
  (55-125 deg, below the ball) is excluded, and a robust circle fit rejects outliers. The overlay in check24b.png
  follows the outline closely, including the side that overlaps the dark trousers.
- Frame 24: circle diameter 147.5 px; ellipse axes 143.4 x 153.3 px. The ball is about 215 px off-axis, so
  perspective stretches it along the radial direction, as expected.
- A cone fit to the edge rays (exact sphere geometry) gives an angular diameter 2a = 10.437 deg.
  Diameter = 2*D*sin(a) = **45.5 cm**. Fitting 1/sin(a) as a smooth trend over frames 20-28 gives 45.6 cm.
- The plain method-card formula D * pixel extent / f gives 48.3 cm with the circle diameter and 47.0 cm with the
  ellipse minor axis. It overestimates off-axis because it ignores the cos(theta) factors.
- The scene/ record's diameter at frame 24 (155.6 px, from GrabCut) is too large: its mask leaked into the
  shadow and trousers. With the plain formula it would give 51 cm.

## Checks
- Frames 20-28 give a smooth, consistent angular-size trend (rms of the edge fit is about 1 px).
- Speed check against the prior (2.1464 m/s at 1.0 s): with depth taken from angular size, the one-step speed
  from frame 24 to 25 is 2.10 m/s, but the 4-frame average is about 1.78 m/s. The prior is only roughly
  reproduced (it depends on depth ratios, not on the absolute size).
- 45 cm is a standard yoga-ball size, which is a good sanity check.

## Answer
46 cm. This is the exact-geometry value of 45.5 cm, moved slightly toward the method-card value of about 47-48 cm.
Confidence: moderate-high, about ±5%.
