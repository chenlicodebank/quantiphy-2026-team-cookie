# Q1301: height of the traffic light (simulation_0063)

The file's frame rate (24 fps) matches question_fps (24). Frames: 0.58 s → f14 and 1.58 s → f38.

**Answer: 4.96 m.** This is the near-left traffic light (pole x≈377, two 3-lamp heads, a pedestrian signal, and a
sign on top). It is the prominent one. The bbox height runs from the pole base to the top of the sign.

## Geometry (static, almost level camera; principal point taken as the image centre)
- **Horizon.** Two ground-plane vanishing points, from code-fitted edge lines (`edges.py`, `edges2.py`):
  - VP1 = (-103, 527.7), where the near-curb and right-sidewalk front-edge lines meet.
  - VP2 = (5077, 525.8), where the far-sidewalk edge and the right-sidewalk back edge meet.
  - The horizon is v_h ≈ 527.5 near x≈400. Identical lamp posts A, C and D (top/base fit) give 528.
- **Focal length.** The two streets are taken as perpendicular: f² = −(u1−cx)(u2−cx) − (v1−cy)(v2−cy) → **f ≈ 2175 px**
  (horizontal FOV ≈ 53°).
- **Ground mapping (unit = camera height H).** A ground pixel (u, v) maps to X = (u−cx)/(v−v_h), Z = f/(v−v_h).

## Metric scale: camera height
1. **Prior: the white van's acceleration is 4 m/s².** (`vanwheel3.py`, `vanwin.py`, `vanwinfit.py`)
   - The van's near-side rear-wheel contacts (f28-38) lie on a line through VP2 (residual 0.14 px), so the van drives
     parallel to that street.
   - I tracked the van's brown side window (left edge, right edge and middle) from f26 to f71, mapped it onto the
     near-side line, and fitted a quadratic: a = 1.827 H/s², so **H_road = 2.19 m**. The fit residual is 0.4 px. It
     implies the van started from rest at t ≈ −0.04 s, which is consistent with uniform acceleration.
   - Sensitivity: about ±1% for f ±100 px, ±1.5% for v_h ±1.5 px, and ±0.4% for the side-plane offset.
   - The record's `rear_x` is unreliable for this. It tracks the near-rear corner early (it agrees with the wheel in
     f30-38) but the far-rear corner late, because the rear face becomes visible (~50 px wide at f71). Using it biased
     H up to 2.32. The record's van bottoms are also about 7 px too high.
2. **depth_info, white van** (`vanD2.py`).
   - Van length from the f71 corners is 2.69 H; width is assumed 0.8–1.0 H.
   - The van's centre at f14 and f38 reproduces both given distances with H_road = 2.164–2.186. The ratio
     D38/D14 matches to 0.4%.
3. **depth_info, man** (pelvis above the feet). I re-measured the feet myself:
   - f14: mid-stride, ground under the pelvis at v ≈ 815.5 (feet at 811.5 and 824).
   - f38: feet together at v ≈ 844.
   - Result: camera height above the **sidewalk** H_s = 2.124 (f14) and 2.163 (f38).
- **Curb height.** The right sidewalk's curb face is 6–8 px tall at Z ≈ 20–27 m, which gives ≈ 0.07 m. So:
  - Routes 1–2 give H_s = H_road − 0.07 ≈ 2.10–2.12.
  - Route 3 gives 2.12–2.16.
  - **Adopted H_s = 2.125 m.** The man is then ≈ 1.83 m tall (camera height / man height ≈ 1.16 from the record), which
    is a reasonable sanity check.

## Traffic-light pixels (f70/71, code profiles: `tl_measure.py`, `polewidth.py`, `planterprof.py`)
- **Top.** The sign apex is at v_t ≈ 230.5. It is faint from 228 and clear from 232.
- **Base.** The visible pole ends at v = 746–747, with a widening base flange at 741–746.
  - Just below, at 747, the far brick wall of the planter begins (~0.13 m tall). Ground directly behind that wall
    would project at v ≈ 760, and the visible sidewalk strip behind it is at 739–746.
  - So the true base is hidden in the band v ∈ [747, ~760]. The man's arm occludes the pole at f0, which confirms the
    pole is behind him.
  - The flange suggests the contact is just below the visible end: **adopted v_b ≈ 750 (range 747–755).**
- **Height** = H_s · (v_b − v_t)/(v_b − v_h) = 2.125 · 519.5/222.5 = **4.96 m**.
  - v_b = 747 gives 5.00; v_b = 755 gives 4.90.
  - The pitch is 0.33°, so its correction is under 0.1%.

## Cross-check
The right traffic light (sign top 299, base 694, base fully visible) gives 2.125·395/166.5 = 5.04 m. Traffic signals
in the scene are about 5 m tall, which is consistent.

## Confidence
Moderate to good, about ±4%. The main uncertainties are the hidden base (±1.5%), the camera height (±1.5%) and the curb
height (±1%).
