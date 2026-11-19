# q_2688 – height of the poker tower (cm)

Object: the two playing cards leaned into an A-frame (tent), left of the white cup (scene.json `card_pyramid`).
It stands on the table just behind the flat cards. It does not stand on them: its feet end above the flat cards' far edge at y~500.
Camera is static. The file's fps and question_fps are both 24, so t = 1.0 s is frame 24.

Method (lab method card): f = 0.5959 x 1280 = 763 px; size = depth x pixel extent / f, with depth = 0.905 m (depth_info).
Measured in `measure.py` with column profiles on frame 24:
- top of the ridge: green -> white card transition at y = 415.5 (same over x 676-694)
- feet: left card foot y ~494, right (front) card foot y ~497.5; base under the apex ~496
- pixel height ~80.5 px (+-1.5) -> 0.905 x 80.5 / 763 = 0.0955 m = 9.5 cm
Crop check: frames/card2.png. Frames 0 and 48 are the same in this region (static).

Second-route / scale check: the ping-pong ball at t = 1.0 (frame 24) is ~27.7 px (scene record), and 1.055 x 27.7 / 763 = 3.83 cm,
close to the 4 cm prior, so the depth+f scale holds (pixel sizes might run ~4 % small). Other objects come out plausible:
cup 128 px at 0.845 m = 14.2 cm, jar height 76 px at 1.008 m = 10.0 cm.
Caveat: the card's long side measures ~86 px (~10 cm), which is more than a standard 8.9 cm poker card. So either the cards
are larger, or the true height is a little lower (about 8.5-9 cm).
Answer: 9.5 cm. Confidence: moderate (about +-7 %).
