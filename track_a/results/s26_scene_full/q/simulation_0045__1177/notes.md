# Q1177 — distance between the left pillar of the near door and the right pillar of the far door

The file and the question both run at 33 fps, so t=1 → frame 33 and t=2 → frame 66.

## What I measured
- The right-hand facade has two residential doors:
  - **Near door:** the wooden arched door at x≈1650–1730. Its stoop has two stone newel pillars with urn tops. The left
    one has its body at x≈1320–1415 and its base at y≈598–603. The right one is at x≈1450–1545.
  - **Far door:** the door between white columns at x≈1255–1300. Its stoop has two turned newel posts standing on stone
    blocks, at x≈1085 and x≈1145. The right block's bottom is at y≈501 (found from the intensity profile in
    `a7_profiles.py`).
- **Reading used:** pillar = stoop newel pillar, with left and right as seen in the image. That makes the asked pair the
  stone pillar (≈1365, 598) and the far door's right newel post (≈1145, 497). These are the two pillars on either side of
  the planter between the stoops.
- **Other reading:** if "right pillar of the far door" means the white column next to the far door (x≈1318), the
  distance comes out at ≈4.2 m (f=1900). That number rests on a weaker facade estimate (`a5_geom.py`).

## The depth_info does not match the image
- Image-only depth ratios Z(66)/Z(33), from distances to the street vanishing point (585,200) and from apparent heights:
  - cyclist 1.453 (given distances: 1.394);
  - pedestrian 1.115 (given distances: 1.070).
- At t=1 the cyclist's wheel (y=563) and the pedestrian's feet (y=572) are at nearly the same image height. The cyclist
  rig is 285 px tall and the pedestrian 315 px, so the two are at about the same depth. The given values (12.1 m and
  17.2 m) would make the pedestrian a 2.6 m giant walking below road level.
- No pinhole camera, with the principal point free or fixed, reproduces all four given distances (`a3_fit.py`).
- The depth **differences** do agree with the prior: 4.78 m in 1 s ≈ 4.87 m/s × cos(street angle).
- **Scale used (Option A):** depth along the camera axis Z from the image ratio plus the given depth difference
  (`a4_scale.py`, `a6_newels.py`). This gives cyclist Z(33) ≈ 10.4 m, so its speed over frames 33–66 is 4.82–4.88 m/s,
  matching the prior. It gives pedestrian Z(33) ≈ 10.3 m and a walking speed of 1.27 m/s.
- **Focal length:** f ≈ 1850 px (range 1500–2300). The speed constraint gives f≈1200 for the pelvis point and f≈1800 for
  the wheel-contact point. Requiring a plausible pedestrian height (≈1.75 m) and cyclist rig height (≈1.6 m) gives
  f≈1800–1900.

## Geometry
- The sidewalk plane contains the street direction, so ground points satisfy Z·(v−200) = const. I fitted the constant
  from the pedestrian's lowest-foot rows over all frames; the median is Z·(v−200) ≈ 3840 px·m. This relation does not
  depend on cx or cy.
- Pillar bases (base centres on the sidewalk) at f=1900:
  - stone pillar ≈ (2.06, 1.09, 9.65) m;
  - far newel ≈ (1.24, 0.78, 12.89) m;
  - distance between them 3.35 m. Using pillar centres (raised by about 0.7–0.85 m) instead of bases gives 3.34 m.
- **Sensitivity:**
  - f = 1200 / 1600 / 2600 → 3.64 / 3.43 / 3.27 m;
  - base row ±5 px → ±0.11–0.2 m;
  - vanishing-point row ±5 px → ±0.04 m;
  - taking the plane constant from the cyclist instead of the pedestrian → 3.30 m.

## Second route
Using the cyclist's road plane (wheel contacts) instead of the pedestrian's sidewalk gives 3.30 m, against 3.35 m from the
pedestrian.

## Answer
**3.35 m.**

Confidence is moderate. The main risks are:
- which objects count as "pillars" (the white-column reading gives ≈4.2 m);
- the given depth_info is inconsistent with the image. If its absolute cyclist depths were used for scale, the answer
  would be about 15 % larger (≈3.9 m).
