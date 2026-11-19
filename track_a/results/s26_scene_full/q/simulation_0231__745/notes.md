# Q745 – height of the black cat incl. tail (m)

Prior: cat speed = 0.714 m/s. 2D scene: the cat walks along the desk top, parallel to the image plane, with a static camera, so one m/px scale applies. fps = question_fps = 24.

Script: `measure.py` reads scene/tracks/cat.csv (I checked the record against frames 12 and 24 with zoomed crops).
- Pixel speed: linear fits of x(frame) give torso_cx 8.91, cx_dark 9.00, cx_mask 8.99 px/frame. End-to-end values are 8.85–8.96. I used 8.93 px/frame = 214.3 px/s.
  Scale = 0.714 / 214.3 = 0.003332 m/px.
- Height incl. tail = bbox_y1 − bbox_y0 + 1, the feet at y≈741 up to the tail tip at y≈597–610. I left out frame 0 (a ghost artefact) and frames 21–25, where the tail tip is low contrast over the dark board and the bbox misses it (confirmed visually at f24). Median over the remaining frames is 140.5 px (range 132–146).
- Height = 140.5 × 0.003332 = 0.468 m.

Check: by eye on frame 12 the tail tip is at y≈605 and the feet at ≈741, about 137 px or 0.456 m. That agrees with the median to within 3%. The range 132–146 px corresponds to 0.44–0.49 m.
Confidence: moderate-high. The main uncertainty is how the tail pose varies, about ±4%.
