# Q2023 – diameter of the wine glass (cm); prior: Monopoly money width = 7.5 cm

Internet video, near top-down static objects (glass and bills do not move; the camera only drifts slightly, and
the sizes are measured on frame 0). The question asks for a size, so the fps / question_fps difference does not matter.
Following the annotation convention, one planar scale comes from the prior: no perspective correction.

## Scale (prior object)
- "Width" of a bill lying flat = its shorter side (a long side of 7.5 cm would make the short side about 3.4 cm, which is implausible).
- Top (upside-down) 500 bill, frame 0, RGB column profiles (prof2.py): the top edge against the white board is at y≈419
  and the bottom edge against the wood is at y≈571 (x=1900), giving a **short side of 152 px** (the bill is rotated about 3°).
  The left edge is at x≈1864 and the right edge at about 2178, giving a long side of about 314 px (ratio 2.07).
- Second route: the rotated middle 500 bill's corners give a short side of about 153–155 px (bill_mid.png).
- Scale = 7.5 / 152 = 0.0493 cm/px.

## Glass
I read rim and silhouette points on CLAHE-enhanced zooms (glass_enh_0.png, g_ll.png, g_ur.png) and fitted them in
glassfit.py. The overlay in frames/glassfit.png shows a good ellipse fit.
- Rim ellipse: major axis **258 px**, which is the unforeshortened rim diameter (minor axis 222 px from the tilt).
- Widest bowl silhouette perpendicular to the glass axis: **277 px**.
- Horizontal bounding width of the bowl: 324 px. This is not a diameter, because the glass is seen obliquely along a diagonal axis.
- Answer: the mean of the rim and bowl readings, 267 px × 0.0493 = **13.2 cm**.
  The readings correspond to 12.7 cm (rim), 13.7 cm (bowl) and 16.0 cm (horizontal).

Confidence: medium. The scale is solid (±2%). Which glass width the annotator drew is the main uncertainty (about ±4%
between rim and bowl).
