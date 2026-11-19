# q_2739: distance white cup to pink bottle (cm)

Lab video, 24 fps (file and question_fps agree), 1280x720. Focal f = 0.5959*1280 = 762.8 px, principal point (640, 360).
Both objects are static, so I measured on frame 24 (t = 1 s).

## Pixel centres (measure.py, colour masks, checked against a gridded crop)
- Pink bottle (pink mask): x 641-688, y 330 to about 480 (the base is partly hidden by the leaning card).
  Centre is about (665-666, 405), ±3 px in y.
- White cup (white mask): x 725-794, y 375-498 (rows below 498 are the table/card). Centre is (759.5, 436.5).
- These agree with the extents in scene.json (bottle 642-690 / 331-477, cup 724-795 / 375-498).

## 3D
Depths from depth_info: bottle 0.9998 m, cup 0.8740 m.
- Method card back-projection ((u-cx)/f, (v-cy)/f, 1) x depth: **16.5 cm** (16.4 if the bottle centre is at y = 410).
- If depth is read as the Euclidean distance along the ray: 17.3 cm (17.2).
- I answer with the method-card convention (16.5). The difference is about 5%, mainly from the 12.6 cm depth gap.

## Checks
- Bottle width is 47 px x 1.0 / 763 = 6.2 cm and the cup top is 69 px x 0.874 / 763 = 7.9 cm. Both are plausible real sizes.
- The cup's base sits lower in the image (y 498) than the bottle's (about 480), so the cup is closer to the camera, which matches the
  depths (0.874 m < 1.000 m).
- Lateral offset: about 10.6 cm horizontally and 3 cm vertically. Depth gap: 12.6 cm. Combined: 16.5 cm.

Confidence: moderate-high. The main uncertainty is the depth convention (±5%).
