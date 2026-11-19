# q_3056 — distance between the ground-floor arch pillars (cm)

Prior: middle duck size = 66 cm. 2D internet clip, static camera (facade drift < 1 px in x). One planar scale, as the annotators used.

## Scale (duck_middle bill tip to tail tip)
Read on 5-6x zoomed crops with 5 px ticks (`duckzoom.py`, `frames/duckz_*.png`, `frames/ducks6.png`):
f0 131.5, f5 134, f10 137, f15 142, f20 146, f25 143, f30 144, f35 142, f40 141, f45 139, f51 139 px.
Median is about 140 px. The scene record's mask value of 127 px cuts off the pale tail tip and the bill, so I did not use it.
Scale = 66 / 140 = 0.471 cm/px. The frame-to-frame spread of ±5 px gives about ±4%.

## Pillars (`measure.py`, `cols.py`)
Front ground-floor column shafts: edges from the brightness gradient of a row profile (y 1150-1350), frames 0, 20 and 40.
- Centres: 273, 682.5, 1089.5, 1495.5, 1895.5, 2293, 2696, 3102.5, 3505.5. Centre-to-centre spacing is 404.1 px (adjacent spacings 397-410; (last-first)/8 = 404.1). The value is the same in all three frames.
- Shaft widths are 80-92 px. The clear gap between adjacent shafts is 319.3 px (314-322).

## Answer
- Centre-to-centre spacing: 404.1 x 0.471 = **190 cm**. This is my answer, because it matches the benchmark's convention of measuring distance between reference points.
- Alternative reading, the clear opening between shafts: 319.3 x 0.471 = 150 cm.
- Check: the three frames give the same column spacing. With the duck's length at the ends of its range (131.5 or 146 px), the answer would be 203 or 183 cm.

Confidence: moderate. The scale is good to about ±4%. The main risk is the ambiguity between centre spacing and clear gap.
