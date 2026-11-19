# q_2432: width of the table (cm)

File fps 24 = question_fps 24. This is a lab video, so f = 0.5959 x 1280 = 763 px and the principal point is (640, 360).

## Which dimension
The table's left-right extent across the front edge is about 0.60 m. Its front-to-back depth is much longer: the back edge is at y ≈ 440, close to the
horizon (vanishing point ≈ (597, 351)), which puts it at z ≈ 1.3–1.4 m and the table depth at roughly 0.7–0.8 m. So "width" is the left-right extent.
That is the shorter horizontal side, and it is also the extent named by the distance_table_left and distance_table_right values in depth_info.

## Measurement (table_edges.py, frame 0, mask of non-black pixels row by row)
- Front top edge at y ≈ 532: x from 283 to 923, which is 641 px. The front face (y 535–556) spans x 280–924, which is 644–645 px.
- Pixel extent used: 641.5 px.

## Scale
- Method card: size = distance x pixel extent / f. The mean of the left and right distances is (0.704 + 0.725) / 2 = 0.7145 m.
  0.7145 x 641.5 / 763 = 0.6007 m.
- Second route: back-project the two corners, (282, 533) and (923.5, 533), treating the given distances as sensor z-depth.
  X_left = -0.330 and X_right = +0.269, so the width is 0.600 m (adding dz = 0.021 m changes this by less than 1 mm).
- Alternative reading: if the distances are Euclidean ray lengths, the corners back-project to a width of 0.54 m. A ground-plane estimate from the
  slope_near depth gives 0.555–0.567 m. I chose the method-card value (0.60 m, also a standard table size), but there is about 10 % uncertainty
  depending on how the distances are read.

Answer: 60.0 cm. Confidence: moderate.
