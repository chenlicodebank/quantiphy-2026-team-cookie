# q 2123 – mug diameter (cm); prior: earphone case width = 45 mm

Internet video, static overhead camera, so I used the annotators' convention: one planar scale from the prior.

## Scale (earphone case, frame 29, static)
- The white AirPods-style case lies flat and is rotated about 30°. The lid seam runs along the width direction (~29° below
  the horizontal in the image); the port end points to the lower left.
- `case_profile.py` / `case_profile2.py` take saturation profiles across the case through its centre. Width (across,
  along 29°/35°) at half-contrast is 188–192 px over 13 parallel lines, so I used **191 px**. Length (lid to port, including
  the visible lower wall) is about 221 px. The ratio of 1.15 is close to the real case's 53.5/44.3 = 1.21.
- Scale = 45 mm / 191 px = 0.2356 mm/px.
- The record's `approx_side_lengths_px` [245, 205] is a rough bbox that includes the shading and side wall, so I didn't use it.

## Mug (frame 0, at rest, fully visible)
- `mug_rim.py` casts rays out from the coffee centre and takes the outer edge of the white rim against the wood or side wall
  (overlay in frames/mug_fit.png; the points sit on the rim).
- Circle fit: diameter 418 px (this matches the record's 417).
- Ellipse fit: 391 × 448 px, mean 419.
- Horizontal extent: 437 px (3039–3476). Vertical extent: 403 px. The widest chord is 448 px.
- An annotator drawing a diameter across the opening would most likely get a horizontal or longest chord, about
  437–448 px. The mean or circle-fit value is 418 px.

## Answer
- 437 px × 0.2356 mm/px = **10.3 cm**.
- Alternatives: 9.85 cm (418 px, circle or mean) and 10.55 cm (448 px, major axis). Both are within 5% of 10.3.
- If the case width had been measured as the 205 px bbox, the answer would be 9.6 cm.
- Second route: the circle-fit and ellipse-mean diameters agree (418 vs 419 px), and every chord estimate falls within
  ±5% of the answer.
- Sanity check: the rim is about 10 cm above the desk, nearer the camera, so it looks a little larger than a real mug of
  about 9 cm. The planar convention ignores this.
- Confidence: moderate. The main uncertainty is which pixel line the annotators used for the case width and the mug diameter.
