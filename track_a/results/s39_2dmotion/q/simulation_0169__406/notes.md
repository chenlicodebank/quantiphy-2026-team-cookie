# q_406 — acceleration of the astronaut at t = 2 s (m/s^2)

- question_fps = file fps = 24, so t = 2 s is frame 48. Acceleration = (speed(48) - speed(47)) x fps = second difference
  of the position (frames 46, 47, 48) x fps^2.
- Scale (2D video): prior height = 2.2 m. Pixel height of the upright astronaut at frame 0: own threshold mask
  (gray > 60) 89 px, SAM 3 mask box 89.2 px (vert 90), scene record (gray > 25) 91 px, zoomed frame read by eye
  ~476-567 -> 91 px. They agree within 2.3 pct; the low-threshold/visual value includes the dark visor top, so I use
  90.5 px -> 0.02431 m/px.
- Motion (measure.py): intensity-weighted centroid of the astronaut each frame. SAM centroid at frame 48
  (1307.8, 332.5) matches my track within 1 px. Raw one-frame speeds are noisy (±0.4 px/frame), so the raw second
  difference at frame 48 (-661 px/s^2) is pure noise. The path length vs frame fits a Blender Bezier ease-in/ease-out
  (two keyframes at about frames -0.4 and 78.4, handle fraction 0.335 = smoothstep, D = 274.2 px, rms 0.23 px).
- Acceleration at frame 48 from the smooth curve:
  * Bezier/smoothstep global fit: -31.6 px/s^2
  * global quintic: -32.8 px/s^2
  * local cubic over ±6/8/10 frames: -35.2 / -33.0 / -30.9 px/s^2
  -> ~-32 px/s^2 (decelerating; the speed peak is at frame ~39). x 0.02431 m/px = -0.77 m/s^2.
- Answer: magnitude 0.77 m/s^2 (the astronaut is slowing down; signed value -0.77).
- Confidence: moderate. Value is small and depends on the ease curve shape; routes agree within ~±7 pct.
