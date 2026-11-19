2D single-scale method: person rest height at frame 0 = 42 px = 1.75 m -> 0.0417 m/px. Boat hull silhouette width across its long axis (SAM mask, frame 35) = 130 px (mast excluded; red-hull mask confirms 129 px). Width = 130 x 0.0417 = 5.4 m; length check 356 px -> 14.8 m (L/B 2.7). Second route: passing-pose height 40 px gives 5.7 m, median walking bbox 48 px gives 4.7 m; walking speed 36 px/s -> 1.5 m/s is realistic.

Final message:
I measured the boat's width using the 2D single-scale convention from the person's height prior.

**Key measurements:**
- Person rest height at frame 0 (at rest): 42 px = 1.75 m → scale 0.0417 m/px
- Boat hull silhouette width across its long axis (SAM mask, frame 35): 130 px (mast excluded; red-hull mask confirms 129 px)
- Boat length along axis: 356 px → 14.8 m (L/B ≈ 2.7, plausible)

**Answer: 5.4 m** (second-route range 4.7–5.7 m depending on the person's gait-phase pixel height; walking speed check gives a realistic 1.5 m/s).
