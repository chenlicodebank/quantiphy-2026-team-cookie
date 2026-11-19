# q_2519 – velocity of the red ball at 0.8 s (cm/s)

Lab clip, 24 fps (file and question rates agree), so t = 0.8 s is frame 19. Camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360).
Prior: ball diameter 7 cm. Depths given at frames 5, 10, 14 and 19: 0.8715, 1.166, 1.372 and 1.315 m.

## Measurements (measure.py, velocity.py, orbit.py)
- Ball mask: dark red-brown pixels (max channel 30-115, r > b + 12) near the recorded track. Frames 13-17: the bottom of the
  ball is hidden behind the table's back edge (y ≈ 442), and the horizontal motion blur (~40 px/frame) widens the mask.
  So u = the bbox x-centre (the blur is symmetric) and v = the top edge + the predicted radius (f·0.07/d / 2).
  At frame 19 the bbox is 734-786 x 402-440 and the centre is (760.0, 422.3). The vertical size of 39 px matches 762.8·0.07/1.315 = 40.6 px.
- Back-projecting the 4 given depths gives points that lie on one plane parallel to the table (residuals ≤ 5 mm).
  The ball circles on the table, so the depth in other frames is the ray ∩ plane.
- Route A (raw plane depths): the per-frame depth is noisy because the ray grazes the plane (1 px in v ≈ 2 cm in depth).
  Central difference (P20 − P18)/2 → 185 cm/s. (P22 − P17)/5 → 184 cm/s.
- Route B (orbit model): a conic is fitted to one lap of top-view positions. Each frame is placed on it using only its
  pixel column u, which is the robust coordinate. Forward speeds at frames 17-20: 185, 186, 182 and 174 cm/s.
  Central difference at 19 → 183 cm/s. A 5-frame mean of forward speeds over 17-21 → 172 cm/s.
- Hand check: anchor d19 = 1.315 and take the depth rate of −0.045 m/frame from both routes, so d18 ≈ 1.36 and d20 ≈ 1.27.
  (P20 − P18)/2 → 187 cm/s.
- At frame 19 the ball is near the right-back turn. It moves about 1.6 m/s sideways and about 1 m/s toward the camera.

## Answer
183 cm/s. Confidence: moderate (about ±8 %). The main uncertainty is the depth rate around frame 19, and how the
reference smooths through the turn: averaging over a wider window lowers the value to about 170.
