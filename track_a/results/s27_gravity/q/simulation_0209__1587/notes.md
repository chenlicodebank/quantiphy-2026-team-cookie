# Q1587 – length of the letter under the gun (simulation_0209)

The file and the question both run at 24 fps. The letter is the cream paper under the revolver's barrel. It is static,
and I measured it on frame 0, before the typewriter covers it.

## Camera (3D pinhole, principal point at the image centre, no roll)
- **Focal length f from the fall, g = 9.8 (`fit_cam.py`, `fit_cam2.py`, `fall_theta.py`):** for frames 2-9 I fit a
  projected free fall that starts at distance 4.32 m at t=0. The fall direction is world-down, with the camera
  pitched down by θ.
  - The bottom-edge track (y1) fits best (rms 0.2 px): f = 2770-2900. At θ = 13.5° it also reproduces the given
    4.501 m at t = 0.5 s (4.494-4.500).
  - The bbox-centre track gives f = 2550-2760. It is less reliable because the bbox height grows as more of the top
    of the typewriter shows.
  - f hardly depends on θ.
- **Pitch θ, three routes:**
  - Desk-top silhouette edges against the wall, fitted at sub-pixel level (`desk_vp.py`, `vp_orth.py`): the desk's
    long and short sides must be orthogonal, which gives θ = 13.5° at any f.
  - Free fall with the depth constraint: about 15.5°.
  - The paper must be a rectangle (right angle at its front corner): about 14.6°.
  - I used θ ≈ 14.3°.
- **Desk plane:** taken through the gun origin (given distance 4.704 m) minus 1.5 cm. Moving it by ±1.5 cm changes
  the answer by ±1.3%.
- **Cross-check:** the plane through the resting typewriter predicts a gun distance of 4.71 m, which matches the
  given 4.704 m.

## Paper corners (`paper_edges2.py`, `draw_paper.py`)
I fitted sub-pixel edge lines (strongest gradient along the edge normal, total-least-squares line) and took the
corners as line intersections, so the blur-rounded corners do not bias them:
- left corner L = (1315.7, 624.4)
- front corner B = (1363.2, 643.3)
- right corner R ≈ (1409, 634.5)

The far corner is hidden under the gun barrel. The far edge runs parallel to the front-right edge, as it should.

## Result (`paper_final.py`)
I back-projected the corners onto the desk plane:
- side L-B (the long side, so the length): 0.130-0.135 m for f = 2800-2820 and θ = 13.5-14.5°
- side B-R (the width): about 0.096 m

| f / θ | 13.5° | 14.5° | 15.5° |
|---|---|---|---|
| 2550 | 0.147 | 0.141 | 0.136 |
| 2820 | 0.135 | 0.130 | 0.125 |
| 2900 | 0.132 | 0.127 | 0.122 |

**Answer: 0.131 m.**

Confidence: moderate, about ±6%. The answer is most sensitive to f (0.6-2% per 100 px) and θ (about 4% per degree).
The scene seems to be built somewhat large: the desk top comes out about 2.2 × 0.93 m.
