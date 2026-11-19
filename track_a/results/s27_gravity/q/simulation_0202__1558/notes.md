# Q1558 – width of the table (desk), simulation_0202

File fps = question fps = 24. 3D render, 2124x1080, static camera; principal point assumed at image centre (1062, 540).

## Camera from the prior (fitfall.py)
The magnifying glass falls from rest at about frame 0 (prior: a = 9.8 m/s^2). Model: P(t) = P0 + ½g((t−tr)²−tr²)·down,
with P0 on the f0 pixel ray at the given depth 4.2401 m, down = (0, cosθ, sinθ) for a camera pitched down by θ.
Fitting frames 0-10 (bbox centres from scene/tracks) gives f = 2675 px (HFOV 43°), pitch 15.7°, tr ≈ 0, rms 0.37 px.
This is the same from every starting guess. The x drift of the falling glass toward the centre is reproduced by the pitch.
Checks:
- With the t=0.5 s depth (4.4097 m) on the frame-12 ray, the drop is 1.044 m. That implies impact at t = 0.461 s,
  which matches the observed contact between frames 10 and 11.
- The glass at rest sits 1.400 m below the camera (along world down). The near desk corner, put at its given depth
  3.593 m on pixel (700, 880), is 1.386 m below. So the glass lies on the desk top (origin about 1.4 cm above), and the
  given near-corner depth belongs to the top surface's near corner.

## Desk corners (frame 29, enhanced zoom crops, crops.py)
Top-surface corners: near N (700, 880), far-left L (470, 686), front-right R (1993, 652). The back-right corner B is
hidden by the phone and stand, at about (1590-1615, 522-526).
The top plane runs through N with its normal along world down. L, R and B are intersected with that plane (desk.py-desk4.py).
- Width (short horizontal side) N–L = 0.924 m. Moving the corner pixels by ±5 px gives 0.89-0.96 m.
- Length N–R = 2.25 m; the angle L-N-R is 95° (close to a right angle, so the geometry is consistent).
- The given far-right depth 5.009 m matches the bottom (floor) corner under R. A point 0.76 m below R on the top plane
  has depth 5.005 m, and 0.76 m is a normal desk height. The given distances are therefore consistent with the AABB
  corners top-near and bottom-far-right.

## Second route
I also measured the right short side R–B on the same plane. With B between (1615, 526) and (1590, 524) it gives
0.92-0.96 m. This agrees with N–L.

## Answer
Width (front-to-back depth of the desk) ≈ 0.93 m. The length is about 2.25 m.
Confidence: moderate-high, about ±4%. The main uncertainty is where exactly the corner pixels sit on the molded edge.
