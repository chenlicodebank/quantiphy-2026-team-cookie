# q_3052 — displacement of credit card from start to 0.73 s (cm)

Prior: width of credit card = 83.98 mm. Internet video, 2D planar convention, one scale factor from the prior.

## Correction to scene/ record
The record's card mask (H<=6 or >=172) includes the hand's skin (skin hue 6-9, S~140-160), so its bbox_x1 and
the "~473 px" card length are too large. With a strict red mask (H<=3 or >=175, S>120, V>150; `track2.py`,
overlays frames/ov0.png, ov18.png, ov22.png) the card's long side in sharp frames 15-27 is 416-419 px (by-eye
edges ~422 px). Zoomed checks (frames/right26.png) show the card's rounded right corners at x≈1355, so the whole
card is visible. Card width ≈ 420 px -> scale = 83.98 mm / 420 px = 0.200 mm/px.
Frame 0 is blurred and the card is yawed (visible width 367 px); I did not use it for the scale.

## Track (track2.py, strict mask), pixels
Centre = ((left+right)/2, (top+bottom)/2); f0 (1485.5, 2613), f18 (1165, 2104), f22 (1149.3, 2068).
Top-left corner: f0 (1302, 2464), f18 (957, 1960), f22 (941, 1924). The camera is static (see scene notes).

## Time base
File fps is 24.406, and question_fps is 30. t = 0.73 s gives frame 18 at 24.4 fps and frame 22 at 30 fps. The card
is pushed by hand and slows to a stop, so neither rate looks implausible (initial speed 28 or 35 cm/s), and I
could not tell which one is right. Hedge: I answer between the two readings.

| route | f0->f18 (24.4 fps) | f0->f22 (30 fps) |
|---|---|---|
| centre | 601.5 px = 12.03 cm | 640.4 px = 12.80 cm |
| top-left corner | 615 px = 12.30 cm | 649.5 px = 12.99 cm |

Answer: 12.5 cm. It is within about 4% of every entry in the table. The centre and corner routes agree within
about 2%. The main uncertainties are the time base (about ±3% after hedging) and which pixel width the annotator
used for the card (if they measured the yawed frame 0, about 367 px, the answer would be about 14% larger).
Confidence: moderate.
