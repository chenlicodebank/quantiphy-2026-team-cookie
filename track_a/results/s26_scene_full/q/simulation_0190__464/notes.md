# Q464: speed of the box at t = 1 s (m/s)

- **Which object:** "the box" is the brown cardboard box on the truck roof. Scaled by the 1.33 m prior, the truck comes out about 2.7 m wide, which is realistic. If "the box" meant the truck's cargo body instead, the cardboard box would be only 0.66 m wide.
- **Time base:** fps = question_fps = 120, so t = 1 s is frame 120.
- **Scale (2D, from the box itself):** the box's width at frame 120, measured from the edge gradient in code, is 281 px (x 806.5 to 1087.5). The record gives 281.5 px. I used 281.25 px, so the scale is 1.33 / 281.25 = 0.004729 m/px.
  - The width stays the same over the whole clip, so the box does not change depth.
  - Its motion is purely vertical (horizontal drift < 0.07 px).
- **Motion (measure.py):** I tracked the upper part of the box by template matching (score ≥ 0.989, sub-pixel peak) over frames 60–180. Then I fitted a local quadratic centred on frame 120 with half-windows of 10, 20, 30 and 40 frames. The upward speed came out at 0.1531 to 0.1538 px/frame every time.
  - That gives 0.1535 × 120 × 0.004729 = 0.0871 m/s.
- **Second route (check2.py):** a different template (top edge plus flap, taken from frame 90) over frames 90–150 gives 0.1524 px/frame, which is 0.0865 m/s.
  - The record's track (scene/tracks/cardboard_box.csv, frames 100 to 140) gives (14.557 − 8.408) / 40 = 0.1537 px/frame, which agrees.
  - My own top-edge row detector locked onto the wrong edge, so I did not use it.
- **Answer:** 0.087 m/s.
- **Confidence:** high, within about 2%. The box is accelerating smoothly with no events nearby. A one-frame difference is too noisy at about 0.15 px/frame, so the local fit stands in for it.
