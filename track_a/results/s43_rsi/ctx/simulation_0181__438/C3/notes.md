2D scene: scale from the prior's own object. The brown carton slides down the straight belt; over the unoccluded frames 12-29 the box centre follows a quadratic with a(0.75 s)=736 px/s^2 (rms 0.5 px, v(0.75)=589 px/s), so scale = 2.338/736 = 0.00318 m/px (box ~0.95 x 0.59 m, plausible). At t=1.5 s (frame 36) the box is partly behind the crate, so the centre was taken as trailing edge (never occluded) + half the projected length: increments 40.8 px/frame -> v(36)=980 px/s. Speed = 980 x 0.00318 = 3.11 m/s; second route using the trailing edge for both v and a gives 3.36 m/s, so 3.2 m/s.

Final message:
I measured the box's motion in the 2D render and scaled it with the prior's own object.

**Method**
- Segmented the brown carton (SAM 3 + colour mask) and tracked its centre with three independent trackers: mask centroid, min-area-rect centre, and the unoccluded trailing edge plus half the projected length.
- Frames 12–29 (before the crate occludes the box) give a very clean quadratic: **a(0.75 s) = 736 px/s²** (rms 0.5 px), v(0.75 s) = 589 px/s → scale = 2.338/736 = **0.00318 m/px** (box ≈ 0.95 × 0.59 m — a plausible carton, and the brick course ≈ 0.32 m, which supports this scale).
- At t = 1.5 s (frame 36) the box is partly hidden by the orange crate stack, so the centre was reconstructed from the never-occluded trailing edge plus half the projected length: increments ≈ 40.8 px/frame → **v(36) ≈ 980 px/s**.

**Answer: 3.2 m/s** (route 1: 3.11 m/s; route 2 using the trailing edge for both speed and acceleration: 3.36 m/s). A pure constant-acceleration extrapolation would give ~3.6 m/s, but the measured acceleration of the unoccluded trailing edge clearly falls as the box reaches the crate/end of the belt, so I did not use it.
