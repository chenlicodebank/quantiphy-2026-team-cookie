# Q1726: height of the boat (prior: boat length = 10 m)

The file and the question both run at 24 fps, so no time-base conversion was needed.

## Measurements (`measure.py` → `meas.json`)
I measured soft-coverage masks with sub-pixel edges on every frame:
- **Boat vertical extent** (mast tip to keel bottom): 216.6 px at f0, 221.1 px at f24 and 229.7 px at f71. It grows by 1.060, which matches the depth ratio from depth_info (1.062).
- **Boat horizontal extent**: 177.2 px at f0, 183.2 px at f24 and 198.6 px at f71. It grows by 1.120, so about 5.6% more than depth alone explains.
- **Person**: about 41 px tall throughout.

## Geometry (`fit.py`, `fit2.py`)
- The boat's depth falls by 2.70 m/s (from depth_info) while it moves left across the image at about 74 px/s. So it is heading toward the camera at an angle α to the image plane, and tanα ∝ f.
- The width grows faster than depth alone predicts. This is the perspective of a hull that is angled along its motion, so the boat is not side-on: a side-on boat would grow by exactly the depth ratio.
- **Model**: I back-projected the boat centre with the given depths, set the heading equal to the 3D motion direction, and used a hull of length 10 m with a pointed bow and an effective stern half-width B/2. I fitted f and B jointly to the per-frame horizontal extents over all 72 frames.
- **Result**: f = 3022 ± 42 px and B_eff = 1.6 m, with 0.53 px rms residual. The heading is about 40° from the image plane.

## Answer
Height = vertical pixel extent × Zc / f, which gives **9.78 m at t = 1 s** and 9.76 m averaged over all frames.

## Checks
- **Person**: 41.2 px at their given 139.1 m gives 1.90 m with f = 3022, which is a plausible adult. The alternatives fail this check:
  - a side-on boat (f ≈ 2440) gives H ≈ 12.1 m but a person of 2.35 m;
  - a 3.5 m effective beam (f ≈ 2740) gives H = 10.8 m but a person of 2.10 m.
- **Limits of the check**: the person's origin depth is static while the body walks, so it is only a loose check. Read directly, a 1.75 m person would give f ≈ 3270 and H ≈ 9.0 m.
- **Consistency**: the vertical size growth matches the depth ratio, so the depths are applied to the right object.

## Confidence
Moderate. The result depends on the effective beam and heading, which the growth shape constrains only weakly, so the likely range is about 9.0–10.8 m.
