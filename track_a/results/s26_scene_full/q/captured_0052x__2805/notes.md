# q_2805 — distance between trash bin and shoe (m)

Lab clip, file fps 24 = question_fps 24. Depths are given at t=1.0 s, which is frame 24. Both objects are static.
Camera: f = 0.5959 x 1280 = 762.8 px, principal point (640,360).

## Measurements (frame 24, measure.py / bin.py)
- Shoe: the green-screen foreground mask has bbox (250,626)-(318,687). Its bbox centre is (284.0,656.5) and its
  centroid is (285.7,658.3). It is the same in frames 20-28.
- Bin: the plain foreground mask and the blue-hue mask both merge with the person's dark legs (bbox x0=658-660, which
  is wrong). From the 4x zoomed crop (frames/bin24.png), the bin's own box is about x 680-775, y 484-591, so its centre
  is about (727.5,537.5). The scene record's median centre is (729,534).
- Back-projection: P = unit ray x the given depth (the depth is the distance to the centre). Shoe depth 2.231 m, bin
  depth 2.977 m.

## Result
The distance is 1.558-1.570 m across the centre choices (dist.py). I answer **1.563 m**.

## Check
Varying the centre definitions (bbox centre vs centroid, crop box vs scene median) changes the result by less than
1%. The result is dominated by the lateral offset (about 444 px, roughly 1.3-1.7 m at these depths) and by the depth
difference of 0.75 m. Confidence: high (about ±3%).
