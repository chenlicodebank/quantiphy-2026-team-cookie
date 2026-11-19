# Q1271: length of the white car (the white van), simulation_0061

The file rate and question_fps are both 24 fps. The "white car" is the white full-size van (scene/ calls it `van`), seen side-on and driving right with a yaw of about 16° toward the camera.

## Scale and focal length
- **Prior:** acceleration 4 m/s². **Depth:** van origin at 45.5234 m at f14 and 43.9499 m at f38.
- **Track:** for a trial focal length f (principal point 1080, 540), I back-projected the bbox centres at f14 and f38 with their given depths. That gives two 3D points, and so the van's line of motion.
- **Projection:** I intersected the near-rear corner's rays (`x0` track) with that line, offset by half the length and half the width. This gives the path s(t), and I fitted the acceleration (`scan3.py`, `scan4.py`).
- **Focal lengths that reproduce a = 4 m/s²:**
  - Free quadratic fit: f = 2110–2160.
  - Van at rest at t = 0 (it is static at f0–1): f = 2164–2195.
  - Early window only: up to 2267.
  - Chosen: **f ≈ 2190 px**.
- **Check on f:** the main road's vanishing point, from lamp-post bases C, D and E, is at u ≈ 1750. If the van's street is perpendicular to the main road, that implies f ≈ 2245, which agrees within 2.5%.
- **Late speeds:** per-frame speeds at f50–71 match 4·t within about 1.5%.
- **Correction to the record:** the horizon is at y ≈ 480, not 535. Four identical lamp posts (A, far-left, C, D) all give 478–485. With this horizon, the pedestrian's and the van's ground rows agree on one camera height, about 2.7 m. The van's pixel-height growth from f14 to f66 and from f45 to f71 agrees with the modelled depth change within about 1–2 px.

## Length
- **Measured frames:** f64–71, where the whole van is visible and near the vanishing point (u ≈ 1700), so its width barely adds to the horizontal extent.
- **My zoomed edge readings:** f66 is 1370.6 to 1703.6 (333 px); f71 is 1500.6 to 1843.7 (343 px). The record has 335 and 345.
- **Model:** a 3D box (L, W = 2 m) centred on the fitted line, with the horizontal extent of its projected corners solved for L (`final.py`).

Length L for each focal length:

| f (px) | L (m) |
|---|---|
| 2150 | 6.09 |
| 2185 | 6.00 |
| 2190 | 5.98 |
| 2245 | 5.82 |

- The record's frames f64–69 and f71 give the same values within 0.01 m.
- **Early frames (f8–40):** with W = 2 they give a shorter length, about 5.5–5.7 m. These extents come from template tracking, with the rear edge offset-calibrated and about 6 px too far right at f30. The model also assumes a sharp far-front corner, but the van's front corners are rounded. For both reasons I did not use them.
- **Sanity check:** the van is about 115 px tall at f66, which is about 2.1 m. That gives L/H ≈ 2.85, typical of a Chevy Express-type van (about 6.0 × 2.1 m).

**Answer: 5.98 m.** The uncertainty is about ±3%, mostly from the focal length.
