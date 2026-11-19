# q_603: lampshade diameter (simulation_0215)

The prior is "speed of the black cat = 0.94 m/s". The scene record calls the animal a "black dog", but it is the
only animal and the only moving object, so it is the cat. The camera looks straight down, and fps = question_fps = 24.

## Scale from the prior
The cat walks at a constant speed (record track `scene/tracks/dog.csv`, rechecked in `measure.py`). Linear fits
give 10.991 px/frame for torso_cx, 10.997 for mask_cx and 10.995 for nose_x, which is 263.9 px/s.
Scale = 0.94 / 263.9 = 0.003562 m/px.

## Lampshade (`profile.py`, frame 0, outline drawn in frames/lamp_mask.png)
- Mask: grey > 140 and low saturation. Bbox 148 x 146 px. Pleat-tip diameter (median over 72 angles) 148.3 px.
  Valley (inner pleat) diameter 142 px. Min enclosing circle 150 px. Centre (1191, 224).
- Second route: the raw grey profiles through the centre give the edges at x 1116–1266 and y 149–299, about 150 px.
- Using 148 px with no perspective correction gives 148 x 0.003562 = 0.527 m.

## Perspective correction
The shade sits on the console, roughly 0.8 m up at this scale. The cat's visible back is about 0.25 m up.
I estimated the camera height two ways:
1. A standard 50 mm / 36 mm camera (HFOV 39.6°) over a half-width of 3.42 m on the floor gives H ≈ 9.5 m.
2. The top opening of the shade is shifted 11.7 px outward along the radial direction from the rim centre, 391 px
   from the image centre. With a shade height of 0.25–0.35 m, this gives H ≈ 9–12 m, which agrees with route 1.

The magnification ratio is (H − 0.25) / (H − 0.8) ≈ 1.04–1.07, so the corrected value is about 0.49–0.51 m.

## Answer
0.505 m. This lies between the uncorrected 0.527 m and the perspective-corrected value of about 0.495 m.
Confidence: moderate, within about ±5%. The main uncertainty is the size of the perspective correction.
