# q76: walker speed at t = 1.0 s (frame 24, 24 fps; file fps = question fps)

Method (speed.py plus checks run inline on the scene/ tracks; frame 24 viewed in frames/f24.png):
- Top-down static camera. The walker moves in -x. Pixel speed at frame 24 is the backward difference x(23)-x(24):
  head 14.2 px/frame, shirt 14.5 px/frame. The 3-frame means are 14.4 for both, and the mean over the whole clip is 14.1-14.4.
  The same gait phase one cycle later (frame 58) also gives 14.2.
- Scale: the bike is 1.7 m long. Its tip-to-tip length is about 415 px near x≈1580, where the walker is at frame 24
  (it varies from 408 px at the left of the frame to 418 px at the right: a slight tilt). That gives 244 px/m at wheel-axle height (about 0.35 m).
- Perspective: the camera is at a finite height. Evidence:
  - The rider's torso moves 52.9 px/frame while the bike moves 51.2 px/frame (ratio 1.032).
  - The walker's head drifts 1.8% faster than the shirt.
  - Together these put the camera about 20-35 m (scene units) above the floor.
  - Pelvis (about 0.95 m) vs bike tips (about 0.35 m): the pelvis scale is about 2.5% larger, 250 px/m.
  - The head and shirt sit above the pelvis, so the pelvis pixel speed is about 14.0 px/frame.
- Speed = 14.0 × 24 / 250 = 1.34 m/s. Without the perspective correction: 14.3 × 24 / 244 = 1.41 m/s.
- Answer: 1.35 m/s, the perspective-corrected value (the two routes differ by about 4%).

Confidence: moderate (±5%). The main uncertainties are the pelvis gait oscillation compared with the head and shirt proxies, and the size of the perspective correction.
