# Q1365: average speed of the yellow taxi, from start to end (m/s)

Answer: **4.1 m/s**

## Where the earlier answers part ways
Both answers come from the same kind of track: the taxi back-projected with its given depths (31.05 m at frame 14,
30.43 m at frame 38). They part ways at the **focal length**:
- C1 (4.14) used f ≈ 1795 px, from the road vanishing points and the vertical vanishing point.
- C2 (2.65) used f ≈ 2350 px, from assumed heights of the pedestrian (1.75 m), the taxi and the van (2.4 m). A Chevy
  Express van is about 2.05 m tall, so the 2.4 m van height alone pushes f up by about 15 %. C2 also used the
  centroid track, which the cyclist contaminates in frames 0-20.

## My measurements
- Time base: question_fps = file fps = 24, 72 frames. Frames 0 and 1 are identical (mean abs diff 0.027, against
  0.33 for later frame pairs).
- Focal length (`vp.py`, `geom.py`): I fitted the kerb edges in code (rms 0.3-0.6 px). Two independent lines per road
  direction give vA = (-1284,-254) and vB = (2681,-255). The horizon is level at y ≈ -255. Assuming orthogonal roads
  and the principal point at the image centre gives f = 1776-1783 px, pitch 24°. C1's vertical-VP route gave
  1795-1828.
- Checks of this scale against standard objects:
  - Pedestrian height (frames 0-14, pelvis depth from depth_info): 2.0 m at f = 1780, 1.53 m at f = 2350. At 1780 the
    pedestrian is tall but plausible (the bbox includes blur).
  - Van, frame 71 (`vancheck.py`, `vanlen.py`): wheelbase 3.74 m at f = 1780 (3.35 m at 2350). The length from the
    front-side corner to the rear-side corner is 5.17 m; adding about 0.8 m of front-bumper protrusion gives about
    6.0 m, which matches the 6 m prior. At f = 2350 the van would come out at only about 5.2 m.
  - So f = 2350 is rejected and f ≈ 1780-1830 is used. Camera height is about 9.2-9.4 m (consistent from the taxi and
    van depths).
- Taxi track (`taxispeed.py`): the roof taxi sign, which sits on the car's centre line, was tracked in all 72 frames.
  Each frame's ray is intersected with a plane parallel to the ground. The plane's offset was solved so that the
  origin (0.8 m below the sign) reproduces the given depths at frames 14 and 38; the two frames agree to 0.01-0.02 m.
  Speed = backward difference × 24.

| f | mean per-frame speed, steps 1..71 (incl. the zero 0→1 step) | steps 2..71 |
|---|---|---|
| 1780 | 4.11 | 4.17 |
| 1800 | 4.08 | 4.13 |
| 1830 | 4.02 | 4.08 |

## Second-route checks
- A polynomial-smoothed 3D path (`smoothpath.py`, degree 3-5, residual about 1 cm) gives 4.03-4.18 m/s.
- The record's bbox-centre track gives 4.15-4.24 and its mask-centroid track gives 3.80-3.88. The centroid shifts as
  the car turns and is contaminated by the cyclist early on.
- The chord speed (3.9) is lower than the path speed because the taxi is turning; the path length (sum of per-frame
  steps) is what the question asks for.

## Conclusion
I agree with C1. The focal length C2 took from assumed object heights is too long: with it, the van comes out
clearly shorter than its 6 m prior. I answer 4.1 m/s, the midpoint of 4.03-4.17 (f 1780-1830, with or without the
duplicated first-frame step). Confidence about ±4 %.
