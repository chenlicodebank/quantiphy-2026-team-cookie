# q3201 – longer side of the wallet (cm)

Prior: g = 9.8 m/s^2. 2D clip (rotated 90 deg, gravity = image +x), static camera, 30 fps (file = question fps).

## Scale from gravity (measure.py)
Dark-pixel mask (V < 70, wall region x < 1430) of the wallet, centroid per frame. Free fall frames 67-80
(release at 66). Quadratic fits of cx(frame):
- 67-80: 11.76 px/frame^2; 67-76: 11.73; 68-79: 11.68; 70-80: 11.80. Median second difference 11.86.
- Adopted a = 11.75 px/frame^2 = 10575 px/s^2 -> scale = 9.8 / 10575 = 9.27e-4 m/px.

## Wallet long side
Min-area rectangle of the mask on clean held frames 0-17, 49-65: 246.0-246.8 px (short side 155 px);
overlay frames/ov6.png shows the rect hugging the wallet. Early flight frames 67-68 give 246.5 px too.
Long side = 246.3 px x 9.27e-4 m/px = 0.228 m = **22.8 cm** (short side 14.4 cm).

## Check
Range of acceleration fits (11.68-11.86) gives 22.5-22.9 cm. Bbox extent along the fall direction
(~259 px, tilted) would give 24.0 cm, but that is not the side length. 22.8 cm is plausible for a
zip pouch/wallet. Confidence: good (~3%).
