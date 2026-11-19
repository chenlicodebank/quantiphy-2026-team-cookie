# q_1647 — average flight speed of the bird (m/s)

Prior: bird length = 1.19 m. depth_info: bird 34.584 m at t=0 and 33.999 m at t=1 (cart and house depths are given too,
but their sizes are not, so they can't fix the scale). The file is 22 fps, but question_fps = 24: frame i is t = i/24, so
the t=1 depth goes with frame 24 and speeds are per-frame displacement x 24.

## Method
- Track: scene/tracks/bird.csv (checked on zoomed frames 1, 4, 19, 24, 36–58; the mask covers the bird). Origin path =
  `cx_smooth9, cy_smooth9` (9-frame mean ≈ one wing-beat, which removes the wing-flap wobble of the centroid).
- Focal length: bird length read as beak-to-tail (the bird flies across the view in side profile). Measured on white
  background where the tail and beak are both clear: f44 149 px, f45 147 px, f46 150 px. (At f40–43 the near wing hides
  the tail; over the house the dark tail blends into the wall.) f = Lpx·Z/1.19 with Z from the 3D track → **f ≈ 4203 px**
  (the three frames give 4156–4239).
- 3D track: P0 = 34.584·ray(f0), P24 = 33.999·ray(f24). For each frame, depth = where its ray meets the straight line
  P0→P24 (lateral flight, depth stays at about 33.7–34.6 m). Per-frame speed = |P(i)−P(i−1)|·24, averaged over all 58 steps.
- Script: solve.py (f and the track), final.py (speeds and checks).

## Results
- Per-frame speed has a smooth bell shape: about 2 m/s at the start, about 5.1 m/s around f28–30, about 2.5 m/s at the end.
  This looks like Blender Bezier ease-in/ease-out. Because the profile is symmetric, the image slow-down over f51–58 is
  read as ease-out rather than a turn deep into the scene. The bird does yaw there, and its mask shrinks because white
  feathers are lost against white.
- Mean over all frames: smooth9 3.734, 5-frame smoothing 3.766, 9-frame 'nearest' smoothing 3.636 → **3.72 m/s**.
- Sensitivity: if the bird actually recedes by 1 m over f51–58 → 3.94; by 2 m → 4.30.

## Second route
Using the beak edge (bbox_x1) instead of the centroid gives lateral image speeds of 20.5 / 23.7 / 23.1 / 19.5 px/frame
over f10–20 / 20–30 / 30–40 / 40–50, matching the centroid profile. Net image travel 355→1422 px in 58 frames at
33.9 m / 4203 px ≈ 0.00807 m/px gives 3.56 m/s net lateral. Adding the path curvature and depth components gives about
3.7, consistent.

## Confidence
Moderate. The scale depends on reading "length" as beak-to-tail. If the prior meant wingspan (not measurable here,
because the wings point along the line of sight), the answer would change. The end-of-clip depth behaviour is the second
uncertainty (up to +6% if the bird recedes 1 m).
