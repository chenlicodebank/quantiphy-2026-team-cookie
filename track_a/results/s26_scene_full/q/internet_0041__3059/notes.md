# q3059 - height of the second-floor arches (cm)

Prior: middle duck size = 66 cm, read as its length bill to tail. This is an internet video, so I use one planar scale from the prior.
The camera is static (drift of 1 px or less); this question is about sizes only, so the timing does not matter.

## Duck length (prior object), pixels
The scene/ mask lengths (116 to 130 px) cut off the pale tail tip, which sits on a pale reflection. I read the bill tip
and tail tip on zoomed crops (duck_*.png, d2_*.png):
- frame 0: 132 px (bill tucked in, head drawn back)
- frame 12: about 139.5
- frame 24: about 144
- frame 36: about 143
- frame 51: about 139

I use 140 px, which gives a scale of 66 / 140 = 0.471 cm/px.

## Arch height, pixels (measure.py, profile.py, frame 24)
I took vertical grey-level profiles down the centre line of 9 upper-floor arches.
- The outer edge of the archivolt is at y ≈ 241 to 248.
- The inner apex of the opening (intrados) is at y ≈ 273 to 274.
- The sill, where the column bases stand on the balustrade handrail, is at y ≈ 578 to 585.

Over all 9 arches, the outer-edge-to-sill height is 336 to 338 px, which is very consistent. The ring is 26 px thick,
so the opening (intrados apex to sill) is about 310 px.

## Answer
Opening height: 310 × 0.471 = **146 cm**. This is the answer.

Other readings:
- Outer arch, including the stone ring: 337 px → 159 cm.
- Using the scene/ mask length of 130 px for the duck: 157 cm for the opening.

## Check
- All 9 arches agree to within ±1 px.
- The duck length is consistent across 4 frames (139 to 144 px).

The main uncertainty is which arch extent the annotator measured (opening or ring) and the duck's pixel length.
Note that the ducks are much closer to the camera than the facade, so the real arches are bigger than this. The
answer follows the benchmark's single-scale rule.
