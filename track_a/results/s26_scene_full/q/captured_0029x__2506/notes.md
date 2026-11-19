# q_2506 – velocity of tennis ball at 1.6 s (cm/s)

- t=1.6 s -> frame round(1.6*24)=38 (file fps = question fps = 24).
- Track: scene/tracks/ball.csv (robust circle fit, frames 25-48 sharp, ±1 px). I checked it covers the ball; the ball is rolling left along the back of the table at frame 38.
- Camera: f = 0.5959*1280 = 762.8 px, principal point (640,360).
- Depth: Z ∝ 1/diam_px (a linear fit of 1/diam over the window), set so Z(38)=1.027 m (depth_info).
  Check: the given depth ratio Z(1.24s)/Z(1.6s) = 1.114 matches the size ratio d38/d30 = 1.123.
  (Raw size-depth with D=6.7 cm is ~7% larger than the given depths. Only the ratio is used.)
- 3D centres were back-projected and a linear velocity fit made over windows around frame 38 that avoid the
  35->36 jump (probably a dropped frame):
  36-40: 38.5, 36-41: 38.6, 36-42: 38.0, 37-43: 37.3, 36-48: 38.2 cm/s (vx≈-33, vy≈-0.5, vz≈-20 cm/s).
  Windows that include the 35->36 jump give about 45 (rejected).
- Second check: the ball rolls on the table plane, so image y should grow as Z shrinks. A camera height of
  ~0.118 m above the ball centre gives ~0.7 px/frame for vz=-20 cm/s; the track shows 0.62 px/frame, so the
  depth rate fits. The image-plane-only speed is 33.9 cm/s.
- Answer: ~38 cm/s. Confidence: moderate-good. The main uncertainty is the depth-rate component (±5 cm/s on vz, about ±3 cm/s on |v|).
