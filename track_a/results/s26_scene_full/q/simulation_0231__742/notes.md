# Q742 – speed of the paper airplane at t = 1.25 s

- fps 24 (file and question agree). t = 1.25 s -> frame 30; speed = |p30 - p29| x 24.
- 2D scene (wall parallel to image plane, camera static), so one m/px scale from the prior (cat speed 0.714 m/s).
- Cat pixel speed (scene/tracks/cat.csv, walks at a steady pace for all 50 frames): torso_cx 8.85-8.91 px/frame,
  cx_dark 8.96-9.00, cx_mask 8.93-8.99 (net and linear fit). Used 8.93 px/frame = 214.3 px/s
  -> scale 0.003331 m/px.
- Airplane step from frame 29 to 30 (on the board, crisp):
  - record bbox centre 61.8 px, mask centroid 63.5 px; cubic fit over frames 25-34 gives 61.4 / 61.3 px
  - my own median-background difference mask (measure.py): bbox centre 61.0 px, centroid 61.4 px
  - used 61.4 px/frame.
- Speed = 61.4 x 24 x 0.003331 = 4.91 m/s (equivalently 0.714 x 61.4 / 8.93).
- Check: the record's track and my own segmentation agree to within about 2% on the step. The cat scale is
  uncertain by about 1% because of its gait.
- Confidence: moderate-high. The main risk is a depth difference between the cat (on the desk) and the
  airplane, which the 2D convention ignores.
