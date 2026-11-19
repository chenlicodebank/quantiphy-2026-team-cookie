# q_1730: height of the person (m)

Prior: person speed = 1.3 m/s. depth_info: the origin is at 122.857 m at t=1 s and 122.859 m at t=2 s. That is effectively constant, so the character origin stays put and the distance is of no use for the moving body. The file and the question are both 24 fps.

## Method
- The person walks to the right in side view (checked on enlarged crops `frames/strip.png` and `frames/cmp.png`). The camera is static.
- Image speed (`scale.py`): a linear fit of the smoothed pelvis x gives 41.5 px/s. The mask centroid gives 41.3 px/s and the head-top x gives 40.6 px/s. The first and second halves are equal to within 2 %, and the vertical drift is negligible.
- Scale: the motion is taken as across the view, so 1.3 / 41.53 = 0.0313 m/px.
- Pixel height (`measure.py`, own masks at deficit thresholds of 10, 20 and 40, plus the record's bbox):
  - Over the whole clip it is about 61–64 px.
  - It is about 63–65 px early and about 59–62 px late.
- Result: the walking height is about 61.5–63.5 px × 0.0313 = 1.92–1.99 m. Rest standing height is a little above the walking bbox.

## Caveats and checks
- The apparent size shrinks about 7 % in height (15 % in area) over the clip, while the image speed rises slightly (+2–3 %).
  - A real recession in depth would make the image speed fall roughly as 1/Z² (about 16 %).
  - So the shrink cannot be perspective at constant speed, and I treated the depth motion as small.
  - The feet drift down 3–4 px, which, if anything, means a slight approach.
- The lateral-only assumption gives an upper bound on H. Any depth component of the 1.3 m/s would lower it.
- Scale-free check: the step period is about 16.7 frames, so a step is about 28.7 px, about 0.47 of the body height. That is a long but plausible stride.
- Implied focal length is about 123 / 0.0313 ≈ 3900 px (horizontal field of view about 16°), which is plausible.
- Answer: 1.92 m. This sits slightly below the lateral-only mid estimate (about 1.95–1.97) to allow for some depth motion and for the guidance that adults are not over 2.0 m.
- Confidence: moderate, about ±5 %.
