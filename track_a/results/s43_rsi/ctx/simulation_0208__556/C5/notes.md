2D scene: scale from the prior's free-fall acceleration. Own background-subtraction track and the independent SAM-3 track give a pixel acceleration of 7340 px/s^2 (fit cy = c + 0.5*a*t^2 with v0=0 over frames 0-10, rms 1 px; bbox-mid estimator 7348), so s = 9.8/7340 = 0.001335 m/px (second route: 686 px fall in 0.432 s -> 0.001333 m/px). The typewriter at rest (frames 24-29, upright on the desk) has a SAM mask vertical extent of 173 px (y 851-1023). Height = 173 x 0.001335 = 0.231 m; the weak-perspective check (constant 292 px width during the fall, desk vanishing point at y=728) changes this by <1.5 %.

Final message:
**Answer: 0.231 m**

Method summary:
- **Scale (2D, from the prior):** the typewriter is released from rest and free-falls at 9.8 m/s². Both my own background-subtraction centroid track and the independent SAM-3 track give a pixel acceleration of **7340 px/s²** (fit `cy = c + ½at²` with v₀=0 over frames 0–10, rms ≈ 1 px; bbox-mid estimator 7348). So **s = 9.8/7340 = 0.001335 m/px**. Second route (686 px fall in 0.432 s) gives 0.001333 m/px — 0.2 % agreement.
- **Height in pixels:** the typewriter at rest (frames 24–29, upright on the desk) has a SAM-3 mask vertical extent of **173 px** (y 851–1023, base on the desk at y≈1026).
- **Perspective check:** the projected width stays constant (292 px) over the whole fall while the object moves 520 px vertically, and the desk's parallel edges converge at y=728 → weak perspective (f ≳ 3000 px), so the vertical foreshortening of the height and of the fall acceleration are the same; correction < 1.5 %.

h = 173 × 0.001335 = **0.231 m** (range 0.228–0.233 across estimators), consistent with a vintage typewriter ~0.38 m wide × 0.23 m tall.
