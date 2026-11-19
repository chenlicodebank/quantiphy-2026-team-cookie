# q2158 – velocity of the toy (yellow fruit) at t = 1.2 s

- question_fps = file fps = 24, so t = 1.2 s means frame round(28.8) = 29. f = 0.5959*1280 = 763 px, principal point (640, 360).
- depth_info: distance 1.402 m at f24 and 1.065 m at f29. Prior: free fall, g = 9.8 m/s².
- Track: scene/tracks/fruit.csv ref_x/ref_y (centroid of the filled mask). I checked frames f22–f32 on a crop strip
  (frames/strip.png) and the masks follow the fruit. It is airborne from about f19, the apex is near f25 and it hits the table at f32.

## Route 1: ballistic 3D fit (fit.py)
I fitted P(t) = P29 + V t + ½ g t² ŷ (gravity 9.8 along camera +y, since the camera looks horizontally) to the pixel
track f25–f31 by pinhole projection, with the two given distances as strong constraints.
- The fit residual is 1.4 px RMS, and it reproduces the given distances to within 4–7 mm.
- V(f29) = (-0.13, 1.97, -1.51) m/s, so |V| = 2.48 m/s.
- One-frame forward difference p30 − p29 = 2.64 m/s. The mean of forward speeds over f27–31 = 2.67 m/s.
- Changing the frame window (24–31, 25–30, 26–31) moves the speed by less than 0.03 m/s.
- If the camera were pitched by ±10°, the speed would be 2.38–2.60 m/s (2.57 m/s with the pitch left free).

## Route 2: back-projection with depth linear in time (measure.py)
The horizontal velocity is constant in projectile flight, so here the depth is linear through the two given values.
- Forward speed at f29 = 2.63 m/s. The 3-frame mean (f28–30) = 2.61 m/s, and the 5-frame mean (f27–31) = 2.38 m/s.
- Depth from apparent size (K/size) is too noisy to use, because the fruit is elongated, tumbles and is blurred at f29–31.

## Answer
The instantaneous speed at f29 is about 2.48 m/s. The forward-difference convention (centred at f29.5) gives about 2.64 m/s.
Answer 2.55 m/s, which is within about 4% of both. Confidence: moderate (about ±8%).
