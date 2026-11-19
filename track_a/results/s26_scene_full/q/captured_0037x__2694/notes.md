# q_2694 – height of the poker tower (cm)

The "poker tower" is the card tent: two playing cards leaning against each other, left of the white cup. scene.json calls it
`card_tent`. It is static. The file rate and question_fps are both 24.

## Method (lab method card)
f = 0.5959 x 1280 = 763 px. The depth to the poker tower at t = 1.0 s is 0.905 m.
- `measure.py` and `edges.py` take the per-pixel median of frames 0, 3, 6, 24, 30 and 48 (no ball in front of the tent).
- Top ridge: a sub-pixel 50 % crossing from the black background to the card, over columns 678–697, gives row 415.3–416.4
  (I take 415.5).
- Base: the foot of the front card is at row about 500 (around x 711), and the foot of the back card is at about row 495.
  The ridge is roughly midway between the two in depth, so the table point under it is at row about 497.5.
- Vertical pixel extent: 497.5 − 415.5 = 82 px, so height = 0.905 x 82 / 763 = **9.7 cm**.
  Using the full bbox extent instead (415.5 to 500, 84.5 px) gives 10.0 cm.

## Checks
- Ball scale (the prior): 4 cm at 1.055 m should appear as 28.9 px. At frames 23–24 the ball measures 29–31 px (bbox height
  30 px), which is consistent within about 3 %.
- Credit card (dark card near the front edge, 0.679 m): about 105 px long, which gives 9.3 cm against a real 8.56 cm.
  The depth scale may therefore read up to about 9 % high on some objects.
- Physical sanity check: standard poker cards are 8.9 cm long, so a leaning tent should be at most about 8.9 cm tall. This
  suggests the true value may be somewhat lower (about 8.5–9 cm). I kept the method-card value, using the mid-base reading
  (9.7) rather than the full-bbox reading (10.0).

Confidence: moderate. The plausible range is 8.5–10 cm.
