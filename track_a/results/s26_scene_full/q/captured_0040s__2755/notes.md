# q_2755 – height of the white cup (cm)

- Lab clip, 1280x720, 24 fps (file fps = question_fps = 24). Static camera; cup never moves.
- depth_info gives the cup distance as "8420m", an obvious typo; it is read as 0.8420 m. That fits the scene:
  the card is at 0.69, the cup at 0.842 and the poker tower at 0.91, and the cup's base sits at about the same table depth as the card tent.
- Focal length f = 0.5959 x 1280 = 762.8 px (lab method card).
- Pixel height (measure_cup.py): a mask of low-saturation, bright pixels around the cup, checked on frames 0/10/20/46/48 (identical).
  Bbox y 376–503 gives 127 px; central-column median 126 px. The luminance edges in column 777 are about 375.5 (back rim top)
  and 503.5 (front bottom), so 128 px for the outer silhouette. The front rim is about 379, so front rim to bottom is about 125 px.
- Height = 0.842 x 127 / 762.8 = 0.140 m. The range over the readings above (125–128 px) is 13.8–14.1 cm.
- Check: with Z = 0.842 the cup's base row gives a camera height above the table close to the one from the tent base
  (Z = 0.91), which supports reading the depth as 0.842 m. As a scale check, the credit card prior (85.6 mm) reads
  about 9.5 cm from its horizontal extent of 105 px. That is about 11 % high, probably because the card lies flat and
  slightly rotated, so it is not a clean reference.
- Answer: 14.0 cm. Confidence: moderate-high (the main uncertainty is the depth typo and the rim edge).
