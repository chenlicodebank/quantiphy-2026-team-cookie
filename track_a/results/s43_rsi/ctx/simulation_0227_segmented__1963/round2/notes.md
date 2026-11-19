# q1963 (round 2): acceleration of the "red general chess" at t = 1 s; prior: cat speed 1.041 m/s; no depth_info

File fps = question_fps = 24, so t = 1 s is frame 24. The clip has 50 frames.

## Object
- Zoomed frames (frames/f24.png, frames/round.png) show a white background, six lounge chairs, a walking black cat, a
  pink-red flamingo float, and a static dark basket or bucket between the front chairs.
- No chess piece is visible.
- Like every candidate and round 1, I take the asked object to be the float: it is the only red object and the only
  one that accelerates. This identity cannot be verified and stays open.

## Crux
Every candidate uses the float. They part on the time stencil at t = 1 s: frame 24 is about 0.5 frame from the ease
curve's inflection.

## Verification of round 1's switch (own code)
- `track2.py` tracks the float two independent ways:
  - My own mask of the ring rows (y ≥ 930, largest connected component; overlay frames/ov24.png). It gives the
    centroid cx and the mean left and right row edges xl and xr.
  - Subpixel template matching (TM_CCOEFF_NORMED) of the frame-24 float patch in every frame, giving tx.
- `fit2.py` fits a smoothstep (Blender two-key Bezier) with free key frames to each reference point. Model
  a(24) = (x24 − 2·x23 + x22) evaluated on each fitted curve:

| point | keys (frames) | D (px) | rms (px) | a(24) (m/s²) |
|---|---|---|---|---|
| cx | 0.17 / 49.00 | 428.0 | 0.33 | 0.320 |
| xl | 0.32 / 48.93 | 429.2 | 0.59 | 0.333 |
| xr | 0.27 / 48.91 | 428.7 | 0.70 | 0.326 |
| tx (template) | −0.08 / 49.06 | 428.3 | 0.68 | 0.294 |

- With the keys fixed at frames 0 and 49 and D = 428 px, the analytic value is
  428 × (6 − 12·23/49) / 49² × 576 × 0.007937 = 0.299 m/s².
- Local cubic fits centred on frame 23 (windows ±5 to ±12), with the same stencil:
  - centroid: 0.33–0.41 m/s²;
  - edges and template: 0.24–0.59 m/s² (noisier).
- The analytic d²x/dt² at frame 24 (C1's route) is 0.10–0.13 m/s². This reproduces C1's 0.15 as the off-stencil
  value.
- Raw one-frame second differences are noise-dominated (0.8–5.6 m/s²) and are not used.
- Result: 0.29–0.33 m/s², which agrees with round 1's 0.31 within 10 %. The fault round 1 claimed is real.

## Rechecks
- a. Closure:
  - The scale comes from the cat's linear fit, 5.465 px/frame, so 0.007937 m/px. The prior is reproduced exactly by
    construction.
  - The bbox back and front edges give 5.439 and 5.463 px/frame, so 1.036 and 1.041 m/s (within 0.5 %).
  - The endpoint mean of 5.48 px/frame gives 1.044 m/s (0.3 %).
- b. Plausibility: the float is about 158 px = 1.25 m wide, a realistic inflatable ring. The cat is about 106 px =
  0.84 m nose to tail tip, also realistic.
- c. Units and time base:
  - The unit is m/s².
  - Frame 24 = round(1.0 × 24).
  - Convention: a(24) = (|p24 − p23| − |p23 − p22|) × 24². The y drift is about 0.06 px/frame and is negligible.
- d. Fault proof:
  - C1 (0.15) took the instantaneous second derivative at frame 24 (my value 0.10–0.13). The backward stencil is
    centred on frame 23, where I get 0.29–0.33.
  - C2 (2.5) gave the ramp-phase magnitude (about 0.5 px/frame²), not the value at t = 1 s.
  - C3 and C4 (0.31) are followed.

## Decision
- Switch from the submitted 0.15 to **0.31 m/s²**, following C3. This verifies round 1's proposal.
- Confidence: medium. The value is solid to about ±10 %, but the object identity is assumed.
