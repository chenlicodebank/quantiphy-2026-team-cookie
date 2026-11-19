# Q647 – long side of a marked parking space (simulation_0220)

Prior: robot speed 0.82 m/s. No depth_info. fps = question_fps = 24.

## What the "parking space" is
The floor in front of the wall has two horizontal white stripes (y≈843 far, y≈908 near) and two wide
diagonal white lines (x≈550-650 and x≈1600-1820). The diagonals are floor lines that run away from the camera
(X = const). They meet at a vanishing point near (958, 552), close to the image centre, so the camera is level.
The marked space is the area between the two diagonals: horizontal (X) side × depth (Z) side between the stripes.

## Measurement (measure.py)
- Edges of the diagonal lines fitted on frame 49, rows 850-899 (sub-pixel threshold edges, line fit; the paint
  is a bit wavy, rms 1-2 px). Centre-line slopes dx/dy: L −1.157, R +2.328 → Δslope = 3.484
  (inner edges 3.288, outer edges 3.680). Vanishing point / horizon y_h ≈ 552 (from the outer edges 550, from the inner edges 554).
- Robot speed: the belly-disk ref_x slope is −8.52 px/frame and the mask-centroid slope is −8.50 px/frame, so 204.5 px/s.
  At the robot's depth that gives 0.82/204.5 = 0.00401 m/px.
- Robot ground row: the planted near-foot sole edge is at y≈968 and the far foot at y≈954. The point under the origin is at
  y_r ≈ 958 ± 4.
- Ground-plane geometry for a level camera: at row y the scale is h/(y−y_h) m/px, so camera height
  h = 0.00401 × (958−552) = 1.63 m. The lateral line spacing is W = Δslope × h = 3.484 × 1.63 = **5.67 m**
  (centre to centre).

## Second route
Pixel spacing of the line centres at a single row, scaled row by row: 1014 px at y=843 and 1237 px at y=907.
- With y_h = 552: both rows give 5.67 m.
- With y_h = 540 (exact image centre): 5.61 m and 5.65 m.

## Which side is long
The depth side between the stripes needs the focal length f: ΔZ = f·h·(1/291 − 1/355.5) ≈ 0.00102·f m.
- For a Blender-default 50 mm lens (f ≈ 2667 px, which also fits the absence of visible pillar side faces), ΔZ ≈ 2.7 m.
- So the space is about 5.7 × 2.7 m, a realistic stall, and the horizontal side is the long one.
- The depth side would only be longer if f > 5500 px (hFOV < 20°).

## Uncertainty
- Line edge definition: inner edges give 5.35 m, outer edges 5.99 m. I answer centre to centre.
- y_r ±4 px → ±1%.
- Speed ±2%: the per-frame mean including the vertical bob is 8.81 px/frame, which would give 5.49 m.

The answer is 5.67 m, with a likely error of about ±6%.
