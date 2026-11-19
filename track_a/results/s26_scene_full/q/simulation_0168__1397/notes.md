# q_1397 – diameter of the police van's tyre (simulation_0168)

Answer: **0.735 m** (the vertical extent of the van's front-right tyre, i.e. the tyre's world AABB height).

Prior: the bike's speed is 5.52 m/s (taken as constant). depth_info: the bike origin is 28.219 m away at t=0 and 25.554 m at t=0.5 (frame 12).
The file and question_fps are both 24 fps, so there is no time-base issue.

## Geometry / scale
* The camera is static and **level**. The road vanishing point (VP A) comes from the yellow centre line and the far white
  stop line on frame 0 (lines.py): (2641.8, 540.5), so the horizon is at v = 540.5. The scene record's VP (2777, 516) came from a weak
  kerb fit and is wrong. The cyclist's fitted 3D motion direction projects to u = 2641–2673, v ≈ 535–540, so the cyclist rides
  parallel to the road. The van's flank lines (window top/bottom, sill) vanish at u ≈ 2665–2670, so the van is parallel too.
* Focal length f:
  1. Cyclist kinematics (fit3d.py, zf.py): constant-velocity 3D line fitted to the image track (bbox centre / hip / ground
     point), with |P(0)| = 28.219, |P(0.5)| = 25.554 and |V| = 5.52 imposed. Gives f = 2543–2609 using all 80 frames and
     2500–2730 on frame subsets. This is weakly conditioned, because the motion is almost entirely radial.
  2. Rear bicycle-wheel rim ellipses (hubtrack.py, ellipse_track.py): the rim lies in a vertical plane parallel to VP A, so
     its minor/major ratio fixes f. Frames 68–79 give f = 2618–2665 (median 2638) with uA = 2642, or 2688 with uA = 2665. The front wheel is
     steered and gives 2700–2900, so it is not used. The van hubcap is a dished steel wheel and drifts from 2150 to 2800, so it is rejected.
  * Adopted f ≈ 2645 ± 60 px.
* Camera height H (fixf.py): with f fixed, refit the cyclist's line, then fit the front-wheel ground-contact rows with
  v_g − 540.5 = f·H / (Z_origin(t) − δ). This gives H = 1.184 m and δ = 0.35 m, with a contact-row residual of 0.87 px. The result is the same for all three proxies.
  Check: measuring the bicycle's wheelbase at frame 71 from its two contact points gives 1.11 m, heading 33.4° (VP A gives 32.5°). The
  origin depth lies 40 % of the way from the front contact to the rear contact, which agrees with δ.
* Tyre: D = d_px · Z / f, with Z = f·H / (v_bottom − v_h), so **D = d_px · H / (v_bottom − 540.5)**.

## Tyre measurement (front-right wheel on the visible flank)
* Frame 79 (edges_cols.py): the outer tyre circle runs from top 636.0 to bottom 790.3 at x ≈ 1173, so d = 154.3 px and D = 0.7315.
  If the bottom point is taken at the tangent-to-VP point (x = 1165), d = 156.1 px and D = 0.737.
* Frames 70–79 (tyre_multi.py): D = 0.716–0.740, with mean 0.732 and median 0.7355. Frames 75–79, the largest and cleanest, give 0.734–0.738.
* Sensitivity to f: 2600 → 0.740, 2645 → 0.732, 2690 → 0.723. The choice of origin proxy changes D by less than 0.3 %.

## Cross-checks
* Bicycle rear rim: 124 px at Z = 13.7 m gives a 0.64 m rim outer diameter, which is realistic for a 700c rim.
* Van steel rim: 92.5 px tall gives 0.438 m, consistent with a 16" wheel. A 0.735 m tyre on it has a 0.165 m sidewall, like a 225/75R16 van tyre.

Confidence: about ±3 % (dominated by f).
