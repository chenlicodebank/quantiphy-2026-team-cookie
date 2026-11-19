# q_2970 — middle fingertip speed at 0.4 s (cm/s)

Time base: file fps 30.0003 = question_fps 30, so t = 0.4 s is frame 12. Duplicate frames are 9 and 15 (pulldown), so
12 and 13 are both real frames.

## Fingertip (tips.py, zoom.py, overlay.py)
Right hand, palm down, thumb tucked on the left, so of the two extended fingers the right one is the middle finger.
The pale nail fails a plain skin threshold, so I located the tip from mask code (R-B > -8 and not white) and then
checked it by eye on 16x zoomed crops, using the white segmentation halo as the edge:
- f11 ≈ (1002, 330), f12 ≈ (988.5, 314) (motion-blurred), f13 ≈ (979, 303.5), f14 ≈ (975, 300)
- Forward difference 12→13 (the internet annotation convention): about 14 px per frame (13.4–14.5 depending on the edge
  definition), which gives about 420 px/s.
- The backward difference (11→12) would be 22.7 px and the central difference 18 px, because the finger is slowing
  sharply as it reaches out. I followed the forward-difference convention.
- Check: the index fingertip moves 11.1 px over 12→13 and the hand centroid 10.6 px, which agrees.

## Scale: the credit card is not visible
The prior's credit card was removed by the segmentation: the left hand pinches something, but no card pixels are left.
So I estimated the scale from the keyboard, an Apple Wireless Keyboard (A1314, with the battery tube at the back):
- Footprint 363 x 167 px (scene record; aspect 2.17 matches the real 27.9 x 13.1 cm). 27.9 / 363 = 0.0769 cm/px.
- Key pitch from autocorrelation along the rows (keypitch.py): 24.15 px. A standard 19.05 mm pitch gives 0.0789 cm/px.
- Used 0.0775 cm/px, so a 5.4 cm card would be about 70 px wide.

## Answer
14 px × 30 /s × 0.0775 cm/px ≈ 32.5 cm/s (range from the two scales: 32.3–33.1).

Confidence: moderate. The scale is not tied to the prior, since the card can't be seen. The finite-difference choice
matters a lot: the backward difference would give about 53 cm/s.
