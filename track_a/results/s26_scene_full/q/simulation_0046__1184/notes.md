# q1184: height of the telephone booth (m)

Prior: the moving bicycle's wheel diameter is 0.65 m. depth_info gives the bike and human camera distances at t = 1 s and t = 2 s.
The file's fps (33) equals question_fps (33), so t = 1 s is f33 and t = 2 s is f66. The camera is static. This is a 3D scene.

## Booth pixels (`booth_prof.py`, `booth_vp.py`, frame 0)
- Front face top edge (roof front edge): y = 151.5 (subpixel gradient; it slopes from 152.6 to 151.4 across x 84-220).
- Front-right post bottom on the sidewalk: y = 537 (corner x ≈ 226).
- Front face pixel height: 385.5 px. The booth top is above the camera height, so the front top edge is the top of the booth.
- The right side face's top and bottom edges recede to a vanishing point at about (1190, 339).

## Camera geometry
- **Horizon** (`horizon.py`, `horizon2.py`): I fitted a pencil of 13 long street-parallel lines on the median background (cornices, signs, curb, fence base). This gives y_h = 334.5 and a street vanishing point at x ≈ −15000, so the camera is yawed about 6° and the street recedes to the left. The booth side face gave y_h ≈ 339. I use y_h ≈ 336, roll ≈ 0 and pitch ≈ 1.4°.
- **Focal length.** For perpendicular vanishing points, f² = (1190 − 960)(960 + 15053), so f ≈ 1919 px. The wheel size with the given bike depths gives f = 1947 (t = 1) and 1900 (t = 2), mean 1923. The two routes agree.
- **Wheels** (`wheeltrend.py`): background-difference ellipse fits on both wheels, f14-79. The outer diameter is 102.2 px at f33 and 95.6 px at f66. The ground-contact row is 603.5 at f33 and 591 at f66.
  - Check: the bike's given depth times its row above the horizon is constant to within 0.6% (12.38·267.5 vs 12.92·255), so the bike data are self-consistent.
- **Curb** (`curbedges.py`): the street (where the bike rides) is lower than the sidewalk (where the walker and the booth stand).
  - The curb face is 19-20 px tall at gutter rows 574-590.
  - So curb height / camera height above street = 19.5 / (gutter row − y_h) ≈ 0.079, and Hs = 0.921 · H_street.

## Main route: bike wheel scale plus ground plane (`final.py`)
- For each wheel and frame, camera height above the street is H_street = (0.65 / d_px)·(y_contact − y_h). The median is 1.721 m (1.698 for f < 47, 1.737 for f ≥ 47).
- Camera height above the sidewalk: Hs = 1.585 m.
- Booth depth: Z = f·Hs / (537 − y_h). Booth height = 385.5 · Hs / (537 − y_h) = **3.04 m**.
  - The range is 3.00-3.09 over y_h = 330-342 and the early/late frame halves.
  - Booth front depth ≈ 15.1 m.

## Second route: walker depths
- Booth depth = Z_walker·(feet row − y_h)/(537 − y_h), using feet rows 559 and 557.5 and f = 1900-1947.
- This gives 3.11-3.20 at t = 1 and 3.24-3.34 at t = 2.
- The human depth_info does not fit the image: the walker's pixel height changes by only 1% between t = 1 and t = 2 (246 → 243.5 px, feet 559 → 557.5), while the given depths imply a 4.6% change in Z. With the measured horizon and curb, the given walker depths would put him 4-8% too far for a sidewalk point at row 558.
- So I weight the bike/prior route, which is self-consistent and agrees with the vanishing-point focal length.

## Answer
3.06 m. This is the bike route (3.04), nudged slightly up for the possible blur and antialiasing inflation of the wheel's pixel diameter and towards the walker route.
Confidence is moderate: about ±4% from the geometry, with a larger risk if the human depths are the right ones (≈3.2).
