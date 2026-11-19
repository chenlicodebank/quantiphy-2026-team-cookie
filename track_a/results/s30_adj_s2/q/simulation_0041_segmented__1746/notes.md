# q1746 — width of the boat (m); prior: person height 1.75 m; no depth_info

The file rate and question_fps are both 24 fps. This is a size question, so timing does not matter.

## Where the answers part ways
- C1 (2.78) and C2 (2.63) agree on almost everything. The camera is oblique from above with pitch ≈ 62–64.5°. In deck-plane units the rectified beam is 110 px (C1) or 110.6 px (C2). The perspective factor between the person and the boat is +3 % (C1) or +4.6 % (C2).
  - They differ only in the person's local elevation angle θ_p, which sets the scale (px/m) through the person-height model:
    - C1: θ_p = 61°, s_p = 38.6 px/m.
    - C2: θ_p = 62°, s_p = 40.3 px/m.
  - C1's scale transfer, s_b = s_p·sinθ_b/sinθ_p, is valid for a ground plane (d = h/sinθ_ray). It is equivalent to C2's depth ratio.
- C3 (4.4) used a flat 2D scale of 1.75 m / 47 px, the median bbox height, which ignores the steep pitch: the person's image height is about 1.75·cos 62° plus the foot and head depth. C3 then applied a foreshortening guess in the wrong direction. That gives a boat 13 m long with a 4.4 m beam. I reject it.

## My check
- Person bbox (scene/tracks/person.csv): height 39–51 px, median 46.5, minimum about 39.5. Width 19 px.
- Person model: extent = s·(1.65cosθ + 0.1 + 0.12sinθ).
  - θ = 58° gives s = 36.7 px/m.
  - θ = 60° gives s = 38.4 px/m.
  - θ = 62° gives s = 40.3 px/m.
  - A toe-forward / back-of-head variant at 62° gives about 40.7 px/m.
- Independent check from the width: 19 px / 0.47–0.5 m (shoulders plus arms) = 38–40 px/m. A pitch of 45° would need s ≈ 29 px/m, which would make the person 0.65 m wide, so it is rejected. The steep-pitch scale is confirmed.
- The boat's scale change (0.66 % over 76 px of rows) gives f ≈ 6000 px. The person sits 535 rows higher, so the boat is about 3–5 % closer than the person, consistent with both candidates.
- Beam: 110–110.6 px. Using s_boat ≈ (38.6–40.3)·(1.03–1.046) ≈ 39.8–42.2 px/m gives B = 2.62–2.78 m.
- Plausibility: length ≈ 8–9 m, so L/B ≈ 3.2, which is a normal small fishing boat.

## Answer
The two careful routes bracket the value. I take the middle of the physically consistent θ_p range (61–62°), with a slight allowance for rub rails or fittings in the world AABB: **2.70 m**.

My answer is not an average of votes: C3 is excluded, and the remaining spread comes from one parameter whose plausible range I evaluated directly.

Confidence: moderate, about ±6 %.
