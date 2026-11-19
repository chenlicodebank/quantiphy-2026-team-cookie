# Q2763 — height of the white cup (cm)

File fps = question_fps = 24. The cup does not move (frames 0, 10, 20, 47 and 48 give the same box).
depth_info says the cup is "8420m" away. That is clearly a typo for 0.8420 m: it fits the scene, since the cup stands
behind the credit card (0.69 m) and in front of the poker tower (0.91 m) and tape (0.973 m).

## Measurement (measure.py, prof.py)
- Mask of bright, low-saturation pixels gives the box [740, 378, 813, 501].
- Column profiles at x = 760 / 777 / 795:
  - The silhouette top (back rim of the opening) is at y ≈ 375.5.
  - The dark rim line at 378-380 is the front rim of the opening, so the top ellipse is very thin: the camera is almost level with the cup top.
  - The cup's bottom front edge is at y ≈ 503-503.5. The dark contact line is at 504.
- Pixel heights:
  - Full silhouette: about 127.5 px.
  - Front rim to front bottom: about 123.5 px.
- f = 0.5959 × 1280 = 763 px, D = 0.842 m.
  - Front silhouette: 123.5 × 0.842 / 763 = **13.63 cm**.
  - Full silhouette: 14.07 cm.
  - If the given distance is to the cup's axis, the front surface is ~3.5 cm closer, which would give ~13.1 cm.
- Answer: 13.6 cm (the front-silhouette value, in the middle of the 13.1-14.1 range).

## Check of the scale (card.py)
- The credit card is the navy card with the yellow sticky note. Its edge in the image is ~95 px long (a slanted parallelogram, x ≈ 512/522 to 605/617).
- 95 × 0.69 / 763 = 8.59 cm, against the prior 85.6 mm, so the given depths and f = 763 are consistent.

## Other numbers
Cup top diameter: 74 px, which gives 8.2 cm.

Confidence: moderate. The geometry interpretations span about ±4 %.
