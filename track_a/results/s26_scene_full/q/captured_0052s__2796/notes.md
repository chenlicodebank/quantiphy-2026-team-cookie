# q_2796: distance between basketball and shoe (m)

The file and the question both run at 24 fps. Both objects are static (scene record: ±0.3 px over the whole clip), so I measured at t = 1.0 s (frame 24), the time the depth_info is given for.
The method follows the lab card: f = 0.5959 × 1280 = 762.8 px and (cx, cy) = (640, 360). Each centre is back-projected along its unit ray to the given camera distance: basketball 1.9365 m, shoe 2.2310 m.

Measurements (measure.py, frame 24, foreground mask as in the scene record):
- Basketball: bbox x 756–847, y 623–719 (the bottom touches the image edge). The circle fit on the side outline gives centre (801.7, 671.4) and a diameter of 93.9 px. From the bbox: the widest chord is 92 px, so the centre is (801.5, 669).
- Shoe: bbox x 250–318, y 628–687. Mask centroid (286.8, 658.2); bbox centre (284, 657.5).
- 3D distance: 1.265 to 1.271 m across the four centre combinations. Answer: 1.267 m.

Checks:
- The basketball diameter from depth × px / f is 0.234 m, close to a real basketball (~0.24 m). This confirms the scale and the f/depth convention.
- The centre-choice variants (circle fit vs bbox, centroid vs bbox centre) agree to within 0.5%.
- I did not use the prior (the yoga ball's velocity): the depth_info alone sets the scale.

Confidence: high (about ±3%). The main uncertainty is where the annotator clicked the shoe's centre and possible depth error.
