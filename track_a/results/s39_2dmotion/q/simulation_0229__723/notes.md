# q_723: acceleration of the paper airplane at t = 1.25 s

The file runs at 24 fps and question_fps is also 24, so t = 1.25 s is frame 30. The video is a 2D render with a static
camera. The prior is "length of the chalkboard = 5 m".

## Scale
- `board.py` takes horizontal intensity profiles on frame 45 at rows 310–725:
  - Outer wooden frame: x ≈ 319 to 1691, so **1372 px**.
  - Green surface: x ≈ 342 to 1670, so 1328 px.
  - These match the record in scene/ (1372 and 1327 px).
- The SAM 3 "chalkboard" mask at frame 30 has a box from 324.7 to 1690.1, so 1365 px (0.5 % off my value).
  - SAM includes the outer frame.
  - Its left edge is about 5 px inside mine because the sun beam washes out the left frame bar. My profiles show the
    step at about 319 on every row, so I kept 1372 px.
- I take the chalkboard object as the board including its frame: 5 m / 1372 px = 3.644 mm/px.
- If only the green surface counts, the scale is 3.765 mm/px and the answer would be 3.25 m/s².

## Plane motion
- `measure.py` subtracts a background (median of the plane-free frames) and builds a hysteresis mask. It records
  the bbox centre and the axis midpoint for frames 12–38.
- The full plane is visible in frames 14–35, with length 133–143 px.
- At frame 30 my bbox centre is (1475, 416) and my axis midpoint is (1475, 419.3). The SAM mask at frame 30 has box
  centre (1474.7, 419.2) and length 141 px. They agree within 3 px, and the overlay sits on the plane.
- Acceleration means the change in scalar speed: a(30) = (v(30) − v(29)) · fps. Raw one-frame differences are too
  noisy (±2 px), so I fitted smooth polynomials to x(t) and y(t) and took the backward difference of the fitted
  positions (`fit.py`).
- Own track:
  - deg 4 over frames 14–35: −1.49 px/f²
  - deg 3 over frames 20–35: −1.48
  - deg 3 over frames 22–35: −1.50
  - deg 2 over frames 24–35: −1.60
  - Linear fit of the per-frame speed over frames 20–35: −1.51
- Second route, the SAM 3 track (`fit_sam.py`, bbox centre and centroid):
  - Polynomial fits give −1.29 to −1.64 px/f².
  - Linear fit of the speed: −1.45 to −1.50.
- Chosen value: about −1.50 px/f², i.e. −864 px/s², which is **3.15 m/s²** in magnitude (the plane is decelerating
  along its path).

## Confidence
- The fits spread by about ±8 % (1.3–1.7 px/f²) and the scale is ambiguous by about 3 %.
- Overall I expect the error to be about 10 %.
