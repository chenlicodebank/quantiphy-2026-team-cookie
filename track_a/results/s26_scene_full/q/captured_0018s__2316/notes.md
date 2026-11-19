# Q2316 – width of the box (cm), captured_0018s

Lab video, 24 fps (file fps = question_fps = 24), 1280x720, f = 0.5959*1280 = 763 px, principal point (640,360).
The box is the white carton that the far (left) person holds upright and drops at about f29 (scene/ calls it white_carton).
depth_info gives no distance for the box, only soccer ball 2.80 m, near person 2.002 m, far person 3.13 m.

## Box shape (pixels)
- Held (f12, f20, f26), column profile (profile.py): sharp left edge at x≈469, a bright face from 469 to ≈484
  (**≈15 px**), then a darker face from 484 to 490.5 (≈6.5 px). The box sits ~12° left of the optical axis (u≈480), so when
  it squarely faces the camera its right side face shows at ≈0.21·b. That gives narrow front face a ≈ 15 px and
  side b ≈ 31 px.
- Lying on its side (f47–48, vprofile.py): a top band of 11–12 px (b·tan(depression ≈18°) → b ≈ 32–35 px) over a front band of
  13.5 px plus a 1–2 px contact line (vertical dimension = a ≈ 14–16 px). This agrees: it lies on its large b×H face.
- Falling (f34–38) the projected width is 25.7–29 px, which fits a rotating a×b ≈ 15×31 section (≤ diagonal 34).
- Height ≈ 50–52 px.
So the box is about a : b : H = 15 : 31 : 51 px. **Width = shorter horizontal extent = a ≈ 15 px.**

## Box depth (no depth_info for it, so estimated)
- Gravity prior: fitted pixel accelerations (fallfit*.py, one dropped camera frame between f35/36) for carton and
  ball on similar windows are nearly equal (ratio 0.98–1.05), so the box is at about the ball's depth (≈2.8–2.9 m). The
  absolute g·f/a gives 3.1 m for the ball against the given 2.8, so the timing is noisy and I used only the ratio.
- Ground contact: the box's front bottom edge lands at row 603 (and ~605 when lying), while the ball's bounce contact is ≈581
  (interpolated). That puts the box ≈0.23–0.28 m nearer than the ball, plus ~5 cm from the front edge to the centre → D ≈ 2.63–2.67 m.
  Relative to the far person's shoes (row 577, 3.13 m) → D ≈ 2.81 m.
- The box covers the forearm that holds the ball, so it is nearer than that arm (< ~2.9 m).
- Adopted D ≈ 2.72 m (Z ≈ 2.64 m).

## Result
width = 15 px × Z/f = 15 × 2.64 / 763 ≈ 5.2 cm; lab-card form D·px/f = 15 × 2.72 / 763 = 5.35 cm. **Answer 5.3 cm.**
Second route: the lying box's front band, 14–16 px at a similar ground depth, gives 5.0–5.6 cm.
Other readings: the broad horizontal side b ≈ 31 px ≈ 11 cm (the box's broad printed face); height ≈ 18 cm.
Confidence: moderate-low. The box depth is not given (±5%), and the face boundary in the held view comes from shading/printing (±1 px).
