# q_3041: length of the Apple Magic Mouse (cm)

Prior: the mouse is 5.71 cm wide. This is a static top-down view, so a single planar scale applies (internet convention), and the time base does not matter.

## Method (measure_mouse.py)
- I used frames 5-14, where the hand no longer covers the mouse. The mouse is the white rounded rectangle at bbox (972, 414)-(1040, 547) and lies vertically in the image.
- I set a half-max threshold between the desk and the mouse in grayscale and found sub-pixel edge crossings. Length is the maximum extent of the columns near the centre; width is the maximum extent of the rows.
- Length = 133.79 px and width = 68.72 px, with a spread across frames of under 0.1 px.
- Scale = 5.71 / 68.72 cm/px, so length = 5.71 × 133.79 / 68.72 = **11.12 cm**.

## Check
- The scene record's integer bbox gives 134 / 69 px, which comes to 11.09 cm and agrees.
- Real-world check: the actual Magic Mouse is about 11.35 × 5.71 cm, so this is within about 2%.

Confidence: high.
