# Q22: distance between the two black lamps (m)

The prior is the orange car's acceleration, -2.86 m/s^2. depth_info is null. fps = question_fps = 30.

## Lamps
Both black lamp posts stand on the left sidewalk. The camera looks straight down with perspective, so tall parts
lean radially away from the image centre. I measured both posts at their round base disks, which are at ground
level and do not lean (`lamps2.py`: radial edge search plus a circle fit, threshold 75, frame 0):
- middle lamp base: (498.6, 1064.1), r = 22.4 px. Its hexagonal head projects about 98 px to the left.
- bottom lamp base: (499.0, 1907.0), r = 22.9 px. Its pole leans off the bottom-left edge of the frame.
- The two base radii are equal, which confirms the two points are corresponding parts at the same height.
- Pixel distance: **843 px**, almost exactly vertical in the image.

Both lamps are the same model, so their origins are at the same height. The distance between the origins is
therefore this ground distance.

## Scale
I used the orange car's track from scene/ (template-matched centre) and checked it with `accel.py`:
- Fitting a quadratic to y over f50-90 gives -0.344 px/frame^2, which is 309.7 px/s^2.
- Over f30-70 it gives 316.8 px/s^2, and over f17-90 it gives 311.5 px/s^2.
- A linear fit to the per-frame speed gives 309.8 px/s^2.
- I used 311 px/s^2, so the scale is 2.86 / 311 = 0.009196 m/px for the tracked car surfaces.

Plain planar answer: 843 x 0.009196 = **7.75 m**.

## Height correction
The tracked car surfaces (roof, hood, trunk) are about 1 m above the ground, so they are slightly closer to the
camera than the lamp bases.
- The lamp head leans with a factor h/(H-h) of about 0.19, which gives a camera height H of about 6.3 x the head
  height.
- Taking a head height of about 4 to 4.5 m gives H of about 25 to 29 m.
- The ground scale is therefore about 3 to 4 % larger than the scale at car-body height.
- Corrected answer: 7.75 x 1.03 to 1.04 = 7.98 to 8.06 m. I answered **7.95 m**, between the planar and corrected
  values and leaning toward the corrected one.

## Sanity checks
At this scale the lane width is 440 px = 4.05 m and the car length is 556 px = 5.1 m, both plausible.

The confidence is moderate to good. The main uncertainty is the height correction, about ±3 %. The pixel
measurement is accurate to about ±0.5 %.
