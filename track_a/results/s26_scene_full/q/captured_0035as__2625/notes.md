# q_2625 — soccer ball diameter (cm)

File fps = question_fps = 24, so t=0.6 s → frame 14 and t=1.6 s → frame 38.
Lab camera: f = 0.5959 × 1280 = 762.75 px.
I read the 4th depth line ("t=1.6s, distance_soccer_ball_camera = 2.4120 m") as a mislabelled basketball depth.
The soccer ball at t=1.6 is 3.052 m away, and 2.412 m with the basketball's 72 px reproduces the 23.2 cm prior.

## Measurements (measure.py plus the scene tracks; frames checked visually in frames/f14.png and f38.png)
- **Frame 38 (clear, little blur):** the soccer ball is about 45–46 px wide (bbox 45×46, area-equivalent 45.3,
  minor axis 45.8; my zoom read 43–46). That gives 3.052 × 45.5 / 762.75 = **18.2 cm** (18.1–18.4).
- **Frame 14 (motion blur):** I used the minor axis across the blur, 51–52 px. That gives 2.758 × 51.5 / 762.75 = **18.6 cm**.
- **Prior check (basketball):** the orange mask's area-equivalent diameter is 72.2 px at frame 38 and 77 px at
  frame 14. That gives 22.8 cm and 22.9 cm, against the prior of 23.2 cm (−1.5%), so the scale is confirmed.
- **Second route (ratio to the basketball at frame 38):** 23.2 × (3.052 × 45.3) / (2.412 × 72.2) = **18.4 cm**.

## Answer
18.4 cm. My soccer-ball mask is unreliable (a white ball on a near-white background), so the pixel diameter
comes from the bbox and minor axis. Confidence: about ±3%.
