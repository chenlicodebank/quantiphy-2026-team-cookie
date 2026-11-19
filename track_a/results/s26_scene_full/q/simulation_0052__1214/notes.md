# q1214 – length of the orange car (simulation_0052)

File fps 30.0033, question_fps 30 (frame = round(t*30); difference negligible). 3D Blender scene; the orange car
(Kia Stinger-like sedan) moves right-to-left parallel to the image plane at constant depth (near-side wheelbase
323.2 px constant within 0.2 % over the clip), decelerating to rest at f87.

## Scale (metres per pixel at the near-side hub plane, s_h)
1. Prior route (scale.py): quadratic fit of the hub reference x (scene track, measured frames f6-34, f46-80):
   0.3348 px/frame^2 (subsets 0.331-0.337) = 301.1 px/s^2 -> s_h = 2.86/301.1 = 0.009497 m/px.
2. depth_info route: the car keeps one depth, so d0^2 - d1^2 = s_h^2 * ((u0-cx)^2 - (u30-cx)^2), independent of f
   and of the vertical offset. With the wheelbase midpoint: s_h = 0.009658 (1.7 % off route 1). With the origin at the
   bbox centre (12.3 px rear of the wheelbase midpoint, from the overhangs below): s_h = 0.009527, 0.3 % from route 1.
   So the origin is at the bbox centre and s_h ≈ 0.00951 (the two routes agree).
   (Green-car depths give a different focal length; they are not used for this answer.)

## Pixel length (ends.py, background difference, rows 690-785)
Each end is measured where it passes near the image centre (cx = 540), so no front/rear face foreshortening shows:
- front overhang (front end to front hub) at f21-22, where the front end is at u ≈ 529-550: 94 ± 1.5 px (20-30 % column threshold, mid-blur)
- rear overhang (rear hub to rear end) at f53-54, where the rear end is at u ≈ 540-550: 118.5 ± 2 px
- wheelbase 323.2 px (hub template matching)
Total length L_px = 535.7 px. That gives L/wheelbase = 1.66, which matches the real Stinger (4.83 / 2.905).
The record's 518 px came from frames where one end shows as the near-side corner silhouette, so it is too short.

## Answer
L = 535.7 × 0.00951 = 5.09-5.10 m (5.087 with the prior scale, 5.104 with the depth scale). Answer: 5.10 m.
Confidence: about ±3 %. The main risks are the blur threshold at the ends (±3 px) and the origin convention: if the
origin were at the wheelbase midpoint, the depth route would give 5.17.
