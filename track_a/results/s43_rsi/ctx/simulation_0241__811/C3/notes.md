Scale from the prior: the brown horse at the back moves 64.64 px/s (masked template matching, frames 0-45, linear fit, residual 0.6 px) = 0.874 m/s -> 0.013521 m/px. House (SAM 3 mask) horizontal extent 806 px (x 619-1424). Perspective check: eave line horizontal at y=105 (camera at eave height), side wall 605 px vs near wall 640 px, and ground-plane relation (794-105)/(710-105) puts the house 1.139x further than the horse (confirmed by the two horses' 1.19 size ratio vs 1.14 predicted). Scale at house 0.01540 m/px -> 806 x 0.01540 = 12.4 m.

Final message:
**Answer: 12.4 m** (question 811, width of the house).

Method summary:
- **Scale anchor**: the brown horse "at the back" — masked template matching over frames 0–45 gave 2.6916 px/frame → 64.64 px/s; with the prior 0.874 m/s → **0.013521 m/px** (cross-checked with the SAM track's edge slope, 2.69 px/frame).
- **House extent**: SAM 3 mask, static, horizontal extent **806 px** (x 619–1424).
- **Depth correction**: the house is a square-plan block rotated ~45° to the camera; its horizontal eave line at y=105 fixes the horizon, and the side vs near wall heights (605 vs 640 px) plus the ground-plane relation show the house sits **1.139× further** than the horse (independently corroborated by the two horses' 1.19 size ratio vs 1.14 predicted).
- Scale at the house 0.01540 m/px → **806 × 0.01540 = 12.4 m** (naive single-scale would give 10.9 m).
