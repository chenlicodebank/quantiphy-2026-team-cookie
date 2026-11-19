# q_1836 — length of the bottom towel of the three stacked towels (m)

The video is 2D and filmed from straight above at 24 fps. The question's frame rate is also 24, so no re-timing is needed.

## Objects
- Cup = the teal rectangle, the only object that moves. It slides right at constant speed.
- Towels = the grey object the scene record calls the "tray", centred near (911, 199) px and turned about 26°.
  Zoomed crops show three stacked layers, one inside the other. The bottom towel is the largest one, so its outline
  is the outer outline of the whole stack.

## Measurements (measure.py)
- Cup speed: I fitted a straight line to the x position of the teal mask centre over frames 2–71. It gives
  14.536 px/frame, or 348.87 px/s. The plain average of the per-frame steps is 14.533 px/frame. The y position stays
  constant within 0.8 px.
- Scale: 0.338 / 348.87 = 9.688e-4 m/px.
- Bottom towel outline: I took the largest connected region of non-white pixels around the towels and fitted the
  smallest rotated box around it.
  - Long side: 374.0, 373.2 and 373.4 px at frames 0, 36 and 71.
  - A second method (PCA extent of the same region) gives the same values, 373.2–374.0 px.
  - Short side: about 188 px.
- Length = 373.5 px × 9.688e-4 = **0.362 m** (the frames give 0.3616–0.3624 m). The width would be about 0.182 m.

## Checks and confidence
- The second method for the towel (PCA extent) and three different frames all agree within 0.2%.
- The cup speed from the line fit and from the per-frame average agree within 0.03%.
- Another reading of "length": if it meant the screen-axis bounding box of the rotated towel (403 px, about 0.39 m),
  the answer would change. I use the towel's own long side instead, following the convention given for "length".
- Confidence: high, assuming the outer outline is the bottom towel.
