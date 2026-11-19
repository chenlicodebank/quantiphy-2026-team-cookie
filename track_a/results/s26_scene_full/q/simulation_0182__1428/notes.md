# Q1428: height of the box (m), simulation_0182

The file fps and question_fps are both 24. The camera is static and level: the box's vertical edges are vertical, and the horizon is at v≈540 (the right-face edges converge at v≈543). I assume the principal point is the image centre (960, 540).

## Box pixel geometry at frame 0 (upright, corner-on, above eye level; crop.py, edges0.py)
- Vertical edges, rim to rim:
  - left edge, x=378: y 249 → 431, **182 px**
  - near edge, x=608: y 237 → 426, **189 px**
  - right edge, x=776: y 284 → 444, **160 px**
- The strip below 426–446 is the visible bottom face, not extra height.
- The loose top flaps stick up above the rim. The left flap tip is at (493, 222), which is ~19–20 px above the rim at that column (rim height there 185 px), so about **+10–11 %**. The right flap tip is only ~+5 %.

## Focal length (three routes)
1. **Box right angle / vanishing points.** The right-face edges meet at u≈1700 and the left-face edges at u≈−5600, both near v=540. That gives f² = −(uL−cx)(uR−cx), so **f ≈ 2200**. The same value comes from Z∝1/h, X∝(u−cx)/h with the right-angle constraint at the near corner: **f ≈ 2208** (sensitive, ±8 %).
2. **Free fall, frames 0–7** (fall.py, fall2.py, template strips). The pixel acceleration is ~2390 px/s² at the left edge, ~2440 at the near edge and ~2090 at the right edge. The profile is linear in u and reaches zero at u≈1670, which matches the right vanishing point. With g = 9.81 and the centre depth 9.522 m, **f ≈ 2140**.
3. **Prior check, ramp slide.** I back-projected the centroid track with depth anchored at 9.384 m at frame 12 and depth changing with apparent size (slide_check.py). At f = 2130–2200, the acceleration over frames 14–24 (around t = 0.75 s) is 2.2–2.6 m/s², which is consistent with the prior of 2.338. Note that the slide acceleration grows later (~3 m/s² over frames 24–35), so this route is loose. Ramp slope ≈ 31°.

Adopted f ≈ 2170 ± 60.

## Height
- **Geometry + depth route.** Using f, the edge heights and depth_info D(0) = 9.522 m to the centre, which is the midpoint of the left and right corners: H_rim = 9.522 / sqrt(5.94 + (f·0.005872)²) = **0.734–0.747 m**.
- **Free-fall route** (independent of f and depth): H = g·h/a = 0.761 (near edge), 0.747 (left), 0.751 (right).
- **Rim height ≈ 0.745 m** (range 0.73–0.76).
- **World AABB height including the raised flaps:** ≈ 0.745 × 1.10–1.11 ≈ **0.82–0.83 m**.

## Ambiguity and answer
The benchmark defines size as the world AABB, and the flaps are part of the rigid box mesh, so they count. However, how far the flap tip sits behind the face is uncertain, and the reference might be the box body alone (0.745). I answer **0.81 m**: about 2–3 % from the flaps-included value and about 9 % from the rim-only value.

Confidence: moderate. The rim height is good to about ±3 %; the main risk is the flap convention.
