# q_1658 — height of the freestanding art display panel

The file rate and question_fps are both 33.

## Object
The "freestanding art display panel" is taken to be one of the two framed paintings on stands, either side of the sculpture.
- Both stand on feet and have the same size: left panel bbox y 464-614, right panel y 464-613.
- If the small silver piece at the far right were meant instead, the same floor method gives about 2.7 m.

## Camera (solve_f.py)
The person walks at constant camera depth: head-top row and pixel speed are constant.
- Pelvis track: 7.63 px/frame.
- Given distances: 5.424 m at t=0 and 4.886 m at t=1. With the 1.3 m/s speed prior, these give f = 902 px and person depth Z = 4.655 m.
- All three constraints agree: speed plus d0 reproduces d1 = 4.886 exactly.

## Panel depth
**The given distance of 4.223 m cannot be the panel's geometry.**
- The person, at Z = 4.655 m, occludes the left panel at frames 28-61, so the panel lies behind the person.
- Taken at face value, 4.223 m would give Z = 4.13 m, a height of 0.69 m, and a panel floating 0.65 m above the floor in front of the walker.
- The asset origin is therefore offset from the geometry. The bench origin is also about 0.3 m in front of its measured geometry.

**Floor-contact route (horizon.py, panel.py):**
- The bench base plate's side edges meet at (540, 542), so the horizon is at v ≈ 540-542 and the camera is level. This agrees with the principal point at the image centre, and the statue's vertical edges show no convergence.
- Person sole at row 732 → camera height H = 4.655 × 192 / 902 = 0.991 m.
- Panel feet at rows 614-615 → Z ≈ 902 × H / 75 ≈ 11.9-12.1 m.
- Height = H + (540 - 464) × Z / f gives 1.995 m (left panel) and 2.009 m (right panel). With the horizon at 542 instead, it gives 2.03 m.
- Check: the plate is a rectangle on the floor. Its front width (817 px at Z = 2.12 m) and back width (632 px at Z = 2.81 m) both come to about 1.93 m.
- Plain pixel height × Z / f gives 151 × 12.18 / 902 = 2.04 m.

## Answer
2.01 m. Confidence is moderate.
- The main risk is a reference answer built from the inconsistent 4.223 m origin distance, which would be about 0.69 m.
- The geometric answer is consistent with the occlusion, the floor contact, and a plausible real size for a freestanding display.
