2D top-down sim. Scale from prior speed 0.67 m/s: fish centroid track gives 541 px/s (linear fit -542.5 px/s, mean 541 px/s over unclipped frames) -> 1.238e-3 m/px. SAM 3 masks give the fish's full head-to-caudal-tip extent, maximal (~845 px) at the most broadside pose (f6-f8; later poses foreshorten to ~640 px). 845 px x 1.238e-3 = 1.05 m. Second route: net displacement/duration (522 px/s) gives 1.08 m (+3%).

Final message:
Answered: **1.05 m** for the fish's length.

Method summary:
- **Scale**: the prior (fish speed 0.67 m/s) matched against the SAM 3 centroid track — linear fit −542.5 px/s (rms 7.5 px), mean 541 px/s over unclipped frames → 1.238×10⁻³ m/px. A second route (net displacement / duration = 522 px/s) agrees within 3.5%.
- **Length**: SAM 3 masks of the fish (which capture the thin caudal filament the scene's colour mask missed) give a full head-to-tail extent of 835–845 px at the most broadside pose (frames 6–8); later poses foreshorten to ~640 px as the body flexes/rolls. 845 px × 1.238×10⁻³ = 1.05 m.
- Notes written to `notes.md`, including the pose-dependence caveat (mean extent would give 0.90 m, body-only ~0.58 m).
