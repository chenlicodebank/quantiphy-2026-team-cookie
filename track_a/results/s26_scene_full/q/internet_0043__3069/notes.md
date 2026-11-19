# q_3069 - height of the green bottle (cm)

Prior: velocity of the white ball at 1.0 s = 33.38 cm/s. The "white ball" is the white egg rolling right to left
(the only moving object). fps = question_fps = 30, so t = 1.0 s is frame 30. The camera is static apart from <0.3 px/frame drift.

## Scale (one planar scale, internet convention)
Egg reference point (scene/tracks/egg.csv, drift-corrected ref_x). I checked the record against frame 30:
- forward difference f30->f31: 44.8 px/frame; backward 45.8; centred 5-frame 45.06; 7-frame 45.0.
- I used about 44.9 px/frame = 1347 px/s, so scale = 33.38 / 1347 = 0.02478 cm/px.

## Bottle pixel height (measure.py, frame 30, column profiles at x = 855/862/870)
- Top (mouth rim against the black monitor): the bright rim starts at y = 255.5.
- Bottom (dark glass base against the light desk): the transition is at y = 773.5.
- Height = 518 px. This agrees with the scene record's 519 px bbox height (frame 0).

## Answer
518 px x 0.02478 = 12.84 cm. Using the forward difference only (44.8): 12.87; using 45.06: 12.80. Answer **12.85 cm**.

## Check / caveats
- Second route: the 519 px bbox from the record gives 12.86 cm, which agrees.
- Sanity: at this scale the egg (~79 px) would be about 2 cm, and a real wine bottle is about 30 cm. So the prior's
  scale is about 2.5x smaller than real-world scale. The benchmark says the prior is exact and sets the scale, so the
  prior-derived value is the answer. If real-world scale were wanted, it would be about 30-35 cm.
- Confidence: high that I reproduced the convention (±2%). The main risk is the prior's own scale.
