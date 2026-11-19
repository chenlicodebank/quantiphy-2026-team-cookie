# q_2733: height of the pink bottle (cm)

Method (lab method card): f = 0.5959 x 1280 = 762.75 px. Height = depth x pixel height / f, with
distance_pink_bottle_camera = 0.9998 m (depth_info). File fps = question fps = 24.

Pixel measurement (measure.py, measure2.py; frames 0, 10 and 48; the bottle is static):
- Top: the R-G profile on columns 652-660 changes from green background to pink at y = 330.5 (the same in all three frames).
- Bottom: the brightness profiles on the unoccluded left side (x = 646-655) drop from about 170 (pink) to a dark contact
  shadow at y ≈ 476.5-477.5. The playing cards hide the centre of the bottom.
- Pixel height is about 146-147 px. scene.json gives 146 px (331-477), which agrees.
- Height = 0.9998 x 146.5 / 762.75 = 0.1920 m, so **19.2 cm**.

Check: the black card with the yellow sticker (credit card, 0.6867 m) is about 101 px long in scene.json, which gives
9.1 cm against the prior's 8.56 cm (+6%). The bbox is rough and the card sits at an angle, but this confirms the scale
is the right order. A 19 cm small thermos is plausible.
Confidence: good (±3%). The main uncertainty is where the bottom edge sits behind the shadow, about ±1.5 px.
