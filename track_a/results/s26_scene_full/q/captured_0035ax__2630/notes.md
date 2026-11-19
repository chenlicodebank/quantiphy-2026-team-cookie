# q2630 – soccer ball velocity at t = 0.6 s (cm/s)

t = 0.6 s -> frame round(0.6*24) = 14 (file fps = question fps = 24). Ball rolling toward camera / right, clear of the
foot (from frame 10) and before the collision with the basketball (frame 19). Frame 14 centre checked on a zoomed crop
(f14.png): ~(525, 408), matching the scene track; own white-mask centroid (524.1, 406.6).

Camera: f = 0.5959*1280 = 762.8 px, principal point (640, 360).

Depth per frame (only t=0.6 given for the soccer ball): floor-plane route. The 4th depth_info line is labelled
"soccer" but 2.412 m fits the basketball at t=1.6 (it gives basketball diam 21.8 cm, same as at t=0.6: 22.1 cm,
prior 23.2 cm), so it was used as the basketball. Back-projected ball centres (soccer f14 @2.758, soccer f38 @3.052,
basketball f14 @2.270, f38 @2.412) were fitted with a plane offset by the ball radii (soccer r = 8.7 cm from its
size at f38, basketball 11.6 cm); residuals <= 1 cm. Each frame's centre ray is intersected with that plane
(reproduces the f14 depth: 2.742-2.748 vs 2.758 given). Depth falls ~5 cm/frame (2.835 m at f12 -> 2.587 m at f17).

Velocity (forward 3D differences, cm/s), frames 12..17:
- scene track centres: 200, 177, 210, 194, 205 -> mean 197.0; chord 12->17 196.6
- own centroid: 203, 190, 195, 189, 205 -> mean 196.3; chord 196.2; 3-frame window 191
Frames 11->12 contain a probable dropped capture frame (doubled step), so the window starts at 12.
Lateral-only (fixed depth) motion gives 159 cm/s, so the depth component matters; the plane route uses it.

Answer: 196 cm/s. Confidence: moderate (±5-8 %): depends on per-frame depths the reference measured directly.
