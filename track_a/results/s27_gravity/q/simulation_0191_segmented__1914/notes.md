# q1914: height of the box (m)

Prior: box acceleration before 0.6 s = 9.8 m/s² (free fall). There is no depth_info. question_fps = file fps = 120.

## Scale (pixel acceleration of the box)
The box falls straight down from rest at frame 0 and hits the truck roof at frame 60. It does not rotate, and its front face keeps a constant 410 px x ~190 px, so it stays at a constant depth. Pixel motion was therefore converted with one scale at the depth of the front face.
- **Route 1 (measure4.py):** subpixel template tracking of the front-face texture, fitted with y = y0 + ½a(t−t0)² over f0-58.
  - Pictogram patch: a = 1977 px/s² (t0 = −0.001 s, rms 0.06 px). Over f10-58 it gives 1973; over f0-45, 1983.
  - Stain patches: 1980-1984.
- **Route 2 (measure3.py):** the front face's bottom-left corner edge gives 1954-1966.
  - The face's top edge is wavy and clipped before f24 (t0 has to be extrapolated), so it is less reliable: 1883.
  - The scene/ track's integer edges give 1952-1994.
- **Adopted:** a = 1977 px/s², so the scale is 9.8/1977 = 0.004957 m/px. Routes 1 and 2 agree within about 1%.
- **Plausibility check:** the truck's cargo box is about 1330 px (6.6 m) long and 433 px (2.15 m) high, and the wheel radius is about 89 px (0.44 m). This is a realistic catering truck, so the scale is consistent.

## Box height in pixels (measure5.py, rest frames 100-160 averaged)
- The front face's top edge is wavy: 214-217 px. The front bottom edge is at about 405.5. Below it is a 3-4 px underside strip seen in perspective (silhouette bottom 409.2).
- **Body height:** about 191.5 px, which gives **0.949 m**. The face height is ~190 px in every frame during the fall (scene track).
- **With the flap:** a dark lid flap at the top-right (x 830-935) rises to y = 199. The extent including it is about 206.5 px, which gives **1.024 m**. The flap sits on the top face, deeper than the front face, so its true height would be slightly larger still.

## Answer
The world AABB may or may not include the ajar flap. I answer between the two readings: 0.99 m. That is within about 4% of both 0.949 and about 1.03.

Confidence: the scale is good to about 1%. The main uncertainty is the flap ambiguity (±4%).
