# Q1531 – speed of the car at t = 1 s (m/s)

Time base: file fps = question_fps = 24, so t = 1 s is frame 24. Speed = one-frame backward difference (frame 23 → 24) × 24.

## Scale (prior: tyre diameter 0.764 m)
- `rimfit.py`: I fitted a circle to the sharp outer edge of the white rim (residual about 0.15 px) to get the hub centre in every frame. For the front-left wheel at frame 24 the hub is at (629.9, 791.5) and the rim diameter is 123.3 px.
- Tyre outer diameter. The bottom edge (tyre to floor) is at y ≈ 884.7, so 2 × (884.7 − 791.5) = 186.3 px. Frames 16-25 give 185.3-187.6 px.
- `drawcirc.py` overlays a circle of D = 186.4 px centred on the rim (frames/c24rim.png). It sits on the tyre outline on the left, top and bottom; the right edge is perhaps 1-2 px wider.
- Chroma-based circle fits (`circfit.py`) depend on the threshold because the wheel-arch shadow blurs the edge: 180-198 px. They agree with the value above only roughly.
- Adopted D = 187 ± 3 px, giving 0.764 / 187 = 4.086 mm/px in the plane of the near-side (left) wheels.
- The rear tyre reads 2-3 px larger (190-192 px). It is darker and more shadowed, and the depth_info names the left front tyre, so I used the front tyre.
- Implied focal length from the depth_info (11.38 m at t = 0.5 s): 187 × 11.38 / 0.764 ≈ 2785 px, which is a horizontal FOV of about 38°. That is plausible. With this focal length the car side is about 4.7 m long, also plausible.

## Motion
- Hub-centre x positions from the rim fits:
  - Front wheel: 920.0, 825.0, 728.2, 629.9, 530.3 at frames 21-25.
  - Rear wheel: 1437.8 (frame 23), 1339.5 (frame 24).
- Step from frame 23 to 24: front 98.3 px, rear 98.3 px.
- Both hub y values stay constant (791.5 front, 789.1 rear) and both wheels shift by the same amount. So the car is translating side-on at constant depth with no yaw, and every point, including the origin, has the same world speed.
- The scale and the displacement are both measured in the plane of the near-side wheels, so no correction for depth is needed.
- Speed = 98.3 px × 4.086 mm/px × 24 = **9.64 m/s**.

## Second route / checks
- The scene record's body template-match shift for frame 23 → 24 is 97.3 px (an average of upper and lower body patches). That gives 9.54 m/s, within 1 %.
- Neighbouring frames show smooth acceleration (front-wheel steps 95.0, 96.8, 98.3, 99.6 px), so the backward difference is not noisy.
- The main uncertainty is the tyre's pixel diameter (±3 px, about ±1.6 %).

Confidence: good (about ±2-3 %).
