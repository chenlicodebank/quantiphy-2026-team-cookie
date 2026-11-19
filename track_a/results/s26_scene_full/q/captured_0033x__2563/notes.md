# q_2563 – velocity of the ping pong ball at t = 1.5 s (cm/s)

Time base: question_fps = file fps = 24 -> t = 1.5 s is frame 36. Lab camera: f = 0.5959 x 1280 = 763 px, c = (640, 360).

## What happens at frame 36
The ball comes off the table's front edge at about frame 35 and falls down-left while it moves fast toward the camera.
Frame 36 is a blur streak, and so is frame 37 (which is also cut by the bottom of the image). The ball is gone from frame 39.
Correction to the scene record: in frames 25-35 the ball is not resting on the table. A shadow or reflection shows below it, so
it is in the air or hopping, and the lower half of the ball has low contrast against the wood.

## Measurements (seg.py, prof.py, xsec.py, halo.py, vel.py)
- Exposure is about 0.7 of a frame: in frames 21-23 (black background) the blur length is about 0.7 x the motion per frame.
- Cross-streak FWHM = ball diameter. It reads 31 px at frames 20-22, where the ball is sharp, and the bbox gives the same value,
  so the method holds. Frame 36: 54 px. Frame 37: 55-60 px (about 57.5).
- Frames 32-34: bbox width minus 0.7 x horizontal motion gives d = 44, 44 and 47 px.
- 1/d is linear in the frame number (residuals about 1 px).
- Centres at mid-exposure: f34 (478, 487), f35 (455, 499) (cy corrected about +2 px for the lost lower edge), f36 (408, 571)
  (middle between the streak ends and the two centroid estimates), f37 (373.5, 650).
- Depth: Z = f x 0.04 / d (tangential diameter). This gives a camera distance at f34 of 0.664 m, against 0.738 m in depth_info.
  The given 1.457 m at t = 0.9 does not fit the ball's size there (31-32 px, about 0.98 m). It does fit frame 0, so the
  0.9 s value looks unreliable and I did not use it.

## Speed at frame 36 (3D back-projection)
| depth scale | p37 - p36 (forward) | (p37 - p35)/2 (central) |
|---|---|---|
| absolute, from the 40 mm prior only | 1.42 m/s | 1.48 m/s |
| anchored to depth_info at f34 (x1.11) | 1.58 m/s | 1.65 m/s |

Velocity f35-37 (absolute scale) is about (-0.47, +1.1, -0.87) m/s: sideways, falling, and toward the camera.

Second route: inside the frame-36 exposure the streak is 104 px long and the diameter is 54 px. That is 50 px of blur in
0.7 frame, about 71 px/frame in the image (1.27 m/s in-plane at Z = 0.57). Adding the depth component of about 0.85 m/s gives
about 1.5 m/s, which agrees.

Answer: 150 cm/s, between the two depth scales. Confidence: moderate, about ±12 %. The main uncertainties are the depth scale
(the diameter-based value and depth_info differ by 10 %) and the centroids in the blurred frames.
