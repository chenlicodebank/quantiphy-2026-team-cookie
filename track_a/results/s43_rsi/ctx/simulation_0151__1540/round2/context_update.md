# Round 2 addendum: Q1540 (blue cart acceleration at t = 1 s)

## Established (round 2 verified round 1's switch with independent code)
- **Pixel acceleration at frame 24 (x22 - 2 x23 + x24): 0.51 px/f² (0.50-0.53).**
  - Template-free LED-blob centroid track: 0.47-0.50.
  - Linear trend of the clean LED second differences 28-40: 0.497 (a = 0 at frame 29.55, jerk -0.076).
  - Joint smoothstep of the record's early speeds plus LED 28-41: 0.50-0.53.
  - Late-only extrapolations bracket these at 0.45-0.56.
  - The motion is a single ease: start-up acceleration about 2.2 px/f², falling linearly to zero at frame 29.6.
- **Cart front tyre: 77 px (76-78).**
  - Dark-mask width 76; left-arc circle fit about 78.
  - The vertical top edge equals the circle fit, so the fender does not occlude it. The bottom is about 2 px short at ground contact.
  - LED edges show no horizontal motion blur.
- **Result: a = 0.51 × 576 × 0.369/77 = 1.41 m/s²** (range 1.36-1.46). Answer 1.40 (C4).
- **Closure on the yellow-tyre prior: -3.5 %.** Yellow tyre 188-189 px vertically, ground-row depth ratio 1.228-1.241. The depth_info route gives f ≈ 2720 px and reproduces the 189 px.

## Ruled out
- **Submitted blend 1.643.** Its component B (1.875) needs about 0.68 px/f², which no clean route gives.
- **C5, C6.** Pixel accelerations of 0.67-0.75 (C6 also used an 86 px tyre).
- **C2, C3, C8, C9 (1.15-1.2).** About 0.42 px/f², below the anchored range.

## Open
- The tyre pixel size (74.5 vertical vs 76-78 horizontal) is a ±2 % effect. The geometry from the yellow tyre predicts 74.4 px, which would give 1.45. Any answer between 1.38 and 1.46 is within 3 % of 1.40.
