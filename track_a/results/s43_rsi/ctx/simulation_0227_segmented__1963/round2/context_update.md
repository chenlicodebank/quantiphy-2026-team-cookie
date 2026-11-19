# Round 2 addendum, q1963

## Established
- **Round 1's switch to 0.31 is verified** with independent code (`track2.py`, `fit2.py`):
  - Tracking: my own ring-row mask (centroid and row edges) plus subpixel template matching.
  - Smoothstep fits: rms 0.33–0.70 px, keys at about frames 0 and 49, D about 428 px.
  - The convention a(24) = x24 − 2·x23 + x22 on the fitted model gives 0.294–0.333 m/s². With the keys fixed at
    frames 0 and 49 it gives 0.299.
- Scale: 0.007937 m/px from the cat. The bbox edges reproduce the prior within 0.5 %.
- C1's 0.15 is reproduced as the off-stencil analytic d²x/dt² at frame 24 (0.10–0.13).
- A zoomed frame confirms that the item between the chairs is a static dark basket or bucket, not a chess piece.

## Ruled out
- 0.15: the wrong time stencil.
- 2.5: the ramp-phase magnitude, not the value at t = 1 s.

## Open
- The identity of the "red general chess". It is not visible, and every session assumes the float.
- Whether the cat and the float are at equal depth. The 2D single-scale convention assumes they are.

## Answer
0.31 m/s² (switch, follows C3, confidence medium).
