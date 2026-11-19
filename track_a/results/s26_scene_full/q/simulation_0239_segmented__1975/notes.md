# q_1975 — average speed of the white horse

- 2D clip, 24 fps (file and question rates agree). Prior: brown horse speed = 0.874 m/s. A single m/px scale comes from the brown horse's pixel speed.
- White horse = the cream animal (lower, row ~865). Brown horse = upper animal (row ~776). I checked both on frame 24.
- Pixel speeds come from the scene tracks (measure.py). For the brown horse I used frames 0-48, because frame 49 is a reset artifact.
  - Brown: net centroid 2.555 px/f, linear fit 2.667, bbox nose 2.646 px/f, mean step 2.563. I used about 2.62 px/f.
  - Cream: net 4.546 px/f, fit 4.616, nose 4.612/4.658, mean step 4.582. I used about 4.60 px/f.
- Ratio 4.60/2.62 = 1.756, so the speed is 0.874 x 1.756 = 1.535 m/s.
- Second route: the nose (bbox x1) speeds give 4.635/2.647 = 1.751, which is 1.530 m/s and agrees.
- Caveat: the cream animal looks about 19% larger. That could mean it is closer to the camera, which would make its true speed lower, perhaps about 1.29 m/s. The image shows no clear depth cue, so I kept the 2D single-scale convention.
- Confidence: moderate to high, with about ±3% from the measurement plus the depth ambiguity.
