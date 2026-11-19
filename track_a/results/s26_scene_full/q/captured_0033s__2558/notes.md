# q2558 — ping pong ball velocity at t=0.5 s (frame 12 at 24 fps; file fps is also 24)

Lab camera: f = 0.5959*1280 = 763 px, principal point (640, 360).

## Measurements (scene/tracks/ball.csv centroids, checked on zoomed crops in frames/crops.png)
- Apex at f8–9 (cy ≈ 181). Ball falls onto the far table edge and bounces at f14. f12 is heavily motion-blurred vertically, but the centroid sits mid-streak (cy 288).
- Vertical pixel steps f9→f14: 10.6, 21.2, 74.9, 54.9, 61.9. The 74.9 jump fits a **dropped frame between f11 and f12**: with gravity steps of about 10.6 px/frame² the expected steps are 32 + 43 = 75, then 54 and 64.
- Depth near f12 from the 40 mm prior: apparent diameter (width across the blur) fitted over f6–14 is 26.1 px at f12, so Z ≈ 1.17 m (it slowly approaches the camera, 1.21 m at f9 and 1.14 m at f14).
- Independent depth check from gravity: pixel acceleration over f9–11 is 10.6 px/frame², so Z = g/24² * 763/10.6 = 1.22 m. This agrees with the size-based depth.
- The given depth_info (1.457 m at 0.9 s, 0.738 m at 1.4 s) does not agree with the ball's apparent size (f22: 31 px means 0.98 m for a 40 mm ball; f34: 37 px means 0.82 m). It also cannot be used at 0.5 s without wild extrapolation (~2 m). So I used the prior-based depth.

## Velocity (3D back-projected centres, vel.py)
- Forward difference f12→13: 206 cm/s. Central difference f11–f13: 245 cm/s. Mean of forward differences f10–f13: 202 cm/s.
- Physics route: the real time from the apex to f12 is about 4.5 frames (counting the dropped frame), so v_vertical = 9.81*4.5/24 ≈ 1.84 m/s. Adding the motion toward the camera (~0.37 m/s) gives about 188 cm/s.

Answer: ~210 cm/s. The routes span 188–245 cm/s. Confidence: moderate. Most of the uncertainty comes from the dropped frame and the depth scale, since the depth_info conflicts with the ball's apparent size.
