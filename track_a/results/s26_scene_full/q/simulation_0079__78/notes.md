# Q78 – distance walker ↔ bike at t = 1.0 s (frame 24, 24 fps; file fps = question fps)

Scene: static, nearly top-down camera; cyclist (lower lane) and walker (upper lane) both moving -x.

Measurements at frame 24 (checked on zoomed crops of the frame):
- Bike: front tip x=443, rear tip x=851, axis y=648 → centre (647, 648). Tip-to-tip length 409 px here, 412 px median
  (grows ~0.0065 px per px of x, ~2 % across the frame, so a slight camera tilt); prior 1.7 m → 1.7/412 m/px.
- Walker head (hair blob) (1574.4, 433.6); shoulders span x≈1530–1602, y≈370–500.
- Perspective: the rider's torso blob shifts relative to the bike by 0.032 px per px of distance from image centre
  (57 px at x=1670 → 5 px at x=240), which gives a camera height of about 28 m in bike units. The pelvis (~1.0 m) is
  under the head (~1.65 m), so the pelvis pixel is (1559.6, 436.2). Check: the shoulder centre (1566) minus its ~10 px
  shift gives ~1556; the feet midpoint plus the ground-to-pelvis shift (~23 px) gives ~1543. These roughly agree.
- Pixel distance from pelvis to bike centre: 937 px.

Results (compute.py):
- 2D single-scale convention: 937 × 1.7/412 = 3.87 m
- Horizontal distance in world, correcting for height: 3.81 m; 3D with the bike origin at 0.35 m: 3.86 m; 3D with the
  bike origin at the ground: 3.94 m.

Answer 3.87 m. All plausible conventions fall within about ±2 % of it. Confidence: good (±3 %).
