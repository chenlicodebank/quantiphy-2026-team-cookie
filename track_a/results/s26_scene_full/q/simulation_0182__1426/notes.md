# q1426 – speed of the box at t = 1.5 s (simulation_0182, 3D)

The question and the file both use 24 fps, so t = 1.5 s is frame 36. The reference speed is the backward difference between frames 35 and 36, which is the speed at t ≈ 1.479 s.
Prior: the box accelerates at 2.338 m/s² after 0.75 s (it slides down a straight ramp). Depths: 9.522 m at t = 0 and 9.384 m at t = 0.5 s (frame 12).

## Camera
- Pitch and roll ≈ 0. Vertical edges (the blue post and the box edges) have dx/dy ≤ 0.002 (`vert.py`). The principal point is assumed to be (960, 540).
- **Focal length from free fall** (`fall.py`, `fall2.py`, and the centroid track). Over frames 0–7 the box falls from rest with no x drift. The silhouette centroid gives a pixel acceleration of about 2260 px/s² (fit with v0 = 0). The whole-box template gives 2255 px/s².
  - Zc = 9.522 / |ray| = 9.33 m, so f = 2258 × 9.33 / 9.81 ≈ **2150 px** (about ±50 px).
  - A template on the front face alone gives a higher acceleration because that face is closer than the centre. I did not use it.

## Ramp direction
- Vanishing point of the ramp (`ramp_edges2.py`, `vp_box.py`):
  - The lower edge of the near rail is clean: y = 0.6680x + 420.0, rms 0.7 px.
  - The far roller edge is noisy: slope 0.603–0.614.
  - The line of the box centroid track has slope 0.612.
  - These lines meet at a vanishing point between (−4550, −2620) and (−5600, −3320). The lines diverge toward the bottom right, so the ramp descends toward the camera, with d ≈ (0.82, 0.48, −0.27 to −0.32).

## Speed
- 3D line model (`final.py`): the line passes through P12, the frame-12 centroid back-projected to 9.384 m (it lies 1 px off the image line of the slide), and runs along d.
- Each centroid in frames 18–35 is mapped to an arc length s along this line. I then fit s(t) with the acceleration fixed at the prior value.
- With f = 2150: v(1.479 s) = 4.09–4.11 m/s, depending on the vanishing point and the frame window. Over f = 2100–2200 it ranges from 4.03 to 4.18.

## Checks
1. Without fixing the acceleration, the fitted value at f = 2150 is 2.25–2.44 m/s², which agrees with the 2.338 prior. Because of that, the focal length from free fall and the scale implied by the prior agree independently.
2. Second route (`fit_vp.py`): I took d from the vanishing point and solved for the focal length that makes the fitted acceleration equal 2.338. This gives f = 2060–2290 and v = 3.9–4.2 m/s.
3. A direction fit with free φ at f = 2150 (`fit3d.py`) gives about 4.10 m/s.
4. Ignoring perspective (one constant pixel scale) would give 3.3–3.4 m/s. That underestimates the speed because the box moves about 0.5 m closer to the camera during the slide.

## Answer
**4.10 m/s.** Confidence is moderate: the uncertainty is about ±4%, and it comes mainly from f and the depth slope of the ramp.
