# q_1069 – width between the two widest eaves of the house (simulation_0014)

File fps = question_fps = 24. 3D Blender render, static camera, 1920x1954.

## Eave span in pixels (frame 72, crop.py zooms)
The front gable's two eave tips are the left roof-board tip at x ≈ 310 (y ≈ 873) and the right barge-board tip at x ≈ 1042
(y ≈ 862), so the span is **≈ 732 px**. The roof edge that continues to x ≈ 1104 is the side eave going back in depth (it points
at the side vanishing point), so it does not add to the width.

## Scale – the gravity prior conflicts with the standard objects
- Gravity route (fit.py, fit2.py): I put the camera's horizon at v ≈ 1120 and got f·h from the given house and cart distances.
  The nest's start comes from depth_info, and its landing point from the ground plane (about 4.4 m away). Fitting a free-fall
  parabola to the nest's height (frames 30–48) and requiring g = 9.8 gives **f ≈ 1550 px** (1390–1650 depending on the frame
  window).
- That f makes everyday objects about 2.9x too big: barn door opening ~8 m tall, barrels ~3.4 m, cart wheel ~3.4 m across,
  nest ~1.1 m. The geometry is not the problem: the nest's depths, the landing depth and its pixel acceleration
  (~6 px/frame²) are all consistent. At a realistic scale the soft-body nest falls at only ~0.35–0.4 g, with a gradual
  release from the branch. So this is a physics or soft-body effect, and the prior gives no usable scale here.
- Following the method rules, the scale comes from standard objects instead. They agree on **f ≈ 4400 px** (HFOV about 25°):
  - cart wheel 192 px across at 27.4 m, 1.2 m wheel → f = 4384
  - door opening 224 px tall at the barn front, about 2.35 m
  - barrels 95 px tall, about 1.0 m
  - nest about 330 px at 5.5 m, about 0.42 m
  - fence about 0.95 m; camera height about 0.66 m

## Depth of the barn front
The given 55.77 m is to the house origin, but the barn is long. Its side-wall beam and side eave run to a vanishing point at
u ≈ 1240–1250 on the horizon (sidevp.py). From that point, the rear wall is about 1.40x as far away as the front and the rear
eave end about 1.46x. With the origin at the bounding-box centre, the front sits at about 1.2x less than the origin distance:
Z_front ≈ 55.77 / 1.215–1.23 ≈ **46 m**.

## Answer
732 px × 46 m / 4384 px ≈ **7.7 m**.

## Second-route check (needs no depth)
Ratios to objects in the same front plane:
- eave span = 3.27 × door-opening height → 7.7 m for a 2.35 m door
- eave span = 7.7 × barrel height → 7.7 m for a 1.0 m barrel

## Confidence
Moderate. The biggest risk is that the scene is really built about 2.9x large, with gravity working normally. In that case
the answer would be about 21–22 m (f ≈ 1550). If the house origin is at the front face rather than the centre, the answer
would be about 9.3 m.
