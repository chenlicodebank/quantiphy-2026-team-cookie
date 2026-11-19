# q_2709: diameter of the white ball (cm)

Lab video, 1280x720, 24 fps (file rate = question_fps = 24). f = 0.5959*1280 = 763 px, principal point (640,360).
depth_info at t = 1.4 s, so frame round(1.4*24) = 34. White ball d = 0.7160 m. Credit card d = 0.6867 m.

## Pixel diameter of the ball (blur-free vertical extent; the motion is horizontal at ~16 px/frame)
Background = median of all frames (`measure.py`). Profiles are in `profile.py`. Crops are in `frames/crops.png`.
- Top edge: half-level crossing between the ball and the background. This edge is sharp (f34: 486.7).
- Bottom edge, route A (`chordfit.py`): half-way into the dark contact shadow. This gives ~41.1 px at f34. It is
  biased low, because the ball's dark underside merges with the shadow.
- Bottom edge, route C (`shadowmin.py`): the sub-pixel minimum of the contact-shadow band. The camera is low
  (about 15 deg elevation, from the card's foreshortening). The table visible just below the silhouette therefore
  lies within R*tan(e/2) of the contact point, so the darkest row marks the silhouette. f34: 43.13 px; linear trend
  over f26-42 gives 43.38 px.
- Route B (`chordfit.py`, independent): a circle fit to the horizontal half-max chord widths. Box motion blur keeps
  the half-max width equal to the chord. On the clean frames f19-26 it gives 42.3-43.2 px, against 42.0-42.9 px
  for route C, so B and C agree. B is unreliable from f27 on because the background is cluttered.
- The scene/ record (35-38 px, from a "brighter than background" mask) excluded the ball's darker lower part, so it
  is too small.

## Scale
- Card check (`card.py`): the card's back and front long edges are 93 and 101 px, midline ~97 px. Predicted
  f*L/Z = 763*0.0856/(0.6867*cos 14.3deg) = 98.2 px, so f = 763 checks to ~1%.
- Method-card formula: D = d*px/f = 0.716*43.13/763 = 4.05 cm (4.07 cm with the trend value).
- Exact projection of a sphere at d = 0.716 m in the ball's image direction (`final.py`). The ball is 12 deg off
  axis, so its vertical image extent is stretched by 1.044. Solving for the same pixel height gives D = 3.88 cm
  (3.90 cm with the trend value).
- Route B suggests route C reads the vertical extent ~0.5-1 px low. That pushes the exact-sphere value to
  ~3.92-3.97 cm.

## Answer
3.95 cm, between the exact-geometry value (3.88-3.97) and the card formula (4.05). This fits a ping-pong
ball (4.0 cm) as a sanity check. Confidence: about ±4%. The main uncertainty is where the bottom silhouette sits
within the contact shadow (±1 px ≈ ±2.4%).
