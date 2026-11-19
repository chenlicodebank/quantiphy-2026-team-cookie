# Q1187: height of the moving bicycle (handlebar top to ground), in metres

Prior: the moving bicycle's wheel diameter is 0.65 m. Depth to the bike is 12.6215 m at t=1 s (f33) and 13.2055 m at t=2 s (f66).
The question fps and the file fps are both 33, so frame = round(t*33).

## Measurements
All measurements are in code, using |frame − median background| profiles (`profile.py`, `prof3.py`) and zoomed crops (`crops.py`, `hbcrop*.py`).
The asked object is the dark-blue bicycle ridden by the cyclist. It is not the static pink bicycle.

| frame | front wheel outer L–R (px) | Dh | tyre bottom y | top of gripping hand y |
|---|---|---|---|---|
| 33 | 1177.5–1279.5 | 102 | 600.6 | 448 |
| 40 | 1022.5–1122.5 | 100 | 597.5 | 447 |
| 50 | 806.5–903.5 | 97 | 594.7 | 445 |
| 60 | 595.5–690.5 | 95 | 591.5 | 443.5 |

- The rider's hand covers the handlebar grip. On 14x crops the stem meets the bar about 3 px below the top of the hand, so I take the bar top as hand top + 3 px (uncertainty ±2 px, about ±1.3 cm).
- The tyre bottom is the lower edge of the dark tyre band below the bright rim.

## Geometry (`solve.py`)
- **Camera pitch.** Long verticals in the background are parallel to within 0.01 px/px (`verticals.py`), so pitch ≈ 0. I put the principal point at the image centre.
- **Why a plain pixel ratio fails.** The horizontal wheel width shrinks faster (102→95 px) than the vertical sizes (about 3%, which matches the depth change). The bike recedes at a heading of about 6.7° to the image plane, so its wheel is foreshortened horizontally by a different amount in each frame. A plain pixel ratio would therefore be biased by up to about 3%.
- **Pinhole model.**
  - The bike origin at t=1 s and t=2 s is back-projected with the given depths. This gives the vertical plane of the bike.
  - For each frame, the 0.65 m wheel circle lying in that plane is projected, and the focal length is solved so the projected width matches the measured Dh.
  - The result is f = 1933, 1931, 1922, 1933 px (mean 1930, sd 4). Because the four frames agree, the model explains the shrinking width.
  - The predicted vertical wheel diameter at f33 is 101 px, which matches the hub-to-bottom reading (about 50 px).
- **Height.** The handlebar-top and tyre-bottom pixels are back-projected onto the bike plane, and the height is their vertical separation. With a common f = 1932 px:
  - To the bar top (hand + 3 px): 0.960 (f33), 0.956 (f40), 0.964 (f50), 0.965 (f60). Mean 0.961 m.
  - To the top of the hand (upper bound): 0.976–0.988 m.
- **Second route.** A simple pixel ratio at f33 and f40, where the bike faces the camera best, gives 0.65 × 149.6/102 = 0.953 and 0.65 × 147.5/100 = 0.959. These agree with the pinhole result.

## Answer
0.965 m. This is the bar-top value, nudged slightly toward the hand-top bound because the bar is hidden by the hand.
Confidence: about ±3%. The main uncertainty is where the bar top sits under the hand.
