# q66 – length of the green car (prior: white car length = 6 m)

2D top-down simulation, fps = question_fps = 24 (time is not needed). One m/px scale comes from the white van
(the "white car"); the parked green sedan is lying horizontally in the lower lane of the horizontal road, x≈336–530, y≈601.

## Measurements (scripts: measure.py, rows.py, vanlen.py, greenlen.py)
- White van, along its vertical axis. Raw columns at f71: the front white edge is at y≈80.5–82. The rear bumper's bright strip
  ends at y≈318, and the dark band at 319–322 plus the fading halo is contact shadow. That gives ≈237 px bumper to bumper.
  A sub-pixel crossing at grey level 195 on 5 columns gives 234–235 at f0, f10 and f70–71. It dips to about 228–230 mid-clip,
  near the image centre (a slight perspective / motion effect). The record's thr25 value is 236 at f0 and f71.
  Adopted: **236 px** (±2).
- Green car, along x. The green body by chroma (G−R>15) spans 336–523 (187 px). The chrome front bumper strip continues to
  about 529.5 (rows 592–610). The rear edge is sharp at about 336.5. Beyond the front, the grey gradient from 530 to 545 is the
  soft shadow (light comes from the upper left, and the van's shadow also falls to +x/+y), so it is excluded.
  Adopted: **193 px** (±3). It is the same at f0, f35 and f71 (the car is static).
- I applied the same convention to both cars: the sharp body plus bumper, with no shadow halo. As a check, the shadow-included
  extents (deviation >12) are green 203 and van ≈244–255. That ratio is 0.80–0.83, which agrees with 193/236 = 0.818.

## Answer
6 m × 193/236 = **4.91 m**. Second route: the level-195 van length of 235 px with the green body plus bumper gives 4.93 m. A
sedan of about 4.9 m next to a 6 m van is plausible.
Confidence: good (about ±3%). The main uncertainty is the faint front bumper of the green car and perspective
(the green car is about 650 px from the image centre, while the van is measured near the top and bottom edges).
