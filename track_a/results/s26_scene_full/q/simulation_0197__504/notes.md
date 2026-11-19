# q_504 — bubble speed at t = 1 s (frame 30)

Time base: fps = question_fps = 30, so t = 1 s is frame 30. The camera is static. The scene is 2D (bubble in a pipette in a plane facing the camera), so I used one metres-per-pixel scale.

## Scale (prior: horizontal width of the "skynova" text = 0.00188 m)
- The brand text runs vertically on the bottle's left side. Only "NOVA" is visible; "SKY" is cut off below the frame. The text's horizontal extent in the image is the letter height.
- `measure.py` masks the white letters (min RGB > 175, low saturation) in x 1050–1260, y 2020–2560. Each of the 4 letters is 78 px wide. The overall column is 80 px wide (x 1106–1185), the extra 2 px coming from the slant. The values are identical at frames 0, 30 and 49. I used 79 px.
- Scale = 0.00188 / 79 = 2.38e-5 m/px.

## Bubble motion
- I used the centroid track in scene/tracks/bubble.csv (checked: it follows the single moving bubble), projected onto the motion axis (−0.855, 0.519).
- The raw backward step 29→30 is 11.1 px. Steps from 26 to 34 vary between 11.1 and 14.1 px because the centroid jitters by about ±1 px.
- `fit.py`: polynomial fits (degree 1–3, windows 22–38 / 24–36 / 25–35 / 26–34) give a velocity of 11.9–12.4 px/frame at frame 29.5. Chords give 12.33 (frames 28→31) and 12.16 (27→33). Adopted: 12.25 px/frame = 367.5 px/s.
- Speed = 367.5 × 2.38e-5 = 0.00875 m/s (0.0086–0.0089 m/s for a text width of 78–80 px).

## Second route
- The independent chord estimates (12.2–12.3 px/frame) agree with the fits.
- Sanity check: with this scale the bubble is about 103 px ≈ 2.5 mm across and the pipette about 3.4 mm wide. Both are plausible for a scene not modelled at real-world scale.

## Answer
0.0087 m/s. Confidence: moderate. The main risk is how the annotator read "horizontal width" of the text: if they meant the full reading-direction length of "skynova", the scale would be very different. The image-horizontal letter height is the only horizontal width that can be measured here.
