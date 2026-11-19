# q 3181 – length of the middle billboard (cm)

Prior: g = 9.8 m/s^2. 2D internet video at 30 fps (file and question rates match). Single scale taken from the ball's pixel gravity.

- Pixel gravity (fitg.py): I fitted parabolas to the ball centre y in background coordinates (cy_bg, camera drift removed), skipping frames truncated at the top (77-80) and at the edges.
  - Rising (66-76): 5327 px/s^2.
  - Falling (81-97): 4747 px/s^2.
  - Joint fit over both: 4956 px/s^2.
  - After the bounce (105-108): 4950 px/s^2.
  - Median of the second differences: 4860.
  - The difference between rising and falling fits probably comes from drag, handheld camera roll, or the tracking. I used about 4980 px/s^2, so the scale is 9.8/4980 = 1.968 mm/px.
- Middle poster outer frame: x 745-1127 at frame 0, so 383 px wide (confirmed on a zoomed grid crop: frames/mid.png). Its longer, horizontal extent is the length.
- Length = 383 x 1.968 mm = 75.4 cm. Sensitivity: 70.5 cm (rising-only fit) to 79.1 cm (falling-only fit).
- Check: ball diameter 121 px x 1.968 mm = 23.8 cm, close to a real basketball (about 24 cm). This supports the scale.

Confidence: moderate-good (about ±5%).
