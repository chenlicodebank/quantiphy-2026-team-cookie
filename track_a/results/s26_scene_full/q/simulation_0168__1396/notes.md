# q_1396 – width of the road the bike and van ride on

Answer: **6.69 m** (asphalt width, kerb base to kerb base, measured perpendicular to the road).
File fps = question_fps = 24, so no time-base issue.

## Geometry (static camera, Blender, no lens distortion)
- `bg.py` builds a clean background image (frame 0 for x<1500, frame 79 for x>=1500). `lines.py` does sub-pixel
  line fits from column/row profiles.
- VP1 (road direction): far white edge line, yellow centre line, near cream line, near kerb edge and far kerb top all
  meet at (2644, 540.6), within about ±10 px.
- VP2 (across the road): the near and far stop lines, plus the cross street's yellow line, meet at (-3307, 536)
  (the three pairwise intersections fall between -3280 and -3361).
- The horizon is level at y≈538, so the camera has almost no pitch or roll. With the principal point at the image
  centre, orthogonal VPs give **f = 2681 px**.
- The scene record's line "y=-0.40x+1627" (VP 2777,516) was a poor fit. I re-measured it (slope -0.445 / -0.47).

## Scale (camera height h)
- Route 1 (depth_info): the bike's distance at t=0 is 28.219 m and at t=0.5 s (frame 12) is 25.554 m. The ground
  point under the origin is the midpoint of the two wheel contacts, hand-read at 7x zoom: f0 (1851,658),
  f12 (1777,669). This gives **h = 1.1787 / 1.1768 m**.
- Route 2 (speed prior): wheel-contact midpoints at frames 0, 12, 24, 48 and 79 projected on the ground plane. The
  along-road position is linear in time (residuals ≤0.04·h), the lateral position is constant (the bike rides
  straight along the road), and a slope of 5.52 m/s gives **h = 1.186 m**.
- The two routes agree within 0.7%. I used h = 1.182 m. Check: the bike's speed over frames 0→12 with route-1 h is
  5.41 m/s against the prior 5.52.

## Road edges (lateral offset c = s/h along the across-road direction)
- The camera is about 1.9 m outside the near kerb, over the near sidewalk: both kerbs lie on the same side of the
  camera's vertical plane through VP1.
- Far kerb: the face is visible. The kerb-top highlight A is at c=7.94, and the face/asphalt boundary (hand-read
  column profiles at x=1420…1800) is at **c = 7.291** (spread ±0.01). The kerb height from (base-A)/(base-vh) is
  0.081·h ≈ 0.096 m. The white line B lies 2.5 px inside the kerb base (c=7.131).
- Near kerb: only its top (light band) and its back face (dark band) are visible. The front top edge E1 is at
  c=1.793 (elevated). Correcting by the kerb height (0.081–0.103·h, from the far kerb and from the near back face)
  puts the road edge below it at **c ≈ 1.63** (range 1.61–1.65).
- Width = (7.291 − 1.63)·1.182 = **6.69 m**.

## Sensitivity / alternatives
- f: VP2 ±500 px changes W by about ±3.5%. The depth–speed consistency prefers a slightly smaller f (about 2600),
  which would give about +1.5%.
- Other readings of "road width":
  - between the painted edge lines: (7.131−1.890)·h = 6.19 m
  - near kerb with no height correction, to the far white line: 6.31 m
  - kerb-top front edges (A to E1): (7.93−1.79)·h·(1−0.08) ≈ 6.68 m
- I answer with the asphalt width between kerbs.
- Confidence: moderate. Geometry is ±3%; the main uncertainty is which edge the reference counts as the road.
