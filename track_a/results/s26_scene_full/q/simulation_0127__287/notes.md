# q_287: speed of the blue car at 1.0 s (m/s)

- This is a 2D top-down render at 24 fps (question_fps is also 24), and the camera does not move. t = 1.0 s is frame 24.
- Prior: the bike's speed is 24 m/s. In the record, both objects move at a constant pixel speed after frame 1, with no
  acceleration, so the bike's speed is 24 m/s at every frame. I use one metres-per-pixel scale:
  scale = 24 / bike pixel speed, so car speed = 24 × car px/frame ÷ bike px/frame.
- **Route 1 (`match.py`)**: NCC template matching along x with a fixed template and a sub-pixel peak.
  - Car template: the body interior, rows 285–350, taken at frame 20. Over frames 14→28 the car moves 25.36 px/frame,
    and the frame 23→24 step is 25.7 px. The match score is 0.92 or more.
  - Cyclist template: rows 583–610, taken at frame 30. Over frames 14→44 it moves 31.82 px/frame. I dropped frames
    45 and later because the match fails near the image edge.
  - Result: 24 × 25.36 / 31.82 = **19.13 m/s**.
- **Route 2**: the record's chained-matching mean steps (car 25.27, cyclist 31.64 px/frame) give 19.17 m/s.
  Background-difference edges (`measure.py`: car rear edge 25.15, cyclist front edge 31.10) are noisier because of
  shadows and give about 19.4.
- The perspective effect on the cyclist (rider height vs ground) is under 1%, which I ignored.
- **Answer: 19.13 m/s.** Confidence: high, about ±1.5%.
