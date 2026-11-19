# q_480 — speed of Io at t = 1 s (m/s)

Prior: Callisto (outermost moon) speed = 0.627 m/s. 2D pole-on render, file fps = question_fps = 30, t = 1 s -> frame 30.

## Method
- 2D scene: one metres-per-pixel scale for everything; scale = 0.627 m/s / Callisto pixel speed.
- Both moons are in uniform circular motion (constant pixel speed, no angular acceleration), so speed at t=1 s = model
  speed (raw one-frame speeds have ~±6 px/s centroid noise).
- Identities checked on frame 30 (frames/f30.png): Io on innermost orbit at (1118, 541), Callisto on outer orbit at (1185, 890).

## Measurements (measure.py, own tracker: green excess over median background, local half-max centroid)
- Io: R = 159.40 px, omega = -1.17868 rad/s -> 187.88 px/s (scene record 187.92). Raw f30 183.4, mean f25-35 188.9, mean all 188.1.
- Callisto: R = 414.16 px, omega = -0.14708 rad/s -> 60.92 px/s (scene record 60.96). Mean all 61.16.
- Note: the first tracker run without background subtraction locked onto the static labels; fixed.

## Answer
v_Io = 0.627 x 187.88 / 60.92 = 1.934 m/s (record values: 1.933; mean-speed ratio: 1.928; local window: 1.944).
Answer 1.933 m/s. Confidence high (< 1 %).
