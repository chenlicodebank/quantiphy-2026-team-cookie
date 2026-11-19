# q_1858 – speed of the astronaut at t = 0.5 s

- 2D segmentation video, 24 fps (file rate = question_fps), t = 0.5 s -> frame 12; speed = backward difference over frames 11->12.
- Scale: prior height 2.2 m. The figure stands upright and its pose is rigid. Its mask height (measure.py: min RGB < 225, largest blob) is 90-91 px in every frame (median 91 counted inclusively; about 90.5 px edge to edge). Scale = 2.2/90.5 = 0.0243 m/px.
- Motion: it rises smoothly and almost vertically. I fitted quadratics to frames 6-18 and took the derivative at frame 11.5, which equals the 11->12 backward step:
  - mask centroid: 2.662 px/frame
  - top of the head: 2.652 px/frame
  - bottom of the feet: 2.663 px/frame
  - The raw step from 11 to 12 is 2.73 px (centroid), which is noisy; the scene/ track agrees.
- Speed = 2.66 px/frame x 24 x 0.0243 = 1.55 m/s. If the height is taken as 91 px instead, the result is 1.545.
- Second route: the head-top and feet-bottom tracks are independent of the centroid and give the same value within 0.5%.
- Confidence: high, within about 3%.
