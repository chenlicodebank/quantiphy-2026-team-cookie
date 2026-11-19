# Q983 – length of the whale (m)

The prior is whale speed = 1.67 m/s. The video is a 2D scene (side-on, horizontal swim), file fps = question fps = 24.

## Scale
- The head moves rigidly at −8.02 px/frame (scene record, head chain track, std 0.1).
- Independent check (measure.py): I template-matched the head between frames 5, 15, 25, 35 and 45 and got exactly −8.0 px/frame. At frames 52 and later the template degrades because the head pitches.
- Pixel speed = 8.02 × 24 = 192.5 px/s, so the scale is 1.67 / 192.5 = 0.008676 m/px.

## Length
- Snout-to-fluke-tip horizontal extent with the whole whale in frame and the body near straight (frames 47–52): bbox_w = 2312–2320 px. At frame 52, with the body straight, it is 2319 px. I confirmed this visually on frames/f52.png: snout at x ≈ 205, fluke tip at x ≈ 2522.
- Length = 2319 × 0.008676 = **20.1 m**.
- Spread: the curled-tail frames give 2217–2290 px (19.2–19.9 m). The straight pose is the rest-pose length, so I answer with it.

## Confidence
Good. The scale is accurate to about 1%, and the length to about 1–3%, depending on which pose the reference box used.
