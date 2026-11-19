# q_2946 – height of the trashbin (cm)

Trashbin = scene's `blue_bin` (blue confetti-pattern bin, top left; static). File fps = question fps = 24; t=1.4 s -> frame 34.
Lab intrinsics: f = 0.5959*1280 = 763 px, c = (640,360). depth_info: trashbin distance 2.303 m.

## Measurements (measure.py, rim.py; frames/bin6.png)
- Mask bbox frame 34: x 288-378, y 110-209 (100 px tall, 91 px wide); identical in frames 10 and 47 (static).
- The bin is a tapered rounded-rectangle bin seen from above, with a corner pointing roughly at the camera. The silhouette top
  (y≈110) is the BACK rim. The front rim (light lip line) sits at y≈137-138 near x≈320-336, and the front bottom at y≈208-209.
  -> front vertical edge ≈ 71 px. Top face: left/right corners (290,122)/(378,127), front-back extent 110->138 ≈ 27 px.
- View depression from top-face foreshortening: sin e ≈ 27/90 -> e ≈ 17 deg. A roll-free floor-plane fit to the other
  depths gives the camera axis about 27 deg down, so the ray to the bin is about 12 deg below horizontal (a rough check, since that fit is poor).

## Height
H ≈ (71 px * D / f + t*sin e) / cos e, with taper t ≈ 3-4 cm (rim sticks out past the base) adding ≈ 1 cm.
- D = front corner ≈ 2.303 - 0.125*cos e ≈ 2.18 m (depth taken as the true centre): H ≈ 22.4 cm
- D = 2.303 m (depth read off the front surface): H ≈ 23.6 cm
- Plain method card (2.303*71/763, no tilt correction): 21.4 cm. Taking the full silhouette (100 px, which includes the top
  face) gives 30.2 cm. That overestimates, because it counts the rim ellipse.
Answer: 23 cm (middle of 22.4-23.6).

Second route: the rim's diagonal is ≈ 88-91 px, about 0.27 m at 2.3 m. That is consistent with a small bin about 19 cm square with a height
of about 22-24 cm (height/diagonal from the image ratio 71/cos17 : 90 ≈ 0.82). Confidence: moderate (±10%). The main uncertainty is
what depth applies to the front edge and the e estimate.
