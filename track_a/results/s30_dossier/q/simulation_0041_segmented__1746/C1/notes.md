# q_1746 — width of the boat (prior: person height 1.75 m), answer 2.78 m

Time base: fps 24 = question_fps; no re-timing issue.

## Geometry (the view is oblique from above, so a flat 2D px-scale does not apply to a beam)
- Camera elevation at the boat from two deck rectangles (foredeck hatch, cockpit cover), robust line fits of their dark
  edges (`edges2.py`): edge slopes 0.305/0.32 (along hull) and -2.63/-2.59 (across). Orthogonality gives
  sin^2(theta) = -m1*m2 → theta_b = 63.6° and 65.6° → **64.5°**. The along-hull slope 0.31 also matches the bow→stern deck
  line. The motion direction (slope 0.28) is ~2° off the hull axis, so I did not use it as the heading.
  Rectifying at 64.5° (`rectify2.py`, frames/rect_64.png) makes both rectangles square-cornered. At 50° they are not.
- Perspective is weak: the boat's bbox shrinks by only ~0.6% while it moves 400 px left and 110 px up (`scalechg.py`),
  which implies f ≳ 5000 px.
- Person (`person.py`): bbox height 39–51 px with a 17-frame step period, width 19–20 px, ground pixel speed 36.8 px/s.
  Body model: projected extent ≈ 1.64·cosθ + 0.11 + 0.15·sinθ (× 1.75 m scale), plus ≈0.37·sinθ in mid-stride.
  - The max/min height ratio 1.27 fits θ_p ≈ 60°.
  - The speed is ≈1.1 m/s and the step length ≈0.75 m.
  - The width is ≈0.5 m.
  - With f ≈ 7000 px, the 550 px row offset gives θ_p ≈ 60–61° at the person, versus 64.5° at the boat.
  - Result: s_person ≈ 38.6 px/m (θ_p = 61°). Scale at the boat: s_b = s_p·sinθ_b/sinθ_p ≈ 39.8 px/m (image-x px per metre).

## Beam measurement (`deckedges.py`, `beam.py`)
- The image is rectified to the deck plane, with a = along hull from the bow tip and b = across (units: image-x px).
- Port gunwale edge: the white/red boundary.
- Starboard gunwale: the silhouette, used only where there are no rails or cabin (a = 20–95 and 180–225).
- Centreline: the midpoint of these. It drifts −8 → −12 because of sheer, and is interpolated in between.
- At a = 185–195 the directly measured width (104–105) matches the symmetric model.
- Maximum beam (a ≈ 140–160), from 2 × the port half-width: **109.6 / 109.9 / 108.7 / 108.8** at frames 0 / 15 / 30 / 45
  (θ = 64.5°). The range is 108–113 for θ_b from 63° to 66°.
- W = 110 / 39.8 ≈ 2.76 m. With the alternative person models (min-height vs max-stride, θ_p = 60–61°), W = 2.76–2.83 m.
  **Answer 2.78 m.**

## Checks
- The same width holds within ±1% across four frames spread over the motion.
- Implied length ≈ 360 units ≈ 9.0 m, so L/B ≈ 3.3, which is plausible for a fishing boat.

## Confidence
Moderate, about ±8%. The main uncertainty is the person's elevation angle θ_p (57–64.5° gives W = 2.9–2.6 m).
A second assumption is that "width" means the beam: if the boat is yawed relative to the world axes, the world AABB could be wider.
