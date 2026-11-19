# q3044 – spacebar length (cm)

Prior: Apple Magic Mouse width = 5.71 cm. The video is an internet clip shot top-down with a static camera, so I used one planar scale. Timing does not matter for a size question (fps 18.48 vs question_fps 26).

Measurements (measure.py, threshold crossings with subpixel interpolation):
- Mouse width: the horizontal extent of the white blob in frames 4-14, after the hand has left it. The subpixel width is 67.4-68.8 px and the integer bbox width is 69-70 px. I used 68.5 px. The record's 69 px agrees.
- Spacebar: the dark keycap run in the bottom key row at y 381-397, frames 0-2, before the hands cover it. Its left-to-right extent is x 585-692, which gives 108.1 px (it is stable across rows and frames).
- Scale = 5.71 / 68.5 = 0.0834 cm/px, so the spacebar is 108.1 x 0.0834 = **9.0 cm**. Using 69-70 px for the mouse instead gives 8.8-8.95 cm.

Check: the same scale gives a mouse length of 134 px -> 11.2 cm (the real mouse is 11.35 cm) and a laptop base of 427 px -> 35.6 cm (a 15" MacBook Pro is 35.9 cm), so the scale holds up. The mouse and the laptop are at about the same depth (both lie on the desk). Confidence: good, about ±3%.
