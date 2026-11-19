# q_743 – acceleration of the paper airplane at t = 1.25 s

- fps = question_fps = 24, so t = 1.25 s is frame 30. This is a 2D scene: a static camera looking straight at the wall, with motion parallel to the wall. One scale converts pixels to metres.
- **Scale (from the prior):** the cat's speed is 0.714 m/s. The cat walks at a steady pace. Its pixel speed from linear fits of x against frame (f0–49) is 8.91 (torso_cx), 9.00 (cx_dark) and 8.99 (cx_mask) px/frame. The net-displacement versions give 8.85–8.96. I took 8.93 px/frame = 214.3 px/s, which gives **0.003332 m/px**.
- **Airplane track:** re-measured in `measure.py`. The mask is the frame minus the frame-49 background (LAB L channel, |diff| > 15, largest component). For each of frames 13–38 I recorded the bbox centre and the midpoint between the PCA axis ends. On the board (f14–32) this agrees with scene/tracks to about 1–2 px. The per-frame speed (backward difference) falls steadily after the apex: f26 66.1, f27 65.7, f28 64.2, f29 61.7, f30 60.6, f31 60.3, f32 58.7 px/frame.
- **Acceleration at frame 30:** a = speed(30) − speed(29).
  - Raw values: −1.19 px/f² (bbox centre) and −1.29 px/f² (axis midpoint).
  - Polynomial fits of position over windows 18–32, 20–32, 22–32 and 24–32 (degree 2–4) give −1.16 to −1.37 px/f².
  - Linear fits of speed against frame over 22–32 and 26–32 give −1.31 to −1.35 px/f².
  - Adopted value: −1.32 px/f² × 576 = −760 px/s² × 0.003332 = **−2.53 m/s²**. It is a deceleration; the answer is given as the magnitude, 2.53.
- **Second route:** the two centre definitions (bbox and axis midpoint) and the scene record's centres all agree to within 0.1 px/f². The speed slope over a wider window agrees too.
- **Confidence:** moderate, about ±10%. The main uncertainties are per-frame noise (fit spread 2.2–2.6 m/s²) and whether the airplane and the cat are at exactly the same depth. The 2D convention assumes they are.
