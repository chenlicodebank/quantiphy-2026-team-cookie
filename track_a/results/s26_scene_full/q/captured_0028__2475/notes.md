# q_2475 – ping pong ball velocity at t = 1.3 s (cm/s)

File fps = question_fps = 24 → t = 1.3 s is frame 31 (first apex after the first bounce at frame 26; apex ≈ 31-32).
Camera: f = 0.5959·1280 = 763 px, principal point (640, 360).

## Method
- Image positions: scene/tracks/ball.csv centre (checked on a zoomed crop of frame 31: ball spans x≈738-760, centre ≈(748, 303)).
- Depth: depth_info gives distance 1.557 m at frame 26 (t=1.1) and 1.4115 m at frame 31 (t=1.3). Checks: ball width
  predicted by f·0.04/d is 16.9 px at frame 24 (bbox 17) and 21.6 px at frame 31 (bbox 21, sub-pixel edge 21.5) → consistent.
  Between bounces (26-36) the ball's horizontal velocity is constant, so distance was interpolated linearly through the
  two anchors (−0.029 m/frame).
- 3D centres = unit ray · distance; velocity = forward differences ×24, averaged over 5 frames centred on 31 (frames 29-33).
- Result: v ≈ (−0.01, −0.11, −0.71) m/s → |v| ≈ 71.8 cm/s (3-frame window 71.3, single forward diff 70.9).
  Motion is almost entirely toward the camera; vertical ≈ 0 at the apex, lateral ≈ 0.

## Second route
- Depth from the ball's apparent width (bbox_w, f·D/w) frames 28-34, no anchors: 7-frame mean velocity 76 cm/s; width growth
  slope ≈0.4 px/frame → dZ/dt ≈ −0.6 m/s. Same magnitude as the anchor route (frame-to-frame width noise is large, so it is only a check).
- Only measuring motion in the image plane would give ~10-15 cm/s, but the depth readings clearly show the ball approaching
  the camera, and the reference uses 3D centres.

## Answer
71 cm/s. Confidence moderate: it depends on the depth rate taken from the given anchors (±15 %).
