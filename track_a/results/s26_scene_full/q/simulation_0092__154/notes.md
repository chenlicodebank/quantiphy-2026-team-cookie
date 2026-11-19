# q_154 — speed of the car at 1.0 s (m/s)

- fps = question_fps = 24 -> t = 1.0 s is frame 24. 2D video, camera static, car moves right->left at constant pixel speed.
- Pixel speed: scene track ref_x frames 3..65 (fully visible) gives 1764 px / 62 frames = 28.45 px/frame, constant.
  Own re-measure (measure.py, background-difference mask, bbox centre): steps at frames 23-26 = 29.0, 28.5, 28.0, 29.0 px
  (mean 28.6; one-frame steps are quantised to +-0.5 px), so 28.45 px/frame is used.
- Scale from the prior (car length 5.67 m): bbox length is 128 px near the image centre and grows to 137 px at the
  image edges because the end faces show off-axis (perspective). The side-on length 128 px is the clean value
  (131-132 px at frame 24 includes some end-face). Scale = 5.67/128 = 0.0443 m/px.
- Speed = 28.45 x 24 x 0.0443 = 30.2 m/s.
- Second route/check: using the frame-24 length (131.5 px) gives 29.4 m/s (3% lower); per-frame step 28.5 px at frame 24
  gives 30.3 m/s. Real-world sanity: ~109 km/h for a pickup, plausible.
- Confidence: good (~3%), the main uncertainty is which pixel length the reference used for the scale.
