# Q1460 — forklift length (fork tips to rear bumper)

File fps = question fps = 24; 72 frames; static camera; 3D Blender scene.

## Method
1. `track.py`: KLT features on the forklift tracked over all 72 frames (forward/backward check); 83 clean full-length tracks kept.
2. `fit.py`: joint fit of a pure translation with uniform acceleration from rest, s(t) = 0.5·a·(t−t0)², a = 2 m/s² (prior):
   x_k(t) = v + (x_k0 − v) / (1 + s(t)/q_k), where v = vanishing point of the motion and q_k = Z_k0/u_z (metres).
   Result: v = (−1142, −482) px, t0 = 0.000 s (frames 0 and 1 look identical because s(1/24) is only 1.7 mm), rms 0.37 px.
3. Focal length from depth_info (`recon.py`): |O(1)| = 16.7953 and |O(2)| = 19.0980 with O(t) = O0 + s(t)u give
   O0·u = 11.277 m and |O0| = 16.079 m, so the angle between the origin ray and u is 45.47°. With the origin's image point at the
   bbox centre or the area centroid, this gives f = 3281 or 3337 px (HFOV ≈ 42°).
   Check: the origin sits at along-u = 11.28 m. The midpoint of fork tip and rear in the reconstruction is 11.39 m, so the origin
   is near the body centre, which is consistent.
4. 3D feature positions are X = Z·((x−cx)/f, (y−cy)/f, 1) with Z = u_z·q, and the length is the extent along u (the direction of travel):
   - fork tip (red features at the very tip of the visible fork): along = 13.48–13.53 m
   - rear bumper/counterweight face (hitch, bottom edge): along = 9.27–9.42 m, minimum 9.27
   - span = 4.26 m. Almost independent of f: 4.258 for f anywhere in 3000–4500, and 4.28 at f = 3000.
5. Second route (`dense.py`): a dense LK grid on the fork-tip and rear regions, tracked from frame 13 to 71, with q from the
   two-frame ratio about the vanishing point. Tip maximum 13.54–13.57 and rear minimum 9.28–9.30 give a span of 4.25–4.28 m.

## Answer
L ≈ 4.27 m. This assumes the forklift drives straight along its own long axis (the tracks are straight lines through one
vanishing point, so it does not rotate).
Confidence: good (±3%). The main uncertainty is exactly where the rearmost point of the curved, untextured rear face lies (±3 cm),
plus a possible small mismatch between heading and travel direction.
