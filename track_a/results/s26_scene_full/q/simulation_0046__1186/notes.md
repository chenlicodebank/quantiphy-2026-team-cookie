# q1186: distance from the left pillar of the near door to the right pillar of the far door

The file rate and question_fps are both 33, so t=1 s is f33 and t=2 s is f66.

## Which objects
- There are two doors with pillars: the green house's wooden door, with stair newel posts on white pedestals at x≈963 and x≈1166, and the stone house's arched door, with gate posts topped by finials at x≈1627 and x≈1852.
- The stone posts' bases sit lower in the image (y≈550-552) than the green pedestals' bases (y≈540-542). The camera is above the ground, so the stone posts are nearer to it.
  - **Near door = stone house door.** Its left pillar base is at (1627, 550), read from the zoomed crop frames/sl.png at f96.
  - **Far door = green house door.** Its right pillar (pedestal + newel post) base is at (1166, 540), read from frames/gr.png at f0.
- Alternative reading (near = green house, far = stone house): green-left to stone-right is ≈7.25 m. I did not use it.

## Scale (wheel2.py, geom.py, geom2.py)
- **Focal length.** I fitted circles to the dark tyre of each moving-bike wheel (wheel2.py). The tyre-centreline radius is 47.3-48.0 px at f33 and 44.2-45.0 px at f66; adding half the tyre width (≈2.7 px) gives the outer diameter, 100-101 px and 94-95 px.
  - Using f = Dpx·Z/0.65, with Z the given distance projected onto the optical axis, gives f = 1902, 1931, 1864 and 1896, so f ≈ 1900 px (horizontal FOV ≈ 53°).
- **Ground plane.** I back-projected the bike origin (hub midpoint) at both depths, put the wheel hubs 0.325 m above the ground, and fitted the pitch: 1.3° down, camera height 1.72 m.
  - With that plane the walker's pelvis comes out 1.01-1.05 m above the ground, which is plausible.
  - If the walker's feet (row 558) must land at his given depth, the pitch would be 1.5-3°.
  - So I took a pitch of about 2°.
- **Pillars.** Each base pixel is intersected with the ground plane:
  - stone-left: Z ≈ 15.2-15.5 m
  - green-right: Z ≈ 15.9-16.3 m
  - The distance is mostly the horizontal gap (461 px), plus a depth gap of ≈0.6-0.7 m.

## Result
| pitch | distance (f=1900) |
|---|---|
| 1.3° | 3.77 m |
| 2.0° | 3.69 m |
| 2.5° | 3.64 m |

Changing f by ±1.5% moves the result by about ±1%. The height difference between the pillar origins is about 0.1 m, which is negligible.

**Answer: 3.7 m.**

## Second-route check
- I set the depth scale from the walker instead (given pelvis depth, feet row 558) and carried it to the pillar rows. That gives pillar depths of 14.9-15.3 m and a distance of ≈3.6-3.75 m, which agrees with the bike route.

## Confidence
Medium, about ±5%.
- The given depths are not fully consistent with the image: between t=1 and t=2 the bike's apparent shrink is 2% larger than the depth ratio implies, and the walker's is 2-3% smaller. This leaves the pitch and the pillar depths uncertain by about 2-3%.
- Which door counts as "near" is a judgement call (see above).
