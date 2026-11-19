# q3025 – size of the baguette (cm), prior: fork = 20.3 cm

Static size question, so time base doesn't matter (file 19.29 fps vs question 25 fps is irrelevant here).
Internet-video convention: one scale = 20.3 cm / fork pixel length, no perspective correction.

## Fork (prior object)
Most forks are held in hands. The only fork lying fully visible is the one on the rim of the
top-right green-pasta plate (pink-blazer diner), frame 0. Endpoints checked on cubic-upsampled crops (`mark.py`,
`frames/fk.png`) and with an HSV profile along the axis (`measure.py`: the handle end shows up as a saturation jump at s≈143 px):
tine tips ≈ (1723.7, 293.7), handle end ≈ (1832, 206.5) → **139 px** (±2-3 px; tine tips are slightly blurred).
Scale = 20.3 / 139 = 0.146 cm/px.

## Baguette
There are three loaves on the board (frame 0, `frames/bg.png`):
- sesame baguette (on top, darkest): ends (1007, 712) to (767, 940) → ~333 px → **48.6 cm**
- plain baguette on the left (fully visible, longest): (1025, 692) to (714, 947) → ~402 px → **58.7 cm**
- plain baguette on the right (partly under the sesame one): (1050, 747) to (765, 990) → ~374 px → **54.6 cm**

The scene record (scene/scene.json) gives only the sesame loaf, at 332 px, and my measurement agrees with it.

## Answer
"The baguette" doesn't say which loaf is meant. The sesame loaf is the one on top, but the plain loaves are the
classic baguettes, and a real baguette is about 55-65 cm long. To keep the relative error under about 10 % for any
of the three readings, I answer **53 cm**, which sits between them.
Confidence: the scale is solid (±2 %); which loaf is meant is the main uncertainty.
