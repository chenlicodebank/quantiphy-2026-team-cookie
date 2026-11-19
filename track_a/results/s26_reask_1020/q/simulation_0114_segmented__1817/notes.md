# q_1817: length of the plane (m)

- 2D top-down video at 24 fps (file rate = question_fps = 24). The plane points nose down and moves straight down the image from rest (frame 0).
- Prior: acceleration = 18 m/s^2. I fitted a quadratic in t = frame/24 to scene `ref_y` (template-matched point; frames with ref_y missing were dropped) in `measure.py`:
  - frames 0-75: a = 342.6 px/s^2; 0-40: 341.8; 10-70: 342.4; 40-75: 349.0. Median of the second differences: 334.
  - Value used: 342.6 px/s^2, so the scale is 18 / 342.6 = 0.05254 m/px.
- Length means the extent along the body, nose to tail, which is the vertical (y) extent in the image. On frame 0 (sharp and static) the mask runs from y = 107 to 213, giving 107 px. A looser threshold gives 108 px. The zoomed crop `frames/f0.png` confirms this.
- Length = 107 × 0.05254 = **5.62 m**.
- Check: the wingspan is 167 px, which gives 8.8 m. A plane 5.6 m long with an 8.8 m wingspan is plausible for a light aircraft. The fits over different frame windows agree within about 2%.
- Confidence: high, about ±3%.
