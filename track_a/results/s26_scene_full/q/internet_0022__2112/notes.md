# Q2112 — length of the monitor (cm); prior: mouse width = 57 mm

Internet video, static overhead camera. The question asks for a size, so the frame rate does not matter.
Convention: one planar scale from the prior (the annotators' method).

- Mouse (white Magic Mouse, static, centre about (1598,1338)): white-mask minAreaRect in `measure.py`, on frames 0, 10 and 35,
  at thresholds V>150/170/190. Width = 101.6–103.4 px, so I used **103 px**. Length 198 px, which gives L/W = 1.92
  (the real mouse is 113.5/57 = 1.99, so this is consistent).
  Scale = 57 / 103 = 0.553 mm/px.
- Monitor (silver iMac seen from above, bottom right, top edge seen almost edge-on as a long diagonal strip): measured tip to tip
  on frame 35 from zoomed crops. Left tip about (1938,2074), right tip about (3110,1604). Length is about 1262–1265 px.
  A brightness profile along the axis gives bright pixels over about 1260 px, which agrees.
- Length = 1263 x 0.553 = 699 mm ≈ **69.9 cm**.
- Check: a real 27" iMac is about 65 cm wide. The monitor top sits higher, closer to the camera, than the mouse, so a planar scale
  should overestimate it slightly, which fits. The scene record (scene.json) only noted the monitor, without a size.
- Confidence: moderate-high on the convention. The main uncertainty is ±2% in the mouse width from edge blur.
