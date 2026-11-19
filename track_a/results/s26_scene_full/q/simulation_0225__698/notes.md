# q_698: width of the beach chair (m)

Prior: the black cat's speed is 1.041 m/s. depth_info: none. fps = question_fps = 24, so no re-timing.

## Scene
A static camera looks almost head-on at a terrace. Three front sun loungers and three back-row loungers are seen from their foot ends, so their horizontal image extent is their **width** (the shorter horizontal extent). The cat walks in +x along the deck in front of the loungers, and its paws stay at y ≈ 920.

## Measurements (in code)
- **Cat speed** (scene/tracks/cat.csv, checked): the mask centroid moves 569.8 → 838.8 px over 49 frames, and the bbox rear edge moves 517 → 786 px. Both give 5.49 px/frame (131.8 px/s), with no vertical drift.
  - Scale at the cat's depth: 1.041 / 131.8 = 0.00790 m/px.
- **Lounger width** (`prof.py`, the strongest horizontal gradients at y 840–895, frame 0): front-leg outer edges at 764–946 (lounger 1), 1008–1188 (lounger 2) and 1250–1431 (lounger 3).
  - Width ≈ 181.5 px.
  - Leg bottoms (ground contact) at y ≈ 900.5 (`legs.py`).
- **Perspective**: the receding deck tile joints (`vp.py`, Hough lines + least squares) meet at a vanishing point (946, 550). So the horizon is at y ≈ 550, the camera pitch is about 0, and the facade verticals are vertical.
  - On the ground plane, metres per pixel scale with 1/(y_ground − y_horizon).
  - So the lounger front (ground y 900.5) is slightly farther away than the cat's line (ground y 920).
  - Factor = (920 − 550) / (900.5 − 550) = 1.056.

## Result
Width = 181.5 px × 0.00790 m/px × 1.056 = **1.51 m**.

The flat 2D scale (no perspective correction) would give 1.43 m. I chose the corrected value because the vanishing point clearly shows that the lounger stands about 5% deeper than the cat's walking line.

## Checks
- **Second route for the cat's pixel speed:** the bbox rear edge and the centroid agree on 269 px net travel.
- **Lounger width:** all three front loungers measure 180–182 px.
- **Sanity check:** at this scale the cat's body is about 0.83 m long. So the render is roughly 1.8–2× real scale, which matches a lounger of about 1.5 m (a real one is about 0.7 m).

Confidence: moderate-high. The main uncertainties are the cat-origin depth and the horizon estimate (±2%) and the per-frame speed convention (±2%).
