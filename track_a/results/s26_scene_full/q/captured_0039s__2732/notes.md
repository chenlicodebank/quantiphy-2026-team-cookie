# q_2732: distance between the white cup and the pink bottle (cm)

Lab video, 24 fps (the file rate and question_fps match). The camera is static and both objects stay still, so I used frame 48, where the ball is gone.

## Method (lab method card)
- Focal length f = 0.5959 x 1280 = 762.8 px; principal point (640, 360).
- Centres are bbox centres, measured in code against the green background (`measure.py`) and checked on a gridded crop (`frames/crop.png`):
  - Pink bottle: x 642-689, y 331 to about 478 (the base is read from the crop; the cards hide part of it). Centre (666, 404.5).
  - White cup: x 726-791, y 376-496. Centre (759-760, 436.5-437).
- Back-projection: direction ((u-cx)/f, (v-cy)/f, 1) normalised, then multiplied by the given Euclidean depth (bottle 0.9998 m, cup 0.8740 m).
  - Bottle at (0.034, 0.058, 0.998) m; cup at (0.135, 0.086, 0.859) m.
- 3D distance: 17.37 cm, and 17.32 cm with the alternative centre pixels. **Answer: 17.35 cm.**

## Checks
- Moving either centre by ±3 px changes the result by about ±0.3 cm. The answer depends mostly on the given depth difference of 12.6 cm. The cup's base sits lower in the image (y 496 against about 478 for the bottle), so the cup is nearer the camera, which agrees with the depths.
- Size sanity check: bottle width 47 px x 1.0 / 763 = 6.2 cm; cup rim 65-71 px x 0.874 / 763 = 7.5-8.1 cm. Both are plausible.
- The prior object (the black card at 0.6867 m) is 101 px long, which gives about 9.1 cm against the true 8.56 cm. The card is seen obliquely, so this matches the scale to within about 6%.

Confidence: moderate to high, about ±1 cm.
