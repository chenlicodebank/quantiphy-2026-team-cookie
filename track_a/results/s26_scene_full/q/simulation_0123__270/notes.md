# q_270: width of the largest of the three stacked towels (m)

The prior is "speed of the cup = 0.338 m/s". The only moving object is the teal object that slides along +x under the left basin. The record calls it `teal_box`; it is the "cup". The round teal cup in the centre does not move, so the prior cannot refer to it. The file fps and question_fps are both 24.

## Scale (2D top-down view)
- `cup.py` tracks the teal object with my own HSV mask, frames 0–71.
- Fitted pixel speed: 14.537 px/frame (median step 14.557), which is 348.9 px/s. This agrees with the record (14.538).
- Scale = 0.338 / 348.9 = 9.688e-4 m/px.
- Sanity check: the cup's top face is 78 × 44 px, which is 7.6 × 4.3 cm. That is plausible.

## Towel
- `towel2.py` rotates frame 0 by 25° about (911, 199), which makes the towel stack axis-aligned (see `frames/towel_rot.png`).
- It then takes Sobel gradient profiles across the bottom (largest) towel:
  - long-side edges at x = -187 and +186, so 373 px
  - short-side edges at y = -92/-93 and +93, so about 186 px
- The other two towels sit inside the bottom towel's outline (checked visually, not measured), so the bottom one is the largest.
- Largest towel:
  - width (the shorter horizontal side) = 186 px × 9.688e-4 = **0.180 m**
  - length = 373 px, which is 0.361 m

## Other reading
The towel is rotated 25° in the image. If "width" meant the shorter extent of a world-axis-aligned bounding box, the answer would be about 326 px, i.e. 0.316 m. I answer with the towel's own side, 0.180 m, following the named-size convention (width = the shorter extent across the object).

## Check
- The scale comes from the same tracked speed by two estimates (linear fit and median step), which agree within 0.15%. The record agrees too.
- Towel edges: corners clicked by eye on the unrotated crop gave short sides of 179 and 187 px and long sides of 362 and 363 px. These match the code measurement within a few px.

## Confidence
Moderate to high for the side-length reading, about ±4%. Possible errors: the towel's thickness and the camera's perspective (the cup and the towel sit at slightly different heights), and the AABB ambiguity above.
