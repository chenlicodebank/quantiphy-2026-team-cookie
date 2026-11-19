# q2724: displacement of the white ball between 1.0 s and 1.5 s (cm)

- question_fps = file fps = 24, so t=1.0 s is frame 24 and t=1.5 s is frame 36.
- Camera: f = 0.5959*1280 = 762.8 px, principal point (640,360). Depths come from depth_info: 1.014 m at 1.0 s and 0.737 m at 1.5 s.
- Ball centres: scene/tracks/ball.csv circle fit gives f24 (542.6, 454.3) and f36 (497.2, 501.8).
  I re-measured them in `measure.py` (mask = bright and low saturation and different from frame 48, with row profiles
  and overlays in frames/mask_*.png). That gave f24 centroid (542.5, 454.5) with width 31 px, and f36 x centre about
  496.6 with rows y480-520, so the centre is at about 500-501. The bottom of the mask is cut off by shading. The two
  measurements agree to about 1 px.
- Back-projection follows the method card, ((u-cx)/f, (v-cy)/f, 1) x depth (`disp.py`):
  - **27.7 cm** for both sets of centres.
  - If depth_info is treated as the Euclidean ray length instead, the result is 28.6 cm.
- Check: the depth and pixel diameter give a ball diameter of 3.94 cm at f24 and 4.10 cm at f36. That is consistent
  with a 4 cm ping-pong ball, so the depths and focal length agree with each other.
- f36 may sit right after an irregular frame step (f35->36). The given depth refers to that frame, so I used it as is.
- Answer: 27.7 cm. Confidence is fairly high (about ±4%).
