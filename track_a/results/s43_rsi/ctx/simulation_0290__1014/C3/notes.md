2D top-down simulation; scale from prior fish speed 0.67 m/s. SAM masks give the fish's full nose-to-caudal-fin-tip extent 835 px (max, frame 8, body straight, fin edge-on; 632-835 px over the tail-beat cycle). Fish pixel speed from silhouette tracking: whole-centroid 512 px/s, rigid head/trunk region 475 px/s (centroid biased by the contracting caudal fin), mean ~500 px/s -> 0.00134 m/px. Length = 835 x 0.00134 = 1.12 m; second route with the median rendered extent (~790 px) gives 1.06 m, so answer ~1.10 m.

Final message:
I measured the fish in this top-down 2D simulation and answered.

**Method summary**
- **Length in pixels:** SAM 3 masks at 10 frames gave the fish's full nose-to-caudal-fin-tip extent. The caudal fin beats between edge-on (long thin spike) and spread (fork), so the extent varies 632–835 px; the maximum, 835 px at frame 8 (body straight, axis 0.8°), is the best estimate of the model's full length. Body depth is constant (~232 px), confirming no perspective scaling.
- **Scale:** from the prior (fish speed 0.67 m/s). The fish's texture is the static water caustics, so template matching was unreliable; silhouette-based tracking gave 512 px/s (whole centroid, biased by the contracting fin) and 475 px/s (rigid head/trunk region), mean ≈ 500 px/s → 0.00134 m/px.
- **Answer:** 835 px × 0.00134 ≈ 1.12 m; the second route (median rendered extent ≈ 790 px) gives 1.06 m, so I quoted **1.10 m** (notes.md written with full measurements and caveats).
