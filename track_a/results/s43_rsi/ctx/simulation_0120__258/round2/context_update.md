# Round 2 addendum (Q258, TV length): round 1's switch to 1.57 is verified

## Established (with my own code, frame 0)
- **Nadir camera, principal point at the image centre.** Four vertical marble-wall joint lines meet at (539.49, 539.46) (m_joints.py, rms 0.15 px).
  This is independent of the TV edges, whose own intersection along x is ill-conditioned (535–539).
- **TV ratio.** Δv/(cx − x) = 1.0457 ± 0.0007 at cx = 539.5 (dark-mask sub-pixel edges in columns 154–211, m_tv2.py). Round 1 had 1.048 and C1 had 1.045.
- **Vacuum.** 8.397 px/frame from two routes (circle centre 8.4035, edge midpoint 8.3904) → 201.5 px/m at the top disc and 198.8 px/m at floor level (8 cm top, H ≈ 5.9 m).
- **Plinth edges.** Front-face top x = 284.77, floor edge x = 295.64.
- **Wall junction x = 219.0.** The marble texture energy drops from about 3 to 0.08 at x = 218.5–219, and the wall joint lines end there.
- **The plinth top x 219–284 is horizontal.** The fireplace frame's end edge sits at a constant y = 408.4–408.5 over x 232–264; on a vertical surface it would be radial and drift about 15 px.
- From these: X_wall = 1.544 m. With the TV's thickness / stand-off k = 1.015–1.035, **L = 1.56–1.59 (central 1.58)**. It would be 1.61 if the face were flush with the wall.
- **Fault reproduced.** Using x = 295.6 as the wall gives X = 1.211 and L = 1.27, which matches the DeepSeek 1.21–1.26.

## Decision
Switch to C1 = **1.57** (high confidence). My value is within 1 % of it.

## Still open (small)
- The TV's stand-off from the wall (±1.5 %).
- The vacuum feature height and camera height correction (±0.5 %).
