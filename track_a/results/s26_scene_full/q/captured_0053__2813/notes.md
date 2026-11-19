# q_2813 – distance white cup to book (captured_0053, lab, 24 fps; file fps = question fps)

- Objects: white cup = small white cylinder at about (565, 428) px; book = white box/card at the bottom, about
  (665, 614) px. Both are static. The "trashbin" in the prior is the moving blue object that the scene record calls a toy car.
- Frame: t = 0.4 s -> frame 10. Camera is static.
- Centres: book = own white-mask bbox in frame 10 (630-699 x 577-650) -> (664.5, 613.5). The cup mask with my threshold
  only caught part of the cup, so I used the scene record's cup bbox (552-578 x 410-446) -> (565, 428), and checked
  it on a 3x crop of frame 10.
- Lab card: f = 0.5959*1280 = 762.8 px, principal point (640, 360). Back-projection uses each depth_info value as the
  Euclidean distance to the centre along the pixel ray: cup 2.516 m, book 2.082 m.
- Distance = |P_cup - P_book| = 0.744 m.
- Sensitivity / second route: moving the centres by ±2 px (record centroids vs. mask centroids) gives 0.739-0.751 m.
  If depth were taken as z instead of ray length, the result would be 0.700 m; the convention here is Euclidean, so I use 0.744.
- I did not use the prior (trashbin velocity); the depths give the scale directly.
- Confidence: high (about ±2%, limited by the depth values and the choice of centre).
