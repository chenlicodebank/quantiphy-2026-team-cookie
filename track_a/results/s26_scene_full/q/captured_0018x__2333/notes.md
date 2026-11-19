# q_2333 — distance between the two people (cm)

The file and the question both run at 24 fps. The people stand still for the whole clip.

## Method (lab method card)
- f = 0.5959 × 1280 = 762.8 px, principal point (640, 360).
- Silhouette mask: any pixel with min(RGB) < 215 on the white background, with the watermark masked out (`measure.py`).
- Person centre: u = median x of the mask rows at 45–60 % of body height (hips, so the outstretched arms are left out);
  v = middle of the head-to-feet bbox.
  - Left (far) person: u ≈ 385, v ≈ 375. Depth 3.130 m.
  - Right (near) person: u ≈ 983, v ≈ 410.5. Depth 2.002 m. Her feet touch the bottom edge, so her v may be slightly low,
    but this barely changes the result because the vertical offset is small.
- Back-projection: P = ((u-cx)/f, (v-cy)/f, 1) × depth.
  - L = (-1.046, 0.062, 3.130), R = (0.900, 0.133, 2.002). Distance = **225.1 cm** at frame 0.

## Checks
- Same measurement at frame 24: 224.4 cm. At frame 48: 225.8 cm (the left bbox there includes the box lying on the floor).
- Using the trunk or leg column instead of the hips changes u by a few px, which changes the result by about ±1 cm.
- If the depth is treated as the Euclidean ray length instead of Z, the result is 214.4 cm (5 % lower). The card says to
  use Z = depth, so the answer uses that reading.

Answer: 224.9 cm (mean of frames 0 and 24). Confidence: good. The main uncertainty is the depth convention (±5 %).
