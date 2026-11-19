# Q1239 – height of the streetlight (simulation_0058, 3D)

Object: the prominent double-lantern street lamp on the near-left sidewalk (the pedestrian walks behind it).
File fps = question fps = 24. The lamp is static, so the time does not matter.

## Pixel extents (lamp_px.py, lamp_base.py, on scene/background_final.png, checked on frame 70)
- Top finial: row 333.5 at the pole axis, x = 129.
- Base plate: dark plate ends at row 817 (front edge). The plate centre on the ground is at about row 811.
  The scene record said 829, which was wrong: the row 817–829 band is sidewalk.

## Camera (fit.py)
- Principal point at (1080, 540). Horizon/vanishing point (1253.1, 422.5) from scene/, which gives pitch and yaw for each f.
- Focal length from the prior (white van, a = 4 m/s²). The van's rear edge on row 520 is back-projected onto
  the vertical plane of its path. That plane runs through the van origin at t = 0.58 s (depth 31.07 m), with its
  direction perpendicular to the main road. A quadratic fit of the path position s(t) gives a = 4 at:
  f = 2201 (frames 2–71) and f = 2245 (frames 2–36, the cleanest part with residual 3 mm). The second half is noisier.
- Check: the 3D chord between the van origins at the two given depths (frames 14 and 38) is 4.45 m. The track
  gives 4.58 m at f = 2200, which scales to about 4.49 m at 2245, so f is consistent at about 2230–2250.
  The chord direction matches the cross-street direction (cos = 0.99997).
- Camera height: each object's origin is placed from its depth, then I solve for its height above the
  ground-contact row. Taking ground contacts at the same depth as the origin:
  - Pedestrian: H = 2.79–2.84 m, pelvis height 0.87–0.88 m, which is plausible.
  - Cyclist: H = 2.75–2.83 m, origin height 0.83–0.87 m.
  - Taxi and van give 2.86–3.12 m. They are biased high because their contact row comes from the near-side or
    front tyres, which are closer to the camera than the origin.
  - Used H ≈ 2.80 m.

## Lamp height (lamp.py)
The base ray is intersected with the ground plane, about 17.6 m from the camera. I then solve for the vertical
height whose top projects to row 333.5:
- f = 2245, H = 2.79: 3.42 m
- f = 2200, H = 2.84: 3.48 m
- The base-row choice (811 or 817) changes the result by only 0.01 m.

Answer: **3.44 m** (f ≈ 2230).

## Sanity check
- The lamp's pixel height is 477 px; the nearby pedestrian is about 240 px and slightly farther away. That gives
  the lamp about 1.9 × a person, so roughly 3.3–3.5 m.
- The pedestrian's pelvis height (0.87 m) and the cyclist's origin height come out plausible. This supports the
  combination of f and H.

Confidence: moderate-good, about ±4%. The main uncertainty is f (2200–2245, about 2%) and H (about 2%).
