# q_1452 – height of the forklift (simulation_0299, 3D Blender render)

Prior: acceleration = 2 m/s² (from rest). Depth: 16.7953 m at t=1 s (frame 24) and 19.0980 m at t=2 s (frame 48).
question_fps = file fps = 24.

## Method
1. **Motion model.** The forklift translates along a straight horizontal line without rotating, with s(t) = ½·2·t² = t².
   The fitted t0 is 0.00 s and the image track starts at frames 1–2, so t0 = 0.
2. **Tracks.**
   - About 107 KLT features on the body (`klt.py`), tracked over frames 4–71.
   - Mask-extreme tracks (`extremes.py`): wheel bottoms, mast top, roof top, fork tip and counterweight.
   - All of these were fitted jointly with a shared heading D and a per-point 3D start position (`pipeline.py`). The median residual is 0.36 px.
   - This track fit is exactly degenerate in f: the cost is flat, so f has to come from somewhere else.
3. **Focal length, route A (vanishing points, `vp_lateral.py`, `vp_solve.py`).**
   - The lateral roof-rear bar has two sub-pixel edges, fitted in frames 12–71 (rms 0.2–0.6 px).
   - Because the body only translates, all these lines meet at the lateral vanishing point vA ≈ (7084, −475).
   - The heading vanishing point from the track is vD = (−1138, −480).
   - Orthogonality gives f² = −(vD−c)·(vA−c), so **f = 3550 ± 16 px** (bootstrap). Frame subsets give 3420–3630.
   - The horizon (vD→vA) has a roll of 0.04°, which confirms a zero-roll camera. So up ⟂ D and up ⟂ the camera x axis.
4. **Focal length, route B (given depths).** With the origin taken as the ground point under the wheelbase centre:
   - f = 3505 reproduces both given depths: 16.797 and 19.095 m, against 16.795 and 19.098 m.
   - Other origin choices: ground under the bbox centre gives f ≈ 3180 (H ≈ 2.79 m); 3D bbox centre gives f ≈ 3440 (its two depths fit worse).
   - Route A agrees with the wheelbase/ground-root reading.
5. **Height.** Height = roof-top (highest point; the mast top is about 0.29 m lower) above the ground. The ground is the wheel-contact level.
   - At f = 3505: H = 2.663 m. At f = 3550: H = 2.645 m.
   - The front wheel's contact gives a ground 0.08 m lower than the rear wheel's.
   - The image-lowest tyre point sits slightly above the true contact, so the true ground is probably a little lower. Small upward nudge.

## Answer
H ≈ **2.67 m**. Spread across the f range 3420–3630 and the ground choice: 2.57–2.74 m.
Confidence: moderate-good (about ±4 %).
