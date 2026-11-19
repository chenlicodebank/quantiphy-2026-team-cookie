# q_1209 — diameter of the moving bicycle's wheel (m)

Answer: **0.636 m** (f ≈ 1880 px; range 0.60–0.66 for f = 1800–2000).
The file and the question both use 33 fps; t=1 s is frame 33, t=2 s is frame 66.

## Wheel pixel size (wheels4.py)
- The fender hides the top of the tyre, so I did not use the tyre outline there. Instead I fitted an ellipse to
  the silver rim's outer edge, sampled all the way round the wheel (it shows under the fender): rms 0.2 px,
  120–135 edge points per wheel. Tyre thickness = distance from the rim edge to the tyre's outer edge, read on
  rays near the bottom of the wheel (3.4–3.9 px).
  Vertical tyre diameter = rim vertical extent + 2 x thickness.
  Overlays are in frames/wheels4_*.png.
- Frame 33: front 100.3 px, rear 104.0 px. Frame 66: front 84.8 px, rear 88.4 px. The front wheel is farther
  from the camera, so it looks smaller, as expected.
- Ellipses fitted to the lower arc of the tyre outline alone (wheels2.py) were unstable (±10 %), so I did not use them.

## Focal length: the two routes disagree
1. Speed prior + walker depths (focal.py): assume the walker covers 1.236 m between t=1 and t=2. Then
   f ≈ 3000 px. But the walker's depths do not fit its own image track at any f (pedcheck.py): moving along its
   track direction, the t=2 depth comes out 16.3–16.55 m, not the given 16.67. So this route rests on data
   that does not hold together.
2. Bike geometry (independent cues that agree):
   - Wheel shape (rimfit2.py, image only): the rim's width/height ratio changes across the frame as the viewing
     angle changes. Fitting an exact projection of a 3D circle over 20 frames per wheel gives
     f = 1790–1970 for camera pitch −5° to +5° (rear and front agree; rms 0.006, versus 0.023 at f = 3000).
     With the pitch implied by a horizon near y ≈ 571 (camera tilted about 5.6° up), f ≈ 1800.
     The fitted wheel heading is 26–27°.
   - The bike's direction of travel from its depths matches that wheel heading at f ≈ 1800–1900. At f = 3000
     the bike would have to travel 13° off its own heading.
   - Constant speed between the depth frames holds at f ≈ 2000 (speedprof.py). At f = 3000 it would
     accelerate by 8 %.
   - Moving the bike along its image vanishing point from the t=1 depth reproduces the t=2 depth (14.64 m) at
     f ≈ 1900–2000 (pedcheck.py).
   - Chosen value: f ≈ 1880 px (horizontal field of view about 54°).

## Diameter (diameter.py)
For each wheel, the 3D centre is placed on the bike's line of travel (bike origin = midpoint between the hubs,
at the given depth). Then I solved for the diameter whose exact projection matches the measured vertical
pixel size.

| f (px) | diameter (m) |
|---|---|
| 1800 | 0.663 |
| 1850 | 0.646 |
| 1900 | 0.630 |
| 1950 | 0.615 |
| 2000 | 0.601 |
| 3000 | 0.408 |

At each f, all four estimates (front and rear at t=1 and t=2) agree within 1 %.
The f = 3000 value (0.408 m) is what the walker-prior route gives.

## Check and confidence
The second check is the four separate estimates (two wheels, two times, each at its own depth). They agree
within 1 % at f ≈ 1800–1900, but differ by 3 % between t=1 and t=2 at f = 3000.
As a sanity check, 0.64 m is a normal adult bike wheel (26"–700c); 0.41 m would be a child's wheel.
Confidence is moderate. The main risk is that the reference really uses f ≈ 3000 (answer 0.41).
