# q_2954 — wine glass diameter (cm), prior: money width = 7.5 cm

Internet (segmented) top-down clip; static objects, so fps (24 vs question_fps 30) is irrelevant. Frame 0 used
(camera drift is <1 % in scale, irrelevant for a size ratio).

## Scale (money width)
Monopoly notes at right (frames/money4.png, money.py, money2.py). "Width" taken as the note's short side
(real notes are ~2:1; 7.5 cm only fits the short side; with that scale the pizza is ~50 cm, the glass ~15 cm, which is
consistent with the scale implied by real Monopoly note length ~13.5 cm — the long-side reading would need a 7.5 x 3.5 cm note).
- top 500 note: short side 69-72 px (yellow mask y 194/196 -> 265-267 at x 876-903), long side ~146 px (874 -> ~1020).
- rotated 500 note: short sides ~65 (left) and ~70 px (right), long ~137-144 px.
- adopted short side = 69 px -> 0.1087 cm/px.

## Glass
Non-white connected mask of the glass (glass.py, frames/glassmask.png): bbox (129,89)-(326,304), long axis at 52 deg.
The bowl/rim silhouette is an ellipse elongated along the tilt axis; its widest extent perpendicular to the axis
(= rim/bowl diameter, unforeshortened direction) = 135 px. (Horizontal row width max 147, vertical 152 — these include
the oblique bowl side, not used.)

## Answer
135 px x 7.5/69 = 14.7 cm.
Check: rotated-note scale (67.5 px) -> 15.0 cm; top-note 72 px -> 14.1 cm. Range 14.1-15.0.
If the annotator meant the note's long side (146 px) the answer would be ~6.9 cm, or if they used the horizontal bowl
width 147 px, ~16 cm. Confidence: moderate (main risk is the interpretation of "width").
