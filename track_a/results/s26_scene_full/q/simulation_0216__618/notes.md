# q_618 — length of the floor mirror (m)

Prior: black cat speed = 0.94 m/s. No depth_info. fps 24 = question_fps (no re-timing issue).

## Measurements (profiles.py, paws.py, compute.py)
- Cat pixel speed: matched upper-body track from scene/tracks/cat.csv, mean 17.73 px/frame (torso centroid
  net 17.61) -> 425.6 px/s -> 0.002208 m/px at the cat's depth. The walk is steady, so mean speed = prior speed.
- Mirror (frame 24, intensity profiles): top edge y = 389, bottom of frame on the floor y = 967 -> 578 px tall;
  ~240-248 px wide. Wall/floor junction just behind it: y = 963 (mirror leans, bottom ~4 px in front of the wall).
- Cat paw contact line: lowest white-paw pixel y = 1021 in every sampled frame (0..48). I used a mid-plane ground
  line of y ≈ 1019.5.

## Perspective (the cat is clearly in front of the mirror)
The TV's vertical edges are vertical to within 1 px (x = 813.5–814.5 from y = 540 to 740), so the camera is level
and the horizon is at the image centre, y = 540. On a flat floor, m/px at a ground contact row y = H_cam/(y − 540).
- From the cat: H_cam = 0.002208 × 479.5 = 1.059 m.
- At the mirror bottom: 1.059/427 = 0.002481 m/px. At the wall (top of the mirror): 1.059/423 = 0.002504 m/px.
- Mirror vertical extent = the part below the horizon (427 px × s_bottom = 1.059 m) plus the part above it
  (151 px × ~0.00249) = **1.435 m**.
- Sanity checks with the same model: TV stand 0.46 m, bench 0.50 m, mirror width ≈ 0.6 m, cat body ≈ 0.54 m.
  All are plausible.
- Second route, a single 2D scale with no perspective: 578 × 0.002208 = 1.276 m. This underestimates because
  the mirror stands ~12% farther away than the cat (ground-row ratio 479.5/427). The perspective result is preferred.

## Interpretation and confidence
"Length" is taken as the mirror's long, vertical dimension (the AABB height). If the asked quantity were the
horizontal extent, it would be ≈ 0.6 m. Uncertainty is about ±3% (paw-line and horizon assumptions), plus the
ambiguity in what "length" means.
