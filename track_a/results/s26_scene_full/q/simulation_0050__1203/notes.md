# q1203 – height of the telephone booth (simulation_0050)

Answer: **3.0 m**

Prior: pedestrian walking speed = 1.236 m/s. depth_info: bike 11.896 m (t=1) and 14.642 m (t=2); human 15.865 m and 16.671 m.
question_fps = file fps = 33, so t=1 is frame 33 and t=2 is frame 66.

## Booth pixels (m3_profile.py, m20/m21, frame 96 background)
The front-right vertical corner edge is at x≈240. Its roof top is at y≈295 and its base bottom at y≈641.5, so the edge is about 346 px tall.
The base corner lies on the curb-top image line B (B is 642.1 at x=240), so the booth stands at the front edge of the sidewalk.

## Camera (pure image geometry, no priors)
- Vertical vanishing point from long vertical edges (m12, m16): about (630–650, −24000…−27700). The lean is zero near x≈620, not at 960, which means a camera roll of about −0.7°.
- The booth box's own vanishing points (m21): side face (1809, 504) from 5 lines; front face (−2853, 577). The horizon slope (−0.016) agrees with that roll. Orthogonality of the side, front and vertical vanishing points gives f ≈ 1800–1900 px with the principal point at the centre.
- The cyclist's motion, using its depth_info, agrees with f ≈ 1900–1950. Three tests point the same way: uniform motion fits with 1 px rms (m6/m13), apparent size × depth stays flat (m15), and the bicycle's foreshortening fits best there (m18).
- With roll slope −0.0126, the horizon fitted from the wheel contacts (m19/m24) is about 525 at the image centre. The vertical vanishing point this implies matches the measured one at f≈1900.

## Inconsistency found
If you take the human's depth_info and the walking-speed prior together, you get f=3015 (m1). Image geometry rules that out: it would need the horizon at y≈740, and the booth's vanishing points would not be orthogonal.
Under the geometric camera, the pedestrian's feet on the sidewalk plane put him at a range of 12.4–12.8 m, not 15.9–16.7 m. In that position his height stays constant at 1.68–1.70 m in every stance frame (drift about 1%), he walks parallel to the cyclist (within 2.6°), and his speed is 1.19 m/s, close to the 1.236 prior (m23).
So the pedestrian's speed prior and the cyclist's depths agree on one metric scale. Only the human depth_info is inconsistent with the image, so I did not use it.

## Height computation (m22, m24)
1. Road plane: from the cyclist's wheel contacts, frames 8–93, with positions along its 3D line built from depth_info.
2. Curb height: from curb lines A (bottom) and B (top), giving 0.13–0.14 m.
3. Booth base: the base pixel's ray intersected with the sidewalk plane.
4. Height: the distance along the vertical until the point projects onto the top row (295).

| f (px), roll slope | scale from cyclist depth | scale from the speed prior (h × 1.236 / measured pedestrian speed) |
|---|---|---|
| 1750–2050, all rolls | 2.72–3.14 m | 2.94–3.07 m |
| 1900, −0.0126 (best fit) | 2.92 m | 3.01 m |

The speed-prior route barely depends on f or roll, and the two routes agree best near f=1850–1900.
For reference, using the human depth_info instead would give about 3.6–3.7 m, and using f=3015 would give about 2.4 m. Both are rejected because they contradict the image geometry above.

Confidence: moderate, about ±7%. The main remaining uncertainties are the exact top row of the roof lip (it could be 292 instead of 295, which adds about 1%) and the horizon/roll.
