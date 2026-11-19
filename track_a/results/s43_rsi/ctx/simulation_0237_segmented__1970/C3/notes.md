Scale from the exact prior: SAM3 track of the brown horse gives 63.6 px/s (linear fits of centroid/right edge 63.6-64.0, net displacement 62.1), so 0.874 m/s / 63.6 px/s = 0.01374 m/px (check: horse 150x42 px -> 2.06x0.58 m, plausible). The house mask (static, frame 0) spans 800 px horizontally (x 621-1420, widest row 800 px) and 716 px vertically; the symmetric diamond top/bottom and parallel vertical edges show a corner-on (~45 deg) orthographic view, so the world-space horizontal AABB width equals the image horizontal extent: 800 x 0.01374 = 11.0 m (10.9-11.3 m over the speed uncertainty). Second route: same scale gives house height 9.8 m and horse 2.06 m, both plausible; the alternative local (unrotated) plan-side reading would be 7.7 m, noted in notes.md.

Final message:
Answered. 

**Method summary:**
- **Scale:** Re-tracked the brown horse with SAM 3 over all 50 frames. Robust pixel speed ≈ 63.6 px/s (centroid linear fit 64.0, right-edge fit 63.8, net displacement 62.1). With the exact prior 0.874 m/s → **0.01374 m/px**. Sanity check: the horse silhouette (150 × 42 px) becomes 2.06 × 0.58 m — a plausible real horse.
- **House:** The mask (static all clip) spans 800 px horizontally (x 621–1420) and 716 px vertically. The symmetric diamond top/bottom silhouettes and parallel vertical edges show a corner-on (~45°) near-orthographic view, so the world-space horizontal AABB width equals the image horizontal extent.
- **Answer:** 800 px × 0.01374 m/px ≈ **11.0 m** (10.9–11.3 m over the speed uncertainty). The main ambiguity (local unrotated plan side ≈ 7.7 m) is recorded in notes.md.
