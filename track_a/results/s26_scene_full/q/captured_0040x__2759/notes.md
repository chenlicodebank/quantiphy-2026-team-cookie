# q_2759: diameter of the white cup's rim (cm)

The file fps and question_fps are both 24. The cup does not move, and neither does the camera.

## Depth
depth_info gives "distance_white_cup_camera = 8420m". This is clearly a typo for 0.8420 m. The other objects on the
table are at 0.69-0.97 m, and the cup stands just behind and to the right of the card tent, so 0.842 m fits.

## Measurement (measure.py)
- I thresholded brightness (>140) row by row near the top of the cup, on frames 0, 5, 10, 15 and 20.
- The rim's full width is reached at rows 379-381: x = 740..813, so **74 px**. It is the same in every frame, and the
  rows below are also 74 px. The tumbler is widest at the top, and the zoomed view (frames/cupzoom.png) shows a clean rim.
- Size = depth x px / f = 0.842 x 74 / 763 = 0.0817 m, so **8.17 cm**.

## Second-route check (scale from the prior card)
- The credit card is the navy card lying flat at the front of the table, with a yellow sticky note on it.
- Its long edges measure about 91 px (top) and 97 px (bottom), mean about 94 px, from frames/cardzoom.png.
- At the given 0.69 m this is 94 x 0.69 / 763 = 8.5 cm, against the true 8.56 cm (under 1 % off). This confirms
  f = 763 px and the depth scale.
- Scaling the cup from the card with the depth ratio gives 8.56 / 94 x 74 x 0.842 / 0.69 = 8.2 cm, which agrees.

Answer: 8.17 cm. Confidence is high, about ±3 %. The main uncertainty is ±1 px at the segmentation edge and the
interpretation of the depth typo.
