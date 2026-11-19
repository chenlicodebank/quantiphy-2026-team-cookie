# q_1661 — height of the pedestal (square base) of the central sculpture

File fps = question_fps = 33. t=1 s -> frame 33.

## Which object
The plinth under the sculpture has two parts. The upper tapered tier (v 673-768) has the same light stone texture as
the sculpture: it is the sculpture's own base. The dark square block below it (u 332-632, v ~773-895) is a
separate object, the "pedestal (square base)". Answer = height of the dark block.
Alternative reading (dark block + stone tier): ~0.90 m.

## Camera (pinhole, principal point at image centre), from depth_info + prior
- Man pelvis at frames 0 and 33: (882.9, 648.3) at 6.84 m and (688.6, 649.8) at 6.49 m. His pixel height and feet row
  stay the same, so the forward depth Z is constant. Solving gives Z = 6.36 m and f = 908 px.
  Check: 1.87 m at 6.36 m -> 267 px, which matches the observed upright bbox height of 265-268 px.
- Camera is level. Feet (sole) at v=786 give a camera height H = 1.722 m. The head top at v=520 gives 1.86 m,
  which fits the 1.87 m prior.
- Check: the right panel stand's base on the floor (v=686, u=719.5) is predicted at 11.06 m from the camera.
  The given value is 11.042 m (0.15 % off).

## Pedestal
Edges measured in code (prof.py) from column profiles of the background image: front-face bottom v=895, top
front edge v=773 (the top face is lighter grey above it, the front face darker below).
- Front-face depth Z_f = H*f/(895-540) = 4.407 m. Block width is 1.46 m.
- Height h = 122 px * Z_f / f = H*122/355 = 0.592 m.
- Consistency check: the projected right edge of the block's top face at u=620 is predicted at v=742.6. It is
  observed at 742.
- Second route: H taken from the panel distance (11.042 m) instead of the feet gives 0.591 m.

Confidence: good for the dark block (about ±2 %). The main risk is the naming ambiguity above.
Answer: 0.59 m.
