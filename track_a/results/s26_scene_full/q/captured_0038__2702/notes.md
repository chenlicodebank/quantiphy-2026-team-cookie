# q_2702 — diameter of the white ball (cm)

Lab video, 24 fps (file and question_fps agree), 1280x720, f = 0.5959*1280 = 763 px.
depth_info at t=1.4 s (frame 34): ball 0.7160 m, credit card 0.6867 m.

## Measurement (scripts: vprof.py, hprof.py, widths.py, crops.py)
- Background = per-pixel median; ball = signed difference from it.
- The scene record's "38 px" vertical size cuts off the ball's shaded lower part. That part is about as dark as
  the table, so its signed difference drops to zero too early. Corrected here.
- Route 1, horizontal width at 50 % of the plateau (centre rows). Motion blur is a symmetric ~14 px ramp, so the
  50 % width is close to the true diameter: 42–44 px in frames 16–29, 44–46 px in frames 36–48. Frames 30–35 are
  unusable (white card behind the ball).
- Route 2, top edge (sharp) to the darkest contact-shadow row: 42.3 px (frames 16–29) rising to 43.3–44 px
  (frames 36–48). Frame 34 itself gives 43.3.
- At frame 34 the diameter is therefore about 43 px (±1).
- D = 0.716 m × 43 / 763 = 4.03 cm.
- Check against the prior: the dark credit card at frame 34 measures about 98 px long, so
  0.6867 × 98 / 763 = 8.8 cm against the true 8.56 cm (+3 %). That bias suggests ~3.9 cm for the ball.
- A ping-pong ball is 4.0 cm (sanity check only).

Answer: 4.0 cm. Confidence: good (±4 %).
