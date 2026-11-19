# q_2268 - height of the toy (cm), prior g = 9.8 m/s^2, no depth_info

The file and the question are both 24 fps. The camera is static. The toy is a plush thrown straight up twice. The scale
comes from gravity: free-flight vertical acceleration in px/s^2 -> m/px = 9.8 / a_px (f cancels).

## Acceleration (px/s^2), parabola fits over free-flight frames
- measure.py: my own background-difference masks (masks.json), fit.py:
  - mask centroid: toss1 2570-2625, toss2 2531 (biased: toss1 turns sideways (yaw) and the tail swings out, limbs flop)
  - mask top edge (head): toss1 3030-3065, toss2 52-59 2928 (second differences very steady, ~5.1 px/frame^2)
  - mask bottom edge (dangling legs): 2325-3045 (noisy)
- headtrack.py: sub-pixel template tracking of the head and the body:
  - head: toss1 16-22 2747, toss2 51-59 3001 (residual < 0.6 px); central second differences ~4.9 px/f^2 (~2820)
  - body: toss1 2846-2990, toss2 2593-2688
- Rigid / head features cluster at 2750-3050, and the mask centroid at ~2550 is skewed by shape changes. Adopted
  a = 2900 px/s^2 (about ±5%) -> 3.38 mm/px.
- Sanity check: the person is 507 px tall -> 1.71 m at this scale, and the toy is slightly in front of her (so she
  is a little taller in reality). That is plausible and favours the upper range over ~2550 (which would make her 1.9 m+).

## Toy pixel height
At the toss-2 apex (frames 54-56) the toy hangs upright and frontal with near-zero velocity (no blur). The mask
from the top of the ears to the feet is 106 / 107 / 104 px, so I use 106 px.

## Answer
106 px x 9.8 / 2900 = 0.358 m -> **35.8 cm**. Range: 34.6 cm (a = 3000) to 37.8 cm (a = 2750). Confidence: moderate
(about ±7%). The main uncertainty is the acceleration estimate.
