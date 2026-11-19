# q1329 – average speed of the bicycle (simulation_0065)

File fps = question_fps = 24; 72 frames. t=0.58 s -> frame 14, t=1.58 s -> frame 38. Static camera.

## Method
1. 3D positions of each origin at f14/f38 = depth_info distance x unit ray through the scene/ reference point,
   principal point (1080,540), focal f unknown (focal.py, check3d.py).
2. Camera geometry: road vanishing point (800,-208) from scene/ (curbs), roll ~0, so pitch = atan(748/f), and the
   ground normal and road direction follow for each f.
3. Bicycle displacement f14->f38 (exactly 1.000 s) is along the road (cross <0.03 m, vertical <0.03 m for any f):
   |d| = 5.57 (f=1300), 5.42 (1600), 5.31 (2000), 5.26 (2300), 5.22 (2600) m. Weak dependence on f.
4. Whole-clip profile (traj.py, vpscan.py): for a point moving along a road-parallel line, 1/(y - y_vp) is linear in
   the along-road distance. Bike head-top track: constant speed (quadratic term ~0, residual 1%), with
   slope = 1.0045 x |d(14->38)| per second (ref_y: 1.0165). Mean per-frame speed over the clip = that slope.
   Choosing y_vp = -190 to -208 gives the best linear fit (this agrees with the curb VP).

## Focal length (two routes that disagree)
- Pedestrian (pelvis): moves perpendicular to the road with constant height only for f ~ 2000-2300. Real-world sizes
  at f=2300 look right: pedestrian 1.72 m, van width with mirrors 2.49 m. Camera height is about 7 m.
- Van acceleration prior 4 m/s^2: the image profile gives acc = (0.87-0.91) x |d_van|, which needs |d_van| = 4.4-4.6 m,
  so f ~ 1250-1500. At f=2300 it would give only 3.6-3.8 m/s^2. Possible causes: an eased (non-uniform)
  acceleration, or the reference-point proxies.
- Bike speed: 5.28 m/s (f=2300), about 5.45 (f=1600), 5.60 (f=1300).

## Answer
5.35 m/s. This sits between the two focal routes, leaning toward the pedestrian and size evidence, and is within
about 4.5% of either extreme. Confidence: moderate-good; the f uncertainty is the main error, about ±4%.
