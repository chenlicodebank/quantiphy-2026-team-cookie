2D planar scale from the prior: person silhouette height ~47.5 px = 1.75 m -> 0.03684 m/px (walking speed then 1.33 m/s, a realistic check). SAM boat mask bow-to-stern extent along the hull axis = 356.5 px (identical at frames 10/30/55, mast excluded), giving 13.1 m; the person's gait makes its pixel height vary 44-51 px, i.e. about +-6% on the answer.

Final message:
**Answer: 13.1 m**

Method summary:
- **Scale (2D planar, from the prior):** the walking person's silhouette height is ~47.5 px (SAM masks 44–49.5 px; colour-threshold silhouette oscillates 39–51 px with the gait, mean 46, median 46.5). With 1.75 m → **0.03684 m/px**. Cross-check: the person's 36.1 px/s then equals 1.33 m/s, a realistic walking speed.
- **Boat length:** SAM 3 boat mask at frames 10/30/55 (fully visible; clipping only starts at f63). Extent along the hull axis (bow tip (184,879) → stern (516,1008), 20°) = **356.5 px**; the mast does not inflate it (hull-only extent identical).
- **Result:** 356.5 × 0.03684 = **13.1 m** (a plausible small fishing boat; beam ≈ 4 m).

Main uncertainty: the person's pixel height varies ±6 % over the walk cycle (44 px → 14.2 m, 51 px → 12.2 m), so the answer carries roughly ±6 % uncertainty. Notes written to `notes.md`.
