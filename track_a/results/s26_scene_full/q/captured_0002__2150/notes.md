# q_2150 – ball velocity at the end of the slope (cm/s)

The "slope" is the white board leaning back on the table: the ball rests on its top edge (frames 0-26), rolls down
its face toward the camera (frames 27-35) and leaves its bottom edge (image y ~425 at x ~620) between frames 35 and 36.
Then it lands on the table (frame 36). The scene record was wrong to say the ball "falls in front of the board": it rolls on it.
File fps = question fps = 24.

Method (`measure.py`): f = 0.5959*1280 = 762.8 px, principal point (640,360). I back-projected the ball centre at frame 24
(depth 1.779 m) and frame 31 (depth 1.736 m). I back-projected the slope ends with their given depths:
board top edge (617,295) @1.815 m, bottom edge (620,425) @1.6715 m. Slope length = 0.329 m.
The ball line agrees with the slope direction to within 2.4 deg. Each frame's ball centre is the point on that 3D line
closest to the pixel ray (I used the tracked centres from scene/tracks/ball.csv).

- Ball position along the slope s (m): f28 0.012, f29 0.028, f31 0.092, f33 0.182, f34 0.239, f35 0.304, f36 0.371.
  The end of the slope (bottom edge projected onto the ball line) is at s = 0.335, so the ball crosses it at about frame 35.5 (t ~1.48 s).
- Route 1, frame differences: forward-difference speed 34->35 = 1.57 m/s and 35->36 = 1.59 m/s.
  The 35->36 step brackets the end of the slope.
- Route 2, prior physics: with a = 4.05 m/s^2 from rest, each tracked s gives a release time of 1.07-1.09 s,
  so the prior and the track agree. v = sqrt(2*4.05*0.335) = 1.645 m/s, reached at t ~1.48 s.
- A quadratic fit over frames 28-35 gives a = 4.5 m/s^2 and v at the end of 1.76 m/s. This is noisier, because the ball
  is faint over the white board.

Answer: 162 cm/s, between the measured 1.58-1.59 m/s and the prior-based 1.645 m/s. Confidence: moderate, about ±7%.
