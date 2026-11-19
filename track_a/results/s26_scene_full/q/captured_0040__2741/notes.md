# q_2741 – height of the poker tower (cm)

Object: "poker tower" = the playing-card tent (blue-backed card on the right, red card on the left) between the tape
roll and the white cup (scene.json `card_tent`). It is static, so I used a median of frames 0,5,10,15,20,40,44,48. File fps = question fps = 24.
Camera (lab card): f = 0.5959 x 1280 = 762.8 px, principal point (640,360).

## Pixel measurements (measure.py, tent_med.png)
- Tent top (ridge, white border of the blue card): y = 416 (left end) to 417.5 (right end).
- Tent bottom: red card base at y ~494-495, blue card base at y ~498-499. The flat cards in front start at y ~500-501,
  so the nearest base corner may be partly hidden.
- Vertical pixel extent: 82-83 px.

## Routes
1. Lab method card: 0.91 m x 82-83 px / 762.8 gives 9.8-9.9 cm. This includes the lower image position of the
   nearer base corner (the table is about 0.16 m below the camera, so depth spread along the base adds a few px).
2. Table plane from the credit card (prior 85.6 mm; corners (527,529.5),(618.5,534.5),(604.5,551),(509.5,544.5)),
   solved with PnP at f = 762.8 (pnp.py, tent_height.py):
   - PnP camera distance = 0.702 m vs the given 0.690 m, which confirms f to ~2% (f~750 would reproduce it exactly).
   - Plane normal is (-0.016, 0.999, 0.03), so the table is almost level in camera coordinates; d = 0.182 m.
   - Base corners projected onto the plane give Z ~0.86-0.88 m. The ridge, placed at the mean base depth, is
     9.1-9.2 cm above the plane. With an exactly level plane through the card centre: 9.3-9.4 cm.
3. Given tent-centre depth 0.91 m at pixel (690,457): the centre is 4.1 cm above the plane, giving a height of
   ~8.2 cm if the centre sits at half height. This is a rough check.

## Answer
9.3 cm. Routes span about 8.2-9.9 cm, and the two main routes give 9.1-9.8 cm. Confidence: moderate, about ±7%.
A standard 8.9 cm poker card would cap the height below 8.9 cm, but the measured card length is ≥9.5 cm, so these
are probably larger cards.
