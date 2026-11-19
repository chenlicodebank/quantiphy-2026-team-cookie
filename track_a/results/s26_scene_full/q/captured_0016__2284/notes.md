# Q2284: soccer-ball displacement between 1.0 s and 1.5 s (cm)

The file is 24 fps and question_fps is 24, so 1.0 s is frame 24 and 1.5 s is frame 36. Camera: f = 0.5959·1280 = 762.8 px, principal point (640, 360).
Depth is given only at t = 1.5 s (ball 1.402 m). The prior (g = 9.8) is used only for the cross-check.

## Measurements
- **Frame 24** (ball held low at the thrower's hip, nearly still at the bottom of the wind-up):
  - The left side is hidden behind the trousers (a black panel is cut by a straight vertical edge at x≈243). The bottom is hidden by the hand.
  - I took half-contrast radial edges (`edges.py`) and fitted a sphere-silhouette cone to the clean top/right arc (`conefit.py`, about 170° of arc, rms 0.55 px).
  - Result: centre (269, 609), angular radius α = 3.72–3.83°, equivalent to a diameter of 99–102 px on the axis.
  - Frames 22 and 23 give α = 3.76° and 3.70°, which is consistent.
  - The scene record's centre for this frame, (272.5, 601.5), is nearly the same. Its bounding box is not reliable (occlusion).
- **Frame 36** (motion-blurred, mostly horizontally):
  - Vertical profiles (`vprof.py`): top edge y≈29, bottom edge y≈124. The bottom black panel is part of the ball; the record's mask missed it and had 116.
  - Vertical extent is 95 px. Frames 37 and 38 give 96 and 94 px, which is consistent.
  - Centre (809.5, 76.5). The x value matches the record; y is corrected from 71.5.
  - Solving the cone for that vertical extent gives α36 = 3.065°.
- **Ball size check:** at 1.402 m the ball diameter is 16.3 cm (z reading) or 15.0 cm (Euclidean reading), which is plausible for a mini ball.
- **Depth at frame 24:** scaled by the ratio of angular sizes, it is 1.055–1.09 m as z (1.12–1.155 m if depth is read as Euclidean).

## Displacement (`depth.py`)
Positions use the card back-projection ((u−cx)/f, (v−cy)/f, 1)·depth.
- With depth read as z: 123.5–125.3 cm.
- With Euclidean depth put into the same card formula: 125.3–127.6 cm.
- Exact Euclidean geometry: 113–115 cm. This is less likely, because depth-camera values are z.

Answer: **125 cm**.

## Second route (`physics.py`)
I fitted a 3D ballistic trajectory to the flight centres (frames 31–42) with |g| = 9.8.
- Assuming the frame dropped between 35 and 36 (the 93 px image jump), the fit has rms 1.9 px and gives z36 ≈ 1.67 m, against the given 1.40 m. Gravity points about 45° down the optical axis, which matches a camera pitched down.
- Without the dropped frame the fit is poor (rms 6 px).
- This only roughly confirms the scale (within about 20%, since depth is weakly constrained by perspective). It supports the order of magnitude, not the 3% level.

## Confidence
Moderate. The main uncertainty is the frame-24 depth inferred from size: about ±4% from the edge fits and the blurred frame-36 extent. If the reference's frame-24 depth was a measured surface depth, the answer could shift by a few cm.
