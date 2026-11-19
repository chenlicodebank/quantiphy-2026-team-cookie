# q1746 — width of the boat (m); prior: person height 1.75 m; no depth_info

The view is not a flat 2D view. The camera looks steeply down at the ground/water plane: we see the boat's deck and the top and front of the person.
The frame rate is 24 fps (the file and the question agree). Timing does not matter for a size question.

## Camera / scale
- Perspective is weak. Template matching over scale (scale_fine.py) shows the boat shrinks about 0.66 % as it moves 76 px up the image.
  On a ground plane, inverse depth is affine in v, so the scale at the boat (v≈990) is about 1.046 × the scale at the person's feet (v≈455).
- Pitch θ: the estimate is θ≈62° below horizontal, from three routes that agree:
  (a) Cabin-roof edges along the axis (≈15.9°) and across the beam (≈−68…−72°). For an orthographic view, tanα·tanβ = −sin²θ, so θ≈57–68°, centre ≈62°.
  (b) The person's bbox width is 19 px (≈0.47 m shoulders/arms), so s≈40 px/m. The minimum (mid-stance) bbox extent is 39.5 px
      = s(1.65 cosθ + 0.10 + 0.12 sinθ) (head-sphere top to toe), which gives θ≈62° and s_person≈40.3 px/m.
  (c) Planted-foot positions step by 25.4 px every ≈17 frames. At θ=62° and s=40.3 that is a step length of 0.71 m ≈ 0.41·H, a natural value.
- Boat axis angle in the image: α = 15.66° from the boat's motion direction (−396,−111 px), confirmed by the roof/cabin edges (14.6–16.3°).
  The ground yaw is φ = atan(tanα/sinθ) ≈ 17.6°.

## Beam measurement (deck_edges.py, beam2.py)
- Far sheer is the top of the silhouette: the bow region x 362–448, and just aft of the cabin x 526–574, leaving out the cabin and a crane.
  Near sheer is the white→red hull-side boundary, median-filtered.
- Both edges are mapped from the image to the boat frame (orthographic inverse with θ, φ). Width = max lateral (far) − min lateral (near).
  - Frame 0: W = 111.8 px·(s·m). Frame 30, a second route: W = 109.4. Mean is 110.6.
  - The far edge is flat at about −857.5 on both sides of the hidden cabin span, so the parallel mid-body is well constrained. The near minimum is at the cabin station.
- B = W / (s_person × 1.046):
  - Height-based scale at θ=62°: 2.65 (f0) / 2.60 (f30).
  - Width-based scale (s=40): 2.67 / 2.62.
- Sensitivity: with the width-based scale, B varies from 2.59 to 2.77 for θ = 58…66°. With the height-based scale, B varies by ±0.2 m for ±2°.

## Answer
Boat width (beam, the shorter horizontal extent) ≈ **2.63 m**. Length check: about 8 m, so L/B ≈ 3, which is plausible for a fishing boat.
Confidence: moderate (about ±8 %). The main uncertainties are the pitch angle, the person-shape model, and whether the sheer lines are the outermost hull points (a rub rail could add a few cm).
