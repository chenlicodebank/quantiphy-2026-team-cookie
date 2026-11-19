# Round 2 addendum: q1194 (bike handlebar-to-ground height)

## Verified (independent code: vp.py, geom.py, plaus.py)
- **Round 1's switch to 1.00 is verified.** Round 2 answers 1.00 (switch from 1.49), confidence high.
- **Horizon and focal length.** My own LSD + RANSAC on the facade cornice lines gives a street VP of (1793, −76.5); the bootstrap y range is −80 to −73.
  - The vertical VP is (958, 8023) from 65 segments.
  - So f = 1874 and the pitch is 13.8°.
  - This agrees with round 1 (−82, f 1887–1958). f ≈ 1185 is ruled out.
- **Camera height.** 4.61 m above the sidewalk, from the 1.8 m walker over 86 frames (sd 0.024).
- **Walker-ground route.** It barely depends on f (under 0.3 % between f 1874 and 1950).
  - H at r = 0.3: 0.97–1.02 over frames 0–60, mean 1.00.
  - H at r = 0.4: mean 0.97.
  - H at r = 0: about 1.07.
- **Bike's given depth.** The model puts the bike origin at 15.9–16.0 m against 16.49 m given (3 % at f = 1874, about 0 % at f = 1950). Closure on the walker's 1.8 m through the bike-depth scale is 3 %.
- **New route: head sizes.** At f33 the rider's head is about 20 px wide and the walker's about 17 px, so the two real heads are about the same size.
  - At the given depths (16.49 vs 11.93 m) the rider's head would be about 1.6× the walker's, which is impossible.
  - This confirms that the walker's given depth refers to an origin offset from the body.
- **Plausibility.**
  - The rider's head is 1.65–1.69 m above the road.
  - The bike moves at 4.66 m/s and the walker at 1.24 m/s.

## Ruled out
- **1.49 (C1) and 1.6 (C3):** both rest on the walker-depth focal length.
- **1.06 (C6):** it uses r = 0.

## Open
- **The grip set-back r (0.3–0.45 m)** leaves about ±3 %.
- **The curb height (0–0.15 m)** leaves about ±2 %.
- Overall the answer range is 0.96–1.03.
