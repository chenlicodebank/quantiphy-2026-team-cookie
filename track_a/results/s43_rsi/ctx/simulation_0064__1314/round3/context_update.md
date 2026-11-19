# Round 2 addendum (q1314, traffic-light height)

## Established (own code: curbs.py, poles.py, scan.py, checks.py)
- **Horizon:** the street VP from sub-pixel fits of the two long near curb edges is (1084, −122), rms 0.4–0.9 px. This confirms the record's −121.
- **Vertical VP:** yv = 7850 ± 50 (7877 at f0/f14, 7794 at f60). f ≈ 2200 at yh −122; f = 2120–2146 at yh −75 to −90.
- **Light height:** 4.99–5.00 m on both near lights, base to sign apex. The camera height comes from five depth routes (pedestrian f38; cyclist f14 and f38; van f14 and f38): 6.2–6.9 m depending on the horizon. The ratio light/Hc is 0.80–0.75 over yh −75 to −122. The product is stable: 4.99 at yh −75 and −90, 5.00 at −122, about 4.9–5.1 at −60 and −190.
- **Prior-only Hc route (new):** the van's ground track fitted with a = 4 from rest at f1. It agrees with the depth routes at yh ≈ −60 to −90.
- **Closure:** a = 3.94 at yh −75 and 3.84 at −90.
- **Plausibility:** pedestrian 1.68–1.75 m, van paint width 1.91–2.03 m.
- **Head-top-only reading:** 4.20 m.

## Ruled out
- f ≈ 2700+ (DeepSeek runs): with the pole VP it implies a horizon at about −477, which contradicts the curb VP.
- 3.4 / 3.85 / 2.9: wrong geometry and the head-top reading.

## Decision
Round 1's switch to C1 (4.97) is verified; my own value is 4.99–5.00.

## Open
- Only the reading: whether the reference AABB includes the crossing sign on top (5.0) or not (4.2). The sign is part of the identical asset on every corner, so including it is the most likely reading.
