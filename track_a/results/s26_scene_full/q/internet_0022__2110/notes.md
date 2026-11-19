# Q2110 – shoulder width of the man (cm)

Prior: mouse width = 57 mm. Internet video, static overhead camera; single planar scale (annotator convention).
Time base irrelevant (static size question).

## Scale
`measure.py`: white-blob mask of the mouse on frame 0, PCA / minAreaRect.
Width (short axis) = 103.4 px (minAreaRect 102.5 x 197.8; matches scene record 102.9 x 198.1).
Scale = 57 / 103.4 = 0.551 mm/px. Check: length 198.8 px -> 110 mm, which is close to a real Magic Mouse (113.5 mm), so the scale is consistent.

## Shoulder width
Dark suit mask (V<120, above the desk edge at y≈790, largest blob), with the outline checked on the overlay frames/body26.png.
Width profile by image row:
- frame 26: y=380..440 -> 869, 884, 904, 919 px (shoulder corners: the outline turns from the sloped top of the shoulder into the arm)
- frame 35: y=400..460 -> 861, 881, 891, 903 px
Lower down, the width keeps growing to about 1120–1200 px. That extra width is the upper arms, which slope out and forward
because he leans on the desk, so it is not counted as shoulder width.
Shoulder width ≈ 900 px (frames 26 and 35 agree within about 2%) -> 900 x 0.551 = 49.6 cm; answer 49.8 cm (scale 57/103).

Alternative reading: the full outer suit extent, arms included (~1120 px), would give ~62 cm. This was rejected because it is not the shoulders.
The man is nearer the camera than the desk, so in reality his shoulders are narrower (~45 cm), but the planar convention ignores this.
Confidence: moderate (the choice of shoulder point gives about ±5%).
