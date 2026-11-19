# q_2821 – distance between the white cup and the book (m)

- Objects: white cup = static tumbler at pixel centre (564.2, 423.8); book = the white printed rectangle
  ("white_card" in scene/) at (664.7, 614.1). Both are static. I checked their centres on a zoomed crop of frame 10
  (t = 0.4 s) and they match the mask centres in scene/static_objects.json.
- Camera: f = 0.5959 x 1280 = 762.8 px, principal point (640, 360). File fps = question fps = 24.
- depth_info at t = 0.4 s: cup 2.516 m, book 2.082 m. I treat these as Euclidean distances along the viewing ray.
- Back-projection (dist.py): each point = d x unit ray. 3D distance = **0.755 m**.
- Checks: if the depths are read as z-depth instead, the distance is 0.723 m (4 % lower). Moving the cup centre by
  ±3 px changes the distance by ±0.01 m. The depth difference (0.43 m) accounts for most of the distance.
- I did not use the prior (trashbin velocity), because the distance comes directly from the depths and the camera.
- Confidence: good, about ±5 %.
