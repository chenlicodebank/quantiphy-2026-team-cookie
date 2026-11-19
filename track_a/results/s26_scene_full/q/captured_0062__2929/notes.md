# q_2929: height of the mario toy (cm)

- Lab video, 1280x720, 24 fps (file fps = question_fps = 24). f = 0.5959*1280 = 762.8 px, principal point (640,360).
- Object: the only toy in the scene is the brown/orange plush figure lying on its back on the floor at
  about (635,625) px. scene/ calls it "plush_bear". It is static for the whole clip (mask identical at frames 30/34/40/48).
  depth_info: mario toy at 2.016 m (t=1.4 s, frame 34).
- The toy lies flat, so its standing height is its feet-to-head-top (ears included) length on the floor:
  feet at the upper left (~580,595), head/ears at the lower right (~690,640).
- Mask: HSV (S>80 with H<30) plus white (gloves/feet), closed and hole-filled (mario2.py, overlay
  frames/mask_S80.png). The outline follows the toy, and the shadow is excluded.
  Extent along the body axis (30-40 deg in the image): 119-121 px. Maximum diameter: 121.6 px.
- Route 1 (method card, depth x px / f): 2.016*119.5/762.8 = 31.5 cm (31.4-31.9).
- Route 2 (perspective-correct): I estimated the floor-plane normal from the vanishing points of the white board's
  rectangle corners (frames 24-48, plane.py), then intersected the extent end-points with a plane through the toy
  centre (3D point at 2.016 m) parallel to the floor (axis.py). This gives 30.2-30.3 cm for every axis angle.
  Route 1 uses the Euclidean depth as z: the true z is 1.90 m, and the floor foreshortening partly compensates.
- The depth_info values do not all fit one floor plane (the trash bin is inconsistent), so I used them only per object.
- Answer: 31.0 cm, between the two routes, which are 4 % apart. Confidence: moderate (±5 %). Mask-edge blur is about ±2 px (±1.7 %).
