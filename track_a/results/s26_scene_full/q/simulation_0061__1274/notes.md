# q1274 – diameter of the bicycle wheel (simulation_0061)

The file and the question both run at 24 fps. 3D Blender scene with a static camera. Principal point is assumed at (1080, 540).

## Scale: focal length from the white van (prior a = 4 m/s², depths at f14 and f38)
- `vanwin.py`: segments the van's tan side windows in every frame. The tracking point is the centre of the middle window, plus 13 px to reach the van's bbox centre (offset measured at f38). Frames 5–55 are clean.
- `focal.py`: for a trial f, back-project the van origin at f14 (D = 45.5234) and f38 (D = 43.9499) and take the straight 3D line through those two points. Every frame's ray is intersected with that line to get the path s(t), and a quadratic is fitted to s(t).
  - Solving a = 4 gives f = 2210 px (frames 3–55). Other frame windows give 2135–2236.
  - The fitted start time is t0 ≈ −0.03 s, i.e. the van starts from rest at about t = 0, for every f tried.
- `final.py`: if the van starts from rest at exactly t = 0, then |P38 − P14| = 2·(1.583² − 0.583²) = 4.333 m, which gives f = 2279. With t0 = −0.034 it gives f = 2199.
- Adopted f ≈ 2225–2240 px (horizontal FOV ≈ 52°).

## Wheel pixel size (`wheel3.py`)
- Background difference against frame i−12, so the bike has moved out of the way.
- A circle is fitted to each white tyre, starting from the cyclist box in the scene record. Fits were drawn and checked on frames 30 and 38 (`frames/wfit*.png`).
- The outer edge is taken at the half-maximum point of radial profiles. The raw profiles show no dark tread outside the white ring, so the white ring is the outer tyre.
- Vertical outer diameter over frames 28–38, both wheels: **34.85 px** (rear ≈ 34.4, front ≈ 35.1). The centreline diameter is 32.5–33.0 px.
- The horizontal extent is ≈ 1 px larger, which looks like motion blur, so I used the vertical one.
- Bike depth is interpolated linearly between f14 (41.901) and f38 (40.3415), and converted to optical-axis depth Zc.

## Result
Diameter = D_px · Zc / f:
- 0.639 m at f = 2210
- 0.631 m at f = 2240
- 0.623 m at f = 2270

Per-frame spread is ±0.007. **Answer: 0.635 m.**

## Checks
- Pedestrian height from the same f: 1.82 m at f14 and 1.84 m at f38. The two frames agree, and the value is plausible.
- Van length ≈ 6 m, which is right for a full-size van. Cyclist speed ≈ 5.2 m/s.
- The cyclist moving parallel to the van is only a weak constraint on f (about 2° difference at f = 2200), so it was not used.
- Confidence: the f uncertainty is about ±3%, and the pixel diameter is good to about ±2%.
