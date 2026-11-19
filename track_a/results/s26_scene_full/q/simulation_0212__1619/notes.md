# q1619 — length of the dog (including tail), metres

File fps = question_fps = 24 (no conversion issue). 3D Blender scene, static camera, principal point assumed (960,540).

## Focal length (focal.py)
Prior: black cat speed 0.94 m/s; cat distance 4.199 m (f0) and 4.481 m (f24).
Back-projecting the cat's core centroid at f0 and f24 (or f23) with those distances and requiring a 3D
displacement of 0.94 m/s x 1 s gives f = 2147–2156 px (bbox centre: 2099–2127). Adopted f = 2150 px (HFOV ≈ 48°).
Check: extrapolating the cat's straight line to f48 lands within ~19 px of its observed position.

## Floor / pitch
With f = 2150: mirror bottom centre (1515,812) at 6.407 m → floor 0.779 m below camera; closest bench leg
(centre (1410,765) at 5.69 m, bottom at v=838) → 0.768 m; cat paws at f0 → 0.785 m. Pitch ≈ 0, floor Y = 0.775 m.
Dog origin height (from given depths at f0 and f12): Y = 0.443 / 0.447 → constant, consistent with zero pitch.

## Dog orientation and length (length.py, length2.py)
The dog turns during the clip; it is oblique to the image plane, so pixel length alone is foreshortened.
Body axis from the near-side front and hind paw floor contacts (read on 3x crops), back-projected to the floor:
f49: front (830,959), hind (1083,932) → axis 29.5° toward the camera; f46: 27.3°; f0: 29.9°.
Mid-sagittal vertical plane = paw line shifted 0.06–0.10 m away from the camera (far-side paws are ~0.21 m across).
Front-most point (head patch tip, (616,806)) and rear-most point (tail tip, (1197,664); at f49 the tail points
straight back — in other frames it wags upward and does not extend past the rump) intersected with that plane:
- length including tail (f49): 1.270–1.291 m over f = 2100–2200, half-width 0.06–0.10 → **1.28 m**
- body only, head tip to rump: 1.007 m (f49), 0.97–0.985 m (f46)

## Second-route check (check_f0.py)
At f0 the same paw/floor method (paws (1420,895), (1605,875)) places the dog's centre at 5.084 m from the camera
vs the given 5.094 m (f = 2100 → 4.98, 2200 → 5.19), so f = 2150 and the floor-plane geometry are confirmed
independently of the cat prior.

## Uncertainty
Paw-contact rows ±3 px change the axis angle by ~±5° → L ±5%. The reading of "including tail" assumes the tail
extended back (f49 pose); if the tail is raised, the extent is ~1.0 m. Dog length is measured along the body axis
(not along arbitrary world axes). Confidence: moderate; estimated error ~5–8%.
